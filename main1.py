def giveWorkout(person):
  if (pesron.level < 4):
    person.uppper = 1
    person.lower = 1
    person.cardios = 3
  elif (4 <= person.level < 7):
    person.upper = 3
    person.lower = 3
    person.cardios = 4
   elif (person.level >= 7):
    person.upper = 10
    person.lower = 10
    person.cardios = 6
    
def readFile(path):
  with open(path, "rt") as f:
    return f.read()

def writeFile(path, contents):
  with open(path, "wt") as f:
    f.write(contents)
    
def cardioWorkout(person):
  
 
