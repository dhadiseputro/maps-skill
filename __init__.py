from mycroft import MycroftSkill, intent_file_handler


class Maps(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('maps.intent')
    def handle_maps(self, message):
        self.speak_dialog('maps')


def create_skill():
    return Maps()

