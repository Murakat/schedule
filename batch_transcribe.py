#!/usr/bin/env python3
"""
Пакетная транскрипция всех 24 аудиозаписей уроков через модель faster-whisper large-v3.
Оптимизировано для CPU (12 потоков, квантование int8).
Результаты сохраняются в папку transcripts/ с временными метками.
"""

import os
import sys
import time
from faster_whisper import WhisperModel

WORKSPACE = "/home/nameowo/Документы/audio"
OUT_DIR = os.path.join(WORKSPACE, "transcripts")
os.makedirs(OUT_DIR, exist_ok=True)

RECORDINGS = [
    # Неделя 1 (3–5 сен)
    ("Литература_03_09", "audio/Литература 3.09 .m4a"),
    ("География_04_09", "audio/География 4.09.m4a"),
    ("Алгебра_04_09_Моя_запись_3", "audio/Моя запись 3.m4a"),
    ("Родная_литература_05_09", "audio/Родная литература 5.09_recovered.m4a"),
    
    # Неделя 2 (7–9 сен)
    ("Русский_язык_07_09", "audio/Русский язык 7.09.m4a"),
    ("Физика_07_09", "audio/Физика 7.09.m4a"),
    ("Литература_07_09_часть1", "audio/Моя запись 11.m4a"),
    ("Литература_07_09_часть2", "audio/Моя запись 12_recovered.m4a"),
    ("Литература_07_09_часть3", "audio/Моя запись 13.m4a"),
    ("Математика_08_09_часть1", "audio/Математика 9.08.m4a"),
    ("Математика_08_09_часть2", "audio/Моя запись 16.m4a"),
    ("География_08_09", "audio/Моя запись 17_recovered.m4a"),
    ("Запись_19_08_09", "audio/Моя запись 19.m4a"),
    ("Математика_09_09_часть1", "audio/Моя запись 20.m4a"),
    ("Математика_09_09_часть2", "audio/Моя запись 21.m4a"),
    ("Физика_09_09", "audio/Моя запись 22.m4a"),
    
    # Неделя 3 (12–18 сен)
    ("Моя_запись_23", "audio/Моя запись 23.m4a"),
    ("Моя_запись_24", "audio/Моя запись 24.m4a"),
    ("Моя_запись_25", "audio/Моя запись 25.m4a"),
    ("Моя_запись_26", "audio/Моя запись 26.m4a"),
    ("Моя_запись_27", "audio/Моя запись 27.m4a"),
    ("Моя_запись_28", "audio/Моя запись 28.m4a"),
    ("Моя_запись_29", "audio/Моя запись 29.m4a"),
    ("Моя_запись_30", "audio/Моя запись 30.m4a"),
]

def main():
    print(f"[{time.strftime('%H:%M:%S')}] Инициализация faster-whisper large-v3 (CPU, int8, 12 потоков)...", flush=True)
    t_start_load = time.time()
    model = WhisperModel(
        "large-v3",
        device="cpu",
        compute_type="int8",
        cpu_threads=12,
        download_root=os.path.expanduser("~/.cache/huggingface/hub")
    )
    print(f"[{time.strftime('%H:%M:%S')}] Модель загружена за {time.time() - t_start_load:.1f}с.", flush=True)

    total_files = len(RECORDINGS)
    for idx, (name, rel_path) in enumerate(RECORDINGS, 1):
        audio_path = os.path.join(WORKSPACE, rel_path)
        out_file = os.path.join(OUT_DIR, f"{name}.txt")

        if os.path.exists(out_file) and os.path.getsize(out_file) > 2000:
            print(f"[{time.strftime('%H:%M:%S')}] [{idx}/{total_files}] Пропуск: {name} (уже существует, {os.path.getsize(out_file)} байт)", flush=True)
            continue

        if not os.path.exists(audio_path):
            print(f"[{time.strftime('%H:%M:%S')}] [{idx}/{total_files}] ОШИБКА: файл не найден {audio_path}", flush=True)
            continue

        print(f"\n=======================================================", flush=True)
        print(f"[{time.strftime('%H:%M:%S')}] [{idx}/{total_files}] Транскрипция: {name} ({rel_path})", flush=True)
        print(f"=======================================================", flush=True)
        t0 = time.time()

        segments, info = model.transcribe(
            audio_path,
            language="ru",
            beam_size=1,
            best_of=1,
            temperature=0.0,
            condition_on_previous_text=False,
            vad_filter=True,
            vad_parameters=dict(min_silence_duration_ms=500)
        )

        count = 0
        with open(out_file, "w", encoding="utf-8") as f:
            for seg in segments:
                s_min = int(seg.start // 60)
                s_sec = int(seg.start % 60)
                e_min = int(seg.end // 60)
                e_sec = int(seg.end % 60)
                time_str = f"[{s_min:02d}:{s_sec:02d} - {e_min:02d}:{e_sec:02d}]"
                text = seg.text.strip()
                line = f"{time_str}  {text}\n"
                f.write(line)
                f.flush()
                count += 1
                if count % 30 == 0:
                    print(f"  [{name} | {time_str}] {text[:70]}...", flush=True)

        elapsed = time.time() - t0
        print(f"[{time.strftime('%H:%M:%S')}] Завершено {name}: {count} сегментов за {elapsed:.1f}с ({elapsed/60:.1f} мин)", flush=True)

    print(f"\n[{time.strftime('%H:%M:%S')}] ВСЕ 24 АУДИОЗАПИСИ УСПЕШНО ТРАНСКРИБИРОВАНЫ!", flush=True)

if __name__ == "__main__":
    main()
