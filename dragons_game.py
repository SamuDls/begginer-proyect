import random
import time


def showIntroduction():
   print("Estas en una cueva llena de dragones.")
   time.sleep(3)
   print("Frente a ti hay dos cuevas.")
   time.sleep(3)
   print("En una de ellas, el dragon es generoso y amigable, compartira su tesoro contigo.")
   time.sleep(3)
   print("El otro dragon el codicioso y hambriento, te devorara inmediatamente.")
   print()


def choiceCave():
   choice = ""
   while choice != "1" and choice != "2":
      print("¿A que cueva quieres entrar. (1 or 2)")
      choice = input()
   
   return choice

def exploringCave(choiceCave):
   print("Te aproximas a la cueva...")
   time.sleep(3)
   print("Es obscura y espeluznante...")
   time.sleep(3)
   print("¡Un gran dragon aparece súbitamente frente a tí! Abre sus fauces y...")
   time.sleep(3)
   print()
   
   friendlyCave = random.randint(1,2)

   if choiceCave == str(friendlyCave):
      print("Te regala un tesoro!")
   else:
      print("Te come de una bocado!")

playAgaing = input("Quieres jugar? (si o no)")

while playAgaing == "si":
   showIntroduction()

   cave = choiceCave()

   exploringCave(cave)

   print('¿Quieres jugar? (sí o no)')


   playAgaing = input()
   




