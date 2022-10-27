print("How many cookies you got?")
a=int(input())

if a<3:
        print("Go on a cookie run you don't have enough")
elif a<10:
        print("The perfect cookie number")
else:
    print("You have to much cookies. Gimme one pls")

#------------------------------------------------------------------------------

print("jedi or sith?\n")

choice = input()

if choice == 'jedi':
    print("You get green light saviar")
elif choice == 'sith':
    print("You get a red light saviar")
else:
    print("That's not an option *Hits you with breadstick*")
    
#------------------------------------------------------------------------------
for i in range(4,42,2):
    print(i)
    
#------------------------------------------------------------------------------
print("new loop\n")
t= 100
while t>= 50:
  print (t)
  t-=10
#------------------------------------------------------------------------------
words = input
while words != "orange":
    words = input("Knock knock, who's goes there?? BANANANNANANNANNANNANANNAN... (Type orange to quit)\n")
#------------------------------------------------------------------------------
def multiply(x,y,z):
  number = (x*y*z);
  return number;

print("Gimme 3 numbers")
x = int (input())
y = int (input())
z = int (input())
 
print("The final result is", x*y*z)

#------------------------------------------------------------------------------

def bottle(x1): 
    for y in range(x1,0,-1):
        print(y,"ON TEH WALL")
print("Give number now")        
x1 = int(input())
bottle (x1)



