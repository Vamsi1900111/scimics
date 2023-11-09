from flask import Flask, jsonify, request
import google.generativeai as palm

app = Flask(__name__)
@app.route('/api/predict',methods=['GET'])
def predict(input_data):
# @app.route('/api/api_predict', methods=['POST'])
# def api_predict(input_data):
    palm.configure(api_key='AIzaSyCpta0zYFZSLw7imatVqW-exaviTfMIqu0')
    response = palm.generate_text(prompt=input_data)
    result = response.result
    return result


if __name__ == '__main__':
    app.run(debug=True,port=5000)
