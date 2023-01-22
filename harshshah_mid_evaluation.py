from tkinter import *
from tkinter import filedialog

root =Tk()
root.title("Word Clone app")



def open_text():
    text_file = filedialog.askopenfilename(initialdir="c:/python/", title="open Text File", filetypes=(("Text Files", "*.txt"), ))
    text_file =open(text_file, 'r')
    stuff =text_file.read()

    my_text.insert(END, stuff)
    text_file.close()

def save_txt():
    text_file = open('sample.txt', 'w')
    text_file.write(my_text.get(1.0, END))


my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
my_text.pack(pady=20)

open_button = Button(root, text="Open Text File", command=open_text)
open_button.pack(pady=5)

save_button =Button(root, text="Save File", command=save_txt)
save_button.pack(pady=5)




root.mainloop()