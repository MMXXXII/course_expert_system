import tkinter as tk
from tkinter import ttk
from engine import recommend
from rules import RULES
from courses import COURSES


choices = {
    "topic": {"Программирование": "programming", "Базы данных": "databases", "Искусственный интеллект": "ai", "Английский язык": "languages"},
    "level": {"Начинающий": 0, "Средний": 1, "Продвинутый": 2},
    "hours": {"3 часа в неделю": 3, "6 часов в неделю": 6, "10 часов в неделю": 10},
    "budget": {"0 руб.": 0, "До 5 000 руб.": 5000, "До 10 000 руб.": 10000, "До 15 000 руб.": 15000},
    "format": {"Онлайн": "online", "Очно": "offline"},
    "goal": {"Изучить теорию": "theory", "Получить практические навыки": "practice", "Подготовиться к работе": "career"}
}

labels = {
    "topic": "Направление", "level": "Уровень подготовки", "hours": "Свободное время в неделю",
    "budget": "Бюджет на курс", "format": "Формат обучения", "goal": "Цель обучения"
}


def show_result():
    profile = {key: choices[key][fields[key].get()] for key in choices}
    found, checked = recommend(profile)
    output.config(state="normal")
    output.delete("1.0", "end")
    details.config(state="normal")
    details.delete("1.0", "end")

    if not found:
        output.insert("end", "Подходящих курсов нет.\n\nПопробуйте увеличить бюджет, количество свободных часов или изменить направление.")
        details.insert("end", "Проверено курсов: " + str(len(checked)) + "\n\n")
        for item in checked:
            if item["course"]["topic"] == profile["topic"]:
                reasons = [reason for _, reason, _, changes in item["trace"] if changes.get("level_ok") is False or changes.get("budget_ok") is False or changes.get("time_ok") is False]
                details.insert("end", item["course"]["name"] + ": " + "; ".join(reasons) + "\n")
    else:
        output.insert("end", "Найдено подходящих курсов: " + str(len(found)) + "\n\n")
        for index, item in enumerate(found[:3], 1):
            course = item["course"]
            output.insert("end", str(index) + ". " + course["name"] + "\n")
            output.insert("end", "   Баллы: " + str(item["score"]) + " | Цена: " + str(course["price"]) + " руб. | " + str(course["hours"]) + " ч/нед.\n")
            output.insert("end", "   Формат: " + ("онлайн" if course["format"] == "online" else "очно") + " | " + str(course["weeks"]) + " недель\n\n")

        best = found[0]
        details.insert("end", "Лучший курс: " + best["course"]["name"] + "\n")
        details.insert("end", "Набрано баллов: " + str(best["score"]) + "\n\n")
        details.insert("end", "Ход логического вывода:\n\n")
        for number, reason, points, changes in best["trace"]:
            details.insert("end", number + " - " + reason)
            if points:
                details.insert("end", " (" + ("+" if points > 0 else "") + str(points) + " баллов)")
            if changes:
                details.insert("end", " → " + ", ".join(changes))
            details.insert("end", "\n")
    output.config(state="disabled")
    details.config(state="disabled")
    tabs.select(0)


root = tk.Tk()
root.title("Экспертная система - Выбор учебного курса")
root.geometry("920x670")
root.minsize(780, 570)
root.configure(bg="#eef3fa")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=7)
style.configure("TLabel", background="#eef3fa", font=("Arial", 10))

header = ttk.Label(root, text="Экспертная система выбора учебного курса", font=("Arial", 18, "bold"))
header.pack(pady=(18, 10))

form = ttk.Frame(root)
form.pack(fill="x", padx=24)
fields = {}

for index, key in enumerate(choices):
    ttk.Label(form, text=labels[key]).grid(row=index // 2 * 2, column=index % 2, sticky="w", padx=10, pady=(6, 2))
    fields[key] = ttk.Combobox(form, state="readonly", values=list(choices[key]), width=35)
    fields[key].current(0)
    fields[key].grid(row=index // 2 * 2 + 1, column=index % 2, sticky="ew", padx=10, pady=(0, 6))

form.columnconfigure(0, weight=1)
form.columnconfigure(1, weight=1)

ttk.Button(root, text="Подобрать курс", command=show_result).pack(pady=12)

tabs = ttk.Notebook(root)
tabs.pack(fill="both", expand=True, padx=24, pady=(0, 22))

output = tk.Text(tabs, font=("Arial", 11), wrap="word", padx=12, pady=12)
details = tk.Text(tabs, font=("Arial", 10), wrap="word", padx=12, pady=12)
knowledge = tk.Text(tabs, font=("Arial", 10), wrap="word", padx=12, pady=12)

tabs.add(output, text="Рекомендации")
tabs.add(details, text="Объяснение")
tabs.add(knowledge, text="База знаний")

for number, conditions, conclusion, points, reason in RULES:
    knowledge.insert("end", number + "  ЕСЛИ " + str(conditions) + "\n")
    knowledge.insert("end", "ТО " + (str(conclusion) if conclusion else "оценка " + str(points)) + "\n")
    knowledge.insert("end", reason + "\n\n")

knowledge.insert("end", "Всего правил: " + str(len(RULES)) + "\n")
knowledge.insert("end", "Курсов в каталоге: " + str(len(COURSES)) + "\n")
knowledge.config(state="disabled")
show_result()
root.mainloop()
