import pygame

# Class to play MIDI files
class MIDIPlayerInterface():

    file_path: str  # File path to reproduce
    volume: float   # Volume of the mixer

    # Set a file path to reproduce
    def setFilePath(self, file_path):
        pass

    # Starts the mixer
    def initMixer(self):
        pass

    # Set the volume of the player
    def setVolume(self, volume):
        pass

    # Plays the file
    def play(self):
        pass

    # Pauses the file playback
    def pause(self):
        pass

    # Unpauses the file playback
    def unpause(self):
        pass

    # Stops the file playback
    def stop(self):
        pass

    # Check if the player is paused
    def playerIsPaused(self):
        pass

# Class that implements MIDIPlayerInterface
class MIDIPlayer(MIDIPlayerInterface):

    file_path: str = "./output/output.mid" # File path to reproduce
    volume: float = 1                      # Volume of the mixer
    freq: int = 44100                      # Sound frequency
    bitsize: int = -16
    channels: int = 2
    buffer: int = 1024
    volume: float = 1

    # Set a file path to reproduce
    def setFilePath(self, file_path):
        self.file_path = file_path

    # Starts the mixer with the parameters
    def initMixer(self):
        pygame.mixer.init(self.freq, self.bitsize, self.channels, self.buffer)

    # Set the volume of the player
    def setVolume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)

    # Plays the file
    def play(self):
        pygame.mixer.music.load(self.file_path)
        pygame.mixer.music.play()

    # Pauses the file playback
    def pause(self):
        pygame.mixer.music.pause()

    # Unpauses the file playback
    def unpause(self):
        pygame.mixer.music.unpause()

    # Stops the file playback
    def stop(self):
        pygame.mixer.music.stop()

    # Check if the player is paused
    def playerIsPaused(self):
        return not pygame.mixer.music.get_busy()

midi_player = MIDIPlayer()
midi_player.initMixer()
midi_player.setVolume(1)
