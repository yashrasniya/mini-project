from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *


def Decryption(key):
    key = check(key)
    if key == 'error':
        return
    path = str(askopenfile()).split("'")[1]
    print('The path of file : ', path)
    print('Key for Decryption : ', key)
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)

    for index, values in enumerate(image):
        image[index] = values ^ key

    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    showinfo('Done', 'Decryption Done...')
    print('Decryption Done...')


def Encryption(key):
    key = check(key)
    if key == 'error':
        return
    path = str(askopenfile()).split("'")[1]
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)

    for index, values in enumerate(image):
        image[index] = values ^ key

    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    with open('keys.txt', 'a') as w:
        w.write(f'path {path} Key {key}\n')

    showinfo('Done', f'File get Saved at {path} with key: {key}')


def check(d):
    try:
        d = int(d.get())
    except ValueError:
        showerror('error', 'KEY SHOULD BE INT')
        return 'error'
    if d > 255 or d < 0:
        showerror('error', 'KEY SHOULD BE IN RANGE OF 0~255')
        return 'error'
    return d


root = Tk()


root.geometry('400x200')
root.title('collage project')
rootFrame=Frame(root).pack()
L=Label(rootFrame,text="KEY")
L.pack(side=LEFT,anchor='nw',pady=10,padx=10)
E = Entry(rootFrame)
E.pack(side=LEFT,anchor='nw',pady=10,padx=10)
BE = Button(rootFrame, text='Encryption', command=lambda: Encryption(E))
BE.pack(side=LEFT,anchor='nw',pady=10,padx=10)
BD = Button(rootFrame, text='Decryption ', command=lambda: Decryption(E))
BD.pack(side=LEFT,anchor='nw',pady=10,padx=10)

root.mainloop()
