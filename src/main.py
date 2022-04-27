from flask import Flask, send_from_directory
from host_info import get_host
from os import path

static_dir = 'front'
HOST = '0.0.0.0'
PORT = 8080

app = Flask(__name__, static_url_path='', static_folder=static_dir)

# redirect to home page 
@app.route("/")
def send_static():
    try:
        return send_from_directory(static_dir, 'index.html')
    except Exception as err:
        return 'Server error', 500

# handle 404 error
@app.errorhandler(404)
def page_not_found(e):
    try:
        return send_from_directory(static_dir, '404page.html')
    except Exception as err:
        return '<h1 style="text-align: center;">Server error :(</h1>', 500

if __name__ == "__main__":
    host = get_host()
    print(f"Host running on {host}")
    app.run(debug=True, host=HOST, port=PORT)

