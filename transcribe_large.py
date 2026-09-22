#!/usr/bin/env python3
"""
Скрипт высокоточного распознавания аудио с помощью модели faster-whisper large-v3.
Оптимизирован для 12-поточного CPU с квантованием int8 (высочайшая точность Whisper без перегрузки памяти).
"""

import os
import sys
import argparse
from faster_whisper import WhisperModel

MODEL_NAME = "large-v3"
DEVICE = "cpu"
COMPUTE_TYPE = "int8"
CPU_THREADS = 12

def get_model():
    print(f"Загрузка модели {MODEL_NAME} (device={DEVICE}, compute_type={COMPUTE_TYPE}, threads={CPU_THREADS})...")
    model = WhisperModel(
        MODEL_NAME,
        device=DEVICE,
        compute_type=COMPUTE_TYPE,
        cpu_threads=CPU_THREADS,
        download_root=os.path.expanduser("~/.cache/huggingface/hub")
    )
    print("Модель успешно загружена!")
    return model

def transcribe_file(model, audio_path, output_path=None, language="ru"):
    print(f"\nРаспознавание файла: {audio_path}")
    segments, info = model.transcribe(
        audio_path,
        beam_size=5,
        language=language,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500)
    )

    print(f"Обнаружен язык: {info.language} (вероятность: {info.language_probability:.2f})")
    print(f"Длительность аудио: {info.duration:.1f} сек.\n")

    lines = []
    for segment in segments:
        start_min = int(segment.start // 60)
        start_sec = int(segment.start % 60)
        end_min = int(segment.end // 60)
        end_sec = int(segment.end % 60)
        time_str = f"[{start_min:02d}:{start_sec:02d} - {end_min:02d}:{end_sec:02d}]"
        text = segment.text.strip()
        print(f"{time_str} {text}")
        lines.append(f"{time_str} {text}")

    full_text = "\n".join(lines)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_text + "\n")
        print(f"\nРезультат сохранен в: {output_path}")

    return full_text

def main():
    parser = argparse.ArgumentParser(description="Высокоточное распознавание аудио с faster-whisper large-v3")
    parser.add_argument("audio", help="Путь к аудиофайлу")
    parser.add_argument("-o", "--output", help="Путь для сохранения текстового файла транскрипции", default=None)
    parser.add_argument("-l", "--lang", help="Язык аудио (по умолчанию 'ru')", default="ru")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()
    model = get_model()
    transcribe_file(model, args.audio, args.output, language=args.lang)

if __name__ == "__main__":
    main()
