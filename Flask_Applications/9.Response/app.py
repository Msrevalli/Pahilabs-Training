from flask import Flask, render_template, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def home():
    # Simple string response
    return "Welcome to the Flask Response Project!"

@app.route('/data')
def data():
    # JSON response
    response_data = {"message": "This is a JSON response", "status": "success"}
    return jsonify(response_data)

@app.errorhandler(404)
def not_found(error):
    # Create a custom response for 404 errors
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

if __name__ == '__main__':
    app.run(debug=True)
