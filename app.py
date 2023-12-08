from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommendation.html', methods=['POST'])
def get_recommended_crop():
    data = request.get_json()
    nitrogen = data.get('nitrogen')
    phosphorus = data.get('phosphorus')
    potassium = data.get('potassium')
    temperature = data.get('temperature')

    # Your recommendation function logic here (use the Python logic from earlier)
    if nitrogen > 5 and phosphorus > 5 and potassium > 5 and temperature > 25:
        recommendation = 'Corn'
    elif nitrogen <= 5 and phosphorus <= 5 and potassium <= 5 and temperature <= 25:
        recommendation = 'Rice'
    else:
        recommendation = 'Other Crop'

    return jsonify({'recommendation': recommendation})

if __name__ == '__main__':
    app.run(debug=True)
