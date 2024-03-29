import FreeText
import MIDIController
import MIDIFileManager
import ConfigReader

# Class to create MIDI files from text
class MIDICreatorInterface():

    freetext: object        # FreeTextInterface object
    controller: object      # MIDIControllerInterface object
    file_manager: object    # MIDIFileManagerInterface object
    config: object          # ConfigReaderInterface object

    # Set the freetext object, to manipulate the text received
    def setFreeText(self, freetext):
        pass

    # Set the controller object, to control MIDI parameters
    def setController(self, controller):
        pass

    # Set the config object, to access the configuration dictionaries
    def setConfig(self, config):
        pass

    # Generate a MIDI file from a text, and store it in the file
    def generateMIDIFile(self, file_path, text):
        pass

# Class that implements MIDICreatorInterface
class MIDICreator():

    freetext: object        # FreeTextInterface object
    controller: object      # MIDIControllerInterface object
    file_manager: object    # MIDIFileManagerInterface object
    config: object          # ConfigReaderInterface object

    # Set the freetext object, to manipulate the text received
    def setFreeText(self, freetext):
        self.freetext = freetext

    # Set the controller object, to control MIDI parameters
    def setController(self, controller):
        self.controller = controller

    # Set the config object, to access the configuration dictionaries
    def setConfig(self, config):
        self.config = config

    # Generate a MIDI file from a text, and store it in the file
    def generateMIDIFile(self, file_path, text):
        self.freetext.setFreeText(text)
        self.controller.midi_manager.setFilePath(file_path)
        self.controller.midi_manager.openFile()
        self.controller.resetParameters()
        self.freetext.goToFirstWord()
        special_commands = self.config.getSpecialCommands()
        notes_translations = self.config.getNotesTranslations()
        notes = self.config.getNotes()
        instruments = self.config.getInstruments()
        word = self.freetext.getCurrentWord()
        while word != "":
            while word != "":
                strip = 1
                if special_commands.get(word[:4],None) == "increase_bpm":
                    self.controller.incrementBPM(80)
                    strip = 4
                elif special_commands.get(word[:2],None) == "octave_up":
                    self.controller.octaveUp()
                    strip = 2
                elif special_commands.get(word[:2],None) == "octave_down":
                    self.controller.octaveDown()
                    strip = 2
                elif special_commands.get(word[:1],None) == "random_bpm":
                    self.controller.setRandomBPM()
                elif special_commands.get(word[:1],None) == "double_volume":
                    self.controller.doubleVolume()
                elif special_commands.get(word[:1],None) == "default_volume":
                    self.controller.setVolumeToDefault()
                elif special_commands.get(word[:1],None) == "change_instrument":
                    self.controller.setRandomInstrument(list(instruments.keys()))
                elif special_commands.get(word[:1],None) == "random_note":
                    self.controller.playRandomNote(list(notes.values()))
                elif special_commands.get(word[:1],None) == "repeat_note":
                    self.controller.repeatNote()
                elif special_commands.get(word[:1],None) == "silence":
                    self.controller.silence()
                elif notes.get(notes_translations.get(word[:1],None),None) != None:
                    self.controller.playNote(notes.get(notes_translations.get(word[:1],None),None))
                word = word[strip:]
            self.freetext.goToNextWord()
            word = self.freetext.getCurrentWord()
        self.controller.midi_manager.closeFile()

# Objects instantiations and configurations
freetext = FreeText.FreeText()
config = ConfigReader.ConfigReader()
config.readConfig()
midi_controller = MIDIController.MIDIController()
midi_controller.setMIDIManager(MIDIFileManager.MIDIFileManager())
midi_creator = MIDICreator()
midi_creator.setFreeText(freetext)
midi_creator.setController(midi_controller)
midi_creator.setConfig(config)
