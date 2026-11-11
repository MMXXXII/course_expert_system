
from rules import RULES


def infer(profile):
    facts = profile.copy()
    history = []
    used = set()

    while True:
        found = False

        for number, conditions, result, explanation in RULES:
            if number in used:
                continue

            if all(facts.get(key) == value for key, value in conditions.items()):
                if any(key in facts and facts[key] != value for key, value in result.items()):
                    continue

                facts.update(result)
                history.append((number, conditions, result, explanation))
                used.add(number)
                found = True

        if not found:
            break

    return facts, history
