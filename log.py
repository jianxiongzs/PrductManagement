import logging

logger = logging.getLogger('ProductManagement')
formatter = logging.Formatter('%(name)s %(asctime)s %(levelname)s: %(message)s')

file_handler = logging.FileHandler('pm.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)
