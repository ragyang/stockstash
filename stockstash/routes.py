from flask import Flask, jsonify, render_template, url_for, flash, redirect
from stockstash import app, mongo, bcrypt
from stockstash.models import User
from stockstash.forms import RegistrationForm, LoginForm, AddStockForm
from flask_login import login_user, current_user, logout_user, login_required
from stockstash.data.stockreader import get_stock_data, get_most_recent_business_day

@app.route("/")
def index():
    return render_template('home.html', title='Stockstash')

# login route
@app.route("/login", methods=['GET', 'POST'])
def login():
    # if current user is logged in, then redirect
    if current_user.is_authenticated:
        return redirect(url_for('portfolio'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects.get(pk=form.username.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('portfolio_test'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# register route
@app.route('/register', methods=['GET','POST'])
def register():
    # if current user is logged in, then redirect
    if current_user.is_authenticated:
        return redirect(url_for('portfolio'))
    # create the registration form object
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(_id=form.username.data,password=hashed_pass,
                    fname=form.fname.data, lname=form.lname.data,
                    brokerage=form.brokerage.data)
        user.save()
        flash(f'Welcome to StockStash {form.fname.data}! '
              f'\nPlease login with your new account.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# portfolio route
@app.route('/portfolio', methods=['GET','POST'])
def portfolio():
    return render_template('portfolio.html', title='Portfolio')

# logout route
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

# portfolio test
@app.route('/portfolio-test', methods=['GET', 'POST'])
@login_required
def portfolio_test():

    print(current_user['_id'])
    print(current_user['password'])
    print(current_user['fname'])
    print(current_user['lname'])
    print(current_user['brokerage'])
    '''
    user = User.objects.get(pk='test1@gmail.com')
    print(user.brokerage)
    ''' 
    stocks = ["fb", "tsla", "aapl", "mvis", "xlnx"]
    date = get_most_recent_business_day()
    data = (get_stock_data(stocks, date, date))
    # create the AddStockForm form object
    form = AddStockForm()
    if form.validate_on_submit():
        # inserthere
        user = User.objects.get(pk=current_user['_id'])
        user.portfolio[0].ticker = "fb"
        user.save()
        flash(f"test flash")
        return redirect(url_for('portfolio-test', 'success'))
    return render_template('portfolio.html', title='Portfolio Test', stockdata=data, form=form)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)