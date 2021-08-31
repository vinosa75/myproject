from tkinter import *

def frame_sentence():
    name = name_tf.get()
    age = int(age_tf.get())
    desc = descipline_tf.get()

    disp_tf.insert(0,f'{age} years old {name} became {desc}.')

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#0f4b6e')

name_tf = Entry(ws)
age_tf = Entry(ws)
descipline_tf = Entry(ws)

name_lbl = Label(
    ws,
    text='Name',
    bg='#0f4b6e',
    fg='white'
)
age_lbl = Label(
    ws,
    text='Age',
    bg='#0f4b6e',
    fg='white'
)

descipline_lbl = Label(
    ws,
    text='Descipline',
    bg='#0f4b6e',
    fg='white'
)

name_lbl.pack()
name_tf.pack()
age_lbl.pack()
age_tf.pack()
descipline_lbl.pack()
descipline_tf.pack()

btn = Button(
    ws,
    text='Frame Sentence',
    relief=SOLID,
    command=frame_sentence
)
btn.pack(pady=10)

disp_tf = Entry(
    ws, 
    width=38,
    font=('Arial', 14)
    )

disp_tf.pack(pady=5)


ws.mainloop()