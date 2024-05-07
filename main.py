import math, os
from random import randint
from time import sleep
from shutil import get_terminal_size

# Written for Python 3.11

######################################################################################################
# HELPER FUNCTIONS


def clearTerminal():

    print("\n" * get_terminal_size().lines, end = "")


def convertStringToFloat(string, Min = None, Max = None, CanBeEqual = True, NumBlacklist = None, AllowInfinity = False):

    length = string.__len__()

    number = None

    if string.isdigit(): # Checking for and returning any positive ints i.e.: 123123

        number = float(string)
        # OR: int(string)


    elif length >= 2 and string[0] == "-": # Checking for and returning any negative ints i.e.: -123123

        string_positive = string.split("-", 1)

        if string_positive[1].isdigit():  

            number = float(string)
            # OR: -int(string_positive[1]) 


        elif length >= 4 and string.find("."): # Checking for and returning any negative fractionals i.e.: i -123.123

            dot_split_positive = string_positive[1].split(".", 1)
    
            if dot_split_positive[0].isdigit() and dot_split_positive[1].isdigit():

                number = float(string)
                # OR: -int(dot_split_positive[0] + dot_split_positive[1]) / pow(10, dot_split_positive[1].__len__()) 


    elif length >= 3 and string.find("."): # Checking for and returning any positive fractionals i.e.: 4.123123

        dot_split = string.split(".", 1)

        if dot_split[0].isdigit() and dot_split[1].isdigit():

    
            number = float(string)
            # OR: int(dot_split[0] + dot_split[1]) / pow(10, dot_split[1].__len__()) 


    if (
        number == None or 
        ( AllowInfinity == False and math.isinf( number ) == True ) or 
        ( NumBlacklist != None and number in NumBlacklist ) or 

        ( CanBeEqual == True and (
            Min != None and number < Min or
            Max != None and number > Max
        ) ) or

        (CanBeEqual == False and (
            Min != None and number <= Min or
            Max != None and number >= Max
        ) )

    ): # end of conditions

        return None
        
    else:

        return number
            

def listFind(haystack, needle):

    # haystack - list
    # needle - anything that a list can contain

    for i in range(0, len(haystack)):

        if haystack[i] == needle:

            return True


    return False


def askUntillFloatInput(FirstMessage, RetryMessage, Min = None, Max = None, CanBeEqual = True, NumBlacklist = None, AllowInfinity = False):

    clearTerminal()

    print(FirstMessage)

    FloatInput = convertStringToFloat(input("Input: "), Min, Max, CanBeEqual, NumBlacklist, AllowInfinity) 

    while FloatInput == None: # convertStringToFloat() returns None if conversion wasn't possible (i.e. input was" h123).

        clearTerminal()

        print(RetryMessage)

        sleep(0.3)
        
        print("\n" + FirstMessage)

        FloatInput = convertStringToFloat(input("Input: "), Min, Max, CanBeEqual, NumBlacklist, AllowInfinity) 


    return FloatInput


def askUntillOptionInput(OptionsList, FirstMessage, RetryMessage):

    # OptionsList should be a list of strings.

    clearTerminal()

    print(FirstMessage)

    OptionInput = input("Option: ")

    while not listFind(OptionsList, OptionInput):

        clearTerminal()

        print(RetryMessage)

        sleep(0.3)

        print("\n" + FirstMessage)

        OptionInput = input("Option: ")


    return OptionInput


######################################################################################################
# DRAWING


