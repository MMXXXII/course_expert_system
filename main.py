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
    "budget": "Бюджет на обучение", "format": "Формат обучения", "goal": "Цель обучения"
}


def write(widget, text):
    widget.config(state="normal")
    widget.delete("1.0", "end")
    widget.insert("end", text)
    widget.config(state="disabled")


def show_result():
    profile = {key: choices[key][fields[key].get()] for key in choices}
    found, checked = recommend(profile)

    result_text = "Найдено подходящих курсов: " + str(len(found)) + "\n\n"
    details_text = "Проверено курсов: " + str(len(checked)) + "\n\n"

    if not found:
        result_text += "Подходящих вариантов нет. Попробуйте изменить бюджет, время или уровень подготовки."
    else:
        for index, item in enumerate(found[:3], 1):
            course = item["course"]
            mode = "онлайн" if course["format"] == "online" else "очно"
            result_text += f"{index}. {course['name']}\n"
            result_text += f"   {item['score']} баллов  |  {course['price']} руб.  |  {course['hours']} ч/нед.\n"
            result_text += f"   {mode}, {course['weeks']} недель\n\n"

        best = found[0]
        details_text += "Лучший вариант: " + best["course"]["name"] + "\n\n"
        details_text += "Сработавшие правила:\n"
        for number, reason, points, conclusion in best["trace"]:
            points_text = f" ({points:+d} баллов)" if points else ""
            details_text += f"{number}: {reason}{points_text}\n"

    details_text += "\nОтклонённые курсы выбранного направления:\n"
    rejected = 0
    for item in checked:
        if item["course"]["topic"] != profile["topic"] or item["facts"].get("candidate"):
            continue
        reasons = [reason for _, reason, _, conclusion in item["trace"] if False in conclusion.values()]
        details_text += item["course"]["name"] + ": " + "; ".join(reasons) + "\n"
        rejected += 1
    if rejected == 0:
        details_text += "Нет\n"

    write(output, result_text)
    write(details, details_text)
    tabs.select(0)


root = tk.Tk()
root.title("Экспертная система – Выбор учебного курса")
root.geometry("900x690")
root.minsize(740, 600)
root.configure(bg="#f2f5fa")

style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#f2f5fa")
style.configure("TLabel", background="#f2f5fa", font=("Segoe UI", 10))
style.configure("TLabelframe", background="#f2f5fa")
style.configure("TLabelframe.Label", background="#f2f5fa", font=("Segoe UI", 11, "bold"))
style.configure("Accent.TButton", background="#2563eb", foreground="white", padding=10, font=("Segoe UI", 10, "bold"))
style.map("Accent.TButton", background=[("active", "#1d4ed8")])
style.configure("TNotebook.Tab", padding=(16, 8))

header = ttk.Label(root, text="Подбор учебного курса", font=("Segoe UI", 21, "bold"))
header.pack(anchor="w", padx=30, pady=(20, 3))

form = ttk.LabelFrame(root, text="Анкета студента", padding=14)
form.pack(fill="x", padx=30)
fields = {}

for index, key in enumerate(choices):
    row = index // 2
    col = index % 2
    ttk.Label(form, text=labels[key]).grid(row=row * 2, column=col, sticky="w", padx=8, pady=(5, 3))
    fields[key] = ttk.Combobox(form, state="readonly", values=list(choices[key]), width=33)
    fields[key].current(0)
    fields[key].grid(row=row * 2 + 1, column=col, sticky="ew", padx=8, pady=(0, 10))

form.columnconfigure(0, weight=1)
form.columnconfigure(1, weight=1)

ttk.Button(root, text="Подобрать курс", style="Accent.TButton", command=show_result).pack(anchor="w", padx=30, pady=14)

tabs = ttk.Notebook(root)
tabs.pack(fill="both", expand=True, padx=30, pady=(0, 12))

output = tk.Text(tabs, wrap="word", font=("Segoe UI", 11), padx=16, pady=16, relief="flat")
details = tk.Text(tabs, wrap="word", font=("Segoe UI", 10), padx=16, pady=16, relief="flat")
knowledge = tk.Text(tabs, wrap="word", font=("Consolas", 10), padx=16, pady=16, relief="flat")

tabs.add(output, text="Рекомендации")
tabs.add(details, text="Объяснение")
tabs.add(knowledge, text="База знаний")

rules_text = ""
for number, conditions, conclusion, points, reason in RULES:
    action = str(conclusion) if conclusion else f"баллы: {points:+d}"
    rules_text += f"{number}  ЕСЛИ {conditions}\nТО {action}\n{reason}\n\n"
write(knowledge, rules_text)

ttk.Label(root, text=f"В базе знаний {len(RULES)} правил  |  В каталоге {len(COURSES)} курса").pack(anchor="w", padx=30, pady=(0, 12))

show_result()
root.mainloop()
