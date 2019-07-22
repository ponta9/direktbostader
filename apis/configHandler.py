import os
import sys
import string
import configparser

class Config(object):

    def __init__(self):
        self.values = configparser.ConfigParser(allow_no_value=True)
        
        if not os.path.exists('settings.ini'):
            #create config
            self.values['DEFAULT'] = {
                                     '# Dont Show browser':None,
                                     'Headless': 'True',
                                     '# Interval between website call in seconds':None,
                                     'Interval': '30',
                                     '# Url to check':None,
                                     'Url': 'https://www.studentbostader.se/sv/sok-bostad/lediga-bostader?actionId=&omraden=&egenskaper=SNABB&oboTyper=#&pagination=0&paginationantal=1000#',
                                     '# Will send crash report to notification services':None,
                                     'CrashReportNotification': 'True'
                                     }
                
            self.values['Pushbullet'] = {'Enabled': 'False',
                                         'FirstPushbullet': 'True',
                                         'Token': 'TOKENHERE',
                                         '# Emails to send notifications to seperated by a comma':None,
                                         'Emails': 'email1@example.com,email2@example.com'
                                         }
                                            
            self.values['Twilio'] = {'Enabled': 'False',
                                     'FirstTwilio': 'True',
                                     'AccountSid': 'ACCOUNTSIDHERE',
                                     'AuthToken': 'AUTHTOKENHERE',
                                     'FromPhoneNumber': 'FROMNUMBERHERE',
                                     '# Emails to send notifications to seperated by a comma':None,
                                     'ToPhoneNumbers': 'Phonenumber1,PhoneNumber2'
                                     }
    
            with open('settings.ini', 'w') as configfile:
                self.values.write(configfile)
            
            sys.exit("settings.ini created now go configure it.")
            
        else:
            self.values.read('settings.ini')
            print("Headless mode = " + str(self.values['DEFAULT'].getboolean('Headless')) )
            print("Pushbullet Enabled = " + str(self.values['Pushbullet'].getboolean('Enabled')) )
            print("Twilio Enabled = " + str(self.values['Twilio'].getboolean('Enabled')) )
            
            if(not self.values['Twilio'].getboolean('Enabled') and not self.values['Pushbullet'].getboolean('Enabled') ):
                print("WARNING NO SMS NOTIFICATION OR PUSHBULLET NOTIFICATION WILL BE SENT")

    def saveValues(self):
        with open('settings.ini', 'w') as configfile:
            self.values.write(configfile)
