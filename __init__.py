import re

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler


class Maps(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

        # initialize settings values
        self.settings["current_location"] = self.get_current_location()

    @intent_file_handler('maps.intent')
    def handle_maps(self, message):
        self.speak_dialog('maps')

    def get_current_location(self):
        """
        obtain user's city from the device's config during initialization
        :return: coordinates (longitude, latitude)
        """

    def get_travel_time(self, start_location="", destination=""):
        """
        Calculates the travel time from the start_location to the destination
        :param start_location: (longitude, latitude)
        :param destination: (longitude, latitude)
        :return: travel time in minutes
        """
        if not destination:
            return

        if not start_location:
            # start_location = user's stored location at device's initialization
            start_location = (0,0)

    def _extract_origin(self, utt):
        rx_file = self.find_resource('origin.rx', 'regex')
        if rx_file:
            with open(rx_file) as f:
                for pattern in f.read().splitlines():
                    patt = pattern.strip()
                    match = re.search(patt, utt)
                    if match:
                        try:
                            return match.group("Origin")
                        except IndexError as e:
                            pass
        return None


    def _extract_destination(self, utt):
        rx_file = self.find_resource('destination.rx', 'regex')
        if rx_file:
            with open(rx_file) as f:
                for pattern in f.read().splitlines():
                    patt = pattern.strip()
                    match = re.search(patt, utt)
                    if match:
                        try:
                            return match.group("Destination")
                        except IndexError as e:
                            pass
        return None

    def _convert_address_to_coordinates(self, address):
        """
        :param address: (string) address format (ex. '1234 lincoln road, San Jose, California 98765')
        :return:  coordinates (longitude, latitude)
        """


    @intent_handler(IntentBuilder("").require("Query").require("Duration").require("Destination"))
    def handle_query_travel_time(self, message):


def create_skill():
    return Maps()

