#hangman
import collections 
def notwon():
  if collections.Counter(alist) == collections.Counter(newlist):
    return False
  else:
    return True

# # checking for humam error ---  still working on it 
def checkinput(x):
  # if its number 
  if (len(x) == 1):
    return x

# store the answer in a list 
alist = []
word = "TEE"
for x in word:
  alist.append(x)
print(alist) #testing 

# creating a empty list with _ with same lenth   
newlist = []
for i in range(0,(len(word))):
  newlist.append("_")
print(newlist) #testing 

counter = 0
while (counter < 5 and notwon()):
  print()
  guess = input("Enter a letter: ")
# use checkinput function here 
  guess = guess.upper()
  success = 0
  for x in range(0, len(word)):
    if word[x] == guess:
      newlist[x] = guess
      #print(newlist) #testing 
      success += 1


    
  if success >= 1:
    for i in newlist:
      print(i, end =" ",)
    print("  :)  way to go")
  else:
    counter += 1
    print(f"Oh NO, you have {5-counter} more tries left")
      
if notwon() == False:
  print()
  print("You Won :)")
elif counter == 5:
  print("You lost ;(")