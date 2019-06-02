# stockstash
> A stock portfolio web application built with Flask.

stockstash is a Flask application ideal for the individual investor. This application allows users to track their own customizable stock market portfolio and watchlist. The application will utilize RESTful web services to call current and historical stock data and a databased backed system to track profile changes and updates.

### Compile / Run Instructions
Run the following commands in the root project directory.

#### Using Flask Development Server:
** Note: use a virtualenv when using this method
``` bash
$ pip install -r requirements.txt
$ python run.py
NOTE: to run with Gunicorn WSGI Server, use the following command instead of $ python run.py
$ ["gunicorn", "--config", "./stockstash/config/gunicorn_config.py", "stockstash:app"]
```


### The Team
Chris Ragasa:  [[LinkedIn](https://www.linkedin.com/in/cragasa/), [GitHub](https://github.com/chrisragasa)]

Derek Yang: [[LinkedIn](https://www.linkedin.com/in/yangd01234567/), [GitHub](https://github.com/yangd01234)]
