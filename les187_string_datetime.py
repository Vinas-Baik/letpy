# Напишите программу, которая будет выводить текущее время на экран вот таким образом

# подключаем библиотеки 
import datetime
import tkinter
import time
import random

# константа цветов
COLORS = ('aquamarine3', 'brown1', 'DarkGoldenrod1', 'coral', 'khaki4', 'LawnGreen', 
          'medium turquoise', 'Red', 'Green', 'Yellow', 'Magenta')

# размер окна 
WIDTH_WINDOWS = 400

# создаем окно
window = tkinter.Tk()

#  создать холст с размерами 400 на 400 пикселей.
canvas = tkinter.Canvas(window, width=WIDTH_WINDOWS, height=WIDTH_WINDOWS)
canvas.pack()

# создаем текст в окне 
text_object = canvas.create_text(200, 200, text=datetime.datetime.now().strftime('%H:%M:%S'), 
                                 fill=random.choice(COLORS), font=('Arial', 60))

while True:
          # перерисоваваем текст со случайным цветом и размером от 55 до 75 символов 
    canvas.itemconfig(text_object, text=datetime.datetime.now().strftime('%H:%M:%S'), 
                      fill=random.choice(COLORS), font=('Arial', random.randint(55, 75)))

    canvas.update()
    time.sleep(1)
    
window.mainloop()
