#!/usr/bin/env python3

import LCD1602
import time
from datetime import datetime

def setup():
	LCD1602.init(0x27, 1)	# init(slave address, background light)
	time.sleep(2)

def destroy():
	LCD1602.clear()

def update_time():
	current_timestamp = datetime.now()
	date_cur = current_timestamp.strftime('%Y-%m-%d')
	time_cur = current_timestamp.strftime('%H:%M:%S')
	LCD1602.write(0, 0, date_cur)
	LCD1602.write(1, 1, time_cur)




if __name__ == "__main__":
	try:
		setup()
		while True:
			update_time()
			time.sleep(0.1)
	except KeyboardInterrupt:
		destroy()
