import mido
import time
import math
import typing
import os

# Class that create and manipulate a MIDI file
class MIDIFileManagerInterface():
    file_path: str      # File path to store MIDI instructions
    file: typing.IO     # IO object that represents a file

    # Set the MIDI file path
    def setFilePath(self, file_path):
        pass

    # Get the MIDI file path
    def getFilePath(self):
        pass

    # Open the MIDI file
    def openFile(self):
        pass

    # Close the MIDI file
    def closeFile(self):
        pass

    # Starts playing a note
    def setNoteOn(self, note, velocity, time):
        pass

    # Stops playing a note
    def setNoteOff(self, note, velocity, time):
        pass

    # Change the instrument that is been played
    def changeInstrument(self, instrument, time):
        pass
    
    # Change the tempo of the song
    def changeTempo(self, bpm, time):
        pass

# Class that implements MIDIFileManagerInterface
class MIDIFileManager():

    file_path: str          # File path to store MIDI instructions
    file: mido.MidiFile     # Mido MIDI File object

    # Set the MIDI file path
    def setFilePath(self, file_path):
        self.file_path = file_path

    # Get the MIDI file path
    def getFilePath(self):
        return self.file_path

    # Open the MIDI file
    def openFile(self):
        dirname = os.path.dirname(self.file_path)
        if not os.path.exists(dirname) and dirname != '':
            os.makedirs(dirname)
        self.file = mido.MidiFile()
        self.tempo_track = mido.MidiTrack()
        self.audio_track = mido.MidiTrack()
        self.instrument_track = mido.MidiTrack()
        self.file.tracks.append(self.tempo_track)
        self.file.tracks.append(self.audio_track)
        self.file.tracks.append(self.instrument_track)

    # Close the MIDI file
    def closeFile(self):
        self.file.save(self.file_path)

    # Starts playing a note on the audio_track
    def setNoteOn(self, note=125, velocity=64, time=0):
        self.audio_track.append(mido.Message('note_on', note=note, velocity=velocity, time=time))
        
    # Stops playing a note on the audio_track
    def setNoteOff(self, note=125, velocity=64, time=1000):
        self.audio_track.append(mido.Message('note_off', note=note, velocity=velocity, time=time))

    # Change the instrument that is been played
    def changeInstrument(self, instrument=0, time=0):
        self.instrument_track.append(mido.Message('program_change', program=instrument, time=time))

    # Change the tempo of the song
    def changeTempo(self, bpm=60, time=0):
        self.tempo_track.append(mido.MetaMessage('set_tempo', tempo=math.ceil(mido.bpm2tempo(bpm)/2), time=time))
