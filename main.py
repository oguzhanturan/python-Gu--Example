import tkinter
import docx
import sqlite3
from tkinter import *

window = tkinter.Tk()
window.title("Python Modules Helper")
# label = tkinter.Label(window, text="Python Modules Helper").grid(row=0, column=0)
window.geometry('800x550+400+100')

labelModuleList = tkinter.Label(window, text="Python Module List").grid(row=0, column=0, pady=10)
lb_moduleList = tkinter.Listbox(window, exportselection=0)
lb_moduleList.config(width=30, height=15)
lb_moduleList.grid(row=1, column=0, padx=10)
lb_moduleList.event_generate("<<ListboxSelect>>")
lb_moduleList.bind("<<ListboxSelect>>", lambda x: getSelectedItemFromModules())

moduleList = ["abc",
              "aifc",
              "argparse",
              "array",
              "ast",
              "asynchat",
              "asyncio",
              "asyncore",
              "atexit",
              "audioop",
              "base64",
              "bdb",
              "binascii"]

## Yapı => funcList = {
#   "ModulAdı" : {
#       1:"Fonksiyon1 Adı",
#       2:"Fonksiyon2 Adı"
#   }
#   "ModulAdı" : {
#       1:"Fonksiyon1 Adı",
#       2:"Fonksiyon2 Adı"
#   }
# }

funcList = {
    "abc": {
        1: "abctest1",
        2: "abctest2"
    },
    "aifc": {
        1: "aifctest1",
        2: "aifctest2"
    },
    "argparse": {
        1: "argparsetest1",
        2: "argparsetest2"
    },
    "array": {
        1: "arraytest1",
        2: "arraytest2"
    },
    "ast": {
        1: "asttest1",
        2: "asttest2"
    }
}

print(funcList['abc'])
for i in range(len(moduleList)):
    lb_moduleList.insert(i, moduleList[i])
#
# lb_moduleList.insert(2, "aifc")


labelFuncList = tkinter.Label(window, text="Python Function List").grid(row=0, column=1, pady=10)
lb_fncList = tkinter.Listbox(window, exportselection=0)
lb_fncList.config(width=30, height=15)
lb_fncList.grid(row=1, column=1)
lb_fncList.event_generate("<<ListboxSelect>>")
lb_fncList.bind("<<ListboxSelect>>", lambda x: getSelectedItemFromFunctions())

tb_engList = tkinter.Label(window, text="İngilizce Açıklama", borderwidth=2, relief="groove")
tb_engList.config(width=25, height=15)
tb_engList.grid(row=1, column=2)

tb_trkList = tkinter.Label(window, text="Türkçe Açıklama", borderwidth=2, relief="groove")
tb_trkList.config(width=25, height=15)
tb_trkList.grid(row=1, column=3, padx=5, pady=20)

tb_exCode = tkinter.Label(window, text="Örnek", borderwidth=2, relief="groove")
tb_exCode.config(width=25, height=15)
tb_exCode.grid(row=2, column=1, padx=10)

tb_exScreen = tkinter.Label(window, text="Ekran Çıktısı", borderwidth=2, relief="groove")
tb_exScreen.config(width=25, height=15)
tb_exScreen.grid(row=2, column=2, padx=10)

button = tkinter.Button(window, text="Çıkış",command=quit)
button.grid(row=2, column=3)

tb_test = tkinter.Label(window, text="", borderwidth=2, relief="groove")
tb_test.grid(row=2, column=0, padx=10)


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.insert(0, str(para.text))

    return '\n'.join(fullText)


def getSelectedItemFromModules():
    # Listbox doldurur.
    lbSelected = lb_moduleList.curselection()[0]
    tb_test['text'] = lb_moduleList.get(lbSelected)
    lb_fncList.delete('0', 'end')
    for a in funcList[lb_moduleList.get(lbSelected)]:
        lb_fncList.insert(a, funcList[lb_moduleList.get(lbSelected)][a])


def getSelectedItemFromFunctions():
    lb2Selected = lb_fncList.curselection()[0]
    print(lb_fncList.get(lb2Selected))
    # data/fonkAdı/fonkAdı.docx
    docEng = getText("data/" + lb_fncList.get(lb2Selected) + "/" + lb_fncList.get(lb2Selected) + "-Eng.docx")
    docTr = getText("data/" + lb_fncList.get(lb2Selected) + "/" + lb_fncList.get(lb2Selected) + "-Tr.docx")
    docExample = getText("data/" + lb_fncList.get(lb2Selected) + "/" + lb_fncList.get(lb2Selected) + "-kod.docx")
    docScreen = getText("data/" + lb_fncList.get(lb2Selected) + "/" + lb_fncList.get(lb2Selected) + "-ekran.docx")

    tb_engList['text'] = docEng
    tb_trkList['text'] = docTr
    tb_exCode['text'] = docExample
    tb_exScreen['text'] = docScreen


window.mainloop()
