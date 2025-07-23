from tkinter import *
from PIL import Image,ImageTk
import random
from tkinter import messagebox

root=Tk()
root.geometry("800x800")
root.title("Rock-Paper-Scissor")

user_score=0
comp_score=0
draw=0

def click(user):
    global user_score,comp_score,draw
    choice=["rock","paper","scissor"]
    comp_choice=random.choice(choice)
    
    print(f"Userchoose {user}")
    print(f"computer {comp_choice}")

    if comp_choice==user:
        draw+=1
        messagebox.showinfo('message',"Its a Draw")


    elif comp_choice=="rock" and user=="paper" or \
    comp_choice=="paper" and user=="scissor" or \
    comp_choice=="scissor" and user=="rock":
        user_score+=1
        messagebox.showinfo("Message","User Win")


    else:
        comp_score+=1
        messagebox.showinfo("Message","Computer Wins")

    l1.config(text=f"User score:{user_score}")
    l2.config(text=f"Computer score:{comp_score}")
    l3.config(text=f"Draw:{draw}")


options=[("rock.png","rock"),("paper.png","paper"),("scissors.png","scissor")]
photos=[]

frame=Frame(root,bg="lightblue")
frame.pack(pady=100)

for img,name in options:
    image=Image.open(img)
    image=image.resize((200,200))
    photo=ImageTk.PhotoImage(image)
    photos.append(photo)

    label=Label(frame,image=photo)
    label.pack(side="left")
    label.bind("<Button>",lambda event,x=name:click(x))

l1=Label(root,text="Your score:0",font=("Lucida"))
l1.pack()

l2=Label(root,text="Computer score:0",font=("Lucida"))
l2.pack()

l3=Label(root,text="Draw:0",font=("Lucida"))
l3.pack()

root.mainloop()