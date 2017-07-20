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

    def notify_all(self, apartments):
        if not apartments:
            return

        with open("emails.json") as file:
            emails = json.load(file)["emails"]

        for apartment in apartments:
            for email in emails:
                print("Notifying %s about %s" % (email, apartment["address"]))
                self.send_apartment_found_push(email, apartment["href"], apartment["address"])

    def send_crash_report(self, exception):
        title = "Crash"
        body = str(exception)

        r = requests.post(url="https://api.pushbullet.com/v2/pushes",
                          headers={"Access-Token": self.token, "Content-Type": "application/json"},
                          data='{"body": "%s", "title": "%s", "type": "note", "email": "%s"}'
                               % (body, title, "tresxnine@gmail.com"))

        if r.status_code != 200:
            raise Exception("Pushbullet error: " + r.text)

    # Never used, and probably will never be.
    def send_initial_greeting(self, email):
        title = "Hej %s!" % email
        body = "Du kommer nu att fa mail (eller Pushbullet notiser, om du laddar ner Pushbullet-appen)" \
               "sa fort en lagenhet laggs upp pa studentbostaders hemsida. Lycka till!"

        r = requests.post(url="https://api.pushbullet.com/v2/pushes",
                          headers={"Access-Token": self.token, "Content-Type": "application/json"},
                          data='{"body": "%s", "title": "%s", "type": "note", "email": "%s"}'
                               % (body, title, email))

        if r.status_code != 200:
            raise Exception("Pushbullet error: " + r.text)
