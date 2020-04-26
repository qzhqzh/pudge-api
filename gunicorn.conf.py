import multiprocessing


proc_name = 'gunicorn_pudge'

bind = "0.0.0.0:80"
workers = 1
threads = 1
# workers = multiprocessing.cpu_count() * 2 + 1  # 官网推荐，这个测试机会卡

accesslog = '/root/www/config/storage/logs/config.gunicorn.access.logs'
# accesslog = '-' # 记录到标准输出，可以在配合 supervisor 的时候，有 supervisor 来转储日志
errorlog = '/root/www/config/storage/logs/config.gunicorn.error.logs'
loglevel = 'info'

reload = True  # 热加载
