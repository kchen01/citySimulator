# City Simulator
# Kevin Chen and Teagan Johnson
# Intro to CS(CS111) at Carleton College, 2019

from graphics import *
import random
import time

#creates window and sets coordinates
win = GraphWin("City", 1450,800, autoflush = False)
win.setCoords(0,0,1450,800)

#creates the opening screen of the simulation
def displayOpeningScreen():
    back = Rectangle(Point(0,0), Point(1450,800))
    back.setFill("white")
    back.draw(win)

    title = Text(Point(725, 500), "City Simulator")
    title.setSize(36)
    title.setStyle("bold italic")
    title.draw(win)

    message = Text(Point(725, 400), "Click to start")
    message.setSize(18)
    message.draw(win)

    #waits for user to click
    win.getMouse()

#gets the month input from the user
def getMonth():
    background = Rectangle(Point(0,0), Point(1450,800))
    background.setFill("white")
    background.draw(win)

    simulationTitle = Text(Point(725, 500), "Please enter the month")
    simulationTitle.setSize(24)
    simulationTitle.draw(win)

    directions = Text(Point(725, 400), "Must be a string")
    directions.setSize(12)
    directions.draw(win)

    enterButton = Rectangle(Point(650, 275), Point(800,245))
    enterButton.draw(win)
    buttonText = Text(Point(725, 260), "Enter")
    buttonText.setSize(12)
    buttonText.draw(win)

    monthInputBox = Entry(Point(725, 300), 20)
    monthInputBox.draw(win)

    point = win.getMouse()
    xvalue = point.getX()
    yvalue = point.getY()

    #makes sure the user clicks the enter button to input his/her response
    click = False
    while click == False:
        if (xvalue >= 650 and xvalue <= 800) and (yvalue >= 245 and yvalue <= 275):
            click = True
        else:
            click = False
            point = win.getMouse()
            xvalue = point.getX()
            yvalue = point.getY()

    month = monthInputBox.getText()
    month = month.lower()
    monthInputBox.undraw()

    #makes sure the inputted month is valid
    input = False
    while input == False:
        if month == 'january' or month == 'february' or month == 'march' or month == 'april'\
         or month == 'may' or month == 'june' or month == 'july' or month == 'august'\
          or month == 'september' or month == 'october' or month == 'november' or month == 'december':
            input = True
        else:
            background = Rectangle(Point(0,0), Point(1450,800))
            background.setFill("white")
            background.draw(win)

            isTrueMonth = Text(Point(725, 400), "That's not a valid month!")
            isTrueMonth.setSize(12)
            isTrueMonth.draw(win)

            simulationTitle = Text(Point(725, 500), "Please enter the month:")
            simulationTitle.setSize(24)
            simulationTitle.draw(win)

            enterButton = Rectangle(Point(650, 245), Point(800,275))
            enterButton.draw(win)
            buttonText = Text(Point(725, 260), "Enter")
            buttonText.draw(win)

            monthInputBox = Entry(Point(725, 300), 20)
            monthInputBox.draw(win)

            point = win.getMouse()
            xvalue = point.getX()
            yvalue = point.getY()
            #makes sure the user clicks the enter button to input his/her response
            click = False
            while click == False:
                if (xvalue >= 650 and xvalue <= 800) and (yvalue >= 200 and yvalue <= 300):
                    click = True
                else:
                    click = False
                    point = win.getMouse()
                    xvalue = point.getX()
                    yvalue = point.getY()

            month = monthInputBox.getText()
            month = month.lower()

    win.update()
    return month

