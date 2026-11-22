from courses import COURSES
from rules import RULES


def check_course(profile, course):
    if course["level"] == profile["level"]:
        relation = "same"
    elif course["level"] < profile["level"]:
        relation = "lower"
    else:
        relation = "higher"

    if course["price"] == 0:
        budget_state = "free"
    elif course["price"] <= profile["budget"]:
        budget_state = "within"
    else:
        budget_state = "over"

    if course["hours"] > profile["hours"]:
        time_state = "over"
    elif course["hours"] <= profile["hours"] / 2:
        time_state = "light"
    else:
        time_state = "fits"

    facts = profile.copy()
    facts.update({
        "course_topic": course["topic"],
        "course_level": course["level"],
        "course_goal": course["goal"],
        "course_format": course["format"],
        "level_relation": relation,
        "budget_state": budget_state,
        "time_state": time_state,
        "format_match": profile["format"] == course["format"],
        "goal_match": profile["goal"] == course["goal"],
        "practice": course["practice"],
        "certificate": course["certificate"],
        "teacher": course["teacher"],
        "short_course": course["weeks"] <= 7
    })

    score = 0
    trace = []
    fired = set()

    while True:
        changed = False
        for number, condition, conclusion, points, reason in RULES:
            if number in fired:
                continue
            if all(facts.get(key) == value for key, value in condition.items()):
                facts.update(conclusion)
                score += points
                trace.append((number, reason, points, conclusion))
                fired.add(number)
                changed = True
        if not changed:
            break

    return {"course": course, "score": score, "facts": facts, "trace": trace}


def recommend(profile):
    checked = [check_course(profile, course) for course in COURSES]
    matched = [item for item in checked if item["facts"].get("candidate")]
    matched.sort(key=lambda item: (-item["score"], item["course"]["price"], item["course"]["hours"]))
    return matched, checked
