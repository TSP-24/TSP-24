from flask import Flask, request, jsonify
from flask_cors import CORS
from csv2scores import calculate_engagement

app = Flask(__name__)
CORS(app)

current_csv_data = None
current_csv_filename = None

@app.route('/uploads', methods=['POST'])
def process_file():
    data = request.get_json()
    if 'data' not in data:
        return jsonify(error='No data provided'), 400
    csv_data = data['data']
    csv_filename = data['filename']
    global current_csv_data
    global current_csv_filename
    current_csv_data, current_csv_filename = csv_data, csv_filename
    try:
        # Convert the string data to a DataFrame
        scores_df, assessments = calculate_engagement(csv_data, csv_filename)
        # Convert scores_df to JSON
        scores_json = scores_df.to_json(orient='records')
        # Return both as part of the response
        return jsonify(scores=scores_json, assessments=assessments)
    except Exception as e:
        return jsonify(error=str(e)), 500
    
@app.route('/weights', methods=['POST'])
def process_weights():
    weights = request.get_json()
    try:
        # Convert the string data to a DataFrame
        scores_df, assessments = calculate_engagement(current_csv_data, current_csv_filename, weights)
        # Convert scores_df to JSON
        scores_json = scores_df.to_json(orient='records')
        # Return both as part of the response
        return jsonify(scores=scores_json, assessments=assessments)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)