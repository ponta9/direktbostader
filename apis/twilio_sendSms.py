# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


class Sms(object):

    def __init__(self, account_sid,auth_token):
        self.client = Client(account_sid, auth_token)
    
    
    def notify_all(self, apartments, fromNumber, toNumbers):
        if not apartments:
            return
        
        for apartment in apartments:
            for toNumber in toNumbers:
                print("\nNotifying %s about %s" % (toNumber, apartment["address"]), end="\r", flush=True)
                message = self.client.messages \
                    .create(
                        body="Apartment on " + apartment["address"] + " " + apartment["href"],
                        from_=fromNumber,
                        to=toNumber
                        )
        print("\n")#new line so the noticication is not overwritten

    def send_crash_report(self, exception, fromNumber, toNumber):
        
        message = self.client.messages \
            .create(
                body="Crash " + str(exception),
                from_=fromNumber,
                to=toNumber
                )

    def send_initial_greeting(self, fromNumber, toNumbers):
        message ="\nYou will now receive a SMS when a apartment becomes available on the provided link"
        print(message)
        print("If you didn't receive the above SMS please check your Twilio config")
        for toNumber in toNumbers:
            message = self.client.messages \
                .create(
                    body=message,
                    from_=fromNumber,
                    to=toNumber
                    )
