import random

# Class that controls the MIDI parameters
class MIDIControllerInterface():

    midi_manager: object    # MIDIFileManagerInterface object
    bpm: int                # Beats per minute of the sound
    volume: int             # Notes volume
    last_note: int          # Last note number
    octave: int             # Current note octave

    # Set midi manager attribute
    def setMIDIManager(self, midi_manager):
        pass

    # Plays a note
    def playNote(self, note):
        pass

    # Plays a random note
    def playRandomNote(self, notes):
        pass

    # Repeat the last note played
    def repeatNote(self):
        pass

    # Change an octave to the next one
    def octaveUp(self):
        pass

    # Change an octave to the previous one
    def octaveDown(self):
        pass

    # Doubles the notes volume
    def doubleVolume(self):
        pass

    # Set the volume to default value            
    def setVolumeToDefault(self):
        pass

    # Keep the audio silent for a certain duration
    def silence(self):
        pass

    # Increments the BPM by a given amount
    def incrementBPM(self, increment):
        pass

    # Set a random BPM
    def setRandomBPM(self):
        pass

    # Set a random instrument
    def setRandomInstrument(self, instruments):
        pass

    # Changes the instrument being played
    def changeInstrument(self, instrument):
        pass

    # Reset controller parameters to default
    def resetParameters(self):
        pass

# Class that implements MIDIControllerInterface
class MIDIController(MIDIControllerInterface):

    midi_manager: object            # MIDIFileManagerInterface object
    bpm: int = 90                   # Beats per minute of the sound
    default_bpm: int = 90           # Default beats per minute
    max_bpm: int = 250              # Max BPM permitted
    min_bpm: int = 90               # Min BPM permitted
    volume: int = 64                # Notes volume
    default_volume: int = 64        # Default notes volume
    max_volume: int = 127           # Max volume permitted
    last_note: int = 0              # Last note number
    note_duration: int = 1000       # Note duration in milliseconds
    global_timer: int = 0           # Global timer to synchronize the MIDI tracks
    octave: int = 4                 # Current note octave
    max_octave: int = 8             # Max octave permitted
    min_octave: int = 0             # Min octave permitted

    # Set midi manager attribute
    def setMIDIManager(self, midi_manager):
        self.midi_manager = midi_manager

    # Plays a note
    def playNote(self, note):
        note_to_play = note + (self.octave*12)
        self.midi_manager.setNoteOn(note_to_play, self.volume)
        self.midi_manager.setNoteOff(note_to_play, self.volume, self.note_duration)
        self.global_timer = self.global_timer + int(self.note_duration/(self.bpm/60))
        self.last_note = note

    # Plays a random note from the notes received
    def playRandomNote(self, notes):
        note_to_play = notes[random.randint(0,len(notes)-1)]
        self.playNote(note_to_play)

    # Repeat the last note played
    def repeatNote(self):
        self.playNote(self.last_note)

    # Changes from an octave to the next one
    def octaveUp(self):
        self.octave = self.octave + 1
        if self.octave > self.max_octave:
            self.octave = self.max_octave

    # Changes from an octave to the previous one
    def octaveDown(self):
        self.octave = self.octave - 1
        if self.octave < self.min_octave:
            self.octave = self.min_octave

    # Doubles the notes volume
    def doubleVolume(self):
        self.volume = self.volume * 2
        if self.volume > self.max_volume:
            self.volume = self.max_volume

    # Set the volume to default value
    def setVolumeToDefault(self):
        self.volume = self.default_volume

    # Keep the audio silent for a certain duration
    def silence(self):
        current_volume = self.volume
        self.volume = 0
        self.repeatNote()
        self.volume = current_volume

    # Increments the BPM by a given amount
    def incrementBPM(self, increment):
        self.bpm = self.bpm + increment
        if self.bpm > self.max_bpm:
            self.bpm = self.max_bpm
        self.changeTempo(self.bpm)

    # Set a random BPM between min_bpm and max_bpm
    def setRandomBPM(self):
        self.bpm = random.randint(self.min_bpm,self.max_bpm)
        self.changeTempo(self.bpm)

    # Set a random instrument from the instruments received
    def setRandomInstrument(self, instruments):
        instrument_to_set = int(instruments[random.randint(0,len(instruments)-1)])
        self.changeInstrument(instrument_to_set)

    # Changes the instrument being played
    def changeInstrument(self, instrument):
        self.midi_manager.changeInstrument(instrument, self.global_timer)

    # Changes the tempo of the music
    def changeTempo(self, bpm):
        self.midi_manager.changeTempo(bpm, self.global_timer)

    # Reset the timer that syncs the tracks
    def resetGlobalTimer(self):
        self.global_timer = 0

    # Reset the octave
    def resetOctave(self):
        self.octave = int(self.max_octave/2)

    # Reset controller parameters to default
    def resetParameters(self):
        self.resetGlobalTimer()
        self.resetOctave()
        self.changeTempo(self.default_bpm)
        self.bpm = self.default_bpm
        self.last_note = 0
        self.volume = self.default_volume
