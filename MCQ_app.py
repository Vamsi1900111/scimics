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
    palm.configure(api_key='AIzaSyCpta0zYFZSLw7imatVqW-exaviTfMIqu0')
    def generate(text):
        response = palm.generate_text(prompt=text)
        return response.result
    stream=request.form['stream']
    course=request.form['course']
    count1=request.form['1Q_count']
    Q1_time=request.form['1Q_time']
    text="generate only"+ count1+"Multi choice questions on "+course+"for"+stream
    questions_string = generate(text)
    # answers=palm.generate_text(prompt='generate only correct option for each question:'+questions_string)
    # answers_list=answers.result
    questions_string=str(questions_string).split('\n')
#parameter-2:
    Q2_time=request.form['2Q_time']
    Q2a_count=request.form['2Q_a_count']
    Q2b_count=request.form['2Q_b_count']
    Q2c_count=request.form['2Q_c_count']
    Q2d_count=request.form['2Q_d_count']
    count2=Q2a_count
    text="generate "+ count2+"Multi choice questions on each of listening,reading,writting,speaking."
    result2 = generate(text).split('\n')
#parameter-3:
    Q3_time=request.form['3Q_time']
    Q3a_count=request.form['3Q_a_count']
    Q3b_count=request.form['3Q_b_count']
    count3=max(int(Q3b_count),int(Q3a_count))
    text="generate "+ str(count3)+"Multi choice questions on each of Quantitative Aptitude,Analytical Reasoning."
    result3 = generate(text).split('\n')
#parameter-4:
    Q4_time=request.form['4Q_time']
    Q4a_count=request.form['4Q_a_count']
    Q4b_count=request.form['4Q_b_count']
    count4=max(int(Q4b_count),int(Q4a_count))
    text="generate "+ str(count4)+"Multi choice questions on each of Group Activities,Peer Feedback."
    result4 = generate(text).split('\n')
#parameter-5:
    Q5_time=request.form['5Q_time']
    Q5a_count=request.form['5Q_a_count']
    Q5b_count=request.form['5Q_b_count']
    count5=max(int(Q5b_count),int(Q5a_count))
    text="generate "+ str(count5)+"Multi choice questions on each of Adaptability,Continous learning."
    result5 = generate(text).split('\n')
#parameter-6:
    Q6_time=request.form['6Q_time']
    Q6a_count=request.form['6Q_a_count']
    Q6b_count=request.form['6Q_b_count']
    Q6c_count=request.form['6Q_c_count']
    Q6d_count=request.form['6Q_d_count']
    Q6e_count=request.form['6Q_e_count']
    count6=max(int(Q6b_count),int(Q6a_count))
    text="generate "+ str(count6)+"Multi choice questions on each of Prioritization tasks and setting clear goals,Estimation of time required for tasks and setting deadlines,Handling multitasking and managing multiple assignments,Understanding project life cycles, from initiation to completion,Utilization of tools or software related to time and project management."
    result6 = generate(text).split('\n')
#parameter-7:
    Q7_time=request.form['7Q_time']
    Q7a_count=request.form['7Q_a_count']
    Q7b_count=request.form['7Q_b_count']
    count7=max(int(Q7b_count),int(Q7a_count))
    text="generate "+ str(count7)+"Multi choice questions on each of Scenario-based questions on professional conduct,Setting up Mock interview sessions on our Platform."
    result7 = generate(text).split('\n')
    time=int(Q1_time)+int(Q2_time)+int(Q3_time)+int(Q4_time)+int(Q5_time)+int(Q6_time)+int(Q7_time)
    count=int(count1)+int(count2)+int(count3)+int(count4)+int(count5)+int(count6)+int(count7)
    return render_template('result.html',time=str(time),count=str(count), result1=questions_string,result2=result2,result3=result3,result4=result4,result5=result5,result6=result6,result7=result7)
if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
