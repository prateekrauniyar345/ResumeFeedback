from flask import Flask, request, url_for
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)



@app.route('/', methods=['GET'])
def main():
    return "Hello, World!"



if __name__ == '__main__':
    app.run(debug=True, port=5001)