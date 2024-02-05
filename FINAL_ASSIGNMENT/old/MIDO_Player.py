import mido
import time
import math

def sleep_milliseconds(milliseconds):
    return time.sleep(milliseconds/1000)

# Open Windows device to synthesize the MIDI output
midi_output = mido.open_output(mido.get_output_names()[0])

# Open a file to store the MIDI output
midi_file = mido.MidiFile()
tempo_track = mido.MidiTrack()
audio_track = mido.MidiTrack()
midi_file.tracks.append(tempo_track)
midi_file.tracks.append(audio_track)

# Calculates two different tempos for the music using the BPM
bpm_1 = 60
bpm_2 = 120
tempo_1 = math.ceil(mido.bpm2tempo(bpm_1)/2)
tempo_2 = math.ceil(mido.bpm2tempo(bpm_2)/2)

# Set fixed duration for each note
milliseconds = math.ceil((bpm_1/60)*1000)

# Plays the note in Windows device
midi_output.send(mido.Message('note_on', channel=0, note=64, velocity=64, time=0))
sleep_milliseconds(milliseconds)
midi_output.send(mido.Message('note_off', channel=0, note=64, velocity=64, time=0))
midi_output.send(mido.Message('note_on', channel=0, note=64, velocity=64, time=0))
sleep_milliseconds(milliseconds)
midi_output.send(mido.Message('note_off', channel=0, note=64, velocity=64, time=0))
midi_output.send(mido.Message('note_on', channel=0, note=64, velocity=64, time=0))
sleep_milliseconds(milliseconds/(bpm_2/bpm_1))
midi_output.send(mido.Message('note_off', channel=0, note=64, velocity=64, time=0))
midi_output.send(mido.Message('note_on', channel=0, note=64, velocity=64, time=0))
sleep_milliseconds(milliseconds/(bpm_2/bpm_1))
midi_output.send(mido.Message('note_off', channel=0, note=64, velocity=64, time=0))
midi_output.send(mido.Message('note_on', channel=0, note=64, velocity=64, time=0))
sleep_milliseconds(milliseconds/(bpm_2/bpm_1))
midi_output.send(mido.Message('note_off', channel=0, note=64, velocity=64, time=0))

# Stores the note in a track of the MIDI file
tempo_track.append(mido.MetaMessage('set_tempo', tempo=tempo_1, time=0))
tempo_track.append(mido.MetaMessage('set_tempo', tempo=tempo_2, time=milliseconds*2))
audio_track.append(mido.Message('note_on', note=64, velocity=64, time=0))
audio_track.append(mido.Message('note_off', note=64, velocity=64, time=milliseconds))
audio_track.append(mido.Message('note_on', note=64, velocity=64, time=0))
audio_track.append(mido.Message('note_off', note=64, velocity=64, time=milliseconds))
audio_track.append(mido.Message('note_on', note=64, velocity=64, time=0))
audio_track.append(mido.Message('note_off', note=64, velocity=64, time=milliseconds))
audio_track.append(mido.Message('note_on', note=64, velocity=64, time=0))
audio_track.append(mido.Message('note_off', note=64, velocity=64, time=milliseconds))
audio_track.append(mido.Message('note_on', note=64, velocity=64, time=0))
audio_track.append(mido.Message('note_off', note=64, velocity=64, time=milliseconds))

# Saves MIDI file
midi_file.save('song.mid')
