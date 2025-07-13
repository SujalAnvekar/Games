from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe")

x = True
flag = 0

def click(button):
    global x, flag
    if button["text"] == "" and x:
        button["text"] = 'X'
        x = False
        flag += 1
        winner()
    elif button["text"] == "" and not x:
        button["text"] = 'O'
        x = True
        flag += 1
        winner()
    else:
        messagebox.showinfo("Tic-Tac-Toe", "Already selected!")

def disable():
    for btn in all_buttons:
        btn.config(state=DISABLED)

def restart():
    global x, flag
    x = True
    flag = 0
    for btn in all_buttons:
        btn.config(state=NORMAL, text="")

def winner():
    possible_wins = [
        (btn1, btn2, btn3),
        (btn4, btn5, btn6),
        (btn7, btn8, btn9),
        (btn1, btn4, btn7),
        (btn2, btn5, btn8),
        (btn3, btn6, btn9),
        (btn1, btn5, btn9),
        (btn3, btn5, btn7)
    ]

    for combo in possible_wins:
        if combo[0]["text"] == combo[1]["text"] == combo[2]["text"] != "":
            winner = combo[0]["text"]
            messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            disable()
            return

    if flag == 9:
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        disable()

all_buttons = []

# Creating game buttons
btn1 = Button(root, text="", font=("Arial", 50), fg="White", bg="Yellow", width=3, command=lambda: click(btn1))
btn1.grid(row=0, column=0)
all_buttons.append(btn1)

btn2 = Button(root, text="", font=("Arial", 50), fg="White", bg="Yellow", width=3, command=lambda: click(btn2))
btn2.grid(row=0, column=1)
all_buttons.append(btn2)

btn3 = Button(root, text="", font=("Arial", 50), fg="White", bg="Yellow", width=3, command=lambda: click(btn3))
btn3.grid(row=0, column=2)
all_buttons.append(btn3)

btn4 = Button(root, text="", font=("Arial", 50), fg="White", bg="Yellow", width=3, command=lambda: click(btn4))
btn4.grid(row=1, column=0)
all_buttons.append(btn4)

btn5 = Button(root, text="", font=("Arial", 50), fg="White", bg="Yellow", width=3, command=lambda: click(btn5))
btn5.grid(row=1, column=1)
all_buttons.append(btn5)

btn6 = Button(root, text="", font=("Arial", 50), fg="White", bg="Yellow", width=3, command=lambda: click(btn6))
btn6.grid(row=1, column=2)
all_buttons.append(btn6)

btn7 = Button(root, text="", font=("Arial", 50), fg="White", bg="Yellow", width=3, command=lambda: click(btn7))
btn7.grid(row=2, column=0)
all_buttons.append(btn7)

btn8 = Button(root, text="", font=("Arial", 50), fg="White", bg="Yellow", width=3, command=lambda: click(btn8))
btn8.grid(row=2, column=1)
all_buttons.append(btn8)

btn9 = Button(root, text="", font=("Arial", 50), fg="White", bg="Yellow", width=3, command=lambda: click(btn9))
btn9.grid(row=2, column=2)
all_buttons.append(btn9)

btn10 = Button(root, text="Restart", font=("Arial", 20, "bold"), bg="Gray", fg="White", command=restart)
btn10.grid(row=3, column=1)

root.mainloop()
