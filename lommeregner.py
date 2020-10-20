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

print("Vælg en måde du vil renge på")



regne_måder = [{"name": "a+b", "func": lambda a,b : a+b},
               {"name": "a-b", "func": lambda a,b : a-b},
               {"name": "a*b", "func": lambda a,b : a*b},
               {"name": "a/b", "func": lambda a,b : a/b},
               {"name": "a**b", "func": lambda a, b : a**b},
               {"name": "sqrt(a)", "func": lambda a : math.sqrt(a)},
               {"name": "pi", "func": lambda : math.pi},
               {"name": "e", "func": lambda : math.e},
               {"name": "|a|", "func": lambda a : abs(a)},
               {"name": "!a", "func": lambda a : math.factorial(a)},
               {"name": "floor a", "func": lambda a : math.floor(a)},
               {"name": "ceil a", "func": lambda a : math.ceil(a)},
               {"name": "[CLEAR]", "func": lambda : os.system("CLEAR")},
]




for i in range(0, len(regne_måder)):
  print(str(i+1) + ". " +regne_måder[i]["name"])

choice = int(input())

func = regne_måder[choice-1]["func"]

numbers_of_args = len(getfullargspec(func).args)


if numbers_of_args == 2:
  print(func(float(input("a: ")), float(input("b: "))))
if numbers_of_args == 1:
  print(func(float(input("a: "))))
if numbers_of_args == 0:
  print(func())
