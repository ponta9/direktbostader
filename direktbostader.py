import os
import time

from apis.studentbostader_api import Checker
from apis.pushbullet_api import Pusher, notify_all
from apis.gspread_api import Driver


FREQ = 30
PHANTOMJS_PATH = os.path.join(os.getcwd(), "phantomjs")
URL = "https://www.studentbostader.se/sv/sok-bostad/lediga-bostader?actionId=&omraden=&egenskaper=SNABB&objektTyper="
PUSHBULLET_TOKEN = "o.qF8AZoBuPs1fjJvhHGl4utSckK79c5Hi"

checker = Checker(PHANTOMJS_PATH, URL)
pusher = Pusher(PUSHBULLET_TOKEN)
driver = Driver()

while True:
    time.sleep(FREQ)
    apartments = checker.get_new()
    notify_all(pusher, driver, apartments)
    checker.refresh()
