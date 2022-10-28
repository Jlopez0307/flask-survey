from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cats'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def app_home():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', survey_title = title, instructions = instructions)

@app.route('/questions/<int:q_num>')
def question(q_num):
    question = satisfaction_survey.questions[q_num]
    return render_template('question_0.html', q_num=q_num , question = question)

@app.route('/answer', methods = ['POST'])
def handle_answers():
    return redirect(f"/questions/{q_num}")

