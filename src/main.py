from flask import Flask 
from os import path

app = Flask(__name__, static_url_path='', static_folder='front')

# serve static files
@app.route("/")
def send_static():
    return 'hello'

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)

