from mycroft import MycroftSkill, intent_file_handler


class RecipeReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.recipe.intent')
    def handle_reader_recipe(self, message):
        self.speak_dialog('reader.recipe')


def create_skill():
    return RecipeReader()

