import PySimpleGUI as gi
from MIDICreator import midi_creator
from MIDIPlayer import midi_player

# Defining UI theme
gi.theme('Black')

# Title text
title = [
    gi.Text("TextToMIDI", font=("System", 32))
]

# First column creation, containing text input and text file path
column1 = [
    [
        gi.Text("Text file:", font=("System", 12)),
        gi.In(size=(50, 1), enable_events=True, key="text_file_path", default_text="./input/text.txt"),
        gi.FileBrowse(file_types=(("Text Files", "*.txt"),))
    ],
    [
        gi.Button('Read file', button_color=('white', 'firebrick3'), key="read_file")
    ],
    [
        gi.Multiline(size=(70, 30), key='textbox')
    ]
]

# Second column creation, generate and reproduce MIDI files
column2 = [
    [
        gi.Text("Generate MIDI file", font=("System", 24)),
    ],
    [
        gi.Text("Folder to save file:", font=("System", 12)),
        gi.In(size=(50, 1), enable_events=True, key="midi_save_folder", default_text="./output"),
        gi.FolderBrowse()
    ],
    [
        gi.Text("File name:", font=("System", 12)),
        gi.In(size=(50, 1), enable_events=True, key="midi_save_file", default_text="output"),
    ],
    [
        gi.Button('Generate file', button_color=('white', 'firebrick3'), key="generate_file")
    ],
    [
        gi.HSeparator()
    ],
    [
        gi.Text("Reproduce MIDI file", font=("System", 24)),
    ],
    [
        gi.Text("Midi file:", font=("System", 12)),
        gi.In(size=(50, 1), enable_events=True, key="midi_read_file_path", default_text="./output/output"),
        gi.FileBrowse(file_types=(("Midi files", "*.mid"),))
    ],
    [
        gi.Button('Reproduce file', button_color=('white', 'firebrick3'), key="reproduce_file"),
        gi.Button('Pause reproduction', button_color=('white', 'firebrick3'), key="pause_file"),
        gi.Button('Stop reproduction', button_color=('white', 'firebrick3'), key="stop_file")
    ],
]

# Defining layout based on title and columns declared
layout = [
    [
        [
            [title],[gi.HSeparator()]
        ],
            gi.Column(column1, vertical_alignment = 't'),
            gi.VSeperator(),
            gi.Column(column2, vertical_alignment = 't')
    ]
]

# Starting window object
window = gi.Window("TextToMIDI", layout)

# Program loop
while True:
    event, values = window.read()
    # Checking read_file button event
    if event == "read_file":
        try:
            with open(values['text_file_path'], 'r', encoding="utf-8") as text_file:
                window['textbox'].update(value=values['textbox'] + text_file.read())
        except:
            gi.popup_ok("No file found")
    # Checking generate_file button event
    elif event == "generate_file":
        folder = values['midi_save_folder']
        filename = values['midi_save_file']
        text = values['textbox']
        if folder == "":
            gi.popup_ok("No folder specified")
        elif filename == "":
            gi.popup_ok("No filename specified")
        elif text == "":
            gi.popup_ok("No text has been given")
        else:
            if filename[-4:] != ".mid":
                filename = filename + ".mid"
            file_path = folder + "/" + filename
            try:
                midi_creator.generateMIDIFile(file_path, text)
            except:
                gi.popup_ok("Error: File didn't generate")
            else:
                gi.popup_ok("File generated successfully")
    # Checking reproduce file button event
    elif event == "reproduce_file":
        file_path = values['midi_read_file_path']
        if file_path == "":
            gi.popup_ok("No file found")
        else:
            if file_path[-4:] != ".mid":
                file_path = file_path + ".mid"
            midi_player.setFilePath(file_path)
            try:
                midi_player.play()
            except:
                gi.popup_ok("No file found")
    # Checking pause_file reproduction button event
    elif event == "pause_file":
        if midi_player.playerIsPaused():
            midi_player.unpause()
        else:
            midi_player.pause()
    # Checking stop_file reproduction button event
    elif event == "stop_file":
        midi_player.stop()
    # Exit program when closing window
    elif event == "OK" or event == gi.WIN_CLOSED:
        break

# Close window
window.close()
