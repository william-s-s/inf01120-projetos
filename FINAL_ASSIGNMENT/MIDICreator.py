import FreeText
import MIDIController
import MIDIFileManager
import ConfigReader

# Class to create MIDI files from text
class MIDICreatorInterface():
    
    freetext: object
    controller: object
    file_manager: object
    config: object

    def setFreeText(self, freetext):
        pass

    def setController(self, controller):
        pass

    def setConfig(self, config):
        pass

    def generateMIDIFile(self, file_path, text):
        pass

class MIDICreator():

    freetext: object
    controller: object
    file_manager: object
    config: object

    def setFreeText(self, freetext):
        self.freetext = freetext

    def setController(self, controller):
        self.controller = controller

    def setConfig(self, config):
        self.config = config

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

freetext = FreeText.FreeText()
config = ConfigReader.ConfigReader()
config.readConfig()
midi_controller = MIDIController.MIDIController()
midi_controller.setMIDIManager(MIDIFileManager.MIDIFileManager())
midi_creator = MIDICreator()
midi_creator.setFreeText(freetext)
midi_creator.setController(midi_controller)
midi_creator.setConfig(config)
