import requests
import google.generativeai as palm
import base64
import json
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/get_mcq', methods=['POST'])
def get_mcq():
    if request.method == 'POST':
        data = request.json
        result = MCQ_questions(data)
        return result
def MCQ_questions(data):
    palm.configure(api_key='AIzaSyCpta0zYFZSLw7imatVqW-exaviTfMIqu0')
    def generate(text):
        response = palm.generate_text(prompt=text)
        return response.result
    course=data['course']
    stream=data['stream']
    count1=data['1Q_count']
    Q1_time=data['1Q_time']
    text="generate only"+ count1+"Multi choice questions on "+course+"for"+stream
    questions_string = generate(text)
    a1=generate("give only correct option names for all the questions: \n"+str(questions_string)).split('\n')
    questions_string=str(questions_string).split('\n')
#parameter-2:
    Q2_time=data['2Q_time']
    Q2a_count=data['2Q_a_count']
    Q2b_count=data['2Q_b_count']
    Q2c_count=data['2Q_c_count']
    Q2d_count=data['2Q_d_count']
    count2=Q2a_count
    text="generate "+ count2+"Multi choice questions on each of listening,reading,writting,speaking."
    result2 = generate(text)
    a2=generate("give only correct option names for all the questions: \n"+str(result2)+" .only correct option names").split('\n')
    result2=str(result2).split('\n')
#parameter-3:
    Q3_time=data['3Q_time']
    Q3a_count=data['3Q_a_count']
    Q3b_count=data['3Q_b_count']
    count3=max(int(Q3b_count),int(Q3a_count))
    text="generate "+ str(count3)+"Multi choice questions on each of Quantitative Aptitude,Analytical Reasoning."
    result3 = generate(text)
    a3=generate("give only correct option names  for all the below questions: \n"+str(result3)+" .only correct option names").split('\n')
    result3=str(result3).split('\n')
#parameter-4:
    Q4_time=data['4Q_time']
    Q4a_count=data['4Q_a_count']
    Q4b_count=data['4Q_b_count']
    count4=max(int(Q4b_count),int(Q4a_count))
    text="generate "+ str(count4)+"Multi choice questions on each of Group Activities,Peer Feedback."
    result4 = generate(text)
    a4=generate("give only correct option names  for all the below questions: \n"+str(result4)+" .only correct option names").split('\n')
    result4=str(result4).split('\n')
#parameter-5:
    Q5_time=data['5Q_time']
    Q5a_count=data['5Q_a_count']
    Q5b_count=data['5Q_b_count']
    count5=max(int(Q5b_count),int(Q5a_count))
    text="generate "+ str(count5)+"Multi choice questions on each of Adaptability,Continous learning."
    result5 = generate(text)
    a5=generate("give only correct option names  for all the below questions: \n"+str(result5)+" .only correct option names").split('\n')
    result5=str(result5).split('\n')   
#parameter-6:
    Q6_time=data['6Q_time']
    Q6a_count=data['6Q_a_count']
    Q6b_count=data['6Q_b_count']
    Q6c_count=data['6Q_c_count']
    Q6d_count=data['6Q_d_count']
    Q6e_count=data['6Q_e_count']
    count6=max(int(Q6b_count),int(Q6a_count),int(Q6c_count),int(Q6d_count),int(Q6e_count))
    text="generate "+ str(count6)+"Multi choice questions on each of Prioritization tasks and setting clear goals,Estimation of time required for tasks and setting deadlines,Handling multitasking and managing multiple assignments,Understanding project life cycles, from initiation to completion,Utilization of tools or software related to time and project management."
    result6 = generate(text)
    a6=generate("give only correct option names  for all the below questions: \n"+str(result6)+" .only correct option names").split('\n')
    result6=str(result6).split('\n')
#parameter-7:
    Q7_time=data['7Q_time']
    Q7a_count=data['7Q_a_count']
    Q7b_count=data['7Q_b_count']
    count7=max(int(Q7b_count),int(Q7a_count))
    text="generate "+ str(count7)+"Multi choice questions on each of Scenario-based questions on professional conduct,Setting up Mock interview sessions on our Platform."
    result7 = generate(text)
    a7=generate("give only correct option names  for all the below questions: \n"+str(result7)+" .only correct option names").split('\n')
    result7=str(result7).split('\n')
    time=int(Q1_time)+int(Q2_time)+int(Q3_time)+int(Q4_time)+int(Q5_time)+int(Q6_time)+int(Q7_time)
    count=int(count1)+int(count2)+int(count3)+int(count4)+int(count5)+int(count6)+int(count7)
    def get_data(parameter_questions,name):
        l=[]
        d={}
        for i in parameter_questions:
            i=str(i).replace("*","")
            l.append(i)
        d[name]=l   
        json_data = json.dumps(d, indent=1)
        return json_data
    p1=get_data(questions_string,"parameter_1")
    p2=get_data(result2,"parameter_2")
    p3=get_data(result3,"parameter_3")
    p4=get_data(result4,"parameter_4")
    p5=get_data(result5,"parameter_5")
    p6=get_data(result6,"parameter_6")
    p7=get_data(result7,"parameter_7")
    with open("questions_data.json", "w") as json_file:
        json.dumps({'Questions':[p1,p2,p3,p4,p5,p6,p7]}, indent=1)
    return json.dumps({'Questions':[p1,p2,p3,p4,p5,p6,p7],'answers':[a1,a2,a3,a4,a5,a6,a7]}, indent=1)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)  # Change the port if needed
