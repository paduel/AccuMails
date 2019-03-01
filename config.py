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
HTML_PATH = "templates/rentabilidades.html"

# Database File
EXCEL_PATH = 'templates/rentabilidades.xlsx'

# Mail Subject
SUBJECT = 'Resumen 2018'

# smtp settings
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = '465'

# the address and name the email comes from
FROM_NAME = 'AccurateQuant'
FROM_EMAIL = 'alertas.accuratequant@gmail.com'
FROM_PASSWORD = 'EstateAlLoro'

# test recipients list
TEST_RECIPIENTS = [
    {'EMAIL':'jcarpio@accuratequant.com','NAME': 'Jose', 'SALDO_MEDIO_MONEDA': 'dynamic input 2',
     'SALDO_FINAL_MONEDA': 'dynamic input 3', 'PRIMER_INGRESO': 'dynamic input 4', 'CODIGO_CUENTA': 'dynamic input 5'}
]