#gets the date input from the user
def getDay(month):
    background = Rectangle(Point(0,0), Point(1450,800))
    background.setFill("white")
    background.draw(win)

    simulationTitle = Text(Point(725, 500), "Please enter the day of the month")
    simulationTitle.setSize(24)
    simulationTitle.draw(win)

    directions = Text(Point(725, 400), "Must be a number")
    directions.setSize(12)
    directions.draw(win)

    enterButton = Rectangle(Point(650, 275), Point(800,245))
    enterButton.draw(win)
    buttonText = Text(Point(725, 260), "Enter")
    buttonText.setSize(12)
    buttonText.draw(win)

    dayInputBox = Entry(Point(725, 300), 20)
    dayInputBox.draw(win)

    point = win.getMouse()
    xvalue = point.getX()
    yvalue = point.getY()

    #makes sure the user clicks the enter button to input his/her response
    click = False
    while click == False:
        if (xvalue >= 650 and xvalue <= 800) and (yvalue >= 245 and yvalue <= 275):
            click = True
        else:
            click = False
            point = win.getMouse()
            xvalue = point.getX()
            yvalue = point.getY()

    day = dayInputBox.getText()
    dayInputBox.undraw()

    #runs a loop until input is valid
    input = False
    while input == False:
        #checks to see if input is valid
        try:
            if (month == 'january' or month == 'march' or month == 'may' or month == 'july'\
             or month == 'august' or month == 'october' or month == 'december') and (1 <= int(day) <=31):
                input = True
            elif (month == 'april' or month == 'june' or month == 'september'\
             or month == 'november') and (1 <= int(day) <=30):
                input = True
            elif (month == 'february' and 1 <= int(day) <= 28):
                input = True
            else:
                background = Rectangle(Point(0,0), Point(1450,800))
                background.setFill("white")
                background.draw(win)

                simulationTitle = Text(Point(725, 500), "Please enter the day of the month")
                simulationTitle.setSize(24)
                simulationTitle.draw(win)

                directions = Text(Point(725, 400), "That's not a valid day!")
                directions.setSize(12)
                directions.draw(win)

                enterButton = Rectangle(Point(650, 275), Point(800,245))
                enterButton.draw(win)
                buttonText = Text(Point(725, 260), "Enter")
                buttonText.setSize(12)
                buttonText.draw(win)

                dayInputBox = Entry(Point(725, 300), 20)
                dayInputBox.draw(win)

                point = win.getMouse()
                xvalue = point.getX()
                yvalue = point.getY()

        #if input is not a number
        except:
            background = Rectangle(Point(0,0), Point(1450,800))
            background.setFill("white")
            background.draw(win)

            simulationTitle = Text(Point(725, 500), "Please enter the day of the month")
            simulationTitle.setSize(24)
            simulationTitle.draw(win)

            directions = Text(Point(725, 400), "That's not a number!")
            directions.setSize(12)
            directions.draw(win)

            enterButton = Rectangle(Point(650, 275), Point(800,245))
            enterButton.draw(win)
            buttonText = Text(Point(725, 260), "Enter")
            buttonText.setSize(12)
            buttonText.draw(win)

            dayInputBox = Entry(Point(725, 300), 20)
            dayInputBox.draw(win)

            point = win.getMouse()
            xvalue = point.getX()
            yvalue = point.getY()

            #makes sure the user clicks the enter button to input his/her response
            click = False
            while click == False:
                if (xvalue >= 650 and xvalue <= 800) and (yvalue >= 245 and yvalue <= 275):
                    click = True
                else:
                    click = False
                    point = win.getMouse()
                    xvalue = point.getX()
                    yvalue = point.getY()

        day = dayInputBox.getText()
        dayInputBox.undraw()

    for item in win.items[:]:
        item.undraw()
    win.update()

    return day

#draws the quit button
def drawQuitButton():
    button = Rectangle(Point(0,700), Point(100,800))
    button.draw(win)
    button.setFill("red")

    text = Text(Point(50,750), "Quit")
    text.draw(win)
#draws the start over button
def drawStartOverButton():
    button = Rectangle(Point(1350,700), Point(1450,800))
    button.draw(win)
    button.setFill("green")

    text = Text(Point(1400,750), "Restart")
    text.draw(win)
#draws the pause button
def drawPauseButton():
    button = Rectangle(Point(675,700), Point(775,800))
    button.draw(win)
    button.setFill("yellow")

    text = Text(Point(725,750), "Pause")
    text.draw(win)


#Tree class
class Tree():
    #constructor for the tree class
    def __init__(self, size):
        self.size = size

    #draws the tree based on the size inputted by the user
    def makeTree(self, color):
        xvaluestump = random.randint(0,1450)
        yvaluestump = random.randint(120,135)
        stump = Rectangle(Point(xvaluestump, yvaluestump), Point((xvaluestump + 10 + self.size * 5), (yvaluestump + 10 + self.size * 5)))
        stump.setFill("brown")
        stump.setOutline("brown")
        stump.draw(win)

        treebody = Polygon(Point((xvaluestump - 10 - self.size * 5), (yvaluestump + 10)), Point((xvaluestump + 20 + self.size * 5), (yvaluestump + 10)), Point((xvaluestump + 5), (yvaluestump + 50 + self.size * 10)))
        treebody.setFill(color)
        treebody.setOutline(color)
        treebody.draw(win)

