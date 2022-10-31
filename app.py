from flask import Flask, render_template, redirect, request, flash
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
    res = responses
    if len(res) != q_num:
        flash('Please answer questions in order')
        return redirect(f"/questions/{len(res)}")

    if len(res) == len(satisfaction_survey.questions):
        return redirect('/survey_done')
    
    q_choices = satisfaction_survey.questions[q_num].choices


    question = satisfaction_survey.questions[q_num]
    return render_template('question_0.html', q_num=q_num , question = question, q_choices = q_choices)

@app.route('/answer', methods = ['POST'])
def handle_answers():
    res = request.form['answer']
    responses.append(res)
    app.logger.info(responses)
    return redirect(f"/questions/{len(responses)}")

@app.route('/survey_done')
def render_done():
    return render_template('survey_done.html')

