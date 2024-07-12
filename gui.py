import PySimpleGUI as gu

label = gu.Text('My Test To DO App')
input_field = gu.InputText(tooltip="Enter your todo list")
button = gu.Button('Add', tooltip='Click to Add todo')

window = gu.Window('My Test To DO App',[[label,input_field,button]])
window.read()
window.close()
