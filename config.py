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
"""   """
# MailTemplate file
HTML_PATH = "templates/modelo_720.html"
# Database File
EXCEL_PATH = 'templates/Datos_email_def.xlsx'

# Attachment file path
ATTACHMENT_PATH = 'assets/'
ATTACHMENT_NAME = 'Ejemplo 720 2019.pdf'
# Mail Subject
SUBJECT = 'Accurate Quant - Modelo 720'

"""   """

# smtp settings
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = '465'

# the address and name the email comes from
#FROM_EMAIL = 'alertas.accuratequant@gmail.com'
#FROM_PASSWORD = 'EstateAlLoro'
FROM_NAME = 'AccurateQuant'
FROM_EMAIL = 'info@accuratequant.com'
FROM_PASSWORD = 'Accurate2'

# test recipients list
TEST_RECIPIENTS = [
    {'EMAIL':'acarpio@accuratequant.com','NAME': 'Jose', 'SALDO_MEDIO_MONEDA': 'dynamic input 2',
     'SALDO_FINAL_MONEDA': 'dynamic input 3', 'PRIMER_INGRESO': 'dynamic input 4', 'CODIGO_CUENTA': 'dynamic input 5'}
]


#  add or modify category names and links as per your requirements.
# https://support.awesome-table.com/hc/en-us/articles/115002196665-Display-images-from-Google-Drive
_IDS_IMAGES_DRIVE = {'graph1': '1SGrU_The288mvi_lF15Av3Z1GyJ6AarU',
                     'graph2': '1o3SoM3nPXUOnAKYjYiOf_5Ny1Uhu0Zvc',
                     'graph3': '1XD-uMceKATRIaQcKkqhJbiI1SmXfr33h',
                     'graph4': '1N2db5GAttk0TtGehGACRxjWJXZfSZfOS',
                     'graph5': '1zoU9wVgfXOHtittDZnokfEaLT6Iv2IZ0',}

CATEGORY_TYPE = {K: 'https://drive.google.com/thumbnail?id='+_IDS_IMAGES_DRIVE[K]+'&sz=w600-h600'
                 for K in _IDS_IMAGES_DRIVE}