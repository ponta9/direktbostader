# **Currently looking for appartment myself. Will release once i find something for myself :). Also its my first python project so be gentle**

# Direktbostader-Chrome 
A server-app for checking Studentbostäder's website for new apartments. The standard link checks after accommodations on first come, first served' basis

### Prerequisites
Here is the software and what version i know its currently working on

```
Python 3.7.3
Selenium 3.141.0
Twilio 6.29.1
Requests 2.22.0
```

# New Features
* [X] Support for Chromedriver instead of deprecated Phanomjs support in Selenium
* [X] Fixed Selenium checking as it crashed with chrome
* [x] Setting to Enable/Disable Headless mode
* [X] Showing time while checking so you can be sure its not frozen and removing INFO messages from Chrome
* [X] Sending SMS with Twillio
* [ ] Completing this readme

I may also add(but dont count on it)
* [ ] A proper settings file

# Original Features
* PhantomJS with Selenium(Support is deprecated)
* PushBullet api to interact with Pushbullet
* Selenium to check available accommodations
* Already seen apartments in a file.

###  Getting Started
Tested on Windows and Linux. 

Add Email/Emails in emails.json(For Pushbullet)
```
{"emails": ["example@example.comm"]}
```

## Running the program
Run direktbostader.py

This how the program should look when running. Updating the current time when it checks(currently every 30 seconds)
![Image of how the program should look](https://i.imgur.com/wkdtIOZ.png)

## Built With

* [Twilio](https://github.com/twilio/twilio-python) - A module for using the Twilio REST API and generating valid TwiML.
* [Selenium](https://github.com/SeleniumHQ/selenium) - A browser automation framework and ecosystem
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) - WebDriver for Chrome
* [PushBullet](https://www.pushbullet.com) - Send notifications to your phone


## Credits
* **Daniel Roos** [RoosDaniel](https://github.com/RoosDaniel) - For making the initial program -  [direktbostader](https://github.com/RoosDaniel/direktbostader)
