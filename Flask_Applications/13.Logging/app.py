import os
from flask import Flask, request, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)

# Create a logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Set up logging to a file
logging.basicConfig(
    filename='logs/app.log',  # Log file path
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.route('/')
def index():
    app.logger.debug('Index page accessed')
    return "Welcome to the Index Page!"

@app.route('/process-data', methods=['POST'])
def process_data():
    app.logger.info('Received data for processing')

    try:
        # Simulate data processing
        data = request.get_json()
        if not data or 'value' not in data:
            raise ValueError("Missing 'value' in request data")
        
        # Log the received value
        app.logger.info('Processing value: %s', data['value'])

        # Simulated processing
        result = data['value'] * 2  # Just an example operation
        app.logger.debug('Processed result: %s', result)

        return jsonify({'result': result}), 200

    except ValueError as e:
        app.logger.error('ValueError occurred: %s', e)
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        app.logger.critical('An unexpected error occurred: %s', e)
        return jsonify({'error': 'Internal Server Error'}), 500

@app.before_request
def log_request_info():
    app.logger.info('Request Headers: %s', request.headers)
    app.logger.info('Request Body: %s', request.get_json())

if __name__ == '__main__':
    app.run(debug=True)
