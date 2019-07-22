import requests
import json


class Pusher(object):

    def __init__(self, token):
        self.token = token

    def send_apartment_found_push(self, email, href, address):
        title = "Apartment on %s!" % address
        body = "Click here to view it."

        r = requests.post(url="https://api.pushbullet.com/v2/pushes",
                          headers={"Access-Token": self.token, "Content-Type": "application/json"},
                          data='{"body": "%s", "title": "%s", "type": "link", "url": "%s", "email": "%s"}'
                               % (body, title, href, email))

        if r.status_code != 200:
            raise Exception("Pushbullet error: " + r.text)

    def notify_all(self, apartments, emails):
        if not apartments:
            return

        for apartment in apartments:
            for email in emails:
                print("\nNotifying %s about %s" % (email, apartment["address"]), end="\r", flush=True)
                self.send_apartment_found_push(email, apartment["href"], apartment["address"])
                
        print("\n")#new line so the noticication is not overwritten

    def send_crash_report(self, exception, email, twilioEnabled):
        title = "Crash"
        if twilioEnabled:
            from twilio.base.exceptions import TwilioRestException
            if exception is TwilioRestException:
                body = "Cant handle Twilio exception. Please check the console"
            else:
                body = str(exception) 

        r = requests.post(url="https://api.pushbullet.com/v2/pushes",
            headers={"Access-Token": self.token, "Content-Type": "application/json"},
            data='{"body": "%s", "title": "%s", "type": "note", "email": "%s"}'
                 % (body, title, email))

        if r.status_code != 200:
            raise Exception("email should be here: " + email + "Pushbullet error: " + r.text)

    # Never used, and probably will never be.
    def send_initial_greeting(self, emails):
        body = "You will now receive a Pusbullet when a apartment becomes available on the provided link"
        print(body)
        print("If you didn't receive a the above message on Pusbullet please check your pusbullet config")
        for email in emails:
            title = "Hej %s!" % email
            r = requests.post(url="https://api.pushbullet.com/v2/pushes",
                headers={"Access-Token": self.token, "Content-Type": "application/json"},
                data='{"body": "%s", "title": "%s", "type": "note", "email": "%s"}'
                     % (body, title, email))

            if r.status_code != 200:
                raise Exception("Pushbullet error: " + r.text)
