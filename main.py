
import tkinter as tk
from tkinter import ttk
from engine import infer
from rules import RULES

options = {
    "interest": {
        "Программирование": "programming",
        "Базы данных": "databases",
        "Искусственный интеллект": "ai",
        "Английский язык": "languages"
    },
    "level": {
        "Начинающий": "beginner",
        "Средний": "intermediate",
        "Продвинутый": "advanced"
    },
    "time": {
        "Мало": "low",
        "Средне": "medium",
        "Много": "high"
    },
    "budget": {
        "Бесплатно": "free",
        "Можно платно": "paid"
    }
}


def recommend():
    profile = {
        key: options[key][boxes[key].get()]
        for key in options
    }

    facts, fired = infer(profile)

    result.config(state="normal")
    result.delete("1.0", "end")

    result.insert(
        "end",
        "Рекомендуемый курс:\n" +
        facts.get("course", "Не найден") + "\n\n"
    )

    result.insert(
        "end",
        "Формат обучения:\n" +
        facts.get("format", "Не определён") + "\n\n"
    )

    result.insert("end", "Сработавшие правила:\n\n")

    for number, conditions, new_facts, explanation in fired:
        result.insert("end", number + ": " + explanation + "\n")
        result.insert("end", "Новый факт: " + str(new_facts) + "\n\n")

    result.config(state="disabled")


def show_rules():
    window = tk.Toplevel(root)
    window.title("База знаний")
    window.geometry("720x520")

    text = tk.Text(window, wrap="word", font=("Arial", 11))
    text.pack(fill="both", expand=True, padx=10, pady=10)

    for number, conditions, new_facts, explanation in RULES:
        text.insert(
            "end",
            number + "\nЕСЛИ " + str(conditions) +
            "\nТО " + str(new_facts) +
            "\n" + explanation + "\n\n"
        )

    text.config(state="disabled")


root = tk.Tk()
root.title("Экспертная система - Выбор курса")
root.geometry("780x600")
root.configure(bg="#f2f6ff")

tk.Label(
    root,
    text="Экспертная система выбора курса",
    font=("Arial", 18, "bold"),
    bg="#f2f6ff"
).pack(pady=16)

form = tk.Frame(root, bg="#f2f6ff")
form.pack(pady=5)

boxes = {}

labels = {
    "interest": "Интересы",
    "level": "Уровень подготовки",
    "time": "Свободное время",
    "budget": "Бюджет"
}

for key in options:
    tk.Label(
        form,
        text=labels[key],
        bg="#f2f6ff",
        font=("Arial", 11)
    ).pack(anchor="w")

    boxes[key] = ttk.Combobox(
        form,
        values=list(options[key]),
        state="readonly",
        width=36
    )

    boxes[key].current(0)
    boxes[key].pack(pady=(3, 10))

tk.Button(
    root,
    text="Подобрать курс",
    command=recommend,
    bg="#2a5db0",
    fg="white",
    font=("Arial", 11, "bold")
).pack(pady=8)

tk.Button(
    root,
    text="Показать 44 правила",
    command=show_rules
).pack(pady=4)

result = tk.Text(
    root,
    height=12,
    wrap="word",
    font=("Arial", 11)
)

result.pack(fill="both", expand=True, padx=20, pady=12)
result.insert("end", "Выбери параметры и нажми «Подобрать курс».")
result.config(state="disabled")

root.mainloop()
