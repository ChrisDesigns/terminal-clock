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
    return returnClock(minutes, seconds)

def returnClock(firstUnit, secondUnit):
  minWithLead = "{:02d}".format(firstUnit)
  secWithLead = "{:02d}".format(secondUnit)

  leadingMin = formatASCII(int(minWithLead[0])).split('\n')
  followingMin = formatASCII(int(minWithLead[1])).split('\n')
  
  leadingSec = formatASCII(int(secWithLead[0])).split('\n')
  followingSec = formatASCII(int(secWithLead[1])).split('\n')

  seperator = [".", " ", "."]

  clockDisplay = r"""
        ___________________
     _.'-------------------'._
    |   ___________________   |
    |  /                   \  |
    |  |                   |  |
    |  |                   |  |
    |  \___________________/  |
    `-_______________________-'
         '_'            '_'      
    """ \
    .split('\n')

  clock = clockDisplay[4:7]

  for index in range(3):
    clockStr = clock[index]
    clockStr = clock[index] = clockStr[:9] + leadingMin[index] + clockStr[12:]
    clockStr = clock[index] = clockStr[:13] + followingMin[index] + clockStr[16:]
    clockStr = clock[index] = clockStr[:17] + seperator[index] + clockStr[18:]
    clockStr = clock[index] = clockStr[:19] + leadingSec[index] + clockStr[22:]
    clock[index] = clockStr[:23] + followingSec[index] + clockStr[26:]

  return '\n'.join(clockDisplay[:4] + clock + clockDisplay[7:])
    

def returnClearScreen():
    return "\033[2J\033[3J\033[H"