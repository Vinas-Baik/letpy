import datetime
import tkinter
import time
import random

COLORS = ('aquamarine3', 'brown1', 'DarkGoldenrod1', 'coral', 'khaki4', 'LawnGreen', 
          'medium turquoise', 'Red', 'Green', 'Yellow', 'Magenta')

WIDTH_WINDOWS = 400

# создаем окно
window = tkinter.Tk()

#  создать холст с размерами 400 на 400 пикселей.
canvas = tkinter.Canvas(window, width=WIDTH_WINDOWS, height=WIDTH_WINDOWS)
canvas.pack()

text_object = canvas.create_text(200, 200, text=datetime.datetime.now().strftime('%H:%M:%S'), 
                                 fill=random.choice(COLORS), font=('Arial', 60))

while True:

    canvas.itemconfig(text_object, text=datetime.datetime.now().strftime('%H:%M:%S'), 
                      fill=random.choice(COLORS), font=('Arial', random.randint(55, 75)))

    canvas.update()
    time.sleep(1)
    
window.mainloop()
