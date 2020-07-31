# ToDo
# 1. [X] Create Flask API for Trivia Quiz API
# 2. [X] Function to return 1 question, correct ans, answers, require the question number
# 3. [ ] Ask user which question they want
# 4. [ ] Error / Exception handling
# 5. [ ] Allow different quantity of questions
# 6. [ ] Allow selection from a list of categories

from quiz import Quiz
from flask import Flask, jsonify

app = Flask(__name__)

c = Quiz() 

@app.route('/')
def index():
    return "App Started"

@app.route('/session_token')
def getSessionToken():
    return jsonify(c.getSessionToken())

@app.route('/question/<int:question_no>', methods = ['GET'])
def getQuestion(question_no:int):
    return jsonify(c.getQuestion(question_no))

@app.route('/answer_list/<int:question_no>', methods = ['GET'])
def getAnswersList(question_no:int):
    return jsonify(c.getAnswersList(question_no))

@app.route('/correct_answer/<int:question_no>', methods = ['GET'])
def getCorrectAnswer(question_no:int):
    return jsonify(c.getCorrectAnswer(question_no))

if __name__ == '__main__':
    app.run(debug = True)