#hangman
import collections 
def notwon():
  if collections.Counter(list) == collections.Counter(newlist):
    return False
  else:
    return True

# # checking for humam error ---  still working on it 
def checkinput(x):
  # checking for humam error
  # if number 
  if (len(x) == 1):
    return x

# store the answer in a list 
list = []
word = "TESLA"
for x in word:
  list.append(x)
#print(list) #testing 

# creating a empty list with _ with same lenth   
newlist = []
for i in range(0,(len(word))):
  newlist.append("_")
#print(newlist) #testing 

counter = 0
while (counter < 5 and notwon()):
  print()
  guess = input("Enter a letter: ")
  
  guess = guess.upper()
  success = 0
  for x in word:
     
    if x == guess :
      newlist[list.index(x)] = guess
      #print(newlist) #testing 
      success += 1

      for i in newlist:
        print(i, end =" ",)
    
  if success >= 1:
    print("Yes, way to go")
  else:
    counter += 1
    print(f"Oh NO, you have {5-counter} more try left")
      
if notwon() == False:
  print()
  print("You Won :)")
elif counter == 5:
  print("You lost ;(")