from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import time
from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             DeeplTranslator)
from config import OPENAI_API_KEY, DEEPL_API_KEY

root = Tk()
root.geometry('1080x400')

root.resizable(0,0)
root.config(bg='black')

root.title('Redsetta Stone')

Label(root, text = 'Text Translator', font = 'arial 20 bold', bg = 'black').pack()

Label(root, text = 'Hendricks Technomancy', font = 'arial 15 bold', bg = 'black', width = '20').pack(side = 'bottom')

Label(root, text = 'Enter text here', font = 'arial 13 bold', bg = 'black').place(x=50,y=70)

Input_text = Text(root, font = 'arial 12', height = 11, wrap = WORD, padx = 5, pady = 5, width = 60)
Input_text.place(x=50,y=100)

Label(root, text = 'Translation', font = 'arial 13 bold', bg = 'black').place(x=590,y=70)

Output_text = Text(root, font = 'arial 12', height = 11, wrap = WORD, padx = 5, pady = 5, width = 60)
Output_text.place(x = 590, y = 100)

t_engine = ['Google Translator', 'ChatGpt Translator (3.5 Turbo)', 'ChatGpt Translator (4o)', 'DeepL Translator']

languages = [
    GoogleTranslator().get_supported_languages("as_dict"),
    ChatGptTranslator(api_key=OPENAI_API_KEY).get_supported_languages("as_dict"),
    ChatGptTranslator(api_key=OPENAI_API_KEY).get_supported_languages("as_dict"),
    DeeplTranslator(api_key=DEEPL_API_KEY).get_supported_languages("as_dict"),
    ]
translation_service = ttk.Combobox(root, value = t_engine, width = 22)
translation_service.place(x=425,y=30)
translation_service.set('Choose engine')

src_lang = ttk.Combobox(root, value = "Engine?", width = 22)
src_lang.place(x=260,y=65)
src_lang.set('Choose source language')

targ_lang = ttk.Combobox(root, value = "Engine?", width = 22)
targ_lang.place(x=800,y=65)
targ_lang.set('Choose target language')

def set_language(event):
    language = list(languages[int(translation_service.current())].keys())

    src_lang['value'] = ''
    targ_lang['value'] = ''

    src_lang['value'] = language
    targ_lang['value'] = language

translation_service.bind("<<ComboboxSelected>>", set_language)

def Translate():
    translator = [GoogleTranslator(),
                  ChatGptTranslator(api_key=OPENAI_API_KEY,model="gpt-3.5-turbo"),
                  ChatGptTranslator(api_key=OPENAI_API_KEY,model="gpt-4o"),
                  DeeplTranslator(api_key=DEEPL_API_KEY)]

    translator[int(translation_service.current())].source = languages[int(translation_service.current())][f"{src_lang.get()}"]
    translator[int(translation_service.current())].target = languages[int(translation_service.current())][f"{targ_lang.get()}"]

    translated = translator[int(translation_service.current())].translate(text = Input_text.get(1.0, END)).strip(' " ' )

    Output_text.delete(1.0, END)
    Output_text.insert(END, translated)

translate_button = Button(root, text = 'Translate', font = 'arial 12 bold', pady = 5, command = Translate, bg = 'red', activeforeground = 'red')
translate_button.place(x=490,y=320)

file_label = StringVar()
fl2 = Label(root, textvariable = file_label, fg = 'red')
fl2.place(x=100,y=340)
file_label.set('File name')

def open_file():
    file_path = askopenfile(mode = 'r', filetypes=[("Word files", "*.docx"),("Excel files", '*.xlsx')])
    if file_path is not None:
        file_label.set(file_path)
        pass

def upload_file():
    pb1 = ttk.Progressbar(root, length  = 300, mode = 'determinate')
    pb1.place(x=100,y=280)
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt'),
             ("Word files", "*.docx"),
             ("Excel files", '*.xlsx')]
    file = filedialog.asksaveasfile(initialdir = '/Users/nephthys/Technomancy/Ouroboros/Rosetta_Stone/to_be_translated', filetypes = files, defaultextension = files)
    pb1.destroy()
    Label(root, text = 'File uploaded successfully!', foreground = 'green').grid(row = 4, columnspan = 3, pady = 10)

adhar = Label(root, text = 'Upload file to be translated')
adhar.place(x=100,y=280)

adharbtn = Button(root, text = 'Browse files', command = lambda:open_file())
adharbtn.place(x=100,y=310)

upld = Button(root, text = 'Upload file', command = upload_file)
upld.place(x=100,y=360)

root.mainloop()
