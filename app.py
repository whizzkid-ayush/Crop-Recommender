import csv
from flask import Flask, request, jsonify, render_template
import sys
path = 'whizzkiddayush.pythonanywhere.com'

app = Flask(__name__)

def read_csv_file():
    data = []
    with open('Crop_recommendation.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def get_recommended_crop(nitrogen, phosphorus, potassium, temperature):
    crops_data = read_csv_file()


@app.route('/getRecommendedCrop', methods=['POST'])
def get_recommended_crop_from_post():
    data = request.get_json()
    nitrogen = float(data.get('nitrogen'))
    phosphorus = float(data.get('phosphorus'))
    potassium = float(data.get('potassium'))
    temperature = float(data.get('temperature'))

    recommendation = get_recommended_crop(nitrogen, phosphorus, potassium, temperature)

    return jsonify({'recommendation': recommendation})

@app.route('/recommendation.html', methods=['GET'])
def get_recommendation_html():
    return render_template('recommendation.html')

if __name__ == '__main__':
    app.run(debug=True)