#Firework class, only accessed on July 4th
class Firework():
    def __init__(self, xvalue, yvalue):
        self.xvalue = xvalue
        self.yvalue = yvalue
    #makes each individual firework
    def makeFirework(self):
        colors = ['red', 'blue', 'orange', 'coral', 'orangered', 'hotpink']
        line1 = Line(Point(self.xvalue, self.yvalue), Point(self.xvalue + 35, self.yvalue + 35))
        line2 = Line(Point(self.xvalue, self.yvalue), Point(self.xvalue - 35, self.yvalue - 35))
        line3 = Line(Point(self.xvalue, self.yvalue), Point(self.xvalue + 49.49, self.yvalue))
        line4 = Line(Point(self.xvalue, self.yvalue), Point(self.xvalue, self.yvalue + 49.49))
        line5 = Line(Point(self.xvalue, self.yvalue), Point(self.xvalue - 49.49, self.yvalue))
        line6 = Line(Point(self.xvalue, self.yvalue), Point(self.xvalue, self.yvalue - 49.49))
        line7 = Line(Point(self.xvalue, self.yvalue), Point(self.xvalue + 35, self.yvalue - 35))
        line8 = Line(Point(self.xvalue, self.yvalue), Point(self.xvalue - 35, self.yvalue + 35))
        line1.setFill(random.choice(colors))
        line2.setFill(random.choice(colors))
        line3.setFill(random.choice(colors))
        line4.setFill(random.choice(colors))
        line5.setFill(random.choice(colors))
        line6.setFill(random.choice(colors))
        line7.setFill(random.choice(colors))
        line8.setFill(random.choice(colors))
        line1.draw(win)
        line2.draw(win)
        line3.draw(win)
        line4.draw(win)
        line5.draw(win)
        line6.draw(win)
        line7.draw(win)
        line8.draw(win)

#draws the background for the city
def drawBackground():
    drawRoad()
    drawRiver()
    drawGrass()
    drawQuitButton()
    drawStartOverButton()
    drawPauseButton()

