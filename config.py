"""
Global config file. Change variable below as needed but ensure that the log have the correct permissions.
"""

from datetime import datetime

# file settings
LOG_FILENAME = 'tmp/pymailer.log'
CSV_RETRY_FILENAME = '/tmp/pymailer.csv'
STATS_FILE = 'tmp/pymailer-%s.stat' % str(datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')

# ACTION 
# -live for live environment 
# -test for test environment
ACTION = '-test'

# MailTemplate file
HTML_PATH = "mailTemplate.html"

# Database File
CSV_PATH = 'database.csv'

# Mail Subject
SUBJECT = 'SUBJECT'

# smtp settings
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = '465'

# the address and name the email comes from
FROM_NAME = 'AccurateQuant'
FROM_EMAIL = 'alertas.accuratequant@gmail.com'
FROM_PASSWORD = 'EstateAlLoro'

# test recipients list
TEST_RECIPIENTS = [
    {'email':'jcarpio@accuratequant.com','name': 'Jose', 'SALDO_MEDIO_MONEDA': 'dynamic input 2',
     'SALDO_FINAL_MONEDA': 'dynamic input 3', 'PRIMER_INGRESO': 'dynamic input 4', 'CÓDIGO_CUENTA': 'dynamic input 5'},
    {'email':'ialonso@accuratequant.com','name': 'Igor', 'SALDO_MEDIO_MONEDA': '50000',
     'SALDO_FINAL_MONEDA': '50000', 'PRIMER_INGRESO': '50000', 'CÓDIGO_CUENTA': 'X123321'}
]
