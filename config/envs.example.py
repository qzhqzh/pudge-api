import os

DATABASE_NAME = 'pudge'
DATABASE_USER = 'pudge'
DATABASE_PASSWORD = 'pudge'
DATABASE_HOST = 'pudge-db'
DATABASE_PORT = '5432'

BACKUP_DIR = os.path.join('storage', 'backups')
SCAN_DIRS = [
    os.path.join('storage', 'scan')
]

MODE = 'dev'
