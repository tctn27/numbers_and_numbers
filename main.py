from tkinter import *
import random

root = Tk()
root.title("Numbers and Numbers")

target = random.randint(100, 999)

numbers = [random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
           random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
           random.choice([25, 50, 75, 100]), random.choice([25, 50, 75, 100])]
numbers.sort()

title = Label(root, text="Numbers and Numbers")
title.grid(row=0, column=0, columnspan=7)

target_label = Label(root, text="Target is " + str(target))
target_label.grid(row=1, column=0, columnspan=7)

output = ""


def submit():
    global output, target, root
    difference = abs(target - eval(output))
    results = Tk()
    results.title("Numbers and Numbers")

    if difference == 0:
        congratulations = Label(results, text="Nicely done!")
        congratulations.pack()
        score = Label(results, text="You got the target, " + str(target) + ", exactly!")
        score.pack()
    else:
        out = Label(results, text="Unlucky! You were " + str(difference) + " away from hitting that target\n"
                                                                           "Better luck next time!")
        out.pack()

    root.destroy()


def write(value):
    global output, out_label, button_0, button_1, button_2, button_3, button_4, button_5
    if value in [0, 1, 2, 3, 4, 5]:
        [button_0, button_1, button_2, button_3, button_4, button_5][value].config(state=DISABLED)
        value = numbers[value]
    output += str(value)
    try:
        out_label["text"] = "Current equation: \n" + str(output) + " = " + str(eval(output))
    except SyntaxError:
        out_label["text"] = "Current equation: \n" + str(output) + " = "


def clear():
    global output, out_label, button_0, button_1, button_2, button_3, button_4, button_5
    button_0.config(state="normal")
    button_1.config(state="normal")
    button_2.config(state="normal")
    button_3.config(state="normal")
    button_4.config(state="normal")
    button_5.config(state="normal")
    output = ""
    out_label["text"] = "Current equation: "


button_0 = Button(root, text=numbers[0], command=lambda: write(0))
button_0.grid(row=2, column=0)

button_1 = Button(root, text=numbers[1], command=lambda: write(1))
button_1.grid(row=2, column=1)

button_2 = Button(root, text=numbers[2], command=lambda: write(2))
button_2.grid(row=2, column=2)

button_3 = Button(root, text=numbers[3], command=lambda: write(3))
button_3.grid(row=2, column=3)

button_4 = Button(root, text=numbers[4], command=lambda: write(4))
button_4.grid(row=2, column=4)

button_5 = Button(root, text=numbers[5], command=lambda: write(5))
button_5.grid(row=2, column=5, columnspan=2)

#  end numbers, start operations

plus_button = Button(root, text="+", command=lambda: write("+"))
plus_button.grid(row=3, column=0)

minus_button = Button(root, text="-", command=lambda: write("-"))
minus_button.grid(row=3, column=1)

multiply_button = Button(root, text="*", command=lambda: write("*"))
multiply_button.grid(row=3, column=2)

divide_button = Button(root, text="/", command=lambda: write("/"))
divide_button.grid(row=3, column=3)

power_button = Button(root, text="^", command=lambda: write("^"))
power_button.grid(row=3, column=4)

open_brackets = Button(root, text="(", command=lambda: write("("))
open_brackets.grid(row=3, column=5)

closed_brackets = Button(root, text=")", command=lambda: write(")"))
closed_brackets.grid(row=3, column=6)

submit_button = Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=4)

clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=4, column=4, columnspan=3)

out_label = Label(root, text="Current equation: " + output)
out_label.grid(row=5, column=0, columnspan=7)

root.mainloop()
