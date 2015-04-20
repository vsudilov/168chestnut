import multiprocessing

#bind = "0.0.0.0:5002"
bind = "unix:/tmp/gunicorn_168.sock"
workers = multiprocessing.cpu_count() * 2 + 1
max_requests = 100
preload_app = True
chdir = '/var/www_168/168chestnut/forum'
daemon = True
debug = False
errorlog = '/tmp/gunicorn.168.error.log'
accesslog = '/tmp/gunicorn.168.access.log'
pidfile = '/tmp/gunicorn.168.pid'
