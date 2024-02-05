import json

# Class to load MIDI configuration from a file
class ConfigReaderInterface():

    config: dict = {}

    # Read configuration
    def readConfig(self):
        pass

    # Return the special commands configuration
    def getSpecialCommands(self):
        pass

    # Return the notes translations
    def getNotesTranslations(self):
        pass

    # Return notes information
    def getNotes(self):
        pass

    # Return instruments information
    def getInstruments(self):
        pass

# Class that implements ConfigReaderInterface
class ConfigReader():

    config: dict = {}

    # Read configuration from config.json
    def readConfig(self):
        with open('config.json') as config_data:
            self.config = json.load(config_data)
            config_data.close()

    # Return the special commands configuration
    def getSpecialCommands(self):
        return self.config['SPECIAL_COMMANDS']

    # Return the notes translations
    def getNotesTranslations(self):
        return self.config['NOTES_TRANSLATIONS']

    # Return notes information
    def getNotes(self):
        return self.config['NOTES']

    # Return instruments information
    def getInstruments(self):
        return self.config['INSTRUMENTS']