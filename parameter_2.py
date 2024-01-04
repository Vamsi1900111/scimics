import requests
import google.generativeai as palm
import base64
import json
from flask_cors import CORS
from flask import Flask,request, jsonify
from bs4 import BeautifulSoup
app = Flask(__name__)
CORS(app)
@app.route('/parameter2', methods=['POST'])
def get_mcq():
    if request.method == 'POST':
        data = request.json
        result = MCQ_questions(data)
        return result
def MCQ_questions(data):
    def split_json(ques_list):
        try:
            inn=[]
            out=[]
            for i in range(len(ques_list[0])):
                if ques_list[0][i]=="{":
                    inn.append(i)
                if ques_list[0][i]=="}":
                    out.append(i)
            l=[]
            d=ques_list[0]
            for i,j in zip(inn,out):
                dk=d[i:j+1]
                # print(dk)
                dd=json.loads(dk)
                l.append(dd)
            return l
        except:
            ques_list
    palm.configure(api_key='AIzaSyCpta0zYFZSLw7imatVqW-exaviTfMIqu0')
    format="""\n
    {
      "question": "Sample question?",
      "category": "Category1",
      "options": ["Option1", "Option2", "Option3", "Option4"],
      "correct_answer": "CorrectOption"
    },{
      "question": "Another sample question?",
      "category": "Category2",
      "options": ["Option1", "Option2", "Option3", "Option4"],
      "correct_answer": "CorrectOption"
    }
    //other questions
"""
    def generate(text):
        response = palm.generate_text(prompt=text)
        return response.result
#parameter-2:
    course=data['course']
    stream=data['stream']
    count1a=data['1Q_a_count']
    Q1_time=data['1Q_time']
    count1b=data['1Q_b_count']
    category=course+"for"+stream
    count1=max(int(count1a),int(count1b))
    inputt="""{
        "testname": "Technical Proficiency",
        "categories": [%s,'Hands-on-coding'],
        "question_counts": [%s,%s]
        }"""%(category,count1a,count1b)
    text="Generate "+count1+" sets of Technical Proficiency test questions based on user-provided input:\n"+inputt+"\nThe output should be in the following format:\n"+format
    result1 = generate(text)
    result1={
        "testname": "Technical Proficiency",
        "questions":split_json([result1])
    }
    time=int(Q1a_time)+int(Q1b_time)
    data={'MCQ_Questions':[result1]}
    path="parameter-2_Questions.json"
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=1)
    except:
        pass
    return data
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)  # Change the port if needed
