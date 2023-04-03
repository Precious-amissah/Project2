import PySimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()

# Setting the properties of the voices
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[1])

# Create a theme
sg.theme('DarkAmber')

# Create a layout
layout = [
    [sg.Text('Enter text to speak')],
    [sg.InputText()],
    [sg.Button('Speak'), sg.Button('Exit')]
]

# Create a window
window = sg.Window('Text to Speech app', layout)

# Create an event
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Speak':
        text = values[0]
        engine.say(text)
        engine.runAndWait()

# Close and save resources
window.close()
engine.stop()