#draws stuff based on the user's date input
def drawDateStuff(playerMonth, playerDay):
    month = playerMonth
    day = playerDay
    #January
    if month == 'january':
        drawTrees("white")
        snowflakes = makeSnow()
        #New Years
        if day == '1':
                sign = Rectangle(Point(696,590), Point(789,610))
                sign.setFill("coral")
                sign.setOutline("navy")
                sign.draw(win)

                sign2 = Rectangle(Point(880,650), Point(995,670))
                sign2.setFill("salmon")
                sign2.setOutline("maroon1")
                sign2.draw(win)

                signText2 = Text(Point(937.5, 660), "Happy New Year")
                signText2.setFill("snow")
                signText2.setSize(12)
                signText2.setStyle("bold italic")
                signText2.draw(win)
        elif day == '20':
                sign = Rectangle(Point(696,590), Point(789,610))
                sign.setFill("coral")
                sign.setOutline("navy")
                sign.draw(win)

                sign2 = Rectangle(Point(880,650), Point(995,670))
                sign2.setFill("salmon")
                sign2.setOutline("maroon1")
                sign2.draw(win)

                signText2 = Text(Point(937.5, 660), "Happy MLK day!")
                signText2.setFill("snow")
                signText2.setSize(12)
                signText2.setStyle("bold italic")
                signText2.draw(win)
    #February
    elif month == 'february':
        drawTrees("white")
        snowflakes = makeSnow()
    #March
    elif month == 'march':
        drawTrees()
        snowflakes = makeSnow()
    #April
    elif month == 'april':
        drawTrees()
        if day == '10':
            sign = Rectangle(Point(880,650), Point(995,670))
            sign.setFill("salmon")
            sign.setOutline("maroon1")
            sign.draw(win)

            signText = Text(Point(937.5, 660), "Teagan's birthday!")
            signText.setFill("snow")
            signText.setSize(12)
            signText.setStyle("bold italic")
            signText.draw(win)
        elif day == '12':
            colors = ["hot pink", "light sky blue", "medium spring green", "plum1", "pink", "mediumOrchid1", "lavender blush"]
            for i in range(10):
                color = random.choice(colors)
                egg = easterEgg(color)
                egg.makeEgg()

    elif month == 'may':
        drawTrees()
        if day == '9':
            sign = Rectangle(Point(880,650), Point(995,670))
            sign.setFill("salmon")
            sign.setOutline("maroon1")
            sign.draw(win)

            signText = Text(Point(937.5, 660), "Kevin's birthday!")
            signText.setFill("snow")
            signText.setSize(12)
            signText.setStyle("bold italic")
            signText.draw(win)

        elif day == '10':
            sign = Rectangle(Point(880,650), Point(995,670))
            sign.setFill("salmon")
            sign.setOutline("maroon1")
            sign.draw(win)

            signText = Text(Point(937.5, 660), "Happy Mother's Day!")
            signText.setFill("snow")
            signText.setSize(12)
            signText.setStyle("bold italic")
            signText.draw(win)
        elif day == '25':
                sign = Rectangle(Point(696,590), Point(789,610))
                sign.setFill("coral")
                sign.setOutline("navy")
                sign.draw(win)

                sign2 = Rectangle(Point(880,650), Point(995,670))
                sign2.setFill("salmon")
                sign2.setOutline("maroon1")
                sign2.draw(win)

                signText2 = Text(Point(937.5, 660), "Happy Memorial Day!")
                signText2.setFill("snow")
                signText2.setSize(12)
                signText2.setStyle("bold italic")
                signText2.draw(win)
    #June
    elif month == 'june':
        drawTrees()
        if day == '21':
            sign = Rectangle(Point(880,650), Point(995,670))
            sign.setFill("salmon")
            sign.setOutline("maroon1")
            sign.draw(win)

            signText = Text(Point(937.5, 660), "Happy Father's Day!")
            signText.setFill("snow")
            signText.setSize(12)
            signText.setStyle("bold italic")
            signText.draw(win)
    #July
    elif month == 'july':
        drawTrees()
    #August
    elif month == 'august':
        drawTrees()
    #September
    elif month == 'september':
        drawTrees()
        #Labor Day
        if day == '2':
            sign = Rectangle(Point(880,650), Point(995,670))
            sign.setFill("salmon")
            sign.setOutline("maroon1")
            sign.draw(win)

            signText = Text(Point(937.5, 660), "Happy Labor Day!")
            signText.setFill("snow")
            signText.setSize(12)
            signText.setStyle("bold italic")
            signText.draw(win)

    #October
    elif month == 'october':
        drawTrees()
        if day == '31':
            for i in range(10):
                pumpkin = Pumpkin(size = random.randint(1,4))
                pumpkin.makePumpkin()
    #November
    elif month == 'november':
        drawTrees()
        if day == '11':
            sign = Rectangle(Point(880,650), Point(995,670))
            sign.setFill("salmon")
            sign.setOutline("maroon1")
            sign.draw(win)

            signText = Text(Point(937.5, 660), "Happy Veterans Day!")
            signText.setFill("snow")
            signText.setSize(12)
            signText.setStyle("bold italic")
            signText.draw(win)
        elif day == '26':
            sign = Rectangle(Point(880,650), Point(995,670))
            sign.setFill("salmon")
            sign.setOutline("maroon1")
            sign.draw(win)

            signText = Text(Point(937.5, 660), "Happy Thanksgiving!")
            signText.setFill("snow")
            signText.setSize(12)
            signText.setStyle("bold italic")
            signText.draw(win)

    #December
    elif month == 'december':
        drawTrees("white")
        snowflakes = makeSnow()
        #Christmas
        if day == '25':
                colors = ['red', 'green', 'blue', 'yellow', 'pink']
                for j in range(100):
                    for i in range(10):
                        if i == 0:
                            color = random.choice(colors)
                            christmasLight = Circle(Point(random.randint(50,200), random.randint(300,600)), 2)
                            christmasLight.setOutline(color)
                            christmasLight.setFill(color)
                            christmasLight.draw(win)
                        elif i == 1:
                            color = random.choice(colors)
                            christmasLight = Circle(Point(random.randint(345,460), random.randint(300,695)), 2)
                            christmasLight.setOutline(color)
                            christmasLight.setFill(color)
                            christmasLight.draw(win)
                        elif i == 2:
                            color = random.choice(colors)
                            christmasLight = Circle(Point(random.randint(200,400), random.randint(300,620)), 2)
                            christmasLight.setOutline(color)
                            christmasLight.setFill(color)
                            christmasLight.draw(win)
                        elif i == 3:
                            color = random.choice(colors)
                            christmasLight = Circle(Point(random.randint(440,600), random.randint(300, 660)), 2)
                            christmasLight.setOutline(color)
                            christmasLight.setFill(color)
                            christmasLight.draw(win)
                        elif i == 4:
                            color = random.choice(colors)
                            christmasLight = Circle(Point(random.randint(695,790), random.randint(300, 690)), 2)
                            christmasLight.setOutline(color)
                            christmasLight.setFill(color)
                            christmasLight.draw(win)
                        elif i == 5:
                            color = random.choice(colors)
                            christmasLight = Circle(Point(random.randint(600,800), random.randint(300, 540)), 2)
                            christmasLight.setOutline(color)
                            christmasLight.setFill(color)
                            christmasLight.draw(win)
                        elif i == 6:
                            color = random.choice(colors)
                            christmasLight = Circle(Point(random.randint(875,1000), random.randint(300, 725)), 2)
                            christmasLight.setOutline(color)
                            christmasLight.setFill(color)
                            christmasLight.draw(win)
                        elif i == 7:
                            color = random.choice(colors)
                            christmasLight = Circle(Point(random.randint(1160,1299), random.randint(300, 700)), 2)
                            christmasLight.setOutline(color)
                            christmasLight.setFill(color)
                            christmasLight.draw(win)
                        elif i == 8:
                            color = random.choice(colors)
                            christmasLight = Circle(Point(random.randint(1290,1450), random.randint(300, 575)), 2)
                            christmasLight.setOutline(color)
                            christmasLight.setFill(color)
                            christmasLight.draw(win)
                        elif i == 9:
                            color = random.choice(colors)
                            christmasLight = Circle(Point(random.randint(1000,1200), random.randint(300, 650)), 2)
                            christmasLight.setOutline(color)
                            christmasLight.setFill(color)
                            christmasLight.draw(win)
    if month == 'january' or month == 'february' or month == 'march' or month == 'december':
        return snowflakes

