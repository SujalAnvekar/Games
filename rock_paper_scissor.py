# Rock,Paper,Scissors

import random
user_score=0
comp_score=0

dict={
  "R":"Rock",
  "P":"Paper",
  "S":"Scissors"
}

while True:
  user=input("Enter (P/R/S) to play or Q  to quit:").upper()
  if user=="Q":
   break

  if user not in dict:
    print("Enter R/P/S")
    continue

  computer=random.choice(["R","S","P"])

  print(f"You choose {dict[user]}")
  print(f"Computer choose {dict[computer]}")
  if(user==computer):
    print("Draw")
  elif(user=="R" and computer=="S") or \
  (user=="P" and computer=="R") or \
  (user=="S" and computer=="P"):
    print("You win")
    user_score+=1
  else:
    print("you lose")
    comp_score+=1
    
  print(f"Your score:{user_score}")
  print(f"Computer score:{comp_score}")