from tkinter import *
import random

my_list = []
entry_list = []
count = 3
increment = 3


def quit_function():
    root.quit()


def forget():
    empty.pack_forget()
    empty2.pack_forget()
    true_text.pack_forget()
    entry.pack_forget()
    v.set("")
    button.pack_forget()


def loss_message():
    you_lost["bg"] = root["bg"]
    you_lost.pack()
    quit_button.pack()


def onclick():
    global count
    global increment
    entry_list.extend(entry.get())

    if increment == 3:
        a = 0
    else:
        a = increment-1

    while a < count:
        if len(entry_list) == count:
            if entry_list[a] == my_list[a]:
                a += 1
            else:
                forget()
                loss_message()
                return
        else:
            forget()
            loss_message()
            return

    increment += 1
    count += increment
    true_text.pack()
    lb.after(1000, advance)


def check():
    empty.pack()
    entry.pack()
    empty2.pack()
    button.pack()
    lb['text'] = ' '


def advance():
    global count
    global increment

    root['bg'] = str(random.choice(["red", "violet", "blue", "yellow", "purple", "orange", "turquoise", "green",
                                    "maroon", "cyan", "teal", "olive", "darksalmon", "plum", "aqua",
                                    "pink", "lime", "khaki", "gold", "peru", "crimson", "darkseagreen"]))
    lb['bg'] = root['bg']
    true_text['bg'] = root['bg']
    empty['bg'] = root['bg']
    empty2['bg'] = root['bg']

    lb.place(x=random.randint(1, 573), y=random.randint(1, 366))

    if len(my_list) < count:

        forget()
        lb['text'] = str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
        my_list.extend(lb['text'])

        print(my_list)
        lb.after(1000, advance)

    else:
        check()


root = Tk()
root.title("Game")
root.minsize(640, 480)
root.maxsize(640, 480)

lb = Label(root, text='\nAre You Ready?', font=("Courier", 75))
lb.after(2000, advance)
lb.pack(side='top')

empty = Label(root, font=("ComicSans", 30), text='\nEnter Your Answer!\n')
empty2 = Label(root, font=("Arial", 10), text='\n')

v = StringVar()
entry = Entry(root, font=("Calibri", 25), bd=10, textvariable=v)
button = Button(root, text="Check", command=onclick, font=("Arial", 10), bd=4)

quit_button = Button(root, text="Quit", command=quit_function, font=("Arial", 10), bd=4)

true_text = Label(root, text="Correct!", font=("Times new Roman", 100))
you_lost = Label(root, text="You Lost!", font=("Courier", 70))

root.mainloop()
