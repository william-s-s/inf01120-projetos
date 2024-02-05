import pygame.midi
from midiutil import MIDIFile
import time

def device_info_to_string(device_info):
    device_info_string = [None] * 4
    device_info_string[0] = device_info[0].decode('utf-8')
    device_info_string[1] = device_info[1].decode('utf-8')
    if device_info[2] == 1:
        device_info_string[2] = 'Input'
    elif device_info[3] == 1:
        device_info_string[2] = 'Output'
    else:
        device_info_string[2] = 'Undefined'
    if device_info[4] == 1:
        device_info_string[3] = 'Open'
    else:
        device_info_string[3] = 'Closed'
    return device_info_string

def print_device_info(device_info_string):
    print('Device Interface: ' + device_info_string[0])
    print('Device Name: ' + device_info_string[1])
    print('Device Type: ' + device_info_string[2])
    print('Device Status: ' + device_info_string[3])

def get_device_info(id):
    return pygame.midi.get_device_info(id)

def get_default_audio_output_device():
    return pygame.midi.get_default_output_id()


pygame.midi.init()
default_audio_output_device = get_default_audio_output_device()
device_info = get_device_info(default_audio_output_device)
print_device_info(device_info_to_string(device_info))
player = pygame.midi.Output(default_audio_output_device)

midi_file = MIDIFile(1, file_format=1)
midi_file.addProgramChange(0, 0, 0, 0)
midi_file.addTempo(0, 0, 60)
midi_file.addTempo(0, 1, 120)
midi_file.addTempo(0, 3, 240)
midi_file.addNote(0, 0, 64, 0, 10, 127)
midi_file.addNote(0, 0, 65, 1, 1, 127)
midi_file.addNote(0, 0, 66, 2, 1, 127)
midi_file.addNote(0, 0, 67, 3, 1, 127)
midi_file.addNote(0, 0, 68, 4, 1, 127)
midi_file.addNote(0, 0, 69, 5, 1, 127)
with open("midi_test_file.mid", "wb") as output_file:
    midi_file.writeFile(output_file)

player.set_instrument(0)
# [[[INSTRUCTION,PARAMETER1,PARAMETER2],DELTATIME]]
player.write([[[144,64,127],pygame.midi.time()]])
player.write([[[145,69,127],pygame.midi.time()]])
time.sleep(0.5)
player.write([[[128,64,127],pygame.midi.time()]])
player.write([[[129,69,127],pygame.midi.time()]])
player.write([[[144,80,127],pygame.midi.time()]])
player.write([[[145,85,127],pygame.midi.time()]])
time.sleep(0.5)
player.write([[[128,80,127],pygame.midi.time()]])
player.write([[[129,85,127],pygame.midi.time()]])

del player
pygame.midi.quit()
