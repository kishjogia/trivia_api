from questions import Question
import html
import json
import random
import requests

class Quiz(object):
    def __init__(self):
        self.__SESSION_TOKEN = ""
        self.__QUESTION_LIST = []

        self.__getQuestionsList()

    # internal function to get 10 random questions
    def __requestQuestions(self):
        if self.__SESSION_TOKEN == "":
            self.getSessionToken

        URL = "https://opentdb.com/api.php?amount=10&type=multiple&token=" + self.__SESSION_TOKEN
        response = requests.get(URL)                # get a set of random questions

        return response.text
    
    def __getQuestionsList(self):
        questions_tdb = json.loads(self.__requestQuestions())
        questions_tdb = questions_tdb['results']

        unescape = html.unescape

        for question_dict in questions_tdb:
            category = unescape(question_dict['category'])
            question = unescape(question_dict['question'])
            correct_ans = unescape(question_dict['correct_answer'])
            wrong_ans = unescape(question_dict['incorrect_answers'])

            self.__QUESTION_LIST.append(Question(category, question, correct_ans, wrong_ans))

        return True

    # Get the session token, this is useful so different questions appear each time
    def  getSessionToken(self):
        if self.__SESSION_TOKEN == "":
            session_key = requests.get("https://opentdb.com/api_token.php?command=request")
            token = json.loads(session_key.text)
            self.__SESSION_TOKEN = token['token']

        return self.__SESSION_TOKEN
    
    def getQuestion(self, question_no):
        if len(self.__QUESTION_LIST) == 0:
            self.__getQuestionsList()

        return self.__QUESTION_LIST[question_no].question
    
    def getAnswersList(self, question_no):
        answers = self.__QUESTION_LIST[question_no].wrong_ans
        answers.append(self.__QUESTION_LIST[question_no].correct_ans)
        random.shuffle(answers)

        return answers
    
    def getCorrectAnswer(self, question_no):
        return self.__QUESTION_LIST[question_no].correct_ans