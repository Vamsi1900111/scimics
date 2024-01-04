import requests
import google.generativeai as palm
import base64
import json
from flask_cors import CORS
from flask import Flask,request, jsonify
from bs4 import BeautifulSoup
app = Flask(__name__)
CORS(app)
@app.route('/parameter4', methods=['POST'])
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
#parameter-4:
    Q6_time=data['6Q_time']
    Q6a_count=data['6Q_a_count']
    Q6b_count=data['6Q_b_count']
    Q6c_count=data['6Q_c_count']
    Q6d_count=data['6Q_d_count']
    count6=max(int(Q6b_count),int(Q6a_count),int(Q6c_count),int(Q6d_count))
    count6=str(count6)
    inputt="""{
        "testname": "Personality and Behavioral",
        "categories": ["Interpersonal and Team work Skills:focus on teamwork dynamics and communication within a group.", "Adaptability and Continuous Learning: emphasize the ability to adapt to changes and continue learning in a professional environment.","Project Management and Time Management: deal with organizing, planning, and managing time effectively for projects.","Professional Etiquette and Interview Preparedness: cover the basics of professional conduct and preparing for job interviews."],
        "question_counts": [%s,%s,%s,%s]
        }"""%(count6,count6,count6,count6)
    text="Generate "+count6+" sets of Personality and Behavioral test questions based on user-provided input:\n"+inputt+"\nThe output should be in the following format:\n"+format
    result6 = generate(text)
    result6={
        "testname": "Personality and Behavioral",
        "questions":split_json([result6])
    } 
    def generate(text):
        response = palm.generate_text(prompt=text)
        return response.result

    time=int(Q6_time)
    count=int(count6)
    data={'MCQ_Questions':[result6]}
    path="parameter-4_Questions.json"
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=1)
    except:
        pass
    return data
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)  # Change the port if needed
