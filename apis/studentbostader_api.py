from selenium import webdriver
import sys
import time
import string
import json


class Checker(object):

    def __init__(self, path_to_driver, url):
        self.path_to_driver = path_to_driver
        if "windows" in sys.platform:
            self.path_to_driver += ".exe"

        self.browser = webdriver.PhantomJS(executable_path=self.path_to_driver)
        self.browser.set_window_size(1120, 550)
        self.browser.get(url)

        # In order to make sure the page is fully loaded
        time.sleep(5)

        print("Checker started")

    def get_new(self):
        new = []

        unfiltered_hrefs = self.browser.find_elements_by_tag_name('a')
        filtered_hrefs = []

        for a in unfiltered_hrefs:
            if "sok-bostad/ledig-bostad?refid=" in a.get_attribute('href'):
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
        self.browser.get(self.browser.current_url)


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
