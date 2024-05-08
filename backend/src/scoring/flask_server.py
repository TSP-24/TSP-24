from flask import Flask, request, jsonify
from flask_cors import cross_origin
from csv2scores import calculate_engagement

app = Flask(__name__)

@app.route('/your-backend-endpoint', methods=['POST'])

@cross_origin(origins=['http://localhost:3000'])
def process_file():
    data = request.get_json()
    if 'data' not in data:
        return jsonify(error='No data provided'), 400
    csv_data = data['data']
    csv_filename = data['filename']
    try:
        # Convert the string data to a DataFrame
        scores_df = calculate_engagement(csv_data, csv_filename)
        return scores_df.to_json(orient='records')
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/<path:path>', methods=['OPTIONS'])
def options(path):
    return '', 200, {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

if __name__ == '__main__':
    app.run(debug=True, port=5000)