#building class that creates the buildings in the background
class Building:
    #contructor for the building class
    def __init__(self, bottomLeft, upperRight, color, windowSize = 1, windowThickness = 1):
        self.width = upperRight.getX() - bottomLeft.getX()
        self.height = upperRight.getY() - bottomLeft.getY()
        self.bottomLeft = bottomLeft
        self.upperRight = upperRight
        self.lowerX = bottomLeft.getX()
        self.lowerY = bottomLeft.getY()
        self.higherX = upperRight.getX()
        self.higherY = upperRight.getY()
        self.windowSize = windowSize
        self.windowThickness = windowThickness
        self.color = color
    #returns the width of each building
    def getWidth(self):
        return self.width
    #returns the height of each building
    def getHeight(self):
        return self.height
    #draws the buildings
    def drawBuilding(self):
        build = Rectangle(self.bottomLeft, self.upperRight)
        build.draw(win)
        build.setFill(self.color)

    #makes windows for each individual building
    def makeWindows(self):

        if self.windowSize == 1:
            for i in range(int((self.width)/15)):
                line1 = Line(Point(self.lowerX + (i*15), self.lowerY), Point(self.lowerX + (i*15), self.higherY))
                line1.draw(win)
            for i in range(int((self.height)/15)):
                line2 = Line(Point(self.lowerX , (self.lowerY) + (i*15)), Point(self.higherX, self.lowerY + (i*15)))
                line2.draw(win)

        elif self.windowSize == 2:
            for i in range(int((self.width)/25)):
                line1 = Line(Point(self.lowerX + (i*25), self.lowerY), Point(self.lowerX + (i*25), self.higherY))
                line1.draw(win)
            for i in range(int((self.height)/25)):
                line2 = Line(Point(self.lowerX , (self.lowerY) + (i*25)), Point(self.higherX, self.lowerY + (i*25)))
                line2.draw(win)

        elif self.windowSize == 3:
            for i in range(int((self.width)/35)):
                line1 = Line(Point(self.lowerX + (i*35), self.lowerY), Point(self.lowerX + (i*35), self.higherY))
                line1.draw(win)
            for i in range(int((self.height)/35)):
                line2 = Line(Point(self.lowerX , (self.lowerY) + (i*35)), Point(self.higherX, self.lowerY + (i*35)))
                line2.draw(win)
#draws the buildings
def importBuildings():
    building1 = Building(Point(50,300), Point(200, 600), "grey", windowSize = 1, windowThickness = 1)
    building1.drawBuilding()
    building1.makeWindows()

    building2 = Building(Point(345,300), Point(460, 695), "steelblue3", windowSize = 3, windowThickness = 1)
    building2.drawBuilding()
    building2.makeWindows()

    building3 = Building(Point(200,300), Point(400, 620), "navajowhite4", windowSize = 2, windowThickness = 1)
    building3.drawBuilding()
    building3.makeWindows()

    building4 = Building(Point(440,300), Point(600, 660), "ivory3", windowSize = 1, windowThickness = 1)
    building4.drawBuilding()
    building4.makeWindows()

    building5 = Building(Point(695,300), Point(790, 690), "snow3", windowSize = 1, windowThickness = 1)
    building5.drawBuilding()
    building5.makeWindows()

    building6 = Building(Point(600,300), Point(800, 540), "goldenrod4", windowSize = 1, windowThickness = 1)
    building6.drawBuilding()
    building6.makeWindows()

    building7 = Building(Point(875,300), Point(1000, 725), "mint cream", windowSize = 2, windowThickness = 1)
    building7.drawBuilding()
    building7.makeWindows()
    topper = Polygon(Point(875,725), Point(937.5,765), Point(1000,725))
    topper.setFill("mint cream")
    topper.draw(win)
    antenna = Line(Point(937.5,785), Point(937.5,765))
    antenna.draw(win)

    building8 = Building(Point(1160,300), Point(1299, 700), "gray25", windowSize = 2, windowThickness = 1)
    building8.drawBuilding()
    building8.makeWindows()

    building9 = Building(Point(1290,300), Point(1450, 575), "burlywood3", windowSize = 2, windowThickness = 1)
    building9.drawBuilding()
    building9.makeWindows()

    building10 = Building(Point(1000,300), Point(1200, 650), "grey", windowSize = 2, windowThickness = 1)
    building10.drawBuilding()
    building10.makeWindows()

    smallBuilding1 = Rectangle(Point(840,300), Point(870, 400))
    smallBuilding1.setFill("SkyBlue2")
    smallBuilding1.draw(win)

    smallBuilding2 = Polygon(Point(805, 300), Point(805, 440), Point(835,420), Point(835,300))
    smallBuilding2.setFill("DodgerBlue3")
    smallBuilding2.draw(win)

    smallBuilding3 = Rectangle(Point(800, 300), Point(815, 345))
    smallBuilding3.setFill("ivory2")
    smallBuilding3.draw(win)

    smallBuilding4 = Rectangle(Point(817, 300), Point(860, 325))
    smallBuilding4.setFill("AntiqueWhite1")
    smallBuilding4.draw(win)

    skywalk1 = Rectangle(Point(800, 340), Point(875, 330))
    skywalk1.setFill("gold2")
    skywalk1.draw(win)

    skywalk2 = Rectangle(Point(800,330), Point(875, 320))
    skywalk2.setFill("gray69")
    skywalk2.draw(win)
