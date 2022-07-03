from flask import Flask
import utils

candidats = utils.create_table()
app = Flask(__name__)

@app.route("/")
def page_test():
    summary_line= "<pre>"
    for candidat in candidats:
        summary_line += utils.vuvestu_stroky(candidat)
    summary_line += "<pre>"
    return summary_line

@app.route('/candidates/<candidat>')
def page_candidates(candidat):
    for x in candidats:
        if x['name'] == candidat:
            return utils.vuvestu_stroky(x)
    else: return "Кондитат с таким именем не найден"


@app.route("/skills/<skill>")
def page_skills(skill):
    summary_line = "<pre>"
    for candidat in candidats:
        if skill.upper() in candidat['skills'].upper():
            summary_line += utils.vuvestu_stroky(candidat)
    summary_line += "<pre>"
    if len(summary_line) == 10:
        return "Кондитат с таким навыком не найден"
    else:
        return summary_line


if __name__ == "__main__":
    app.run()