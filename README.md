
# Direktbostader-Chrome 
A server-app for checking Studentbostäder's website for new apartments. The standard link checks after accommodations on first come, first served' basis

### Prerequisites
Here is the software and what version i know its currently working on

```
Python 3.7.3
Selenium 3.141.0
Twilio 6.29.1
Requests 2.22.0
ChromeDriver 75.0.3770.140
configparser 3.7.4
```

# New Features
* [X] Support for Chromedriver instead of deprecated Phanomjs support in Selenium
* [X] Fixed Selenium checking as it crashed with chrome
* [x] Setting to Enable/Disable Headless mode
* [X] Showing time while checking so you can be sure its not frozen and removing INFO messages from Chrome
* [X] Sending SMS with Twillio
* [X] A proper settings file
* [X] Now sends out the welcome message on Pushbullet and Twilio
* [X] This readme

# Original Features
* PhantomJS with Selenium(Support is deprecated)
* PushBullet api to interact with Pushbullet
* Selenium to check available accommodations
* Already seen apartments in a file.

###  Getting Started
Tested on Windows but i don't see why it should not work in Linux

On the first run the program will create a settings.ini file
Here is a example config

Example Config
```
[DEFAULT]
headless = true
interval = 30
url = https://www.studentbostader.se/sv/sok-bostad/lediga-bostader?actionId=&omraden=&egenskaper=SNABB&oboTyper=#&pagination=0&paginationantal=1000#
crashreportnotification = True

[Pushbullet]
enabled = True
firstpushbullet = False
token = o.ojfs9hjsehf3420i529562h34hu9234
emails = myEmail@domain.com,my2Email@domain.com

[Twilio]
enabled = true
firsttwilio = False
accountsid = ybdsahusdhqrhu3hurh9q3re3
authtoken = uh41hu43pfdhnufh223uh4r2
fromphonenumber = +46numberhere
tophonenumbers = +46numberhere,+46numberhere
```

Twilio is for receiving the info by SMS **P.S you can get free trial with more then enough balance**
Pushbullet is for receiving the info with a push notification on your phone


## Running the program
Run direktbostader.py

First time running a module(twilio/pushbullet) you should recive a welcome message on the service to check that it is working
Example "You will now receive a Pusbullet when a apartment becomes available on the provided link"

This how the program should look when running. Updating the current time when it checks(currently every 30 seconds)
![Image of how the program should look](https://i.imgur.com/wkdtIOZ.png)

## Built With

* [Twilio](https://github.com/twilio/twilio-python) - A module for using the Twilio REST API and generating valid TwiML.
* [Selenium](https://github.com/SeleniumHQ/selenium) - A browser automation framework and ecosystem
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) - WebDriver for Chrome
* [PushBullet](https://www.pushbullet.com) - Send notifications to your phone
* [ConfigParser](https://docs.python.org/3/library/configparser.html) - A config 


## Credits
* **Daniel Roos** [RoosDaniel](https://github.com/RoosDaniel) - For making the initial program -  [direktbostader](https://github.com/RoosDaniel/direktbostader)
