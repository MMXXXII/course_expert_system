from courses import COURSES
from rules import RULES


def check_course(profile, course):
    facts = profile.copy()
    facts.update({
        "course_topic": course["topic"],
        "course_level": course["level"],
        "course_goal": course["goal"],
        "course_format": course["format"],
        "format_match": profile["format"] == course["format"],
        "goal_match": profile["goal"] == course["goal"],
        "practice": course["practice"],
        "certificate": course["certificate"],
        "teacher": course["teacher"],
        "short_course": course["weeks"] <= 7
    })

    if course["level"] == profile["level"]:
        facts["level_relation"] = "same"
    elif course["level"] < profile["level"]:
        facts["level_relation"] = "lower"
    else:
        facts["level_relation"] = "higher"

    if course["price"] == 0:
        facts["budget_state"] = "free"
    elif course["price"] <= profile["budget"]:
        facts["budget_state"] = "within"
    else:
        facts["budget_state"] = "over"

    if course["hours"] > profile["hours"]:
        facts["time_state"] = "over"
    elif course["hours"] * 2 <= profile["hours"]:
        facts["time_state"] = "light"
    else:
        facts["time_state"] = "fits"

    score = 0
    trace = []

    for number, conditions, conclusion, points, reason in RULES:
        if all(facts.get(key) == value for key, value in conditions.items()):
            facts.update(conclusion)
            score += points
            trace.append((number, reason, points, conclusion))

    return {"course": course, "score": score, "facts": facts, "trace": trace}


def recommend(profile):
    checked = [check_course(profile, course) for course in COURSES]
    matched = [item for item in checked if item["facts"].get("candidate")]
    matched.sort(key=lambda item: (-item["score"], item["course"]["price"], item["course"]["hours"]))
    return matched, checked