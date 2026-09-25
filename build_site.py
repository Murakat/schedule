import os, json, re, glob

# 1. Read all markdown notes
notes_map = {}
topics_map = {}
for path in sorted(glob.glob("dist/notes/*.md")):
    fname = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    notes_map[fname] = content
    
    # Extract topic
    topic = ""
    m = re.search(r"### ТЕМА УРОКА\s*>+ *(.*)", content)
    if m:
        topic = m.group(1).replace("<u>", "").replace("</u>", "").replace("**", "").strip()
    topics_map[fname] = topic

print(f"Loaded {len(notes_map)} notes.")

# 2. Base structure for weeks and days
schedule_data = {
    "group": "МТО-138",
    "term": "I полугодие 2026-2027 учебного года",
    "weeks": [
        {
            "id": 1,
            "title": "Неделя 1",
            "range": "31 авг — 5 сен 2026",
            "dates": ["2026-08-31", "2026-09-01", "2026-09-02", "2026-09-03", "2026-09-04", "2026-09-05"]
        },
        {
            "id": 2,
            "title": "Неделя 2",
            "range": "7 сен — 12 сен 2026",
            "dates": ["2026-09-07", "2026-09-08", "2026-09-09", "2026-09-10", "2026-09-11", "2026-09-12"]
        },
        {
            "id": 3,
            "title": "Неделя 3",
            "range": "14 сен — 19 сен 2026",
            "dates": ["2026-09-14", "2026-09-15", "2026-09-16", "2026-09-17", "2026-09-18", "2026-09-19"]
        },
        {
            "id": 4,
            "title": "Неделя 4",
            "range": "21 сен — 26 сен 2026",
            "dates": ["2026-09-21", "2026-09-22", "2026-09-23", "2026-09-24", "2026-09-25", "2026-09-26"]
        }
    ],
    "days": [
        # WEEK 1
        {
            "date": "2026-08-31",
            "date_display": "31 августа 2026 г. (Понедельник)",
            "short_day": "31 авг",
            "weekday": "Пн",
            "week": 1,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-01",
            "date_display": "1 сентября 2026 г. (Вторник)",
            "short_day": "1 сен",
            "weekday": "Вт",
            "week": 1,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "Торжественная линейка", "room": "Актовый зал", "teacher": "Начало в 10:00", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "Классный час", "room": "каб. 305", "teacher": "Коклюгина Н.А.", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-02",
            "date_display": "2 сентября 2026 г. (Среда)",
            "short_day": "2 сен",
            "weekday": "Ср",
            "week": 1,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "Математика", "room": "каб. 303", "teacher": "Садыкова Р.З.", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "Математика", "room": "каб. 303", "teacher": "Садыкова Р.З.", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "Физика", "room": "каб. 307", "teacher": "Кузнецова Е.С.", "has_notes": False},
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-03",
            "date_display": "3 сентября 2026 г. (Четверг)",
            "short_day": "3 сен",
            "weekday": "Чт",
            "week": 1,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "Физика", "room": "каб. 307", "teacher": "Кузнецова Е.С.", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "История", "room": "каб. 201", "teacher": "Попова А.А.", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "География", "room": "каб. 307", "teacher": "Бахтина С.А.", "has_notes": False},
                {
                    "num": 4, "time": "14:00 – 15:30", "subject": "Литература", "room": "каб. 203", "teacher": "Галавова Г.В.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-03_Литература.md",
                    "notes_md": notes_map.get("2026-09-03_Литература.md", ""),
                    "topic": topics_map.get("2026-09-03_Литература.md", "")
                },
                {"num": 5, "time": "15:40 – 17:10", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-04",
            "date_display": "4 сентября 2026 г. (Пятница)",
            "short_day": "4 сен",
            "weekday": "Пт",
            "week": 1,
            "lessons": [
                {
                    "num": 1, "time": "08:30 – 10:00", "subject": "География", "room": "каб. 307", "teacher": "Бахтина С.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-04_География.md",
                    "notes_md": notes_map.get("2026-09-04_География.md", ""),
                    "topic": topics_map.get("2026-09-04_География.md", "")
                },
                {
                    "num": 2, "time": "10:10 – 11:40", "subject": "Математика (Алгебра)", "room": "каб. 303", "teacher": "Садыкова Р.З.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-04_Алгебра.md",
                    "notes_md": notes_map.get("2026-09-04_Алгебра.md", ""),
                    "topic": topics_map.get("2026-09-04_Алгебра.md", "")
                },
                {"num": 3, "time": "12:10 – 13:40", "subject": "Математика", "room": "каб. 303", "teacher": "Садыкова Р.З.", "has_notes": False},
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-05",
            "date_display": "5 сентября 2026 г. (Суббота)",
            "short_day": "5 сен",
            "weekday": "Сб",
            "week": 1,
            "lessons": [
                {
                    "num": 1, "time": "08:30 – 09:50", "subject": "Родная литература", "room": "каб. 203", "teacher": "Демидова Л.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-05_Родная_литература.md",
                    "notes_md": notes_map.get("2026-09-05_Родная_литература.md", ""),
                    "topic": topics_map.get("2026-09-05_Родная_литература.md", "")
                },
                {"num": 2, "time": "10:00 – 11:20", "subject": "Информатика", "room": "каб. 401", "teacher": "Алиева Э.Р.", "has_notes": False},
                {"num": 3, "time": "11:30 – 12:50", "subject": "Информатика", "room": "каб. 401", "teacher": "Алиева Э.Р.", "has_notes": False},
                {"num": 4, "time": "13:00 – 14:20", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },

        # WEEK 2
        {
            "date": "2026-09-07",
            "date_display": "7 сентября 2026 г. (Понедельник)",
            "short_day": "7 сен",
            "weekday": "Пн",
            "week": 2,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {
                    "num": 4, "time": "14:00 – 15:30", "subject": "Физика", "room": "каб. 307", "teacher": "Кузнецова Е.С.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-07_Физика.md",
                    "notes_md": notes_map.get("2026-09-07_Физика.md", ""),
                    "topic": topics_map.get("2026-09-07_Физика.md", "")
                },
                {
                    "num": 5, "time": "15:40 – 17:10", "subject": "Русский язык", "room": "каб. 203", "teacher": "Галавова Г.В.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-07_Русский_язык.md",
                    "notes_md": notes_map.get("2026-09-07_Русский_язык.md", ""),
                    "topic": topics_map.get("2026-09-07_Русский_язык.md", "")
                },
                {
                    "num": 6, "time": "17:20 – 18:50", "subject": "Литература", "room": "каб. 203", "teacher": "Галавова Г.В.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-07_Литература.md",
                    "notes_md": notes_map.get("2026-09-07_Литература.md", ""),
                    "topic": topics_map.get("2026-09-07_Литература.md", "")
                }
            ]
        },
        {
            "date": "2026-09-08",
            "date_display": "8 сентября 2026 г. (Вторник)",
            "short_day": "8 сен",
            "weekday": "Вт",
            "week": 2,
            "lessons": [
                {
                    "num": 1, "time": "08:30 – 10:00", "subject": "Математика (Алгебра)", "room": "каб. 303", "teacher": "Садыкова Р.З.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-08_Математика.md",
                    "notes_md": notes_map.get("2026-09-08_Математика.md", ""),
                    "topic": topics_map.get("2026-09-08_Математика.md", "")
                },
                {
                    "num": 2, "time": "10:10 – 11:40", "subject": "Математика (Алгебра)", "room": "каб. 303", "teacher": "Садыкова Р.З.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-08_Математика.md",
                    "notes_md": notes_map.get("2026-09-08_Математика.md", ""),
                    "topic": topics_map.get("2026-09-08_Математика.md", "")
                },
                {
                    "num": 3, "time": "12:10 – 13:40", "subject": "География", "room": "каб. 307", "teacher": "Бахтина С.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-08_География.md",
                    "notes_md": notes_map.get("2026-09-08_География.md", ""),
                    "topic": topics_map.get("2026-09-08_География.md", "")
                },
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-09",
            "date_display": "9 сентября 2026 г. (Среда)",
            "short_day": "9 сен",
            "weekday": "Ср",
            "week": 2,
            "lessons": [
                {
                    "num": 1, "time": "08:30 – 10:00", "subject": "Математика (Алгебра)", "room": "каб. 303", "teacher": "Садыкова Р.З.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-09_Математика.md",
                    "notes_md": notes_map.get("2026-09-09_Математика.md", ""),
                    "topic": topics_map.get("2026-09-09_Математика.md", "")
                },
                {
                    "num": 2, "time": "10:10 – 11:40", "subject": "Математика (Алгебра)", "room": "каб. 303", "teacher": "Садыкова Р.З.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-09_Математика.md",
                    "notes_md": notes_map.get("2026-09-09_Математика.md", ""),
                    "topic": topics_map.get("2026-09-09_Математика.md", "")
                },
                {
                    "num": 3, "time": "12:10 – 13:40", "subject": "Физика", "room": "каб. 204", "teacher": "Кузнецова Е.С.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-09_Физика.md",
                    "notes_md": notes_map.get("2026-09-09_Физика.md", ""),
                    "topic": topics_map.get("2026-09-09_Физика.md", "")
                },
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-10",
            "date_display": "10 сентября 2026 г. (Четверг)",
            "short_day": "10 сен",
            "weekday": "Чт",
            "week": 2,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 5, "time": "15:40 – 17:10", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 6, "time": "17:20 – 18:50", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-11",
            "date_display": "11 сентября 2026 г. (Пятница)",
            "short_day": "11 сен",
            "weekday": "Пт",
            "week": 2,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-12",
            "date_display": "12 сентября 2026 г. (Суббота)",
            "short_day": "12 сен",
            "weekday": "Сб",
            "week": 2,
            "lessons": [
                {
                    "num": 1, "time": "08:30 – 10:00", "subject": "Математика (Алгебра)", "room": "каб. 303", "teacher": "Садыкова Р.З.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-12_Математика.md",
                    "notes_md": notes_map.get("2026-09-12_Математика.md", ""),
                    "topic": topics_map.get("2026-09-12_Математика.md", "")
                },
                {"num": 2, "time": "10:10 – 11:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },

        # WEEK 3
        {
            "date": "2026-09-14",
            "date_display": "14 сентября 2026 г. (Понедельник)",
            "short_day": "14 сен",
            "weekday": "Пн",
            "week": 3,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 4, "time": "14:00 – 15:30", "subject": "Биология", "room": "каб. 305", "teacher": "Валеева А.Р.", "has_notes": False},
                {"num": 5, "time": "15:40 – 17:10", "subject": "Русский язык", "room": "каб. 203", "teacher": "Галавова Г.В.", "has_notes": False},
                {"num": 6, "time": "17:20 – 18:50", "subject": "Литература", "room": "каб. 203", "teacher": "Галавова Г.В.", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-15",
            "date_display": "15 сентября 2026 г. (Вторник)",
            "short_day": "15 сен",
            "weekday": "Вт",
            "week": 3,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "Математика", "room": "каб. 201", "teacher": "Садыкова Р.З.", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "Математика", "room": "каб. 201", "teacher": "Садыкова Р.З.", "has_notes": False},
                {
                    "num": 3, "time": "12:10 – 13:40", "subject": "География", "room": "каб. 207", "teacher": "Бахтина С.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-15_География.md",
                    "notes_md": notes_map.get("2026-09-15_География.md", ""),
                    "topic": topics_map.get("2026-09-15_География.md", "")
                },
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-16",
            "date_display": "16 сентября 2026 г. (Среда)",
            "short_day": "16 сен",
            "weekday": "Ср",
            "week": 3,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "Математика", "room": "каб. 303", "teacher": "Садыкова Р.З.", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "Математика", "room": "каб. 303", "teacher": "Садыкова Р.З.", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "Физика", "room": "каб. 307", "teacher": "Кузнецова Е.С.", "has_notes": False},
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-17",
            "date_display": "17 сентября 2026 г. (Четверг)",
            "short_day": "17 сен",
            "weekday": "Чт",
            "week": 3,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {
                    "num": 4, "time": "14:00 – 15:30", "subject": "Биология", "room": "каб. 305", "teacher": "Валеева А.Р.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-17_Биология.md",
                    "notes_md": notes_map.get("2026-09-17_Биология.md", ""),
                    "topic": topics_map.get("2026-09-17_Биология.md", "")
                },
                {
                    "num": 5, "time": "15:40 – 17:10", "subject": "Биология", "room": "каб. 305", "teacher": "Валеева А.Р.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-17_Биология.md",
                    "notes_md": notes_map.get("2026-09-17_Биология.md", ""),
                    "topic": topics_map.get("2026-09-17_Биология.md", "")
                },
                {
                    "num": 6, "time": "17:20 – 18:50", "subject": "Литература", "room": "каб. 203", "teacher": "Галавова Г.В.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-17_Литература.md",
                    "notes_md": notes_map.get("2026-09-17_Литература.md", ""),
                    "topic": topics_map.get("2026-09-17_Литература.md", "")
                }
            ]
        },
        {
            "date": "2026-09-18",
            "date_display": "18 сентября 2026 г. (Пятница)",
            "short_day": "18 сен",
            "weekday": "Пт",
            "week": 3,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "Родная литература", "room": "библиотека", "teacher": "Демидова Л.А.", "has_notes": False},
                {
                    "num": 2, "time": "10:10 – 11:40", "subject": "Родная литература", "room": "библиотека", "teacher": "Демидова Л.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-18_Родная_литература.md",
                    "notes_md": notes_map.get("2026-09-18_Родная_литература.md", ""),
                    "topic": topics_map.get("2026-09-18_Родная_литература.md", "")
                },
                {
                    "num": 3, "time": "12:10 – 13:40", "subject": "География", "room": "каб. 302", "teacher": "Бахтина С.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-18_География.md",
                    "notes_md": notes_map.get("2026-09-18_География.md", ""),
                    "topic": topics_map.get("2026-09-18_География.md", "")
                },
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-19",
            "date_display": "19 сентября 2026 г. (Суббота)",
            "short_day": "19 сен",
            "weekday": "Сб",
            "week": 3,
            "lessons": [
                {"num": 1, "time": "08:30 – 09:50", "subject": "Родная литература", "room": "каб. 203", "teacher": "Демидова Л.А.", "has_notes": False},
                {"num": 2, "time": "10:00 – 11:20", "subject": "Родная литература", "room": "каб. 203", "teacher": "Демидова Л.А.", "has_notes": False},
                {"num": 3, "time": "11:30 – 12:50", "subject": "География", "room": "каб. 311", "teacher": "Бахтина С.А.", "has_notes": False},
                {"num": 4, "time": "13:00 – 14:20", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },

        # WEEK 4
        {
            "date": "2026-09-21",
            "date_display": "21 сентября 2026 г. (Понедельник)",
            "short_day": "21 сен",
            "weekday": "Пн",
            "week": 4,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {
                    "num": 4, "time": "14:00 – 15:30", "subject": "Биология", "room": "библиотека", "teacher": "Валеева А.Р.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-21_Биология.md",
                    "notes_md": notes_map.get("2026-09-21_Биология.md", ""),
                    "topic": topics_map.get("2026-09-21_Биология.md", "")
                },
                {
                    "num": 5, "time": "15:40 – 17:10", "subject": "Русский язык", "room": "каб. 203", "teacher": "Галавова Г.В.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-21_Русский_язык.md",
                    "notes_md": notes_map.get("2026-09-21_Русский_язык.md", ""),
                    "topic": topics_map.get("2026-09-21_Русский_язык.md", "")
                },
                {
                    "num": 6, "time": "17:20 – 18:50", "subject": "Литература", "room": "каб. 203", "teacher": "Галавова Г.В.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-21_Литература.md",
                    "notes_md": notes_map.get("2026-09-21_Литература.md", ""),
                    "topic": topics_map.get("2026-09-21_Литература.md", "")
                }
            ]
        },
        {
            "date": "2026-09-22",
            "date_display": "22 сентября 2026 г. (Вторник)",
            "short_day": "22 сен",
            "weekday": "Вт",
            "week": 4,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {
                    "num": 4, "time": "14:00 – 15:30", "subject": "География", "room": "каб. 303", "teacher": "Бахтина С.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-22_География.md",
                    "notes_md": notes_map.get("2026-09-22_География.md", ""),
                    "topic": topics_map.get("2026-09-22_География.md", "")
                },
                {
                    "num": 5, "time": "15:40 – 17:10", "subject": "История", "room": "каб. 207", "teacher": "Попова А.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-22_История.md",
                    "notes_md": notes_map.get("2026-09-22_История.md", ""),
                    "topic": topics_map.get("2026-09-22_История.md", "")
                },
                {
                    "num": 6, "time": "17:20 – 18:50", "subject": "История", "room": "каб. 207", "teacher": "Попова А.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-22_История.md",
                    "notes_md": notes_map.get("2026-09-22_История.md", ""),
                    "topic": topics_map.get("2026-09-22_История.md", "")
                }
            ]
        },
        {
            "date": "2026-09-23",
            "date_display": "23 сентября 2026 г. (Среда)",
            "short_day": "23 сен",
            "weekday": "Ср",
            "week": 4,
            "lessons": [
                {
                    "num": 1, "time": "08:30 – 10:00", "subject": "География", "room": "каб. 305", "teacher": "Бахтина С.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-23_География.md",
                    "notes_md": notes_map.get("2026-09-23_География.md", ""),
                    "topic": topics_map.get("2026-09-23_География.md", "")
                },
                {
                    "num": 2, "time": "10:10 – 11:40", "subject": "Английский язык", "room": "каб. 206/221", "teacher": "Хакимова Г.Р. / Гилазова",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-23_Английский_язык.md",
                    "notes_md": notes_map.get("2026-09-23_Английский_язык.md", ""),
                    "topic": topics_map.get("2026-09-23_Английский_язык.md", "")
                },
                {
                    "num": 3, "time": "12:10 – 13:40", "subject": "Информатика", "room": "каб. 301", "teacher": "Алиева Э.Р.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-23_Информатика.md",
                    "notes_md": notes_map.get("2026-09-23_Информатика.md", ""),
                    "topic": topics_map.get("2026-09-23_Информатика.md", "")
                },
                {
                    "num": 4, "time": "14:00 – 15:30", "subject": "Информатика", "room": "каб. 301", "teacher": "Алиева Э.Р.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-23_Информатика.md",
                    "notes_md": notes_map.get("2026-09-23_Информатика.md", ""),
                    "topic": topics_map.get("2026-09-23_Информатика.md", "")
                }
            ]
        },
        {
            "date": "2026-09-24",
            "date_display": "24 сентября 2026 г. (Четверг)",
            "short_day": "24 сен",
            "weekday": "Чт",
            "week": 4,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 2, "time": "10:10 – 11:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 3, "time": "12:10 – 13:40", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {
                    "num": 4, "time": "14:00 – 15:30", "subject": "Биология", "room": "каб. 305", "teacher": "Валеева А.Р.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-24_Биология.md",
                    "notes_md": notes_map.get("2026-09-24_Биология.md", ""),
                    "topic": topics_map.get("2026-09-24_Биология.md", "")
                },
                {
                    "num": 5, "time": "15:40 – 17:10", "subject": "Литература", "room": "каб. 203", "teacher": "Галавова Г.В.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-24_Литература.md",
                    "notes_md": notes_map.get("2026-09-24_Литература.md", ""),
                    "topic": topics_map.get("2026-09-24_Литература.md", "")
                },
                {"num": 6, "time": "17:20 – 18:50", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-25",
            "date_display": "25 сентября 2026 г. (Пятница)",
            "short_day": "25 сен",
            "weekday": "Пт",
            "week": 4,
            "lessons": [
                {"num": 1, "time": "08:30 – 10:00", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {
                    "num": 2, "time": "10:10 – 11:40", "subject": "География", "room": "каб. 302", "teacher": "Бахтина С.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-25_География.md",
                    "notes_md": notes_map.get("2026-09-25_География.md", ""),
                    "topic": topics_map.get("2026-09-25_География.md", "")
                },
                {
                    "num": 3, "time": "12:10 – 13:40", "subject": "География", "room": "каб. 302", "teacher": "Бахтина С.А.",
                    "has_notes": True, "notes_file": "dist/notes/2026-09-25_География.md",
                    "notes_md": notes_map.get("2026-09-25_География.md", ""),
                    "topic": topics_map.get("2026-09-25_География.md", "")
                },
                {"num": 4, "time": "14:00 – 15:30", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        },
        {
            "date": "2026-09-26",
            "date_display": "26 сентября 2026 г. (Суббота)",
            "short_day": "26 сен",
            "weekday": "Сб",
            "week": 4,
            "lessons": [
                {"num": 1, "time": "08:30 – 09:50", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 2, "time": "10:00 – 11:20", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 3, "time": "11:30 – 12:50", "subject": "—", "room": "", "teacher": "", "has_notes": False},
                {"num": 4, "time": "13:00 – 14:20", "subject": "—", "room": "", "teacher": "", "has_notes": False}
            ]
        }
    ]
}

app_json = json.dumps(schedule_data, ensure_ascii=False, indent=2)

html_template = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>Расписание и конспекты — Группа МТО-138 (2026-2027)</title>
  
  <!-- KaTeX CSS -->
  <link rel="stylesheet" href="vendor/katex.min.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" onerror="this.onerror=null;">

  <!-- KaTeX & Marked JS -->
  <script src="vendor/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js" onerror="this.onerror=null;"></script>
  <script src="vendor/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js" onerror="this.onerror=null;"></script>

  <style>
    :root {
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --primary: #2563eb;
      --primary-hover: #1d4ed8;
      --primary-light: #eff6ff;
      --border: #e2e8f0;
      --border-subtle: #cbd5e1;
      --radius: 14px;
      --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.04);
      --shadow-lg: 0 10px 20px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    body {
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding: 24px 16px 80px;
    }

    .container {
      max-width: 1180px;
      margin: 0 auto;
    }

    header {
      margin-bottom: 20px;
      text-align: center;
    }

    .group-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #e0e7ff;
      color: #3730a3;
      padding: 4px 14px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 8px;
    }

    h1 {
      font-size: 1.85rem;
      font-weight: 800;
      color: #1e293b;
      letter-spacing: -0.02em;
    }

    .subtitle {
      color: var(--text-muted);
      font-size: 0.95rem;
      margin-top: 4px;
    }

    /* Main View Navigation Tabs */
    .mode-nav {
      display: flex;
      justify-content: center;
      gap: 12px;
      margin: 20px 0 26px;
    }

    .mode-btn {
      padding: 10px 22px;
      font-size: 0.95rem;
      font-weight: 700;
      border: 1px solid var(--border);
      border-radius: 12px;
      background: #ffffff;
      color: #475569;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .mode-btn:hover {
      background: var(--primary-light);
      color: var(--primary);
      border-color: #bfdbfe;
    }

    .mode-btn.active {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.28);
    }

    /* Week Switcher */
    .week-nav-container {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 12px 16px;
      margin-bottom: 16px;
      box-shadow: var(--shadow-sm);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      max-width: 860px;
      margin-left: auto;
      margin-right: auto;
    }

    .week-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 42px;
      height: 42px;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: #ffffff;
      color: #1e293b;
      cursor: pointer;
      transition: all 0.2s ease;
      flex-shrink: 0;
    }

    .week-btn:hover:not(:disabled) {
      background: var(--primary-light);
      border-color: #bfdbfe;
      color: var(--primary);
    }

    .week-btn:disabled {
      opacity: 0.35;
      cursor: not-allowed;
      border-color: #e2e8f0;
    }

    .week-info {
      text-align: center;
      flex: 1;
    }

    .week-title-text {
      font-size: 1.15rem;
      font-weight: 700;
      color: #0f172a;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }

    .week-badge {
      background: #f1f5f9;
      color: #475569;
      font-size: 0.78rem;
      padding: 2px 8px;
      border-radius: 6px;
      font-weight: 600;
    }

    .week-subtitle-text {
      font-size: 0.86rem;
      color: var(--text-muted);
      margin-top: 2px;
    }

    /* Date Bar */
    .date-bar {
      display: flex;
      gap: 8px;
      background: #e2e8f0;
      padding: 6px;
      border-radius: var(--radius);
      margin-bottom: 20px;
      overflow-x: auto;
      max-width: 860px;
      margin-left: auto;
      margin-right: auto;
    }

    .date-tab {
      flex: 1;
      min-width: 90px;
      padding: 10px 8px;
      border: none;
      background: transparent;
      border-radius: 10px;
      cursor: pointer;
      font-weight: 600;
      font-size: 0.92rem;
      color: #475569;
      transition: all 0.15s ease;
      white-space: nowrap;
      text-align: center;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }

    .date-tab:hover {
      color: var(--primary);
      background: rgba(255, 255, 255, 0.6);
    }

    .date-tab.active {
      background: #ffffff;
      color: var(--primary);
      box-shadow: 0 2px 4px rgba(0,0,0,0.08);
      font-weight: 700;
    }

    .date-tab .tab-badge {
      display: inline-block;
      width: 7px;
      height: 7px;
      background: #2563eb;
      border-radius: 50%;
    }

    .day-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      padding: 0 2px;
      max-width: 860px;
      margin-left: auto;
      margin-right: auto;
    }

    .current-day-title {
      font-size: 1.25rem;
      font-weight: 700;
      color: #1e293b;
    }

    .date-picker {
      padding: 6px 12px;
      border: 1px solid var(--border);
      border-radius: 8px;
      background: white;
      font-size: 0.88rem;
      color: var(--text);
      cursor: pointer;
    }

    /* Lessons List */
    .lessons-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
      max-width: 860px;
      margin: 0 auto;
    }

    .lesson-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.2s ease;
      box-shadow: var(--shadow-sm);
    }

    .lesson-card:hover {
      box-shadow: var(--shadow);
      border-color: #cbd5e1;
    }

    .lesson-card.has-notes {
      border-left: 4px solid var(--primary);
      background: #fafcff;
    }

    .lesson-card.is-empty {
      opacity: 0.6;
      background: #f8fafc;
    }

    .lesson-left {
      display: flex;
      align-items: flex-start;
      gap: 16px;
    }

    .lesson-num {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: #f1f5f9;
      color: #475569;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 0.95rem;
      flex-shrink: 0;
    }

    .lesson-card.has-notes .lesson-num {
      background: #dbeafe;
      color: var(--primary);
    }

    .lesson-info {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }

    .lesson-time {
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    .lesson-subject {
      font-size: 1.08rem;
      font-weight: 700;
      color: #1e293b;
    }

    .lesson-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      font-size: 0.85rem;
      color: #64748b;
      margin-top: 2px;
    }

    .lesson-topic {
      margin-top: 5px;
      font-size: 0.85rem;
      color: #0369a1;
      background: #e0f2fe;
      display: inline-block;
      padding: 3px 8px;
      border-radius: 6px;
      font-weight: 500;
      max-width: 500px;
    }

    .btn-notes {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--primary);
      color: white;
      padding: 9px 18px;
      border-radius: 8px;
      border: none;
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.15s ease;
      white-space: nowrap;
      text-decoration: none;
    }

    .btn-notes:hover {
      background: var(--primary-hover);
    }

    /* ========================================================= */
    /* BY SUBJECT VIEW (Google Docs Outline + Divided Dates)     */
    /* ========================================================= */
    .subjects-view-container {
      display: none;
    }

    .subjects-view-container.active {
      display: block;
    }

    .subject-filter-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: center;
      margin-bottom: 24px;
    }

    .subject-pill {
      padding: 8px 18px;
      border-radius: 20px;
      border: 1px solid var(--border);
      background: #ffffff;
      color: #475569;
      font-size: 0.92rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .subject-pill:hover {
      background: var(--primary-light);
      color: var(--primary);
      border-color: #bfdbfe;
    }

    .subject-pill.active {
      background: #1e293b;
      color: #ffffff;
      border-color: #1e293b;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.2);
    }

    .subjects-layout {
      display: grid;
      grid-template-columns: minmax(0, 1fr) 300px;
      gap: 32px;
      align-items: start;
    }

    .subjects-content {
      display: flex;
      flex-direction: column;
      gap: 28px;
    }

    /* Date Divider Ribbon */
    .date-divider {
      display: flex;
      align-items: center;
      gap: 14px;
      margin: 12px 0 6px;
      scroll-margin-top: 24px;
    }

    .date-divider-line {
      flex: 1;
      height: 2px;
      background: #e2e8f0;
    }

    .date-divider-badge {
      background: #1e293b;
      color: #ffffff;
      font-size: 0.9rem;
      font-weight: 700;
      padding: 5px 18px;
      border-radius: 14px;
      letter-spacing: 0.01em;
      white-space: nowrap;
    }

    /* Subject Note Card */
    .subject-note-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 16px;
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      scroll-margin-top: 24px;
    }

    .subject-note-header {
      padding: 16px 24px;
      background: #f8fafc;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }

    .subject-note-header-left h3 {
      font-size: 1.22rem;
      font-weight: 800;
      color: #0f172a;
    }

    .subject-note-meta {
      font-size: 0.86rem;
      color: var(--text-muted);
      margin-top: 2px;
    }

    .subject-note-body {
      padding: 26px 30px;
    }

    /* Google Docs Style Outline Sidebar */
    .docs-outline {
      position: sticky;
      top: 24px;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 18px 20px;
      box-shadow: var(--shadow-sm);
      max-height: calc(100vh - 48px);
      overflow-y: auto;
    }

    .docs-outline-title {
      font-size: 0.88rem;
      font-weight: 800;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
    }

    .outline-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .outline-item {
      font-size: 0.88rem;
      line-height: 1.4;
    }

    .outline-link {
      display: block;
      padding: 6px 10px;
      border-radius: 8px;
      color: #334155;
      text-decoration: none;
      transition: all 0.15s ease;
      cursor: pointer;
    }

    .outline-link:hover {
      background: var(--primary-light);
      color: var(--primary);
    }

    .outline-link.active {
      background: #dbeafe;
      color: var(--primary);
      font-weight: 700;
    }

    .outline-link.level-date {
      font-weight: 800;
      color: #0f172a;
      padding-top: 10px;
      font-size: 0.92rem;
      border-top: 1px solid #f1f5f9;
      margin-top: 4px;
    }

    .outline-item:first-child .outline-link.level-date {
      border-top: none;
      margin-top: 0;
      padding-top: 4px;
    }

    .outline-link.level-topic {
      padding-left: 12px;
      font-weight: 500;
      color: #1e40af;
      font-size: 0.86rem;
      line-height: 1.45;
    }

    /* ========================================================= */
    /* FULLSCREEN MODAL FOR NOTES                                */
    /* ========================================================= */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: #ffffff;
      z-index: 1000;
      display: none;
      flex-direction: column;
      overflow: hidden;
    }

    .modal-backdrop.active {
      display: flex;
    }

    .modal-header {
      padding: 16px 36px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #ffffff;
      flex-shrink: 0;
      box-shadow: var(--shadow-sm);
    }

    .modal-title-group h2 {
      font-size: 1.45rem;
      font-weight: 800;
      color: #0f172a;
    }

    .modal-meta {
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-top: 3px;
    }

    .btn-close-fullscreen {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 20px;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: #f8fafc;
      color: #1e293b;
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .btn-close-fullscreen:hover {
      background: #fee2e2;
      border-color: #fca5a5;
      color: #991b1b;
    }

    .modal-body {
      flex: 1;
      overflow-y: auto;
      padding: 40px 24px 80px;
      display: flex;
      justify-content: center;
    }

    .modal-content-container {
      width: 100%;
      max-width: 900px;
    }

    /* Markdown & Math Content Styles */
    .notes-rendered {
      font-size: 1.05rem;
      line-height: 1.75;
      color: #334155;
    }

    .notes-rendered h1 {
      font-size: 1.6rem;
      color: #0f172a;
      margin-bottom: 16px;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 8px;
      font-weight: 800;
    }

    .notes-rendered h2 {
      font-size: 1.35rem;
      color: #0f172a;
      margin: 24px 0 12px;
      font-weight: 700;
    }

    .notes-rendered h3 {
      font-size: 1.2rem;
      color: #1e293b;
      margin: 20px 0 10px;
      font-weight: 700;
    }

    .notes-rendered h4 {
      font-size: 1.08rem;
      color: #334155;
      margin: 16px 0 8px;
      font-weight: 700;
    }

    .notes-rendered p {
      margin-bottom: 14px;
    }

    .notes-rendered ul, .notes-rendered ol {
      margin-bottom: 16px;
      padding-left: 26px;
    }

    .notes-rendered li {
      margin-bottom: 6px;
    }

    .notes-rendered blockquote {
      border-left: 4px solid var(--primary);
      background: #eff6ff;
      padding: 12px 18px;
      border-radius: 0 8px 8px 0;
      margin: 16px 0;
      color: #1e3a8a;
    }

    .notes-rendered hr {
      border: none;
      height: 1px;
      background: #e2e8f0;
      margin: 24px 0;
    }

    .notes-rendered u {
      text-decoration: underline;
      text-decoration-color: #2563eb;
      text-underline-offset: 4px;
      text-decoration-thickness: 2px;
      font-weight: 600;
      color: #0f172a;
    }

    .notes-rendered .table-container {
      width: 100%;
      overflow-x: auto;
      margin: 18px 0;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
      background: #ffffff;
    }

    .notes-rendered table,
    .notes-rendered .notes-table {
      width: 100%;
      border-collapse: collapse;
      margin: 0;
      font-size: 0.95rem;
    }

    .notes-rendered th, .notes-rendered td {
      border: 1px solid #e2e8f0;
      padding: 10px 14px;
      text-align: left;
      vertical-align: top;
      line-height: 1.5;
    }

    .notes-rendered th {
      background: #f1f5f9;
      font-weight: 700;
      color: #1e293b;
    }

    .notes-rendered tr:nth-child(even) td {
      background: #f8fafc;
    }

    .notes-rendered tr:hover td {
      background: #f1f5f9;
    }

    /* Math Formulas Styling */
    .math-display-container {
      margin: 18px 0;
      padding: 14px 18px;
      background: #f8fafc;
      border-radius: 8px;
      border: 1px solid #e2e8f0;
      text-align: center;
      overflow-x: auto;
    }

    .katex {
      font-size: 1.15em;
    }

    .katex-display {
      margin: 0.4em 0 !important;
    }

    @media (max-width: 960px) {
      .subjects-layout {
        grid-template-columns: 1fr;
      }
      .docs-outline {
        position: static;
        max-height: none;
        margin-bottom: 24px;
      }
    }

    @media (max-width: 640px) {
      body {
        padding: 16px 10px 60px;
      }
      .week-nav-container {
        padding: 10px 12px;
      }
      .lesson-card {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
      }
      .btn-notes {
        width: 100%;
        justify-content: center;
      }
      .modal-header {
        padding: 12px 16px;
      }
      .modal-body {
        padding: 24px 14px 60px;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="group-badge">Группа МТО-138 • I полугодие 2026-2027</div>
      <h1>Расписание и конспекты</h1>
      <p class="subtitle">Учебные материалы, расписание и записи уроков</p>
    </header>

    <!-- Main Navigation Mode Switcher -->
    <div class="mode-nav">
      <button class="mode-btn active" id="btnModeSchedule" onclick="switchViewMode('schedule')">
        Расписание по дням
      </button>
      <button class="mode-btn" id="btnModeSubjects" onclick="switchViewMode('subjects')">
        Все конспекты по предметам
      </button>
    </div>

    <!-- VIEW 1: Daily Schedule -->
    <div id="viewSchedule">
      <!-- Week Navigation with 2 Arrows -->
      <div class="week-nav-container">
        <button class="week-btn" id="prevWeekBtn" onclick="changeWeek(-1)" title="Предыдущая неделя">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="15 18 9 12 15 6"></polyline>
          </svg>
        </button>

        <div class="week-info">
          <div class="week-title-text" id="weekTitle">
            <span id="weekName">Неделя 4</span>
            <span class="week-badge" id="weekBadge">Текущая неделя</span>
          </div>
          <div class="week-subtitle-text" id="weekDates">21 сен — 26 сен 2026</div>
        </div>

        <button class="week-btn" id="nextWeekBtn" onclick="changeWeek(1)" title="Следующая неделя">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </button>
      </div>

      <!-- Date Tabs for current active week only -->
      <div class="date-bar" id="dateTabs"></div>

      <div class="day-header">
        <div class="current-day-title" id="dayTitle">Загрузка...</div>
        <input type="date" id="dateInput" class="date-picker" value="2026-09-21">
      </div>

      <div class="lessons-list" id="lessonsList"></div>
    </div>

    <!-- VIEW 2: By Subject with Google Docs Outline -->
    <div id="viewSubjects" class="subjects-view-container">
      <div class="subject-filter-bar" id="subjectFilterBar"></div>

      <div class="subjects-layout">
        <!-- Main notes stream with date divider ribbons -->
        <main class="subjects-content" id="subjectsContent"></main>

        <!-- Right-side Google Docs Style Outline -->
        <aside class="docs-outline">
          <div class="docs-outline-title">Оглавление</div>
          <ul class="outline-list" id="outlineNav"></ul>
        </aside>
      </div>
    </div>
  </div>

  <!-- Fullscreen Modal for Notes -->
  <div class="modal-backdrop" id="modalBackdrop">
    <div class="modal-header">
      <div class="modal-title-group">
        <h2 id="modalSubject">Предмет</h2>
        <div class="modal-meta" id="modalMeta">Дата • Время • Кабинет • Преподаватель</div>
      </div>
      <button class="btn-close-fullscreen" onclick="closeModal()" title="Закрыть (Esc)">
        &times; Закрыть
      </button>
    </div>

    <div class="modal-body">
      <div class="modal-content-container">
        <div class="notes-rendered" id="modalNotesRendered"></div>
        <div style="text-align: center; margin-top: 48px; padding-top: 24px; border-top: 1px solid #e2e8f0;">
          <button class="btn-close-fullscreen" onclick="closeModal()">&times; Закрыть конспект</button>
        </div>
      </div>
    </div>
  </div>

  <script>
    const APP = @@APP_DATA@@;

    let currentWeekIndex = 3; // Default to Week 4
    let currentDate = '2026-09-21';
    let currentMode = 'schedule';
    let selectedSubject = 'Все предметы';

    function init() {
      // Date Picker listener
      const dateInput = document.getElementById('dateInput');
      dateInput.addEventListener('change', (e) => {
        selectDate(e.target.value);
      });

      // Keyboard Esc for modal
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
      });

      // Scroll listener for outline highlighting
      window.addEventListener('scroll', updateActiveOutlineItem, { passive: true });

      updateWeekUI();
      renderTabs();
      renderDay(currentDate);
      initSubjectFilterBar();
      renderSubjectsView();
    }

    // ==========================================
    // View Mode Switching
    // ==========================================
    function switchViewMode(mode) {
      currentMode = mode;
      const btnSchedule = document.getElementById('btnModeSchedule');
      const btnSubjects = document.getElementById('btnModeSubjects');
      const viewSchedule = document.getElementById('viewSchedule');
      const viewSubjects = document.getElementById('viewSubjects');

      if (mode === 'schedule') {
        btnSchedule.classList.add('active');
        btnSubjects.classList.remove('active');
        viewSchedule.style.display = 'block';
        viewSubjects.classList.remove('active');
      } else {
        btnSchedule.classList.remove('active');
        btnSubjects.classList.add('active');
        viewSchedule.style.display = 'none';
        viewSubjects.classList.add('active');
        renderSubjectsView();
      }
    }

    // ==========================================
    // Daily Schedule View
    // ==========================================
    function changeWeek(delta) {
      const newIndex = currentWeekIndex + delta;
      if (newIndex < 0 || newIndex >= APP.weeks.length) return;
      currentWeekIndex = newIndex;
      
      const targetWeek = APP.weeks[currentWeekIndex];
      if (!targetWeek.dates.includes(currentDate)) {
        currentDate = targetWeek.dates[0];
        document.getElementById('dateInput').value = currentDate;
      }

      updateWeekUI();
      renderTabs();
      renderDay(currentDate);
    }

    function updateWeekUI() {
      const week = APP.weeks[currentWeekIndex];
      document.getElementById('weekName').textContent = week.title;
      document.getElementById('weekDates').textContent = week.range;
      
      document.getElementById('prevWeekBtn').disabled = (currentWeekIndex === 0);
      document.getElementById('nextWeekBtn').disabled = (currentWeekIndex === APP.weeks.length - 1);
    }

    function renderTabs() {
      const container = document.getElementById('dateTabs');
      const targetWeek = APP.weeks[currentWeekIndex];
      const weekDays = APP.days.filter(d => targetWeek.dates.includes(d.date));

      container.innerHTML = weekDays.map(d => {
        const hasNotesAny = d.lessons.some(l => l.has_notes);
        return `
          <button class="date-tab ${d.date === currentDate ? 'active' : ''}" onclick="selectDate('${d.date}')">
            <span>${d.weekday}, ${d.short_day}</span>
            ${hasNotesAny ? '<span class="tab-badge" title="Есть конспект"></span>' : ''}
          </button>
        `;
      }).join('');
    }

    function selectDate(date) {
      currentDate = date;
      document.getElementById('dateInput').value = date;

      const weekIdx = APP.weeks.findIndex(w => w.dates.includes(date));
      if (weekIdx !== -1 && weekIdx !== currentWeekIndex) {
        currentWeekIndex = weekIdx;
        updateWeekUI();
      }

      renderTabs();
      renderDay(date);
    }

    function renderDay(date) {
      const dayData = APP.days.find(d => d.date === date);
      const titleEl = document.getElementById('dayTitle');
      const listEl = document.getElementById('lessonsList');

      if (!dayData) {
        titleEl.textContent = `${date} (Нет данных)`;
        listEl.innerHTML = `
          <div style="background:white; border-radius:14px; padding:36px; text-align:center; color:#64748b; border:1px dashed #cbd5e1;">
            В этот день занятий нет в расписании.
          </div>
        `;
        return;
      }

      titleEl.textContent = dayData.date_display;

      listEl.innerHTML = dayData.lessons.map(l => {
        const isEmpty = l.subject === '—';
        return `
          <div class="lesson-card ${isEmpty ? 'is-empty' : ''} ${l.has_notes ? 'has-notes' : ''}">
            <div class="lesson-left">
              <div class="lesson-num">${l.num}</div>
              <div class="lesson-info">
                <span class="lesson-time">${l.time}</span>
                <span class="lesson-subject">${l.subject}</span>
                ${(l.room || l.teacher) ? `
                  <div class="lesson-meta">
                    ${l.room ? `<span>${l.room}</span>` : ''}
                    ${l.teacher ? `<span>${l.teacher}</span>` : ''}
                  </div>
                ` : ''}
                ${l.topic ? `<div class="lesson-topic">${l.topic}</div>` : ''}
              </div>
            </div>
            ${l.has_notes ? `
              <div class="lesson-actions">
                <button class="btn-notes" onclick="openNotes('${dayData.date}', ${l.num})">
                  Открыть конспект
                </button>
              </div>
            ` : ''}
          </div>
        `;
      }).join('');
    }

    // ==========================================
    // By Subject View with Google Docs Outline
    // ==========================================
    const SUBJECT_CATEGORIES = [
      'Все предметы',
      'Математика',
      'Физика',
      'Биология',
      'География',
      'Литература',
      'Родная литература',
      'Русский язык'
    ];

    function initSubjectFilterBar() {
      const container = document.getElementById('subjectFilterBar');
      container.innerHTML = SUBJECT_CATEGORIES.map(cat => `
        <button class="subject-pill ${cat === selectedSubject ? 'active' : ''}" onclick="selectSubjectFilter('${cat}')">
          ${cat}
        </button>
      `).join('');
    }

    function selectSubjectFilter(cat) {
      selectedSubject = cat;
      initSubjectFilterBar();
      renderSubjectsView();
    }

    function normalizeSubject(name) {
      if (!name) return '';
      if (name.includes('Математика') || name.includes('Алгебра')) return 'Математика';
      if (name.includes('Физика')) return 'Физика';
      if (name.includes('Биология')) return 'Биология';
      if (name.includes('Родная литература')) return 'Родная литература';
      if (name.includes('Литература')) return 'Литература';
      if (name.includes('География')) return 'География';
      if (name.includes('Русский')) return 'Русский язык';
      return name;
    }

    function getAllNotesList() {
      const notesList = [];
      const seenFiles = new Set();

      APP.days.forEach(d => {
        d.lessons.forEach(l => {
          if (l.has_notes && l.notes_md && l.notes_file && !seenFiles.has(l.notes_file)) {
            seenFiles.add(l.notes_file);
            notesList.push({
              date: d.date,
              date_display: d.date_display,
              lesson: l,
              category: normalizeSubject(l.subject)
            });
          }
        });
      });

      // Chronological sort
      notesList.sort((a, b) => a.date.localeCompare(b.date));
      return notesList;
    }

    function renderSubjectsView() {
      const allNotes = getAllNotesList();
      const filtered = (selectedSubject === 'Все предметы')
        ? allNotes
        : allNotes.filter(n => n.category === selectedSubject);

      const contentEl = document.getElementById('subjectsContent');
      const outlineEl = document.getElementById('outlineNav');

      if (filtered.length === 0) {
        contentEl.innerHTML = `
          <div style="background:white; border-radius:16px; padding:48px; text-align:center; color:#64748b; border:1px dashed #cbd5e1;">
            По выбранному предмету конспектов пока нет.
          </div>
        `;
        outlineEl.innerHTML = `<li class="outline-item" style="color:#94a3b8; padding:8px;">Нет записей</li>`;
        return;
      }

      let contentHtml = '';
      let outlineHtml = '';
      let lastDate = '';

      filtered.forEach((item, index) => {
        const cardId = `note-card-${item.date}-${index}`;

        // Date Divider Ribbon
        if (item.date !== lastDate) {
          lastDate = item.date;
          const dateAnchor = `date-divider-${item.date}`;
          contentHtml += `
            <div class="date-divider" id="${dateAnchor}">
              <div class="date-divider-line"></div>
              <div class="date-divider-badge">${item.date_display}</div>
              <div class="date-divider-line"></div>
            </div>
          `;

          outlineHtml += `
            <li class="outline-item">
              <a class="outline-link level-date" href="#${dateAnchor}" onclick="scrollToElement('${dateAnchor}', event)">
                ${item.date_display.split('(')[0].trim()}
              </a>
            </li>
          `;
        }

        // Render card
        contentHtml += `
          <article class="subject-note-card" id="${cardId}">
            <div class="subject-note-header">
              <div class="subject-note-header-left">
                <h3>${item.lesson.subject}</h3>
                <div class="subject-note-meta">
                  ${item.date_display} • ${item.lesson.time} ${item.lesson.room ? '• ' + item.lesson.room : ''} ${item.lesson.teacher ? '• ' + item.lesson.teacher : ''}
                </div>
              </div>
            </div>
            <div class="subject-note-body">
              <div class="notes-rendered">${renderMarkdown(item.lesson.notes_md, cardId)}</div>
            </div>
          </article>
        `;

        // Outline: Only main topic link (no subtopics)
        const topicLabel = item.lesson.topic || item.lesson.subject;
        const subjectPrefix = (selectedSubject === 'Все предметы') ? `<strong>${item.category}:</strong> ` : '';
        outlineHtml += `
          <li class="outline-item">
            <a class="outline-link level-topic" href="#${cardId}" onclick="scrollToElement('${cardId}', event)">
              ${subjectPrefix}${topicLabel}
            </a>
          </li>
        `;
      });

      contentEl.innerHTML = contentHtml;
      outlineEl.innerHTML = outlineHtml;
    }

    function scrollToElement(id, e) {
      if (e) e.preventDefault();
      const el = document.getElementById(id);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    function updateActiveOutlineItem() {
      if (currentMode !== 'subjects') return;
      const links = document.querySelectorAll('.docs-outline .outline-link');
      if (!links.length) return;

      const fromTop = window.scrollY + 120;
      let currentActive = null;

      links.forEach(link => {
        const targetId = link.getAttribute('href').replace('#', '');
        const target = document.getElementById(targetId);
        if (target && target.offsetTop <= fromTop) {
          currentActive = link;
        }
      });

      links.forEach(l => l.classList.remove('active'));
      if (currentActive) {
        currentActive.classList.add('active');
      }
    }

    // ==========================================
    // Markdown & KaTeX Engine with Heading Anchors
    // ==========================================
    function renderMarkdown(md, baseId = '') {
      if (!md) return '';

      const mathTokens = [];

      // Display math $$...$$
      let text = md.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, (match, expr) => {
        let rendered = '';
        if (window.katex && typeof katex.renderToString === 'function') {
          try {
            rendered = katex.renderToString(expr.trim(), { displayMode: true, throwOnError: false });
          } catch (e) {
            rendered = '<pre class="math-fallback">' + expr.trim() + '</pre>';
          }
        } else {
          rendered = '<div class="math-fallback">' + expr.trim() + '</div>';
        }
        const token = '@@MATH_BLOCK_' + mathTokens.length + '@@';
        mathTokens.push({ token, html: '<div class="math-display-container">' + rendered + '</div>' });
        return '\\n\\n' + token + '\\n\\n';
      });

      // Inline math $...$
      text = text.replace(/\\$([^\\$\\n]+?)\\$/g, (match, expr) => {
        let rendered = '';
        if (window.katex && typeof katex.renderToString === 'function') {
          try {
            rendered = katex.renderToString(expr.trim(), { displayMode: false, throwOnError: false });
          } catch (e) {
            rendered = '<code>' + expr.trim() + '</code>';
          }
        } else {
          rendered = '<code>' + expr.trim() + '</code>';
        }
        const token = '@@MATH_INLINE_' + mathTokens.length + '@@';
        mathTokens.push({ token, html: rendered });
        return token;
      });

      // Parse with fallback/custom renderer with IDs for headings
      let html = parseMarkdownWithAnchors(text, baseId);

      // Restore math tokens
      for (const item of mathTokens) {
        html = html.split('<p>' + item.token + '</p>').join(item.html);
        html = html.split(item.token).join(item.html);
      }

      return html;
    }

    function parseMarkdownWithAnchors(md, baseId) {
      let lines = md.split('\\n');
      let html = '';
      let inList = false;
      let inOrderedList = false;
      let headingIndex = 0;

      for (let i = 0; i < lines.length; i++) {
        let line = lines[i];

        if (line.trim() === '---') {
          if (inList) { html += '</ul>'; inList = false; }
          if (inOrderedList) { html += '</ol>'; inOrderedList = false; }
          html += '<hr>';
          continue;
        }

        if (line.startsWith('# ')) {
          if (inList) { html += '</ul>'; inList = false; }
          if (inOrderedList) { html += '</ol>'; inOrderedList = false; }
          html += '<h1>' + formatInline(line.substring(2)) + '</h1>';
          continue;
        }
        if (line.startsWith('## ')) {
          if (inList) { html += '</ul>'; inList = false; }
          if (inOrderedList) { html += '</ol>'; inOrderedList = false; }
          const title = line.substring(3);
          let idAttr = '';
          if (baseId && !title.includes('ТЕМА УРОКА')) {
            headingIndex++;
            idAttr = ` id="${baseId}-h${headingIndex}" style="scroll-margin-top: 24px;"`;
          }
          html += `<h2${idAttr}>` + formatInline(title) + '</h2>';
          continue;
        }
        if (line.startsWith('### ')) {
          if (inList) { html += '</ul>'; inList = false; }
          if (inOrderedList) { html += '</ol>'; inOrderedList = false; }
          const title = line.substring(4);
          let idAttr = '';
          if (baseId && !title.includes('ТЕМА УРОКА')) {
            headingIndex++;
            idAttr = ` id="${baseId}-h${headingIndex}" style="scroll-margin-top: 24px;"`;
          }
          html += `<h3${idAttr}>` + formatInline(title) + '</h3>';
          continue;
        }
        if (line.startsWith('#### ')) {
          if (inList) { html += '</ul>'; inList = false; }
          if (inOrderedList) { html += '</ol>'; inOrderedList = false; }
          const title = line.substring(5);
          let idAttr = '';
          if (baseId && !title.includes('ТЕМА УРОКА')) {
            headingIndex++;
            idAttr = ` id="${baseId}-h${headingIndex}" style="scroll-margin-top: 24px;"`;
          }
          html += `<h4${idAttr}>` + formatInline(title) + '</h4>';
          continue;
        }

        if (line.startsWith('> ')) {
          if (inList) { html += '</ul>'; inList = false; }
          if (inOrderedList) { html += '</ol>'; inOrderedList = false; }
          html += '<blockquote>' + formatInline(line.substring(2)) + '</blockquote>';
          continue;
        }

        // Markdown Table Parser
        if (line.trim().startsWith('|') && line.trim().endsWith('|')) {
          if (inList) { html += '</ul>'; inList = false; }
          if (inOrderedList) { html += '</ol>'; inOrderedList = false; }

          let tableLines = [];
          while (i < lines.length && lines[i].trim().startsWith('|') && lines[i].trim().endsWith('|')) {
            tableLines.push(lines[i].trim());
            i++;
          }
          i--;

          if (tableLines.length >= 2) {
            let headerLine = tableLines[0];
            let sepLine = tableLines[1];
            let isSep = /^\\|(\\s*:?-+:?\\s*\\|)+$/.test(sepLine);
            if (isSep) {
              const parseRowCells = (row) => {
                let raw = row.substring(1, row.length - 1);
                return raw.split('|').map(c => c.trim());
              };

              let alignments = parseRowCells(sepLine).map(col => {
                let left = col.startsWith(':');
                let right = col.endsWith(':');
                if (left && right) return 'center';
                if (right) return 'right';
                return 'left';
              });

              let headers = parseRowCells(headerLine);
              let tableHtml = '<div class="table-container"><table class="notes-table">';
              tableHtml += '<thead><tr>';
              headers.forEach((h, idx) => {
                let align = alignments[idx] || 'left';
                tableHtml += `<th style="text-align: ${align};">` + formatInline(h) + '</th>';
              });
              tableHtml += '</tr></thead><tbody>';

              for (let r = 2; r < tableLines.length; r++) {
                let rowCells = parseRowCells(tableLines[r]);
                tableHtml += '<tr>';
                for (let c = 0; c < headers.length; c++) {
                  let cellContent = rowCells[c] !== undefined ? rowCells[c] : '';
                  let align = alignments[c] || 'left';
                  tableHtml += `<td style="text-align: ${align};">` + formatInline(cellContent) + '</td>';
                }
                tableHtml += '</tr>';
              }
              tableHtml += '</tbody></table></div>';
              html += tableHtml;
              continue;
            }
          }
          for (let tl of tableLines) {
            html += '<p>' + formatInline(tl) + '</p>';
          }
          continue;
        }

        if (line.trim().startsWith('* ') || line.trim().startsWith('- ')) {
          if (inOrderedList) { html += '</ol>'; inOrderedList = false; }
          if (!inList) { html += '<ul>'; inList = true; }
          html += '<li>' + formatInline(line.trim().substring(2)) + '</li>';
          continue;
        } else if (inList) {
          html += '</ul>';
          inList = false;
        }

        if (/^\\d+\\.\\s/.test(line.trim())) {
          if (inList) { html += '</ul>'; inList = false; }
          if (!inOrderedList) { html += '<ol>'; inOrderedList = true; }
          let itemText = line.trim().replace(/^\\d+\\.\\s+/, '');
          html += '<li>' + formatInline(itemText) + '</li>';
          continue;
        } else if (inOrderedList) {
          html += '</ol>';
          inOrderedList = false;
        }

        if (line.trim().length > 0) {
          html += '<p>' + formatInline(line) + '</p>';
        }
      }
      if (inList) html += '</ul>';
      if (inOrderedList) html += '</ol>';
      return html;
    }

    function formatInline(str) {
      return str
        .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
        .replace(/\\*(.*?)\\*/g, '<em>$1</em>')
        .replace(/`([^`]+)`/g, '<code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-size:0.9em;">$1</code>');
    }

    // ==========================================
    // Fullscreen Modal
    // ==========================================
    function openNotes(date, num) {
      const day = APP.days.find(d => d.date === date);
      if (!day) return;
      const lesson = day.lessons.find(l => l.num === num);
      if (!lesson || !lesson.has_notes) return;

      document.getElementById('modalSubject').textContent = lesson.subject;
      document.getElementById('modalMeta').textContent = `${day.date_display} • ${lesson.time} ${lesson.room ? '• ' + lesson.room : ''} ${lesson.teacher ? '• ' + lesson.teacher : ''}`;
      document.getElementById('modalNotesRendered').innerHTML = renderMarkdown(lesson.notes_md);

      document.getElementById('modalBackdrop').classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeModal() {
      document.getElementById('modalBackdrop').classList.remove('active');
      document.body.style.overflow = '';
    }

    window.onload = init;
  </script>
</body>
</html>
"""

full_html = html_template.replace("@@APP_DATA@@", app_json)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)

os.makedirs("html", exist_ok=True)
with open("html/index.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated index.html and html/index.html with all 3 weeks and 16 notes!")
