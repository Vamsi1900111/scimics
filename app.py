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
    text="generate only"+ QA_count+QA_difficulty+"questions on "+course_name+"for"+btech_branch+"branch with answers.(question should start and end with ||)"
    # api_url = 'http://localhost:5000/api/predict'
    # result = requests.post(api_url, json= input_data)
    #text = "Generate 10 question "
    palm.configure(api_key='AIzaSyCpta0zYFZSLw7imatVqW-exaviTfMIqu0')
    # These parameters for the model call can be set by URL parameters.
    #model = 'models/text-bison-001' # @param {isTemplate: true}
    temperature = 0.7 # @param {isTemplate: true}
    candidate_count = 1 # @param {isTemplate: true}
    top_k = 40 # @param {isTemplate: true}
    top_p = 0.95 # @param {isTemplate: true}
    max_output_tokens = 1024 # @param {isTemplate: true}
    input_bytes = text.encode('utf-8')
    encoded_bytes = base64.b64encode(input_bytes)
    text_b64= encoded_bytes.decode('utf-8')
    stop_sequences_b64 = 'W10=' # @param {isTemplate: true}
    safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0RFUk9HQVRPUlkiLCJ0aHJlc2hvbGQiOjF9LHsiY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX1RPWElDSVRZIiwidGhyZXNob2xkIjoxfSx7ImNhdGVnb3J5IjoiSEFSTV9DQVRFR09SWV9WSU9MRU5DRSIsInRocmVzaG9sZCI6Mn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMIiwidGhyZXNob2xkIjoyfSx7ImNhdGVnb3J5IjoiSEFSTV9DQVRFR09SWV9NRURJQ0FMIiwidGhyZXNob2xkIjoyfSx7ImNhdGVnb3J5IjoiSEFSTV9DQVRFR09SWV9EQU5HRVJPVVMiLCJ0aHJlc2hvbGQiOjJ9XQ==' # @param {isTemplate: true}
# Convert the promp5t text param from a bae64 string to a string.
    text = base64.b64decode(text_b64).decode("utf-8")
# Convert the stop_sequences and safety_settings params from base64 strings to lists.
    stop_sequences = json.loads(base64.b64decode(stop_sequences_b64).decode("utf-8"))
    safety_settings = json.loads(base64.b64decode(safety_settings_b64).decode("utf-8"))
    defaults = {
  #'model': model,
  'temperature': temperature,
  'candidate_count': candidate_count,
  'top_k': top_k,
  'top_p': top_p,
  'max_output_tokens': max_output_tokens,
  'stop_sequences': stop_sequences,
  'safety_settings': safety_settings,
    }
# Show what will be sent with the API call.
    response = palm.generate_text(prompt=text)
    questions_string = response.result
    questions = [question.strip() for question in questions_string.split("||") if question]
    # questions = [question.strip() for question in questions_string.split(":") if question]
    questions_list=[]
    answers_list=[]
    for i in range(len(questions)):
        if i%2==0:
            questions_list.append(questions[i])
        if i%2!=0:
            answers_list.append(questions[i])
    questions_dict = {q: a  for q,a in zip(questions_list,answers_list)}
    result = json.dumps(questions_dict, indent=2)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