#pumpkin class
class Pumpkin:
    def __init__(self, size):
        self.size = size

    def makePumpkin(self):
        xvalue = random.randint(0,1450)
        yvalue = random.randint(100,110)

        body = Oval(Point(xvalue, yvalue), Point(xvalue+15+(25*self.size), yvalue+30))
        body.setFill('orange')
        body.draw(win)

        eye1 = Circle(Point(xvalue+10,yvalue+20), 5)
        eye1.setFill('black')
        eye1.draw(win)

        eye2 = Circle(Point(xvalue+30,yvalue+20), 5)
        eye2.setFill('black')
        eye2.draw(win)

        mouth = Rectangle(Point(xvalue+10,yvalue+5), Point(xvalue+30,yvalue+10))
        mouth.setFill('black')
        mouth.draw(win)

        stem = Rectangle(Point(xvalue+15,yvalue+30), Point(xvalue+25,yvalue+35))
        stem.setFill('darkolivegreen3')
        stem.draw(win)

class easterEgg:
    def __init__(self, color):
        self.color = color

    def makeEgg(self):
        xvalue = random.randint(0,1450)
        yvalue = random.randint(100,110)

        egg = Oval(Point(xvalue, yvalue), Point(xvalue + 15, yvalue + 20))
        egg.setFill(self.color)
        egg.draw(win)

#boat class
class Boat:
    def __init__(self, length = 150, x = 10, y = 50, height = 10, direction = 1, size = 1.5):
        listOfColors = ['gray', 'moccasin', 'powderblue', 'beige', 'slategrey', 'dodgerblue', 'lavender', 'steelblue',\
        'dark green', 'cornflower blue', 'wheat3', 'tan1', 'tan4']
        self.color = random.choice(listOfColors)
        self.length = length
        self.possibleXPositions = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]
        self.x = random.choice(self.possibleXPositions)
        self.y = y

        self.height = height
        self.direction = direction
        self.speeds = [1, 2, 3]
        self.speed = random.choice(self.speeds)
        self.size = size

        self.mainBody = Rectangle(Point(self.x, self.y), Point(self.x + self.length * self.size, self.y + self.height * self.size))
        self.secondaryBody1 = Rectangle(Point(self.x + 20 * self.size, self.y + 10 * self.size), Point(self.x + 130 * self.size, self.y + 20 * self.size))
        self.secondaryBody2 = Rectangle(Point(self.x + 20 * self.size, self.y + 20 * self.size), Point(self.x + 130 * self.size, self.y + 30 * self.size))

        self.windowLine1 = Line(Point(self.x + 30 * self.size, self.y + 10 * self.size), Point(self.x + 30 * self.size, self.y + 20 * self.size))
        self.windowLine2 = Line(Point(self.x + 40 * self.size, self.y + 10 * self.size), Point(self.x + 40 * self.size, self.y + 20 * self.size))
        self.windowLine3 = Line(Point(self.x + 50 * self.size, self.y + 10 * self.size), Point(self.x + 50 * self.size, self.y + 20 * self.size))
        self.windowLine4 = Line(Point(self.x + 60 * self.size, self.y + 10 * self.size), Point(self.x + 60 * self.size, self.y + 20 * self.size))
        self.windowLine5 = Line(Point(self.x + 70 * self.size, self.y + 10 * self.size), Point(self.x + 70 * self.size, self.y + 20 * self.size))
        self.windowLine6 = Line(Point(self.x + 80 * self.size, self.y + 10 * self.size), Point(self.x + 80 * self.size, self.y + 20 * self.size))
        self.windowLine7 = Line(Point(self.x + 90 * self.size, self.y + 10 * self.size), Point(self.x + 90 * self.size, self.y + 20 * self.size))
        self.windowLine8 = Line(Point(self.x + 100 * self.size, self.y + 10 * self.size), Point(self.x + 100 * self.size, self.y + 20 * self.size))
        self.windowLine9 = Line(Point(self.x + 110 * self.size, self.y + 10 * self.size), Point(self.x + 110 * self.size, self.y + 20 * self.size))
        self.windowLine10 = Line(Point(self.x + 120 * self.size, self.y + 10 * self.size), Point(self.x + 120 * self.size, self.y + 20 * self.size))

        self.mainBody.setFill(self.color)
        self.secondaryBody1.setFill("gray60")
        self.secondaryBody2.setFill("white")

        self.mainBody.draw(win)
        self.secondaryBody1.draw(win)
        self.secondaryBody2.draw(win)
        self.windowLine1.draw(win)
        self.windowLine2.draw(win)
        self.windowLine3.draw(win)
        self.windowLine4.draw(win)
        self.windowLine5.draw(win)
        self.windowLine6.draw(win)
        self.windowLine7.draw(win)
        self.windowLine8.draw(win)
        self.windowLine9.draw(win)
        self.windowLine10.draw(win)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def moveBoat(self):

        self.mainBody.move(self.speed * self.direction, 0)
        self.secondaryBody1.move(self.speed * self.direction, 0)
        self.secondaryBody2.move(self.speed * self.direction, 0)
        self.windowLine1.move(self.speed * self.direction, 0)
        self.windowLine2.move(self.speed * self.direction, 0)
        self.windowLine3.move(self.speed * self.direction, 0)
        self.windowLine4.move(self.speed * self.direction, 0)
        self.windowLine5.move(self.speed * self.direction, 0)
        self.windowLine6.move(self.speed * self.direction, 0)
        self.windowLine7.move(self.speed * self.direction, 0)
        self.windowLine8.move(self.speed * self.direction, 0)
        self.windowLine9.move(self.speed * self.direction, 0)
        self.windowLine10.move(self.speed * self.direction, 0)

        self.x = self.x + (self.speed * self.direction)

    def reverseDirection(self):
        self.direction = -1 * self.direction

    def changeColor(self):
        listOfColors = ['gray', 'moccasin', 'powderblue', 'beige', 'slategrey', 'dodgerblue', 'lavender', 'steelblue',\
        'dark green', 'cornflower blue', 'wheat3', 'tan1', 'tan4', 'gold2', 'snow4', 'indianred1', 'brown1', 'khaki3']
        self.color = random.choice(listOfColors)
        self.mainBody.setFill(self.color)
    def changeSpeed(self):
        self.speed = random.choice(self.speeds)
