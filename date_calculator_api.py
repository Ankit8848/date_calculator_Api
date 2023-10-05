from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import os

app = Flask(__name__)


@app.route('/calculate_days', methods=['POST'])
def calculate_days():
    try:
        # Get start and end dates from the request JSON data
        data = request.get_json()
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # Check if both start_date and end_date are provided
        if not start_date or not end_date:
            return jsonify({'error': 'Missing start_date or end_date in request JSON'}), 400

        # Parse the date strings into datetime objects
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

        # Calculate the number of days between the two dates
        days_difference = (end_date_obj - start_date_obj).days

        # Prepare the response JSON object
        response_data = {
            'start_date': start_date,
            'end_date': end_date,
            'days_difference': days_difference
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/calculate_future_date', methods=['POST'])
def calculate_future_date():
    try:
        # Get the starting date and number of days from the request JSON data
        data = request.get_json()
        start_date = data.get('start_date')
        days_to_add = data.get('days_to_add')

        # Check if both start_date and days_to_add are provided
        if not start_date or not days_to_add:
            return jsonify({'error': 'Missing start_date or days_to_add in request JSON'}), 400

        # Parse the date string into a datetime object
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')

        # Calculate the future date by adding days
        future_date_obj = start_date_obj + timedelta(days=days_to_add)

        # Convert the future date back to a string
        future_date = future_date_obj.strftime('%Y-%m-%d')

        # Prepare the response JSON object
        response_data = {
            'start_date': start_date,
            'days_to_add': days_to_add,
            'future_date': future_date
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=True)
