import os,platform,logging

if platform.platform('windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),\
        os.getenv('HOMEPATH'),\
            'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print('save to log', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug('start program')
logging.info('some actions')
logging.warning('program die')
