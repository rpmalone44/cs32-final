from flask import Flask, request, render_template
from main import questions, display_question, get_answer, calculate_score, provide_feedback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    # get user information
    name = request.form['name']
    age = request.form['age']
    education_level = request.form['education_level']
    interests = []
    skills = []

    num_interests = int(request.form['num_interests'])
    num_skills = int(request.form['num_skills'])

    for i in range(num_interests):
        interest = request.form[f'interest_{i+1}']
        interests.append(interest)

    for i in range(num_skills):
        skill = request.form[f'skill_{i+1}']
        skills.append(skill)

    # display questions and record answers
    answers = []
    for question in main.questions:
        answers.append(request.form[f'answer_{question["id"]}'])

    # calculate score and give answer
    score = main.calculate_score(answers)
    feedback = main.provide_feedback(score)

    return render_template('result.html', name=name, age=age, education_level=education_level, interests=interests, skills=skills, feedback=feedback)

if __name__ == '__main__':
    app.run()
