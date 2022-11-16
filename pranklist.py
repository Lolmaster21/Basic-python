import random

student = ['Ricardo','Jesse','Adrian','Jackie','Dominick','Simon','Dr. Mo','Chris','Kevin','Desautel']
location = ['Room110','the cafeteria','a dark hallway','the backrooms','the gender neutral bathroom']


def clue():
    derp = student[random.randrange(0,10)]
    prankster = student[random.randrange(0,10)]
    lol = location[random.randrange(0,5)]
    num = random.randrange(0,100)
    
    if num < 10:
        print(derp,"got hit with a water balloon in",lol, "by",prankster)
    elif num < 25:
        print(derp,"got pied in the face in",lol,"by",prankster)
    elif num < 45:
        print(derp,"got a chocolate chip cookie which was actually a oatmeal raisin in",lol,"by",prankster)
    elif num < 65:
        print(derp,"got their shoelaces tied together in",lol,"by",prankster)
    else:
        print(derp,"turned into a bunny with a transfiguration raygun in",lol, "by",prankster)

clue()
