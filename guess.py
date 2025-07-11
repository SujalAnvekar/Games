# guess game
import random
n=random.randint(1,100)
guesses=0
a=-1
while(a!=n):
   a=int(input("Guess a number between 1 to 100:"))
   guesses+=1

   if(a>n):
      print("Lower number please")
   elif a<n:
      print("Higher number please")

print(f"Your guess is correct in {guesses} attempts")