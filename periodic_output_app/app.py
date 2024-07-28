from datetime import UTC, datetime
import os
import time
from dotenv import load_dotenv

load_dotenv()


sleep_time = int(os.getenv("SLEEP_TIME", "10"))

while True:
	print(f"{datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")}: Sleeping for {sleep_time} seconds")
	time.sleep(sleep_time)

