import logging
from datetime import datetime

current_time_stamp=f"{datetime.now().strftime('%Y-%m-%d')}"

log_file_name = f"{current_time_stamp}.log"

logging.basicConfig(filename=f"./logs/{log_file_name}",
                    filemode="a",
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
