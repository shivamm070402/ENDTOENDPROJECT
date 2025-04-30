import os
import logging
from datetime import datetime
import sys

from src.exception import CustomException

# Step 1: Create logs directory if it doesn't exist
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Step 2: Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Step 3: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [Line: %(lineno)d] [%(name)s] [%(levelname)s] - %(message)s",
    level=logging.INFO,
)



