from flask import Flask, jsonify, render_template
import aiohttp
from async_db import async_db_query

app = Flask(__name__)

# Asynchronous route to fetch mock database data
@app.route('/get-data')
async def get_data():
    data = await async_db_query()
    return jsonify(data)

# Asynchronous route to fetch data from an external API
@app.route('/fetch-external')
async def fetch_external():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/posts/1') as response:
            external_data = await response.json()
    return jsonify(external_data)

# Home page route (synchronous)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
