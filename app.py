from flask import Flask, request, url_for, render_template
from dotenv import load_dotenv
import os
from supabase import create_client, Client

load_dotenv()


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/', methods=['GET'])
def main():
    return render_template('dashboard/root.html')


@app.route('/login', methods=['POST'])
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True, port=5001)