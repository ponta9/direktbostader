from selenium import webdriver
import sys
import time
import string
import json
import datetime


class Checker(object):

    def __init__(self, path_to_driver, url, headlessOption):
        self.path_to_driver = path_to_driver
        if "windows" in sys.platform:
            self.path_to_driver += ".exe"
        
        option = webdriver.ChromeOptions()
        option.headless = headlessOption
        option.add_argument('--disable-search-geolocation-disclosure')
        option.add_argument('log-level=1')#Sets console log info level (INFO = 0, WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3)
        self.browser = webdriver.Chrome(executable_path=self.path_to_driver, options=option)
        self.browser.get(url)
        print(self.browser.current_url)


        time.sleep(5)
        print("Cheking...      ", end="\r", flush=True)
        

    def get_new(self):
        new = []

        unfiltered_hrefs = self.browser.find_elements_by_tag_name('a')
        filtered_hrefs = []
        
        for a in unfiltered_hrefs:
            if a.get_attribute('href') == None:
                time.sleep(0) #dirty way to ignore nontype, this is probably a stupid way of doing it.
            elif "sok-bostad/ledig-bostad?refid=" in a.get_attribute('href'):
                filtered_hrefs.append(a.get_attribute('href'))

        complete_address_list = []

        for address in self.browser.find_elements_by_class_name("ObjektAdress"):
            complete_address_list.append(sluggify(address.text))

        combined = []

        for address, href in zip(complete_address_list[1:], filtered_hrefs):   # First is a dummy
                combined.append({"address": address, "href": href})

        for apartment in combined:
            if not previously_seen(apartment["address"]):
                new.append(apartment)
                add_to_previously_seen(apartment["address"])
                
        return new

    def refresh(self):
        self.browser.refresh()
        self.browser.get(self.browser.current_url)
        print("Cheking..." + datetime.datetime.now().strftime("%I:%M:%S %p"),end="\r", flush=True)
        


def add_to_previously_seen(address):
    with open("apis/already_seen.json") as json_file:
        already_seen = json.load(json_file)

    seen = False

    for previous in already_seen:
        if previous["address"] == address:
            seen = True
            previous["time"] = time.time()

    if not seen:
        already_seen.append({"address": address, "time": time.time()})

    with open("apis/already_seen.json", "w") as json_file:
        json.dump(already_seen, json_file, indent=2)

    return seen


def previously_seen(address):

    with open("apis/already_seen.json") as json_file:
        already_seen = json.load(json_file)

    for previous in already_seen:
        if previous["address"] == address:
            seen = time.time() < 60*60*5 + previous["time"]     # If it's been seen in the last five hours
            return seen


def sluggify(address):

    sluggified = ""

    for letter in address:
        if letter in string.ascii_letters or letter in string.digits:
            sluggified += letter
        if letter.isspace():
            sluggified += "_"

    return sluggified
