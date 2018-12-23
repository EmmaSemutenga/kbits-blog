from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'glkvfss;lksvsvsk'

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}', 'success')
        return redirect(url_for('login'))

    return render_template("register.html", form=form, title='Register')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Logged in successfully {form.email.data}', 'success')
        return redirect(url_for('home'))
    else:
        flash(f'Login Unsuccessfully please check username and password', 'danger')
    return render_template("login.html", form=form, title='Login')
#some work to be done above
@app.route('/home')
def home():
    return render_template('home.html')