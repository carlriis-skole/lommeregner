import math
from inspect import getfullargspec
import os

print("""
  _                                                                   
 | |                                                                  
 | |     ___  _ __ ___  _ __ ___   ___ _ __ ___  __ _ _ __   ___ _ __ 
 | |    / _ \| '_ ` _ \| '_ ` _ \ / _ \ '__/ _ \/ _` | '_ \ / _ \ '__|
 | |___| (_) | | | | | | | | | | |  __/ | |  __/ (_| | | | |  __/ |   
 |______\___/|_| |_| |_|_| |_| |_|\___|_|  \___|\__, |_| |_|\___|_|   
                                                 __/ |                
                                                |___/                 
""")

print("vælg en måde du vil renge på")

regne_måder = [{"name": "a+b", "func": lambda a,b : a+b},
               {"name": "a-b", "func": lambda a,b : a-b},
               {"name": "a*b", "func": lambda a,b : a*b},
               {"name": "a/b", "func": lambda a,b : a/b},
               {"name": "a^b", "func": lambda a, b : a**b},
               {"name": "sqrt(a)", "func": lambda a : math.sqrt(a)},
               {"name": "pi", "func": lambda : math.pi},
               {"name": "e", "func": lambda : math.e},
               {"name": "|a|", "func": lambda a : abs(a)},
               {"name": "!a", "func": lambda a : math.factorial(a)},
               {"name": "floor a", "func": lambda a : math.floor(a)},
               {"name": "ceil a", "func": lambda a : math.ceil(a)},
               {"name": "[clear]", "func": lambda : os.system("clear")},
               {"name": "[stop]", "func": lambda : exit()},
]

while True:
  # Printer muligehederne som brugeren har 
  for i in range(0, len(regne_måder)):
    print(str(i+1) + ". " +regne_måder[i]["name"])

  # Finder ud af hvad brugeren valgte
  try:
    choice = int(input("Vælg en metode: "))
  except ValueError:
    print("Metoden du valgte kan ikke bruges")
    print("Skriv tallet ud fra det du vil")
    quit()

  # Finder navnet og regnefunktionen fra valget
  try:
    func = regne_måder[choice-1]["func"]
    name = regne_måder[choice-1]["name"]
  except IndexError:
    print("Det tal du valgte er ikke et valg")
    exit()

  # Finder mængden af argumenter regnefunktionen
  numbers_of_args = len(getfullargspec(func).args)

  # Laver argumenterne til rengerunktionen,
  # laver noget læsteligt tekst
  letters = ["a", "b", "c"]
  args = []
  for i in range(0, numbers_of_args):
    try:
      user_input = float(input(letters[i] + ": "))
    except ValueError:
      print("Please vælg et normalt input")
      exit()
    args.append(user_input)
    name = name.replace(letters[i], " " + str(user_input).replace(".0", "") + " ")

  # Printer resultatet
  print("\n" + name.strip(" ") + " = " + str(func(*args)).replace(".0", ""))

  # Spørg brugeren om personen vil fortsætte
  user_input = input("\nVil du fortsætte? ")
  if user_input == "nej":
    exit()
  elif user_input != "ja":
    print("hvad?")
    exit()