def drawQuadraticBezierCurve(StepSize, grey_line_frequency, StartingPositionX,StartingPositionY, MovingTargetPositionX,MovingTargetPositionY, EndPositionX,EndPositionY):  

    grey_line_frequency = math.floor(grey_line_frequency + 0.5)

    import turtle
    turtle.hideturtle()
    turtle.colormode(255)

    p0Turtle = turtle.Turtle()
    p0Turtle.hideturtle()
    p0Turtle.speed(0)
    p0Turtle.penup()
    p0Turtle.color("green")

    p1Turtle = turtle.Turtle()
    p1Turtle.hideturtle()
    p1Turtle.speed(0)
    p1Turtle.penup()
    p1Turtle.color("red")

    p2Turtle = turtle.Turtle()
    p2Turtle.hideturtle()
    p2Turtle.speed(0)
    p2Turtle.penup()
    p2Turtle.color("blue")

    p0 = {
        "x": StartingPositionX,
        "y": StartingPositionY
    }

    p1 = {
        "x": MovingTargetPositionX,
        "y": MovingTargetPositionY
    }

    p2 = {
        "x": EndPositionX,
        "y": EndPositionY
    }

    # p0 - Starting Position,
    # p1 - The point p0 moves to, 
    # p2 - End Point
    # p0, p1 and p2 are be dictionaries with "x" and "y" as their items.
    # StepSize Is a be a Number from 0 to 1 that doesn't equal 0.

    Loops = int(StepSize / StepSize / StepSize)
    
    StepSizeDecimalsLength = len(str(StepSize))-2 # -2 because it's the "0."
    StepSizeModifier = pow(10,StepSizeDecimalsLength) # StepSize = 0.123 -> 1000

    p0Turtle.goto(p0["x"],p0["y"])
    p0Turtle.pendown()
    p0Turtle.pensize(5)

    p1Turtle.goto(p1["x"],p1["y"])
    p1Turtle.pendown()
    p1Turtle.pensize(5)

    p2Turtle.goto(p2["x"],p2["y"])
    p2Turtle.pendown()
    p2Turtle.pensize(5)
    
    sleep(4)  

    if grey_line_frequency:

        p3Turtle = turtle.Turtle() # grey Line
        p3Turtle.hideturtle()
        p3Turtle.speed(0)
        p3Turtle.penup()
        p3Turtle.color((226,200,200))

        p3Turtle.goto(p1["x"],p1["y"])
        p3Turtle.pendown()
        p3Turtle.pensize(1)
        p3Turtle.goto(p0["x"],p0["y"])


        def drawGreyLine():

            p3Turtle.goto(p0Turtle.pos())
            p3Turtle.pendown()
            p3Turtle.goto(p1Turtle.pos())
            p3Turtle.penup()


    if StepSize <= 0.001:

        if StepSize <= 0.0003:

            WaitTime = StepSize / 4.5

        else:

            WaitTime = StepSize / 2.5


    else:

        WaitTime = StepSize


    for i in range(1,Loops+1): # If StepSize was 0.1 then it would loop 10 times.

        Progress = i / StepSizeModifier

        p0 = {
            "x": (1 - Progress) * p0["x"] + Progress * p1["x"],
            "y": (1 - Progress) * p0["y"] + Progress * p1["y"]
        }

        p1 = {
            "x": (1 - Progress) * p1["x"] + Progress * p2["x"],
            "y": (1 - Progress) * p1["y"] + Progress * p2["y"]
        }

        p0Turtle.goto(p0["x"],p0["y"])
        p1Turtle.goto(p1["x"],p1["y"])
        p2Turtle.goto(p2["x"],p2["y"])

        if grey_line_frequency and i % grey_line_frequency == 0: # Drawing a grey line every X moves

            drawGreyLine()


        if abs(p0["x"] - p2["x"]) < 1 and abs(p0["y"] - p2["y"]) < 1:
            break

        sleep(WaitTime)


    print("Finished the Animation!") 

    turtle.exitonclick()


def drawArc(Angle, Size, Segments):

    import turtle

    turtle.colormode(255)

    turtle.hideturtle()
    turtle.penup()
    turtle.pencolor("green")
    turtle.pensize(4)
    turtle.goto(Size, 0)
    turtle.speed(1)
    
    sleep(4)

    turtle.pendown()

    SegmentAngle = math.radians(Angle / Segments)

    for i in range(math.floor(Segments)):

        Modifier = SegmentAngle * (i + 1)
        turtle.goto(Size*math.cos(Modifier), Size*math.sin(Modifier))



    print("Finished the Animation!")

    turtle.exitonclick()
    

