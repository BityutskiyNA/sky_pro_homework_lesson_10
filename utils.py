import json

def create_table():
    file = open("candidates.json", encoding="utf-8")
    questions = json.load(file)
    return questions


def vuvestu_stroky(candidate):
    summary_line = f"Имя кандидата - {candidate['name']} <br>Позиция кандидата {candidate['position']} " \
              f"<br>{candidate['skills']} <br><br>"
    return summary_line