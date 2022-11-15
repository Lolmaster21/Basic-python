import random
candy = [0,0,0,0,0,0]

def halloween():
    numBars = random.randrange(1,5)
    num = random.randrange(1,100)
    
    if num < 15:
        print("You got",numBars, "butterfingers!")
        candy[0]+=numBars
    elif num < 35:
        print("You got" ,numBars, "hersheys")
        candy[1]+=numBars        
    elif num < 70:
        print("You got",numBars, "a pb cup!")
        candy[2]+=numBars
    elif num < 80:
        print("You got",numBars,  "M&M's")
        candy[3]+=numBars
    elif num < 98:
        print("You got",numBars, "sour patch kids")
        candy[4]+=numBars
    else:
        print("Rock for you")
        candy[5]+= 1
        
halloween()
halloween()
halloween()
halloween()
halloween()
print("Your candybag is now full of:", candy)
