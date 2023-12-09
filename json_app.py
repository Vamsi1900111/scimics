import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import json
app = Flask(__name__)
@app.route('/get_mcq_questions', methods=['POST'])
def get_mcq_questions():
    try:
        data = request.json  # Assuming the data is sent as JSON from React
        result = MCQ_questions(data)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

def MCQ_questions(data):
    url = "https://mcq-generator-xr5k.onrender.com/predict"
    response = requests.post(url, data=data)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        parameter_1_questions = [p.get_text(strip=True) for p in soup.select('div:nth-of-type(1) p')]
        parameter_2_questions = [p.get_text(strip=True) for p in soup.select('div:nth-of-type(2) p')]
        parameter_3_questions = [p.get_text(strip=True) for p in soup.select('div:nth-of-type(3) p')]
        parameter_4_questions = [p.get_text(strip=True) for p in soup.select('div:nth-of-type(4) p')]
        parameter_5_questions = [p.get_text(strip=True) for p in soup.select('div:nth-of-type(5) p')]
        parameter_6_questions = [p.get_text(strip=True) for p in soup.select('div:nth-of-type(6) p')]
        parameter_7_questions = [p.get_text(strip=True) for p in soup.select('div:nth-of-type(7) p')]
    else:
        print("Error:", response.status_code)       
    def get_data(parameter_questions,name):
        l=[]
        d={}
        for i in parameter_questions:
            i=str(i).replace("*","")
            # i=str(i).strip()
            l.append(i)
        d[name]=l   
        json_data = json.dumps(d, indent=2)
        return json_data
    parameter_1_questions=["".join(parameter_1_questions).split('Listening')[0] ]
    p1=get_data(parameter_1_questions,"parameter_1")
    p2=get_data(parameter_2_questions,"parameter_2")
    p3=get_data(parameter_3_questions,"parameter_3")
    p4=get_data(parameter_4_questions,"parameter_4")
    p5=get_data(parameter_5_questions,"parameter_5")
    p6=get_data(parameter_6_questions,"parameter_6")
    p7=get_data(parameter_7_questions,"parameter_7")
    return json.dumps({'Questions':[p1,p2,p3,p4,p5,p6,p7]}, indent=1)
if __name__ == '__main__':
    app.run(port=5000)  # Change the port if needed
