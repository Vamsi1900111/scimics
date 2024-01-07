import requests
import google.generativeai as palm
import base64
import json
from flask_cors import CORS
from flask import Flask,request, jsonify
from bs4 import BeautifulSoup
app = Flask(__name__)
CORS(app)
@app.route('/parameter3', methods=['POST'])
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
    },
    {
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
#parameter-3:
    Q2_time=data['2Q_time']
    Q2a_count=data['2Q_a_count']
    Q2b_count=data['2Q_b_count']
    Q2c_count=data['2Q_c_count']
    Q2d_count=data['2Q_d_count']
    count2=Q2a_count
    # text="generate "+count2+ " each on listening,writting,speaking categories. In this format:\n"+format
    inputt="""{
        "testname": "Communication Skills",
        "categories": ["Listening", "Writing","speaking"],
        "question_counts": [%s,%s,%s]
        }"""%(count2,count2,count2)
    text="Generate "+count2+" sets of communication skills questions based on below-provided input\n"+inputt+"\nThe output should be in the following format:\n"+format
    result21 = generate(text)
#Reading
    format2="""\n
    {
      "Paragraph":"sample paragraph",
      "question": "Sample question?",
      "category": "Category1",
      "options": ["Option1", "Option2", "Option3", "Option4"],
      "correct_answer": "CorrectOption"
    },
    {
      "question": "Another sample question?",
      "category": "Category2",
      "options": ["Option1", "Option2", "Option3", "Option4"],
      "correct_answer": "CorrectOption"
    }
    //other questions
""" 
    inputt2="""{
        "testname": "Communication Skills",
        "categories": ["Reading"],
        "question_counts": [%s]
        }"""%(count2)
    text2="Generate "+count2+" sets of communication skills test paragraph questions based on user-provided input\n"+inputt2+"\nThe output should be in the following format:\n"+format2
    result22 = generate(text2)
#Result
    result2={
        "testname": "Communication Skills",
        "questions":split_json([result21]),
        "comprehensive_questions":split_json([result22])
    }
    time=int(Q2_time)
    count=int(count2)
    data={'MCQ_Questions':[result2]}
    path="parameter-3_Questions.json"
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=1)
    except:
        pass
    return data
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)  # Change the port if needed
