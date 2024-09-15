from flask import Flask, render_template, request
import urllib.request
from urllib.parse import quote
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Get API key from environment variables
    api_key = os.getenv('API_KEY')
    movies_data = None

    if request.method == 'POST':
        query = request.form.get('query')
        encoded_query = quote(query)
        url = f"https://api.watchmode.com/v1/autocomplete-search/?apiKey={api_key}&search_value={encoded_query}&search_type=1"
        
        with urllib.request.urlopen(url) as url:
            movies_data = json.loads(url.read().decode())
    
    return render_template('home.html', movies_data=movies_data)

if __name__ == '__main__':
    # run() method of Flask class runs the application on the local development server.
    app.run(host="0.0.0.0", port=6969, debug=True)