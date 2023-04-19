import PySimpleGUI as sg
path = 'https://github.com/SultonovDilshod/DOTO-app.git'
label1 = sg.Text('Select files to compress')
input1 = sg.Input()
choose_button1 = sg.FilesBrowse('Choose')

label2 = sg.Text('Select destination folder')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose')

compress_btn = sg.Button("Compress")

window = sg.Window("File zipper",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_btn]])
window.read()
window.close()

