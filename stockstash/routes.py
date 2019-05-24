from flask import Flask, jsonify, render_template, url_for, flash, redirect
from stockstash import app, mongo, bcrypt
from stockstash.models import User, Portfolio, Watchlist
from stockstash.forms import RegistrationForm, LoginForm, AddStockForm, AddStockFormWatchlist
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
            return redirect(url_for('portfolio'))
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
                    brokerage=form.brokerage.data, portfolio=Portfolio())
        user.save()
        flash(f'Welcome to StockStash {form.fname.data}! '
              f'\nPlease login with your new account.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# logout route
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

# portfolio
@app.route('/portfolio', methods=['GET', 'POST'])
@login_required
def portfolio():

    # Get the stock data from the current users portfolio
    tickers = []
    user = User.objects.get(pk=current_user['_id'])
    for stock in user['portfolio']:
        tickers.append(stock['ticker'])
    date = get_most_recent_business_day()
    stockdata = (get_stock_data(tickers, date, date))
    
    # Form to add stocks to portfolio
    form = AddStockForm()
    user = User.objects.get(pk=current_user['_id'])
    if form.validate_on_submit():
        new_stock = Portfolio(ticker=form.ticker.data, price=form.price.data)
        user = User.objects.get(pk=current_user['_id'])
        user.portfolio.append(new_stock)
        user.save()
        flash(f'New stock added!', 'success')
        return redirect(url_for('portfolio'))

    return render_template('portfolio.html', title='Portfolio', data=stockdata, form=form)

# watchlist
@app.route('/watchlist', methods=['GET', 'POST'])
@login_required
def watchlist():

    # Get the stock data from api
    tickers = []
    user = User.objects.get(pk=current_user['_id'])
    for stock in user['watchlist']:
        tickers.append(stock['ticker'])
    date = get_most_recent_business_day()
    apidata = (get_stock_data(tickers, date, date))

    # Get the stock data from database
    dbdata = {}
    for stock in user['watchlist']:
        dbdata[stock['ticker']] = {
            'High Price': float(stock['highprice']),
            'Low Price': float(stock['lowprice'])
        }

    # Form to add stocks to portfolio
    form = AddStockFormWatchlist()
    user = User.objects.get(pk=current_user['_id'])
    if form.validate_on_submit():
        new_stock = Watchlist(ticker=form.ticker.data, lowprice=form.lowprice.data, highprice=form.highprice.data)
        user = User.objects.get(pk=current_user['_id'])
        user.watchlist.append(new_stock)
        user.save()
        flash(f'New stock added!', 'success')
        return redirect(url_for('watchlist'))

    return render_template('watchlist.html', title='Watchlist', apidata=apidata,  dbdata=dbdata, form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)