#car class
class Car:
    def __init__(self, length = 40, height = 20, direction = 1, size = 1.5):
        listOfColors = ['gray', 'moccasin', 'powderblue', 'beige', 'slategrey', 'dodgerblue', 'lavender', 'steelblue']
        self.color = random.choice(listOfColors)
        self.length = length
        self.possibleXPositions = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]
        self.possibleYPositions = [195, 260]
        self.x = random.choice(self.possibleXPositions)
        self.y = random.choice(self.possibleYPositions)
        self.height = height
        self.direction = direction
        self.size = size
        self.speeds = [5, 6, 7, 8, 9]
        self.speed = random.choice(self.speeds)

        self.wheel1 = Circle(Point(self.x + 5, self.y), 10 * self.size)
        self.wheel2 = Circle(Point(self.x + (self.length * self.size - 5), self.y), 10 * self.size)
        self.wheel1.setFill("white")
        self.wheel2.setFill("white")

        self.carBody = Rectangle(Point(self.x, self.y), Point(self.x + (self.length * self.size), self.y + (self.height* self.size)))
        self.carBody.setFill(self.color)

        self.carBody.draw(win)
        self.wheel1.draw(win)
        self.wheel2.draw(win)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def moveCar(self):

        self.wheel1.move(self.speed * self.direction, 0)
        self.wheel2.move(self.speed * self.direction, 0)
        self.carBody.move(self.speed * self.direction, 0)

        self.x = self.x + (self.speed * self.direction)

    def reverseDirection(self):
        self.direction = -1 * self.direction

    def changeColor(self):
        listOfColors = ['gray', 'moccasin', 'powderblue', 'beige', 'slategrey', 'dodgerblue', 'lavender', 'steelblue',\
        'dark green', 'cornflower blue', 'wheat3', 'tan1', 'tan4']
        self.color = random.choice(listOfColors)
        self.carBody.setFill(self.color)

    def changeSpeed(self):
        self.speed = random.choice(self.speeds)

