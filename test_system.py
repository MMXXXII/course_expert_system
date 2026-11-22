from itertools import product
from engine import recommend
from courses import COURSES
from rules import RULES

used_rules = set()
tested = 0

for topic, level, hours, budget, study_format, goal in product(
    ["programming", "databases", "ai", "languages"],
    [0, 1, 2],
    [3, 6, 10],
    [0, 5000, 10000, 15000],
    ["online", "offline"],
    ["theory", "practice", "career"]
):
    profile = {
        "topic": topic,
        "level": level,
        "hours": hours,
        "budget": budget,
        "format": study_format,
        "goal": goal
    }

    found, checked = recommend(profile)

    assert len(checked) == len(COURSES)
    assert found
    assert found == sorted(found, key=lambda x: (-x["score"], x["course"]["price"], x["course"]["hours"]))

    for item in checked:
        course = item["course"]
        suitable = (
            course["topic"] == topic
            and course["level"] <= level
            and course["hours"] <= hours
            and course["price"] <= budget
        )
        assert bool(item["facts"].get("candidate")) == suitable

        conclusions = {}
        for number, reason, points, new_facts in item["trace"]:
            used_rules.add(number)
            assert reason
            for key, value in new_facts.items():
                assert key not in conclusions or conclusions[key] == value
                conclusions[key] = value

    tested += 1

assert len(RULES) >= 40
assert len(used_rules) == len(RULES)

examples = [
    ({"topic": "programming", "level": 0, "hours": 3, "budget": 0, "format": "online", "goal": "theory"}, "Python с нуля"),
    ({"topic": "databases", "level": 1, "hours": 6, "budget": 5000, "format": "online", "goal": "practice"}, "SQL: запросы и задачи"),
    ({"topic": "ai", "level": 2, "hours": 10, "budget": 15000, "format": "offline", "goal": "career"}, "Разработка моделей ИИ"),
    ({"topic": "languages", "level": 1, "hours": 3, "budget": 0, "format": "online", "goal": "career"}, "Английский для программистов")
]

for profile, expected in examples:
    found, checked = recommend(profile)
    assert found[0]["course"]["name"] == expected

profile = {"topic": "ai", "level": 0, "hours": 1, "budget": 0, "format": "online", "goal": "theory"}
found, checked = recommend(profile)
assert not found

print("Проверено анкет:", tested)
print("Проверено учебных курсов:", len(COURSES))
print("Сработавших правил:", len(used_rules), "из", len(RULES))
print("Проверено дополнительных сценариев:", len(examples) + 1)
print("Ошибок не найдено")
