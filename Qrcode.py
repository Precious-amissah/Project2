import PySimpleGUI as sg
import qrcode
from tkinter import Tk, colorchooser

# Define the window layout
layout = [
    [sg.Text('Enter text to generate QR Code:')],
    [sg.InputText(key='-INPUT-')],
    [sg.Button('Choose color', key='-CHOOSE_COLOR-'),
     sg.Text('Color', key='-COLOR_TEXT-')],
    [sg.Slider(range=(100, 500), default_value=200, orientation='h', size=(20, 15), key='-SIZE_SLIDER-')],
    [sg.Text('QR Code Size', size=(15, 1)), sg.Text('200', key='-SIZE_DISPLAY-', size=(5, 1))],
    [sg.Button('Create', key='-CREATE_BUTTON-')],
    [sg.Image(key='-QR_CODE-')]
]

# Create the window
window = sg.Window('QR Code Generator', layout)

# Event loop to process events and get user input
while True:
    event, values = window.read()

    # If user closes window or clicks the Cancel button, exit the loop
    if event == sg.WIN_CLOSED:
        break

    # Handle event when user clicks the Choose color button
    if event == '-CHOOSE_COLOR-':
        # Get the current selected color
        color = colorchooser.askcolor()[0]
        # Update the color display in the window
        window['-COLOR_TEXT-'].update(f'Color: {color}')



    # Handle event when user clicks the Create button
    if event == '-CREATE_BUTTON-':
        # Get the text input from the user
        text = values['-INPUT-']

        # Check if user input is empty
        if not text:
            sg.popup('Please enter text to generate QR Code.')
            continue


        # Get the size value from the user
        size = int(values['-SIZE_SLIDER-'])

        # Generate the QR code image
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color=color, back_color='white').resize((size, size))
        filename = 'qrcode.png'
        img.save(filename)

        # Update the QR code image in the window
        window['-QR_CODE-'].update(filename=filename)

        # Update the size display in the window
        window['-SIZE_DISPLAY-'].update(size)

# Close the window
window.close()