#moves the cars, if a car hits another car or the edge of the screen, it changes direction.
#also moves snowflakes if it's in the winter and changes sky color as time passes.
def animate(month, day, snowflakes):

    #creates cars
    car1 = Car()
    car2 = Car()
    car3 = Car()
    car4 = Car()
    car5 = Car()
    car6 = Car()

    boat1 = Boat()
    boat2 = Boat()
    boat2.reverseDirection()

    #moves objects
    exit = False
    count = 0
    listOfFireworks = []
    while exit != True:
        point = win.checkMouse()
        if point is None:
            pass
        else:
            xvalue = int(point.getX())
            yvalue = int(point.getY())

            if (xvalue <= 1450 and xvalue >= 1350) and (yvalue <= 800 and yvalue >= 700):
                exit = True
            elif (xvalue <= 775 and xvalue >= 675) and (yvalue <= 800 and yvalue >= 700):
                point = win.getMouse()
                xvalue = point.getX()
                yvalue = point.getY()
                unpause = False
                while unpause == False:
                    if (xvalue <= 775 and xvalue >= 675) and (yvalue <= 800 and yvalue >= 700):
                        unpause = True
                    elif (xvalue <= 100 and xvalue >= 0) and (yvalue <= 800 and yvalue >= 700):
                        unpause = True
                        win.close()
                    else:
                        point = win.getMouse()
                        xvalue = point.getX()
                        yvalue = point.getY()

            elif (xvalue <= 100 and xvalue >= 0) and (yvalue <= 800 and yvalue >= 700):
                win.close()

        car1.moveCar()
        car2.moveCar()
        car3.moveCar()
        car4.moveCar()
        car5.moveCar()
        car6.moveCar()

        boat1.moveBoat()
        boat2.moveBoat()

        if (car1.getX() >= 1600) or (car1.getX() <= -150):
            car1.reverseDirection()
            car1.changeColor()
            car1.changeSpeed()
        if (car2.getX() >= 1600) or (car2.getX() <= -150):
            car2.reverseDirection()
            car2.changeColor()
            car2.changeSpeed()
        if (car3.getX() >= 1600) or (car3.getX() <= -150):
            car3.reverseDirection()
            car3.changeColor()
            car3.changeSpeed()
        if (car4.getX() >= 1600) or (car4.getX() <= -150):
            car4.reverseDirection()
            car4.changeColor()
            car4.changeSpeed()
        if (car5.getX() >= 1600) or (car5.getX() <= -150):
            car5.reverseDirection()
            car5.changeColor()
            car5.changeSpeed()
        if (car6.getX() >= 1600) or (car6.getX() <= -150):
            car6.reverseDirection()
            car6.changeColor()
            car6.changeSpeed()

        if (boat1.getX() >= 1600) or (boat1.getX() <= -150):
            boat1.reverseDirection()
            boat1.changeColor()
            boat1.changeSpeed()
        if (boat2.getX() >= 1600) or (boat2.getX() <= -150):
            boat2.reverseDirection()
            boat2.changeSpeed()

        #changes sky color
        count = count + 1
        drawSky(int(count/3), int(count/8))

        #makes snow move
        if month == 'january' or month == 'february' or month == 'march' or month == 'december':
            moveSnow(snowflakes)
        if month == 'july' and int(day) == 4 and count % 60 == 0:
            firework = Firework(random.randint(0,1450),random.randint(700,800))
            listOfFireworks.append(firework)
            firework.makeFirework()

        update(100)

#draws sky
def drawSky(blue,green):
    greenvalue = 10 + green
    bluevalue = 10 + blue

    if greenvalue >= 255:
        greenvalue = 255
    if bluevalue >= 255:
        bluevalue = 255
    win.setBackground(color_rgb(0, greenvalue, bluevalue))

#makes road
def drawRoad():
    road = Rectangle(Point(0,150), Point(1450, 300))
    road.draw(win)
    road.setFill("black")

    for i in range(15):
        yellowline = Rectangle(Point((i * 100), 220), Point((50 + (i * 100)), 230))
        yellowline.draw(win)
        yellowline.setFill("yellow")
#makes river
def drawRiver():
    river = Rectangle(Point(0,0), Point(1450, 100))
    river.draw(win)
    river.setFill("blue")
#makes grass
def drawGrass():
    sidewalk = Rectangle(Point(0,100), Point(1450,150))
    sidewalk.draw(win)
    sidewalk.setFill("green")
#makes trees
def drawTrees(color = "darkolivegreen1"):
    for i in range(random.randint(0,60)):
        size = random.randint(0,3)
        tree = Tree(size)
        tree.makeTree(color)

#makes snow if called
def makeSnow():
    snowflakes = []
    for i in range(2000):
        snowflake = Point(random.randint(0,1450),random.randint(0, 3000))
        snowflake.setFill("white")
        snowflake.setOutline("white")
        snowflake.draw(win)
        snowflakes.append(snowflake)
    return snowflakes

#moves the snow down
def moveSnow(snowflakes):

    for flake in snowflakes:
        flake.move(0, -1 * random.randint(1,3))

    snowflake = Point(random.randint(0,1450),random.randint(100, 150))
    snowflake.setFill("white")
    snowflake.setOutline("white")
    snowflake.draw(win)

#the main function of the game
def main():
    while True:

        displayOpeningScreen()
        playerMonth = getMonth()
        playerDay = getDay(playerMonth)

        drawBackground()

        importBuildings()

        dateStuff = drawDateStuff(playerMonth, playerDay)

        animate(playerMonth, playerDay, dateStuff)

main()
