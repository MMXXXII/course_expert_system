
RULES = [
    ("R01", {"interest": "programming"}, {"direction": "python"}, "Интерес к программированию."),
    ("R02", {"interest": "databases"}, {"direction": "db"}, "Интерес к базам данных."),
    ("R03", {"interest": "ai"}, {"direction": "ai"}, "Интерес к искусственному интеллекту."),
    ("R04", {"interest": "languages"}, {"direction": "english"}, "Интерес к английскому языку."),

    ("R05", {"level": "beginner"}, {"stage": "basic"}, "Начальный уровень подготовки."),
    ("R06", {"level": "intermediate"}, {"stage": "middle"}, "Средний уровень подготовки."),
    ("R07", {"level": "advanced"}, {"stage": "advanced"}, "Продвинутый уровень подготовки."),

    ("R08", {"time": "low"}, {"pace": "short"}, "Мало свободного времени."),
    ("R09", {"time": "medium"}, {"pace": "full"}, "Достаточно свободного времени."),
    ("R10", {"time": "high"}, {"pace": "full"}, "Много свободного времени."),

    ("R11", {"budget": "free"}, {"payment": "free"}, "Требуется бесплатное обучение."),
    ("R12", {"budget": "paid"}, {"payment": "paid"}, "Возможно платное обучение."),

    ("R13", {"direction": "python", "stage": "basic", "pace": "short"}, {"course": "Python: быстрый старт"}, "Новичку подходит короткий курс Python."),
    ("R14", {"direction": "python", "stage": "basic", "pace": "full"}, {"course": "Python с нуля"}, "Подходит полноценный курс Python."),
    ("R15", {"direction": "python", "stage": "middle", "pace": "short"}, {"course": "Python: практический интенсив"}, "Подходит интенсив по Python."),
    ("R16", {"direction": "python", "stage": "middle", "pace": "full"}, {"course": "Python: ООП и проекты"}, "Можно изучать ООП и создавать проекты."),
    ("R17", {"direction": "python", "stage": "advanced", "pace": "short"}, {"course": "Python: интенсив по архитектуре"}, "Подходит короткий продвинутый курс."),
    ("R18", {"direction": "python", "stage": "advanced", "pace": "full"}, {"course": "Python: асинхронность и архитектура"}, "Подходит углублённый курс Python."),

    ("R19", {"direction": "db", "stage": "basic", "pace": "short"}, {"course": "SQL: основные запросы"}, "Подходит короткий курс по SQL."),
    ("R20", {"direction": "db", "stage": "basic", "pace": "full"}, {"course": "SQL с нуля"}, "Подходит полный курс SQL."),
    ("R21", {"direction": "db", "stage": "middle", "pace": "short"}, {"course": "SQL: практический интенсив"}, "Подходит интенсив по базам данных."),
    ("R22", {"direction": "db", "stage": "middle", "pace": "full"}, {"course": "Базы данных: индексы и транзакции"}, "Можно изучать продвинутый SQL."),
    ("R23", {"direction": "db", "stage": "advanced", "pace": "short"}, {"course": "SQL: оптимизация запросов"}, "Подходит интенсив по оптимизации."),
    ("R24", {"direction": "db", "stage": "advanced", "pace": "full"}, {"course": "Базы данных: HighLoad"}, "Подходит углублённое изучение баз данных."),

    ("R25", {"direction": "ai", "stage": "basic", "pace": "short"}, {"course": "ИИ: быстрое введение"}, "Подходит краткое знакомство с ИИ."),
    ("R26", {"direction": "ai", "stage": "basic", "pace": "full"}, {"course": "Искусственный интеллект с нуля"}, "Подходит полноценный вводный курс."),
    ("R27", {"direction": "ai", "stage": "middle", "pace": "short"}, {"course": "ИИ: готовые модели и API"}, "Подходит практический курс ИИ."),
    ("R28", {"direction": "ai", "stage": "middle", "pace": "full"}, {"course": "Машинное обучение"}, "Можно изучать алгоритмы машинного обучения."),
    ("R29", {"direction": "ai", "stage": "advanced", "pace": "short"}, {"course": "Нейросети: интенсив"}, "Подходит интенсив по нейросетям."),
    ("R30", {"direction": "ai", "stage": "advanced", "pace": "full"}, {"course": "ИИ: обучение моделей с нуля"}, "Подходит углублённый курс ИИ."),

    ("R31", {"direction": "english", "stage": "basic", "pace": "short"}, {"course": "Английский: основы грамматики"}, "Подходят короткие занятия."),
    ("R32", {"direction": "english", "stage": "basic", "pace": "full"}, {"course": "Английский с нуля для IT"}, "Подходит базовый курс английского."),
    ("R33", {"direction": "english", "stage": "middle", "pace": "short"}, {"course": "Английский: разговорный интенсив"}, "Подходит интенсив разговорного языка."),
    ("R34", {"direction": "english", "stage": "middle", "pace": "full"}, {"course": "Английский для командной работы"}, "Подходит разговорный курс."),
    ("R35", {"direction": "english", "stage": "advanced", "pace": "short"}, {"course": "Английский для IT-собеседований"}, "Подходит подготовка к собеседованию."),
    ("R36", {"direction": "english", "stage": "advanced", "pace": "full"}, {"course": "Английский для международных проектов"}, "Подходит профессиональный английский."),

    ("R37", {"direction": "python", "payment": "free"}, {"format": "Бесплатные уроки Python"}, "Подходят бесплатные материалы."),
    ("R38", {"direction": "python", "payment": "paid"}, {"format": "Python с преподавателем"}, "Подходит платное обучение."),
    ("R39", {"direction": "db", "payment": "free"}, {"format": "Бесплатные SQL-тренажёры"}, "Подходят бесплатные задания."),
    ("R40", {"direction": "db", "payment": "paid"}, {"format": "SQL с преподавателем"}, "Подходит платное обучение SQL."),
    ("R41", {"direction": "ai", "payment": "free"}, {"format": "Бесплатные материалы по ИИ"}, "Подходит самостоятельное обучение."),
    ("R42", {"direction": "ai", "payment": "paid"}, {"format": "ИИ с наставником"}, "Подходит платный курс ИИ."),
    ("R43", {"direction": "english", "payment": "free"}, {"format": "Бесплатные уроки английского"}, "Подходят бесплатные занятия."),
    ("R44", {"direction": "english", "payment": "paid"}, {"format": "Английский с преподавателем"}, "Подходят платные занятия.")
]
