import random
x="Y"
while(x=='y'or x=='Y'):
    number = random.randint(1,6)
    if(number == 1):
        print("[-----------]")
        print("[           ]")
        print("[     o     ]")
        print("[           ]")
        print("[-----------]\n")
    if(number == 2):
        print("[-----------]")
        print("[     o     ]")
        print("[           ]")
        print("[     o     ]")
        print("[-----------]\n")
    if(number == 3):
        print("[-----------]")
        print("[     o     ]")
        print("[     o     ]")
        print("[     o     ]")
        print("[-----------]\n")
    if(number == 4):
        print("[-----------]")
        print("[  o     o  ]")
        print("[           ]")
        print("[  o     o  ]")
        print("[-----------]\n")
    if(number == 5):
        print("[-----------]")
        print("[  o     o  ]")
        print("[     o     ]")
        print("[  o     o  ]")
        print("[-----------]\n")
    if(number == 6):
        print("[-----------]")
        print("[  o     o  ]")
        print("[  o     o  ]")
        print("[  o     o  ]")
        print("[-----------]\n")
    x = input("Do you to Roll the Dice Again...[Y/N]...")
