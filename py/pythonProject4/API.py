import bot
from tkinter import *
import csv


def enter():
    lableAnswer["text"] = bot.analiz(textCommand.get().lower())
    l = bot.list()
    lable2["text"] = bot.list_to_str(l)
    fillability = bot.fill()
    if fillability:
        lableAnswer['text'] += "\nВы согласны с результатом?"


def enter_two():
    fields = bot.list()
    with open('C:\\Users\\Данил\\Desktop\\123.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
       # with open('titanic_train.csv', 'a', newline='') as csvFile:
       #     write = csv.writer(csvFile, delimiter=',')
       #     write.writerow([9999, 0, param[2], 'Name', param[0], param[1], 'test', 'test', 'test', 'test', 'test', 'test'])



root = Tk()
root.title('Bot')
root.geometry('600x500')

textCommand = StringVar()
questionsEntry = Entry(textvariable=textCommand)
questionsEntry.place(x=50, y=80, width=400)

lable1 = Label(text="Введите параметры чтобы узнать цену")
lable1.place(x=50, y=50)

lable2 = Label(text="")
lable2.place(x=50, y=200)

lableAnswer = Label(text="")
lableAnswer.place(x=50, y=100)

button = Button(text="Отправить", command=enter)
button.place(x=450, y=80)

button2 = Button(text="сохранить", command=enter_two)
button2.place(x=450, y=180)

root.mainloop()
