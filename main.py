"""
  A    SSS  K   K IIIII IIIII
 A A  S   S K  K    I     I
A   A S     K K     I     I
AAAAA  SSS  KK      I     I
A   A     S K K     I     I
A   A S   S K  K    I     I
A   A  SSS  K   K IIIII IIIII
            By: SeagullisLearningToCode
"""
from data.frw.GF import *


class askii(object):
    def __init__(self, string, **opt):
        # kwargs
        self.printASCIIList = opt.get("printASCIIList", False)  # ;Prints after ascii art is rendered with the width and height
        self.checkIfYValueReachedASCIIList = opt.get("check", False)  # ;Checks if the y value has reached the length of the Ascii list
        self.getLength = opt.get("getlength", False)  # ;Gets the length of ASCII
        self.amountOfSpacing = opt.get("spacing", 2)  # ;adds additional spacing when input contains " "
        self.reduceSpacing = opt.get("reduceSpacing", True)  # ;Gets rid of any unnecessary spacing for special characters, by default this is set to true
        self.customMode = opt.get("turnCustomModeOn", False)  # ;Enables a Custom limits (OVERRIDES OG LIMITS), *ADVANCED USERS ONLY DUE TO HAVING NO CODE THAT WILL CLEVERLY INCREASE THE LETTER'S FONT SIZE*
        # int
        x = 0  # ; X-Axis
        y = 0  # ; Y-Axis
        # str
        returnString = ""  # ;Var used to print final result
        # lists
        ascii = []  # ;Mapping
        # code
        if self.customMode is True:
            self.customMode_overrideCLimitX = opt.get("x", 0)  # decrease or increase the x-axis limit
            self.customMode_overrideCLimitY = opt.get("y", 0)  # decrease or increase the y-axis limit
            self.customMode_overrideTILimit = opt.get("totalIterLimit", 0)  # decrease or increase the total limit
            self.customMode_generateIterListAmount = opt.get("genIterListAmnt", 0)  # make a iteration list if needed
            if self.customMode_overrideCLimitX > 0 or self.customMode_overrideCLimitY > 0 or self.customMode_overrideTILimit > round(45 / 2):
                coordLimitsX = self.customMode_overrideCLimitX  # ;X-Axis iter limit
                coordLimitsY = self.customMode_overrideCLimitY  # ;Y-Axis iter limit
                limit = self.customMode_overrideTILimit  # ;Total iter Limit
            else:
                coordLimitsX = 5  # ;X-Axis iter limit
                coordLimitsY = 7  # ;Y-Axis iter limit
                limit = 45  # ;Total iter Limit
            if self.customMode_generateIterListAmount > 0:
                iterList = []
                for x in range(self.customMode_generateIterListAmount):
                    iterList.append(0)
        else:
            coordLimitsX = 5  # ;X-Axis iter limit
            coordLimitsY = 7  # ;Y-Axis iter limit
            limit = 45  # ;Total iter Limit

        for asciiList in range(coordLimitsY):  # ;Make nested list
            ascii.append([])

        if self.getLength is True:
            p(len(ascii))

        def addSpace():
            if x == coordLimitsX:
                if not y >= coordLimitsY:
                    ascii[y].append(" ")

        for char in string:  # ;Loop through each character in 'string'
            # ;After it checks which character it is the values that have been added will reset to zero,
            # ;or in simplier terms these shouldn't be changed
            # ;||
            # ;\/
            x = 0
            y = 0
            z = 0  # ;for automated stuffs (mainly used in the arms of the letter K)
            s = 0  # ;Same as z
            if self.reduceSpacing is True:
                coordLimitsX = 5  # X-Axis iter limit

            if char.islower():  # ;Check if the character in initials is a lower character if so that lowercase character becomes an uppercase character
                char = char.upper()

            # ;ALPHA----------------------------------------------------------------
            if char == "s".upper():
                for char_s in range(limit):
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0 or y == 3 or y == coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        elif x > 0:
                            if not x > 4:
                                ascii[y].append("S")
                    elif y == 1 or y == 6:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("S")
                        else:
                            ascii[y].append(" ")
                    elif y == 2:
                        if x == 1:
                            ascii[y].append("S")
                        else:
                            ascii[y].append(" ")
                    elif y == 4:
                        if x < coordLimitsX:
                            ascii[y].append(" ")
                        elif x >= coordLimitsX:
                            ascii[y].append("S")
                    elif y == 5:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("S")
                        else:
                            ascii[y].append(" ")
                    elif y == 6:
                        if x == 1 or x == 4:
                            ascii[y].append(" ")
                        if x > 0:
                            if not x > 3:
                                ascii[y].append("S")
                    addSpace()
                    x += 1

            elif char == "l".upper():
                for char_l in range(limit):
                    if x == coordLimitsX:
                        if not y >= coordLimitsY:
                            ascii[y].append(" ")
                    if x >= coordLimitsX:
                        y += 1
                        x = 0
                    if not y >= coordLimitsY - 1:
                        if x == 0:
                            ascii[y].append("L")
                        else:
                            ascii[y].append(" ")
                    elif y == coordLimitsY - 1:
                        ascii[y].append("L")
                    addSpace()
                    x += 1

            elif char == "c".upper():
                for char_c in range(limit):
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0 or y == 6:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        elif x > 1:
                            ascii[y].append("C")
                    elif y == 1 or y == 5:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("C")
                        else:
                            ascii[y].append(" ")
                    elif y < 5:
                        if x == 1:
                            ascii[y].append("C")
                        else:
                            ascii[y].append(" ")
                    addSpace()
                    x += 1

            elif char == "a".upper():
                for char_a in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0:
                        if x == 3:
                            ascii[y].append("A")
                        else:
                            ascii[y].append(" ")
                    elif y == 1:
                        if x == 2 or x == 4:
                            ascii[y].append("A")
                        else:
                            ascii[y].append(" ")
                    elif y == 2 or y >= 4 and not y == coordLimitsY:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("A")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        ascii[y].append("A")
                    addSpace()

            elif char == "b".upper():
                for char_b in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0 or y == 3 or y == coordLimitsY - 1:
                        if x < coordLimitsX:
                            ascii[y].append("B")
                        else:
                            ascii[y].append(" ")
                    elif 0 <= y < 3 or y < coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("B")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "d".upper():
                for char_d in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0 or y == coordLimitsY - 1:
                        if x < coordLimitsX:
                            ascii[y].append("D")
                        else:
                            ascii[y].append(" ")
                    elif y != 0 and y < coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("D")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "e".upper():
                for char_e in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0 or y == coordLimitsY - 1:
                        ascii[y].append("E")
                    elif 0 < y < 3 or 3 < y < coordLimitsY - 1:
                        if x == 1:
                            ascii[y].append("E")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        if x < 4:
                            ascii[y].append("E")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "f".upper():
                for char_f in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0:
                        ascii[y].append("F")
                    elif 0 < y < 3 or 3 < y < coordLimitsY:
                        if x == 1:
                            ascii[y].append("F")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        if x < 4:
                            ascii[y].append("F")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "g".upper():
                for char_g in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0 or 6 <= y <= coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        elif x > 1:
                            ascii[y].append("G")
                    elif y == 1 or coordLimitsY > y > 3:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("G")
                        else:
                            ascii[y].append(" ")
                    elif y == 2:
                        if x == 1:
                            ascii[y].append("G")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        ascii[y].append("G")
                    addSpace()

            elif char == "h".upper():
                for char_h in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 3:
                        ascii[y].append("H")
                    elif y != 3 and y < coordLimitsY:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("H")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "i".upper():
                for char_i in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0 or y == coordLimitsY - 1:
                        ascii[y].append("I")
                    elif 0 < y < coordLimitsY - 1:
                        if x == 3:
                            ascii[y].append("I")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "j".upper():
                for char_j in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0:
                        ascii[y].append("J")
                    elif 0 < y < coordLimitsY - 3:
                        if x == 3:
                            ascii[y].append("J")
                        else:
                            ascii[y].append(" ")
                    elif y == 1 or coordLimitsY - 1 > y > 3:
                        if x == 1 or x == coordLimitsX - 2:
                            ascii[y].append("J")
                        else:
                            ascii[y].append(" ")
                    elif y == coordLimitsY - 1:
                        if x == 2 or x == coordLimitsX - 2:
                            ascii[y].append("J")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "k".upper():
                for char_k in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if not y > 3:
                            z += 1
                        else:
                            z -= 1
                        x = 0
                    elif 0 <= y <= 2:
                        if x == 1 or x == coordLimitsX - z:
                            ascii[y].append("K")
                        else:
                            ascii[y].append(" ")
                    elif 2 < y <= coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX - z:
                            ascii[y].append("K")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "m".upper():
                for char_m in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0 or 3 < y <= coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("M")
                        else:
                            ascii[y].append(" ")
                    elif 1 <= y <= 2:
                        if x != 3:
                            ascii[y].append("M")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        if x == 1 or x == 3 or x == coordLimitsX:
                            ascii[y].append("M")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "n".upper():
                z = 4
                for char_n in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        z -= 1
                        x = 0
                    elif y == 0 or 3 < y < coordLimitsY:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("N")
                        else:
                            ascii[y].append(" ")
                    elif 0 < y < coordLimitsY - 2:
                        if x == 1 or x == coordLimitsX - z or x == coordLimitsX:
                            ascii[y].append("N")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "o".upper():
                for char_o in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0 or y == coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        elif x > 0:
                            if not x > 4:
                                ascii[y].append("O")
                    elif 0 < y < coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("O")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "p".upper():
                for char_p in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y == 0 or y == 3:
                        if x < coordLimitsX:
                            ascii[y].append("P")
                        else:
                            ascii[y].append(" ")
                    elif 0 < y < 3:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("P")
                        else:
                            ascii[y].append(" ")
                    elif 3 < y <= coordLimitsY - 1:
                        if x == 1:
                            ascii[y].append("P")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "q".upper():
                for char_q in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y >= 5:
                            z += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        elif x > 0:
                            if not x > 4:
                                ascii[y].append("Q")
                    elif 0 < y < coordLimitsY - 2:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("Q")
                        else:
                            ascii[y].append(" ")
                    elif y >= 4:
                        if y == coordLimitsY - 1:
                            if x == 2 or x == coordLimitsX - z or x == coordLimitsX:
                                ascii[y].append("Q")
                            else:
                                ascii[y].append(" ")
                        else:
                            if x == 1 or x == coordLimitsX - z:
                                ascii[y].append("Q")
                            else:
                                ascii[y].append(" ")
                    addSpace()

            elif char == "r".upper():
                z = -2
                for char_r in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y > 4:
                            z += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == 3:
                        if x < coordLimitsX:
                            ascii[y].append("R")
                        else:
                            ascii[y].append(" ")
                    elif 0 < y < 4:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("R")
                        else:
                            ascii[y].append(" ")
                    elif y >= 4:
                        if x == 1 or x == coordLimitsX + z:
                            ascii[y].append("R")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "t".upper():
                for char_r in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0:
                        ascii[y].append("T")
                    elif y > 0:
                        if x == 3:
                            ascii[y].append("T")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "u".upper():
                for char_r in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y < coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("U")
                        else:
                            ascii[y].append(" ")
                    elif y == 6:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        elif x > 0:
                            if not x > 4:
                                ascii[y].append("U")
                    addSpace()

            elif char == "v".upper():
                s = 3
                for char_r in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y > 4:
                            z += 1
                        if y == coordLimitsY - 1:
                            s -= 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y < coordLimitsY - 2:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("V")
                        else:
                            ascii[y].append(" ")
                    elif y > 4:
                        if x == coordLimitsX - z or x == coordLimitsX - s:
                            ascii[y].append("V")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "w".upper():
                for char_m in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y < 3 or y == coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("W")
                        else:
                            ascii[y].append(" ")
                    elif y > 3:
                        if x != 3:
                            ascii[y].append("W")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        if x == 1 or x == 3 or x == coordLimitsX:
                            ascii[y].append("W")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "x".upper():
                s = 4
                for char_m in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if 1 < y <= 5:
                            z += 1
                            s -= 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y <= 1 or y > 4:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("X")
                        else:
                            ascii[y].append(" ")
                    elif 1 < y < 4 or y < 5:
                        if x == coordLimitsX - z or x == coordLimitsX - s:
                            ascii[y].append("X")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "y".upper():
                s = 4
                for char_m in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y < 2:
                            z += 1
                            s -= 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y >= 2:
                        if x == coordLimitsX - 2:
                            ascii[y].append("Y")
                        else:
                            ascii[y].append(" ")
                    elif y < 2:
                        if x == coordLimitsX - z or x == coordLimitsX - s:
                            ascii[y].append("X")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "z".upper():
                for char_m in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y > 1:
                            z += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == coordLimitsY - 1:
                        ascii[y].append("Z")
                    elif 0 < y < coordLimitsY - 1:
                        if x == coordLimitsX - z:
                            ascii[y].append("Z")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == " ".upper():
                coordLimitsX = self.amountOfSpacing
                for char_m in range(limit * self.amountOfSpacing):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif not x == self.amountOfSpacing:
                        ascii[y].append(" ")

            # ;NUM----------------------------------------------------------------
            elif char == "0":  # ;
                for char_0 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y > 1:
                            z += 1
                        x = 0
                    elif y == 0 or y == coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        elif x > 0:
                            if not x > 4:
                                ascii[y].append("0")
                    elif 0 < y < coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX or x == coordLimitsX - z:
                            ascii[y].append("0")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "1":
                z = 2
                for char_1 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if 0 < y <= 4:
                            z += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 4 < y <= 5:
                        if x == 3:
                            ascii[y].append(char)
                        else:
                            ascii[y].append(" ")
                    elif 0 <= y <= 4:
                        if x == 3 or x == coordLimitsX - z and not y == 0:
                            ascii[y].append("1")
                        else:
                            ascii[y].append(" ")
                    elif y == coordLimitsY - 1:
                        ascii[y].append(char)
                    addSpace()

            elif char == "2":
                for char_2 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y >= 2:
                            z += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        elif x > 0:
                            if not x > 4:
                                ascii[y].append("2")
                    elif y == 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("2")
                        else:
                            ascii[y].append(" ")
                    elif 1 < y <= 5:
                        if x == coordLimitsX - z:
                            ascii[y].append("2")
                        else:
                            ascii[y].append(" ")
                    elif y == coordLimitsY - 1:
                        ascii[y].append("2")
                    addSpace()

            elif char == "3":
                for char_3 in range(limit):
                    x += 1
                    if z == 2:
                        z = 0
                    if x > coordLimitsX:
                        y += 1
                        if y > 1:
                            z += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        elif x > 0:
                            if not x > 4:
                                ascii[y].append("3")
                    elif 0 < y < 3 or 3 < y < coordLimitsY:
                        if x == coordLimitsX - z:
                            ascii[y].append("3")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        if 2 < x < coordLimitsX:
                            ascii[y].append("3")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "4":
                for char_4 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y < 3:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("4")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        ascii[y].append("4")
                    elif y > 3:
                        if x == coordLimitsX:
                            ascii[y].append("4")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "5":
                for char_5 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y > 5:
                            z += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0:
                        ascii[y].append("5")
                    elif 0 < y < 3:
                        if x == 1:
                            ascii[y].append("5")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        if x == coordLimitsX:
                            ascii[y].append(" ")
                        else:
                            ascii[y].append("5")
                    elif y > 3:
                        if x == coordLimitsX - z or y == 5 and x == 1:
                            ascii[y].append("5")
                        else:
                            if y == coordLimitsY - 1:
                                if x == 1 or x == coordLimitsX:
                                    ascii[y].append(" ")
                                else:
                                    ascii[y].append("5")
                            else:
                                ascii[y].append(" ")
                    addSpace()

            elif char == "6":
                for char_6 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        else:
                            ascii[y].append("6")
                    elif 0 < y <= 2:
                        if x == 1:
                            ascii[y].append("6")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        if x < coordLimitsX:
                            ascii[y].append("6")
                        else:
                            ascii[y].append(" ")
                    elif 3 < y < coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("6")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "7":
                for char_7 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y > 0:
                            s += 1
                            if y < 6:
                                if s == 2:
                                    z += 1
                                    s = 0
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0:
                        ascii[y].append("7")
                    elif y >= 0:
                        if x == coordLimitsX - z:
                            ascii[y].append("7")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "8":
                for char_8 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == 3 or y == coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        else:
                            ascii[y].append("8")
                    elif 1 <= y < 3 or 3 < y < coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("8")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "9":
                for char_9 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        else:
                            ascii[y].append("9")
                    elif 0 < y < 3:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("9")
                        else:
                            ascii[y].append(" ")
                    elif y > 3:
                        if x == coordLimitsX:
                            ascii[y].append("9")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        if x > 1:
                            ascii[y].append("9")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            # ;Special Characters----------------------------------------------------------------
            # ;May not be accurate due to 5x7 limit
            elif char == "`":
                z = 4
                if self.reduceSpacing is True:
                    coordLimitsX = 2
                    z = 3-coordLimitsX
                for char_sc_000 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y >= 0:
                            z -= 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y <= 1:
                        if x == coordLimitsX - z:
                            ascii[y].append("`")
                        else:
                            ascii[y].append(" ")
                    elif y > 1:
                        ascii[y].append(" ")
                    addSpace()

            elif char == "~":
                for char_sc_001 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y < 3 or y > 4:
                        ascii[y].append(" ")
                    elif y == 3:
                        if x == 2 or x == 3 or x == 5:
                            ascii[y].append("~")
                        else:
                            ascii[y].append(" ")
                    elif y == 4:
                        if x == 1 or x == 4:
                            ascii[y].append("~")
                        else:
                            ascii[y].append(' ')
                    addSpace()

            elif char == "!":
                if self.reduceSpacing is True:
                    coordLimitsX = 4
                for char_sc_002 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y < 4:
                        if x == 0 or x == coordLimitsX:
                            ascii[y].append(" ")
                        else:
                            ascii[y].append("!")
                    elif y == 4 or y == 6:
                        if 0 <= x < 2 or x > 2:
                            ascii[y].append(" ")
                        else:
                            ascii[y].append("!")
                    elif y == 5:
                        ascii[y].append(" ")

            elif char == "@":
                z = 2
                for char_sc_003 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if 4 <= y <= 5:
                            z -= 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        else:
                            ascii[y].append("@")
                    elif y == 1:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append("@")
                        else:
                            ascii[y].append(" ")
                    elif 2 <= y < coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX - z:
                            ascii[y].append("@")
                        elif x == coordLimitsX and 1 <= y <= 3:
                            ascii[y].append("@")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "#":
                for char_sc_004 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y < 2 or y == 3 or y > 4:
                        if x == 1 or x == 3 or x == coordLimitsX:
                            ascii[y].append(" ")
                        else:
                            ascii[y].append("#")
                    elif y == 2 or y == 4:
                        ascii[y].append("#")
                    addSpace()

            elif char == "$":
                for char_sc_005 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == coordLimitsY - 1:
                        if x == 3:
                            ascii[y].append("$")
                        else:
                            ascii[y].append(" ")
                    elif y == 1 or y == 3 or y == 5:
                        if x == 1 or x == coordLimitsX:
                            ascii[y].append(" ")
                        else:
                            ascii[y].append("$")
                    elif y == 2:
                        if x == 1 or x == 3:
                            ascii[y].append("$")
                        else:
                            ascii[y].append(" ")
                    elif y == 4:
                        if x == coordLimitsX or x == 3:
                            ascii[y].append("$")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "%":
                z = 2
                for char_sc_006 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y >= 2:
                            s += 1
                            if 0 < y < 3 and s >= 2:
                                p()
                                z += 1
                                s = 0
                            elif y > 3 and s == 3:
                                p(y)
                                z += 1
                                s = 0
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y < 2:
                        if x == 1 or x == coordLimitsX - 1:
                            ascii[y].append("%")
                        else:
                            ascii[y].append(" ")
                    elif y >= 2:
                        if y < 5:
                            if x == coordLimitsX - z:
                                ascii[y].append("%")
                            else:
                                ascii[y].append(" ")
                        else:
                            if x == coordLimitsX - z or x == coordLimitsX:
                                ascii[y].append("%")
                            else:
                                ascii[y].append(" ")
                    addSpace()

            elif char == "^":
                z = 2
                s = 2
                for char_sc_007 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y > 0:
                            z += 1
                            s -= 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0:
                        if x == 3:
                            ascii[y].append("^")
                        else:
                            ascii[y].append(" ")
                    elif 0 < y < 3:
                        if x == coordLimitsX - z or x == coordLimitsX - s:
                            ascii[y].append("^")
                        else:
                            ascii[y].append(" ")
                    elif y >= 3:
                        ascii[y].append(" ")
                    addSpace()

            elif char == "&":
                z = 1
                s = 3
                for char_sc_008 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == 2:
                        if x == 3:
                            ascii[y].append("&")
                        else:
                            ascii[y].append(" ")
                    elif y == 1:
                        if x == coordLimitsX - z or x == coordLimitsX - s:
                            ascii[y].append("&")
                        else:
                            ascii[y].append(" ")
                    elif y == 3 or y == coordLimitsY - 1:
                        if 1 < x <= 3 or x == coordLimitsX:
                            ascii[y].append("&")
                        else:
                            ascii[y].append(" ")
                    elif y > 3 or y > coordLimitsY - 1:
                        if x == 1 or x == coordLimitsX - 1:
                            ascii[y].append("&")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "*":
                z = 4
                s = 0
                resetIterValues = False  # ;Rolls back the values above to defined values
                for char_sc_009 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if 0 < y < 3:
                            z -= 1
                            s -= 1
                        if y == 3:
                            resetIterValues = True
                        if resetIterValues is True:
                            z = 2
                            s = 2
                            if y > 4:
                                if y <= 5:
                                    z += 1
                                    s -= 1
                                else:
                                    resetIterValues = False
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == coordLimitsY - 1:
                        ascii[y].append(" ")
                    elif 0 < y < 3:
                        if x == coordLimitsX - z or x == coordLimitsX + s:
                            ascii[y].append("*")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        ascii[y].append("*")
                    elif y > 3:
                        if x == coordLimitsX - z or x == coordLimitsX - s:
                            ascii[y].append("*")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "(":
                z = 2
                if self.reduceSpacing is True:
                    coordLimitsX = 3
                    z = 0
                for char_sc_011 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if 0 <= y < 3:
                            z += 1
                        if y > 4:
                            z -= 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y >= 0:
                        if x == coordLimitsX - z:
                            ascii[y].append("(")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == ")":
                z = 2
                if self.reduceSpacing is True:
                    coordLimitsX = 4
                    z = 2
                for char_sc_012 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if 0 <= y < 3:
                            z -= 1
                        if y > 4:
                            z += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y >= 0:
                        if x == coordLimitsX - z:
                            ascii[y].append(")")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "-":
                for char_sc_013 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y < 4 or y > 3:
                        if y == 3:
                            ascii[y].append("-")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "_":
                for char_sc_014 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y >= 0:
                        if y == coordLimitsY - 1:
                            ascii[y].append("_")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "=":
                for char_sc_015 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y < 2 or y == 3 or y >= 5:
                        ascii[y].append(" ")
                    elif y == 2 or y == 4:
                        ascii[y].append("=")
                    addSpace()

            elif char == "+":
                if self.reduceSpacing is True:
                    coordLimitsX = 4
                for char_sc_016 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y <= 1 or y > 4:
                        ascii[y].append(" ")
                    elif 1 < y < coordLimitsY - 1:
                        if 0 < y <= 2 or y == 4:
                            if x == 3:
                                ascii[y].append("+")
                            else:
                                ascii[y].append(" ")
                        if y == 3:
                            if x == 1 and x <= coordLimitsX:
                                ascii[y].append(" ")
                            else:
                                ascii[y].append("+")
                    addSpace()

            elif char == "[":
                for char_sc_017 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == coordLimitsY - 1:
                        if 1 <= x <= 3:
                            ascii[y].append("[")
                        else:
                            ascii[y].append(" ")
                    elif 0 < y < coordLimitsY - 1:
                        if x == 1:
                            ascii[y].append("[")
                    addSpace()

            elif char == "{":
                for char_sc_018 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == coordLimitsY - 1:
                        if 3 <= x < coordLimitsX:
                            ascii[y].append("{")
                        else:
                            ascii[y].append(" ")
                    elif 0 < y < 3 or 3 < y < coordLimitsY - 1:
                        if x == 2:
                            ascii[y].append("{")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        if x == 1:
                            ascii[y].append("{")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "]":
                for char_sc_019 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == coordLimitsY - 1:
                        if 3 <= x <= coordLimitsX:
                            ascii[y].append("[")
                        else:
                            ascii[y].append(" ")
                    elif 0 < y < coordLimitsY - 1:
                        if x == coordLimitsX:
                            ascii[y].append("[")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "}":
                for char_sc_020 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == coordLimitsY - 1:
                        if 2 <= x < coordLimitsX - 1:
                            ascii[y].append("}")
                        else:
                            ascii[y].append(" ")
                    elif 0 < y < 3 or 3 < y < coordLimitsY - 1:
                        if x == coordLimitsX - 1:
                            ascii[y].append("}")
                        else:
                            ascii[y].append(" ")
                    elif y == 3:
                        if x == coordLimitsX:
                            ascii[y].append("}")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "\/"[0]:
                z = 4
                for char_sc_021 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y > 2:
                            z -= 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y < 2:
                        ascii[y].append(" ")
                    elif y >= 2:
                        if x == coordLimitsX - z:
                            ascii[y].append("\/"[0])
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "|":
                for char_sc_022 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y >= 0:
                        if x == 3:
                            ascii[y].append("|")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == ";":
                z = 1
                for char_sc_023 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y > 3:
                            z += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == 3 or y == coordLimitsY - 1:
                        ascii[y].append(" ")
                    elif 1 <= y < 3:
                        if x == 3:
                            ascii[y].append(";")
                        else:
                            ascii[y].append(" ")
                    elif 3 < y <= 6:
                        if x == coordLimitsX - z:
                            ascii[y].append(";")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == ":":
                for char_sc_024 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y == 0 or y == 3 or y == coordLimitsY - 1:
                        ascii[y].append(" ")
                    elif 1 <= y < 3:
                        if x == 3:
                            ascii[y].append(":")
                        else:
                            ascii[y].append(" ")
                    elif 3 < y <= 6:
                        if x == 3:
                            ascii[y].append(":")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == "'":
                for char_sc_025 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y < 2:
                        if x == 1:
                            ascii[y].append("'")
                        else:
                            ascii[y].append(" ")
                    elif y >= 2:
                        ascii[y].append(" ")

            elif char == '"':
                for char_sc_026 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y < 2:
                        if 1 <= x <= 2:
                            ascii[y].append("'")
                        else:
                            ascii[y].append(" ")
                    elif y >= 2:
                        ascii[y].append(" ")

            elif char == ',':
                for char_sc_027 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y <= 5:
                        ascii[y].append(" ")
                    elif y == coordLimitsY - 1:
                        if x == 1:
                            ascii[y].append(",")
                        else:
                            ascii[y].append(" ")

            elif char == '<':
                z = 0
                s = 4
                for char_sc_028 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y >= 0:
                            z += 1
                        if y >= 3:
                            s -= 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y < 4:
                        if x == coordLimitsX - z:
                            ascii[y].append("<")
                        else:
                            ascii[y].append(" ")
                    elif 3 < y <= 6:
                        if x == coordLimitsX - s:
                            ascii[y].append("<")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == '.':
                for char_sc_029 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y <= 4:
                        ascii[y].append(" ")
                    elif y >= 4:
                        if x < 3:
                            ascii[y].append(".")
                        else:
                            ascii[y].append(" ")

            elif char == '>':
                z = 4
                s = 0
                for char_sc_030 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y >= 0:
                            z -= 1
                        if y >= 3:
                            s += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif 0 <= y < 4:
                        if x == coordLimitsX - z:
                            ascii[y].append(">")
                        else:
                            ascii[y].append(" ")
                    elif 3 < y <= 6:
                        if x == coordLimitsX - s:
                            ascii[y].append(">")
                        else:
                            ascii[y].append(" ")
                    addSpace()

            elif char == '/':
                for char_sc_030 in range(limit):
                    x += 1
                    if x > coordLimitsX:
                        y += 1
                        if y > 2:
                            z += 1
                        x = 0
                    elif y >= coordLimitsY:
                        break
                    elif y < 2:
                        ascii[y].append(" ")
                    elif y >= 2:
                        if x == coordLimitsX - z:
                            ascii[y].append("/")
                        else:
                            ascii[y].append(" ")
                    addSpace()

        # ;Print to STDOUT (Not list form)
        x = 0
        for line in ascii:
            for char in line:
                returnString += char
                x += 1
                if x == len(line):
                    returnString += "\n"
                    x = 0

        # ;Keyword Arguments
        if self.printASCIIList is True:
            yCounter = 0
            yCounterActual = 0
            for x_list in ascii:
                yCounterActual += 1
                p(f"{x_list} (<x={len(x_list)}> ,<y={yCounter} | {yCounterActual})>")
                yCounter += 1
        if self.checkIfYValueReachedASCIIList is True:
            if y == len(ascii):
                p("Length has been reached")

        p(returnString)


askii("+", printASCIIList=True)
