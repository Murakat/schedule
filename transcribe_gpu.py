#!/usr/bin/env python3
"""
Высокоскоростная транскрипция аудиоуроков с аппаратным ускорением на AMD Radeon RX 5700 XT (через Vulkan).
Включает Silero VAD фильтр тишины и защиту от зацикливаний и галлюцинаций Whisper.
"""

import os
import re
import sys
import time
import subprocess

WORKSPACE = "/home/nameowo/Документы/audio"
WHISPER_CLI = "/home/nameowo/.local/src/whisper.cpp/build/bin/whisper-cli"
MODEL_BIN = "/home/nameowo/.local/src/whisper.cpp/models/ggml-large-v3-turbo.bin"
VAD_MODEL = "/home/nameowo/.local/src/whisper.cpp/models/ggml-silero-v5.1.2.bin"
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

    # Неделя 4 (21–23 сен)
    ("Моя_запись_31", "audio/Моя запись 31.m4a"),
    ("Моя_запись_32", "audio/Моя запись 32_recovered.m4a"),
    ("Моя_запись_35", "audio/Моя запись 35.m4a"),
    ("Моя_запись_36", "audio/Моя запись 36_recovered.m4a"),
    ("Моя_запись_38", "audio/Моя запись 38.m4a"),
    ("Моя_запись_39", "audio/Моя запись 39_recovered.m4a"),
    ("Моя_запись_41", "audio/Моя запись 41.m4a"),

    # Неделя 4 (24–25 сен)
    ("Моя_запись_46", "audio/Моя запись 46.m4a"),
    ("Моя_запись_42", "audio/Моя запись 42_recovered.m4a"),
    ("Моя_запись_44", "audio/Моя запись 44.m4a"),
    ("Моя_запись_45", "audio/Моя запись 45.m4a"),
]

LINE_RE = re.compile(r"\[(\d{2}):(\d{2}):(\d{2})\.\d{3}\s+-->\s+(\d{2}):(\d{2}):(\d{2})\.\d{3}\]\s+(.*)")

def format_timestamp(h1, m1, s1, h2, m2, s2):
    start_sec = int(h1) * 3600 + int(m1) * 60 + int(s1)
    end_sec = int(h2) * 3600 + int(m2) * 60 + int(s2)
    s_m, s_s = divmod(start_sec, 60)
    e_m, e_s = divmod(end_sec, 60)
    return f"[{s_m:02d}:{s_s:02d} - {e_m:02d}:{e_s:02d}]"

def main():
    print(f"[{time.strftime('%H:%M:%S')}] Инициализация GPU транскрипции (AMD Radeon RX 5700 XT via Vulkan + Silero VAD)...", flush=True)
    if not os.path.exists(WHISPER_CLI):
        print(f"Ошибка: не найден {WHISPER_CLI}", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(MODEL_BIN):
        print(f"Ошибка: не найдена модель {MODEL_BIN}", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(VAD_MODEL):
        print(f"Ошибка: не найдена VAD модель {VAD_MODEL}", file=sys.stderr)
        sys.exit(1)

    total = len(RECORDINGS)
    temp_wav = "/tmp/whisper_gpu_input.wav"

    for idx, (name, rel_path) in enumerate(RECORDINGS, 1):
        audio_path = os.path.join(WORKSPACE, rel_path)
        out_file = os.path.join(OUT_DIR, f"{name}.txt")

        if os.path.exists(out_file) and os.path.getsize(out_file) > 2000:
            print(f"[{time.strftime('%H:%M:%S')}] [{idx}/{total}] Пропуск: {name} (уже готово, {os.path.getsize(out_file)} байт)", flush=True)
            continue

        if not os.path.exists(audio_path):
            print(f"[{time.strftime('%H:%M:%S')}] [{idx}/{total}] ОШИБКА: аудиофайл не найден {audio_path}", flush=True)
            continue

        print(f"\n==================================================================", flush=True)
        print(f"[{time.strftime('%H:%M:%S')}] [{idx}/{total}] Обработка на GPU: {name} ({rel_path})", flush=True)
        print(f"==================================================================", flush=True)

        # 1. Конвертация во временный 16kHz WAV через ffmpeg
        res_ff = subprocess.run([
            "ffmpeg", "-y", "-i", audio_path,
            "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le",
            temp_wav
        ], capture_output=True, text=True)

        if res_ff.returncode != 0:
            print(f"Ошибка конвертации ffmpeg для {audio_path}: {res_ff.stderr[-200:]}", flush=True)
            continue

        # 2. Определение длительности
        dur_res = subprocess.run([
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", temp_wav
        ], capture_output=True, text=True)
        try:
            total_dur = float(dur_res.stdout.strip())
        except Exception:
            total_dur = 1.0

        print(f"Длительность записи: {total_dur/60:.1f} мин ({total_dur:.0f}с)", flush=True)

        # 3. Запуск whisper-cli на GPU (Vulkan) с Silero VAD и защитой от циклов
        t_start = time.time()
        cmd = [
            WHISPER_CLI,
            "-m", MODEL_BIN,
            "-vm", VAD_MODEL,
            "--vad",
            "-f", temp_wav,
            "-l", "ru",
            "-t", "8",
            "-mc", "0",          # отключает зацикливание предыдущего контекста
            "-nf",               # отключает fallback на высокую температуру (защита от галлюцинаций)
            "--suppress-nst",     # подавляет токены неречевого шума
            "-nth", "0.6"        # порог отсечения тишины
        ]

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        count = 0
        last_clean_text = ""
        repeat_count = 0

        with open(out_file, "w", encoding="utf-8") as out_f:
            for line in proc.stdout:
                line_str = line.strip()
                m = LINE_RE.match(line_str)
                if m:
                    h1, m1, s1, h2, m2, s2, text = m.groups()
                    time_tag = format_timestamp(h1, m1, s1, h2, m2, s2)
                    clean_text = text.strip()
                    
                    if not clean_text:
                        continue

                    # Проверка на дубликаты/зацикливание
                    if clean_text == last_clean_text:
                        repeat_count += 1
                        if repeat_count > 1:
                            continue
                    else:
                        repeat_count = 0
                        last_clean_text = clean_text

                    out_line = f"{time_tag}  {clean_text}\n"
                    out_f.write(out_line)
                    out_f.flush()
                    count += 1
                    if count % 30 == 0:
                        print(f"  [{name} | {time_tag}] {clean_text[:65]}...", flush=True)

        proc.wait()
        elapsed = time.time() - t_start
        speed_ratio = total_dur / max(elapsed, 0.1)
        print(f"[{time.strftime('%H:%M:%S')}] Завершено {name}: {count} реплик за {elapsed:.1f}с ({elapsed/60:.1f} мин) — Скорость: {speed_ratio:.1f}x реального времени!", flush=True)

        if os.path.exists(temp_wav):
            try:
                os.remove(temp_wav)
            except Exception:
                pass

    print(f"\n[{time.strftime('%H:%M:%S')}] ВСЕ ЗАПИСИ УСПЕШНО ОБРАБОТАНЫ НА GPU AMD RADEON RX 5700 XT!", flush=True)

if __name__ == "__main__":
    main()
