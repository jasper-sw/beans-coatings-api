import threading
import logging
import sys
from flask_api import create_flask_api

try:
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.WARNING)
    logging.addLevelName(69, "INFO")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.log(69, "Initializing beans-coatings-api...")

    flask_thread = threading.Thread(target=create_flask_api,
                                    name="flask_api",
                                    kwargs={"logger": logger})
    flask_thread.start()
except Exception as e:
    raise e
