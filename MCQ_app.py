# ui_app.py
from flask import Flask, render_template, request, jsonify
import requests
import google.generativeai as palm
import json
import google.generativeai as palm
import base64
import json
import pprint
import base64
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    QA_count=request.form['QA_count']
    course_name = request.form['course_name']
    btech_branch = request.form['btech_branch']
    QA_difficulty = request.form['QA_difficulty']
    text="generate only"+ QA_count+QA_difficulty+"Multi choice questions on "+course_name+"for"+btech_branch+"branch."
    palm.configure(api_key='AIzaSyCpta0zYFZSLw7imatVqW-exaviTfMIqu0')
    response = palm.generate_text(prompt=text)
    questions_string = response.result
    answers=palm.generate_text(prompt='generate only options for:'+response.result)
    answers_list=[i for i in answers.result.split('\n')]
    questions = [question.strip() for question in questions_string.split("\n") if question]
    questions_list=[]
    # answers_list=[]
    y=''
    for i in range(1,len(questions)+1):
        y=y+" "+questions[i-1]
        if i%5==0:
            questions_list.append(y)
            y=''
        # if i%4!=0:
        #     answers_list.append(questions[i])
    # questions = [question.strip() for question in questions_string.split(":") if question]
    questions_dict = {q: a  for q,a in zip(questions_list,answers_list)}
    result = json.dumps(questions_dict, indent=2)
    return render_template('result.html', result=questions,results=answers_list)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
