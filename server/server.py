from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hi'


@app.route('/get_all_location_names')
def get_all_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-control-Allow-origin', '*')

    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_pricepredict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-control-Allow-origin', '*')

    return response


if __name__ == '__main__':
    print('starting python Flask server for home price prediction ......')
    app.run()
