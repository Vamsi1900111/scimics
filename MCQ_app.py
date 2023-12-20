import requests
import google.generativeai as palm
import base64
import json
from flask_cors import CORS
from flask import Flask,request, jsonify
from bs4 import BeautifulSoup
app = Flask(__name__)
CORS(app)
@app.route('/get_mcq', methods=['POST'])
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
            return ques_list
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
    course=data['course']
    stream=data['stream']
    count1=data['1Q_count']
    Q1_time=data['1Q_time']
    category=course+"for"+stream
    inputt="""{
        "testname": "Technical Proficiency",
        "categories": [%s],
        "question_counts": [%s]
        }"""%(category,count1)
    text="Generate "+count1+" sets of Technical Proficiency test questions based on user-provided input:\n"+inputt+"\nThe output should be in the following format:\n"+format
    result1 = generate(text)
    result1={
        "testname": "Technical Proficiency",
        "questions":split_json([result1])
    }
#parameter-2:
    Q2_time=data['2Q_time']
    Q2a_count=data['2Q_a_count']
    Q2b_count=data['2Q_b_count']
    Q2c_count=data['2Q_c_count']
    Q2d_count=data['2Q_d_count']
    count2=Q2a_count
    # text="generate "+count2+ " each on listening,reading,writting,speaking."+"in this format:\n"+format
    inputt="""{
        "testname": "Communication Skills",
        "categories": ["Listening", "Reading", "Writing","speaking"],
        "question_counts": [%s,%s,%s,%s]
        }"""%(count2,count2,count2,count2)
    text="Generate "+count2+" sets of communication skills test questions based on user-provided input\n"+inputt+"\nThe output should be in the following format:\n"+format
    result2 = generate(text)
    result2={
        "testname": "Communication Skills",
        "questions":split_json([result2])
    }
#parameter-3:
    Q3_time=data['3Q_time']
    Q3a_count=data['3Q_a_count']
    Q3b_count=data['3Q_b_count']
    count3=max(int(Q3b_count),int(Q3a_count))
    count3=str(count3)
    inputt="""{
        "testname": "Cognitive Abilities",
        "categories": ["Quantitative Aptitude", "Analytical Reasoning"],
        "question_counts": [%s,%s]
        }"""%(count3,count3)
    text="Generate "+count3+" sets of Cognitive Abilities test questions based on user-provided input:\n"+inputt+"\nThe output should be in the following format:\n"+format
    result3 = generate(text)
    result3={
        "testname": "Cognitive Abilities",
        "questions":split_json([result3])
    }

#parameter-4:
    Q4_time=data['4Q_time']
    Q4a_count=data['4Q_a_count']
    Q4b_count=data['4Q_b_count']
    count4=max(int(Q4b_count),int(Q4a_count))
    count4=str(count4)
    inputt="""{
        "testname": "Interpersonal and Teamwork Skills",
        "categories": ["Group Activities", "Peer Feedback"],
        "question_counts": [%s,%s]
        }"""%(count4,count4)
    text="Generate "+count4+" sets of Interpersonal and Teamwork Skills test questions based on user-provided input:\n"+inputt+"\nThe output should be in the following format:\n"+format
    result4 = generate(text)
    result4={
        "testname": "Interpersonal and Teamwork Skills",
        "questions":split_json([result4])
    }
#parameter-5:
    Q5_time=data['5Q_time']
    Q5a_count=data['5Q_a_count']
    Q5b_count=data['5Q_b_count']
    count5=max(int(Q5b_count),int(Q5a_count))
    count5=str(count5)
    inputt="""{
        "testname": "Adaptability and Continuous Learning",
        "categories": ["Adaptability", "Continous learning"],
        "question_counts": [%s,%s]
        }"""%(count5,count5)
    text="Generate "+count5+" sets of Adaptability and Continuous Learning test questions based on user-provided input:\n"+inputt+"\nThe output should be in the following format:\n"+format
    result5 = generate(text)
    result5={
        "testname": "Adaptability and Continuous Learning",
        "questions":split_json([result5])
    } 
#parameter-6:
    Q6_time=data['6Q_time']
    Q6a_count=data['6Q_a_count']
    Q6b_count=data['6Q_b_count']
    Q6c_count=data['6Q_c_count']
    Q6d_count=data['6Q_d_count']
    Q6e_count=data['6Q_e_count']
    count6=max(int(Q6b_count),int(Q6a_count),int(Q6c_count),int(Q6d_count),int(Q6e_count))
    count6=str(count6)
    inputt="""{
        "testname": "Project Management and Time Management",
        "categories": ["Prioritization tasks and setting clear goals.", "Estimation of time required for tasks and setting deadlines.","Handling multitasking and managing multiple assignments.","Understanding project life cycles, from initiation to completion.","Utilization of tools or software related to time and project management."],
        "question_counts": [%s,%s,%s,%s,%s]
        }"""%(count6,count6,count6,count6,count6)
    text="Generate "+count6+" sets of Project Management and Time Management test questions based on user-provided input:\n"+inputt+"\nThe output should be in the following format:\n"+format
    result6 = generate(text)
    result6={
        "testname": "Project Management and Time Management",
        "questions":split_json([result6])
    } 

#parameter-7:
    Q7_time=data['7Q_time']
    Q7a_count=data['7Q_a_count']
    Q7b_count=data['7Q_b_count']
    count7=max(int(Q7b_count),int(Q7a_count))
    count7=str(count7)
    text="generate "+ str(count7)+"Multi choice questions on each of Scenario-based questions on professional conduct,Setting up Mock interview sessions on our Platform."
    result7 = generate(text)
    inputt="""{
        "testname": "Professional Etiquette and Interview Preparedness.",
        "categories": ["Scenario-based questions on professional conduct", "Setting up Mock interview sessions on our Platform"],
        "question_counts": [%s,%s]
        }"""%(count7,count7)
    text="Generate "+count7+" sets of Professional Etiquette and Interview Preparedness. test questions based on user-provided input:\n"+inputt+"\nThe output should be in the following format:\n"+format
    result7 = generate(text)
    result7={
        "testname": "Professional Etiquette and Interview Preparedness.",
        "questions":split_json([result7])
    }
    time=int(Q1_time)+int(Q2_time)+int(Q3_time)+int(Q4_time)+int(Q5_time)+int(Q6_time)+int(Q7_time)
    count=int(count1)+int(count2)+int(count3)+int(count4)+int(count5)+int(count6)+int(count7)
    data={'MCQ_Questions':[result1,result2,result3,result4,result5,result6,result7]}
    try:
        with open("Questions.json", "w") as json_file:
            json.dump(data, json_file, indent=1)
    except:
        pass
    return data
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)  # Change the port if needed
