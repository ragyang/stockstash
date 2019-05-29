import multiprocessing

# binds web server to port 8000
bind = "0.0.0.0:8000"

# number of worker threads
workers = multiprocessing.cpu_count() * 2 + 1

# access logs in stdout format
accesslog = "-" # STDOUT
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
loglevel = "debug"
capture_output = True
enable_stdio_inheritance = True