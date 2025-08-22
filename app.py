from flask import Flask, request, url_for, render_template, session, flash, redirect
from dotenv import load_dotenv
import os
from supabase import create_client, Client

load_dotenv()


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

print("supabase client created with client : ", supabase)


app = Flask(__name__, template_folder='templates', static_folder='static')
# we need the secret key to protect session data
app.secret_key = os.environ.get("APP_SECRET_KEY")


@app.route('/', methods=['GET'])
def main():
    return render_template('dashboard/home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print("response for login:", email, password)

    return render_template('auths/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')

        print("response for register:", first_name, last_name, email, password)
        # inserting the user into the database
        try : 
            response = supabase.auth.sign_up({
                "email": email,
                "password": password
            })
            flash("Registration successful! Please check your email to confirm your account.", "success")
            session['user'] = response.user
            return redirect(url_for('login'))
        except Exception as e:
            flash("An error occurred during registration. Please try again.", "danger")
            print("Error during registration:", e)  
            return redirect(url_for('register'))
    return render_template('auths/register.html')


response = supabase.auth.get_user()
print("response for get_user:", response)


if __name__ == '__main__':
    app.run(debug=True, port=5001)