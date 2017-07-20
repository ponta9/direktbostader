import os
import time
import traceback

from apis.studentbostader_api import Checker
from apis.pushbullet_api import Pusher

last_notified = 0
FREQ = 30
PHANTOMJS_PATH = os.path.join(os.getcwd(), "phantomjs")
URL = "https://www.studentbostader.se/sv/sok-bostad/lediga-bostader" \
      "?actionId=&omraden=&egenskaper=SNABB&objektTyper=#&pagination=0&paginationantal=1000#"
with open("apis/pushbullet_token") as file:
    PUSHBULLET_TOKEN = file.read()

checker = Checker(PHANTOMJS_PATH, URL)
pusher = Pusher(PUSHBULLET_TOKEN)

while True:
    try:
        apartments = checker.get_new()
        pusher.notify_all(apartments)
        checker.refresh()
        time.sleep(FREQ)
    except Exception as e:
        print(e)
        traceback.print_tb(e.__traceback__)

        if time.time() > 60*30 + last_notified:
            last_notified = time.time()
            pusher.send_crash_report(e)

        checker = Checker(PHANTOMJS_PATH, URL)
