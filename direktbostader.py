import os
import time
import traceback
import configparser

from apis.studentbostader_api import Checker
from apis.configHandler import Config

last_notified = 0
CHROMEDRIVER_PATH = os.path.join(os.getcwd(), "chromedriver")
config = Config() #get the config

#Default
headless = config.values['DEFAULT'].getboolean('Headless')
interval = (int(config.values['DEFAULT']['Interval'])) # messed up for testing
url = config.values['DEFAULT']['Url']
CrashReportNotification = True
#Pushbullet
pushbulletEnabled = config.values['Pushbullet'].getboolean('Enabled')
firstPushbullet = config.values['Pushbullet'].getboolean('FirstPushbullet')
token = config.values['Pushbullet']['Token']
emails = config.values['Pushbullet']['Emails'].split(',')
#Twilio
twilioEnabled = config.values['Twilio'].getboolean('Enabled')
firstTwilio = config.values['Twilio'].getboolean('FirstTwilio')
accountSid = config.values['Twilio']['AccountSid']
authToken = config.values['Twilio']['AuthToken']
fromNumber = config.values['Twilio']['FromPhoneNumber']
toNumbers = config.values['Twilio']['ToPhoneNumbers'].split(',')

checker = Checker(CHROMEDRIVER_PATH,url,headless)

if pushbulletEnabled:
    from apis.pushbullet_api import Pusher
    pusher = Pusher(token)

if twilioEnabled:
    from apis.twilio_sendSms import Sms
    sms = Sms(accountSid,authToken)
    

while True:
    try:
        apartments = checker.get_new()
        if pushbulletEnabled:
            if firstPushbullet:
                pusher.send_initial_greeting(emails)
                config.values['Pushbullet']['FirstPushbullet'] = 'False'
                firstPushbullet = config.values['Pushbullet'].getboolean('FirstPushbullet')
                config.saveValues()

            pusher.notify_all(apartments, emails)
        if twilioEnabled:
            if firstTwilio:
                sms.send_initial_greeting(fromNumber,toNumbers)
                config.values['Twilio']['FirstTwilio'] = 'False'
                firstTwilio = config.values['Twilio'].getboolean('FirstTwilio')
                config.saveValues()

            sms.notify_all(apartments, fromNumber, toNumbers)
        checker.refresh()
        time.sleep(interval) 
    except Exception as e:
        print("\n", end="\r", flush=True)
        print(e)
        traceback.print_tb(e.__traceback__)
        if time.time() > 60*30 + last_notified:
            last_notified = time.time()
            if twilioEnabled:
                sms.send_crash_report(e, fromNumber, toNumbers[0])
            if pushbulletEnabled:
                pusher.send_crash_report(e, emails[0],twilioEnabled) #first email is the one to send crash report to


        checker = Checker(CHROMEDRIVER_PATH, url, headless)