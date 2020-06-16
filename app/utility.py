# give a number 
# return the boolean value for each of nine position
# side note, the 1st / 3rd bits are useless and will always be 0
def returnDisplay(number):
    boolArangement = {
        1: [0,0,0,
            0,0,1,
            0,0,1],
        2: [0,1,0,
            0,1,1,
            1,1,0],
        3: [0,1,0,
            0,1,1,
            0,1,1],
        4: [0,0,0,
            1,1,1,
            0,0,1],
        5: [0,1,0,
            1,1,0,
            0,1,1],
        6: [0,1,0,
            1,1,0,
            1,1,1],
        7: [0,1,0,
            0,0,1,
            0,0,1],
        8: [0,1,0,
            1,1,1,
            1,1,1],
        9: [0,1,0,
            1,1,1,
            0,1,1],
        0: [0,1,0,
            1,0,1,
            1,1,1]
    }
    return boolArangement.get(number,[0,0,0,
                                      0,0,0,
                                      0,0,0])

# Creates the ASCII version number of the number
def formatASCII(number):
  boolArray = returnDisplay(number)
  answer = ""
  for i, value in enumerate(boolArray):
    # if true
    if (value == 1):
      # the center row
      if (i % 3 == 1):
        answer += "_"
      # the right or left
      elif (i % 3 == 0 or i % 3 == 2):
        answer += "|"
    else:
      answer += " "
    # at the end of the row add a newline
    if (i % 3 == 2):
      answer += '\n'
  return answer

def convertTimeFormat(delta):
    total_time = delta.total_seconds()
    minutes = int((total_time % 3600) // 60)
    seconds = int((total_time % 3600) % 60 // 1)
    return returnClock(str(minutes), str(seconds))

# calculates and create the offset space needed
def createSpace(arrayStr):
    taken_space = len(arrayStr)
    offset = 8
    spaceNeeded = offset - (taken_space - 1)
    return " " * spaceNeeded

def returnClock(firstUnit, secondUnit):
    return r"""
        ___________________
     _.'-------------------'._
    |   ___________________   |
    |  /                   \  |
    |  |        m:s        |  |
    |  |                   |  |
    |  \___________________/  |
    `-_______________________-'
         '_'            '_'      
    """ \
    .replace("        m", createSpace(firstUnit) + firstUnit) \
    .replace("s        ", secondUnit + createSpace(secondUnit))
    

def returnClearScreen():
    return "\033[2J\033[3J\033[H"