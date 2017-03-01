import os
import time

from apis.studentbostader_api import Checker
from apis.pushbullet_api import Pusher, notify_all
from apis.gspread_api import Driver

# URL = "https://www.studentbostader.se/sv/sok-bostad/lediga-bostader?actionId=&omraden=&egenskaper=SNABB&objektTyper="
URL = "https://www.studentbostader.se/sv/sok-bostad/lediga-bostader?actionId=&omraden=&egenskaper=&objektTyper="
PUSHBULLET_TOKEN = "o.qF8AZoBuPs1fjJvhHGl4utSckK79c5Hi"
PHANTOMJS_PATH = os.path.join(os.getcwd(), "phantomjs")

checker = Checker(PHANTOMJS_PATH, URL)
pusher = Pusher(PUSHBULLET_TOKEN)
driver = Driver()

while True:
    time.sleep(15)
    apartments = checker.get_new()
    notify_all(pusher, driver, apartments)
    checker.refresh()
