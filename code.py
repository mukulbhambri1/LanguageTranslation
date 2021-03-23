from tkinter import *
root = Tk()
root.title("Language Translation to English")
e=Entry(root,width=100)
e.pack()
e.insert(0,"Enter your text to be translated")
def myClick():
    from google_trans_new import google_translator  
    translator = google_translator()
    hello = e.get()
    translate_text = translator.translate(hello,lang_tgt='en')
    myLabel=Label(root,text=translate_text)
    
    myLabel.pack()
myButton=Button(root,text="Submit",command=myClick)
myButton.pack()
root.mainloop()