######################################################################################################
# CONSOLE INTERFACE


def askDrawArc():

    Angle = askUntillFloatInput("Input the Angle between two ends of the Arc and the centre of it's Circle (a number between 0 and 360)", "Wrong Input! Try Again!", 0, 360, CanBeEqual = True)
    Size = askUntillFloatInput("Input the size Multiplier of the Arc (recommended: 300)", "Wrong Input! Try Again!", 0, CanBeEqual = True, NumBlacklist = [0])
    Segments = askUntillFloatInput("Input the number of segments of the Arc (recommended: 300)", "Wrong Input! Try Again!")

    clearTerminal()

    print("Starting Animation in 4 seconds...")

    return (Angle, Size, Segments)


def askQuadraticBezierCurve():

    # Longer Meessages:
    PositionsModeFirstMessage = """Select Mode:
    1 - Custom - Lets customise all positions.
    2 - Preview - All positions are preset.
    3 - Full Random - Makes all positions random numbers from -400 to 400.

    To select a Mode, type it's number from this list.
"""

    CommonError = "Wrong Position Passed! Try Again!"

    # Questions:

    PositionsMode = askUntillOptionInput(["1", "2", "3"], PositionsModeFirstMessage, "No Mode of this Number found! Select Mode Again!")

    if PositionsMode == "1": # Custom

        StartingPositionX = askUntillFloatInput("Input Starting Point Position X (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)
        StartingPositionY = askUntillFloatInput("Input Starting Point Position Y (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)

        MovingTargetPositionX = askUntillFloatInput("Input Moving Target Point Position X (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)
        MovingTargetPositionY = askUntillFloatInput("Input Moving Target Point Position Y (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)

        EndPositionX = askUntillFloatInput("Input End Position X (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)
        EndPositionY = askUntillFloatInput("Input End Position Y (a number between -400 and 400).", CommonError, Min = -400, Max = 400, CanBeEqual = True)

    elif PositionsMode == "2": # Preview

        StartingPositionX = -400
        StartingPositionY = 0

        MovingTargetPositionX = 0
        MovingTargetPositionY = 400

        EndPositionX = 400
        EndPositionY = 0

    elif PositionsMode == "3": # Full Random

        StartingPositionX = randint(-400, 400)
        StartingPositionY = randint(-400, 400)

        MovingTargetPositionX = randint(-400, 400)
        MovingTargetPositionY = randint(-400, 400)

        EndPositionX = randint(-400, 400)
        EndPositionY = randint(-400, 400)

    else:

        clearTerminal()
        print("ERROR: WRONG POSITIONSMODE SELECTED!")


    StepSize = askUntillFloatInput("Input Step Size (A number between 0 and 1 that isn't 0 (i.e. 0.001))", "Wrong Step Size Passed! Try again!", Min = 0, Max = 1, NumBlacklist = [0])
    GreyLineFrequency = askUntillFloatInput("Input Grey Line Drawing Frequency (full number) (every X steps) OR 0 to Disable", "Wrong Grey Line Frequency Passed! Try again!", Min = 0)

    clearTerminal()

    print("Starting Animation in 4 seconds...")

    return(StepSize, GreyLineFrequency, StartingPositionX,StartingPositionY, MovingTargetPositionX,MovingTargetPositionY, EndPositionX,EndPositionY) # Tuple
        

def askDrawOption():

    FirstMessage = """Options:
    1 - Draw an Arc
    2 - Draw a Quadratic Bézier Curve
    
    To select an Option, type it's number from this List.
"""

    RetryMessage = "No Option of this Number found! Select Option Again!"

    Mode = askUntillOptionInput(["1","2"], FirstMessage, RetryMessage)
 
    if Mode == "1": # Draw an Arc

        drawArc(*askDrawArc())

    elif Mode == "2": # Draw a Quadratic Bezier Curve

        drawQuadraticBezierCurve(*askQuadraticBezierCurve())


######################################################################################################
# RUNNING


askDrawOption()

clearTerminal()

print("Finished!")