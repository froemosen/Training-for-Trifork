import math
import turtle

class Figure:
    def __init__(self, color, penSize, turtleSize, bgColor):
        self.pen = turtle.Turtle(shape = "turtle") #Turtle is defined
        self.pen.pencolor(color) #Color of pen/turtle
        self.pen.pensize(penSize) #Size of pen
        self.pen.turtlesize(turtleSize) #Side of turtle

        self.background = turtle.Screen() #Window is defines
        self.background.setup(800, 800) #Size of window
        self.background.bgcolor(bgColor) #Color of window

class RegularPolygon(Figure):
    def __init__(self, sides, sideLength, newPenColor, newPenSize, newTurtleSize, newBgColor):
        super().__init__(newPenColor, newPenSize, newTurtleSize, newBgColor)

        self.sides = sides #Number of sides
        self.sideLength = sideLength #Length of each side
        
        self.angle = ((self.sides-2)*180)/(self.sides) #sum of all angles, divided by number of sides. 
        
        if (self.sides % 2) == 0: #Check if number of sides is even or uneven
            #Even
            self.height = sideLength*(1+0.33*(self.sides-4)) #0.33 (0.66) is a constant describing the height in relation between height and number of sides (doesn't work perfectly)
        else:  

            #Uneven
            self.height = sideLength*(0.87+0.33*(self.sides-3)) #look at the excel-doc called "Højdeforhold i regulære polygoner.xlsx"

    def draw(self):
        lengthMultiplier = 600/self.height #limits height (and width) to about 600 pixels (size of window is 800)

        self.pen.penup()
        self.pen.setpos((-0.5*self.sideLength*lengthMultiplier), (-0.5*self.height*lengthMultiplier)) #Starting position is set (default is middle of screen)
        self.pen.pendown()

        for sides in range(self.sides):
            self.pen.forward(self.sideLength*lengthMultiplier) #Forward however long the sides should be
            self.pen.right(180 + self.angle) #Does the 180 for at little spin action. Same as doing 90-left(angle)

    def getValues(self):
        if self.sides >= 5:
            self.area = 0.25*self.sides*self.sideLength**2*(math.cos(self.angle))/(math.sin(self.angle))
        elif self.sides == 4:
            self.area = self.sideLength**2
        elif self.sides == 3:
            #regneregler.dk/vilkaarlig-trekant-ligesidet
            s = (self.sideLength*3)/2
            self.area = math.sqrt(s*(s-self.sideLength)*(s-self.sideLength)*(s-self.sideLength))
        else:
            self.area = 0

        self.circumference = self.sides*self.sideLength

        print(F"\nArea  =  {self.area}")
        print(F"Circumference  =  {self.circumference}\n")

class Circle(Figure):
    def __init__(self, radius, newPenColor, newPenSize, newTurtleSize, newBgColor):
        super().__init__(newPenColor, newPenSize, newTurtleSize, newBgColor)

        self.radius = radius

    def draw(self):
        self.pen.penup()
        self.pen.setpos(0, -300) #Starting position is set (default is middle of screen)
        self.pen.pendown()

        self.pen.circle(300) #Universal radius is drawn. Circle does not extend the screen this way

    def getValues(self):
        diameter = self.radius/2
        area = self.radius**2*math.pi
        circumference = diameter*math.pi

        print(F"\nRadius  =  {self.radius}")
        print(F"Diameter  =  {diameter}")
        print(F"Area  =  {area}")
        print(F"Circumference  =  {circumference}\n")

def settings():
    print("\nSETTINGS\n")
    #Colors: https://trinket.io/docs/colors
    newPenColor = input("Input New Pen Color: ") 
    newPenSize = int(input("Input New Pen Size: "))
    newTurtleSize = int(input("Input New Turtle Size: "))
    newBgColor = input("Input New Background Color: ")
    print("") #Layout
    settingsComplete = True
    return newPenColor, newPenSize, newTurtleSize, newBgColor, settingsComplete

def main(settingsComplete, *variables): #yes, i used an args. I'm sorry ;)
    print("MAIN MENU")
    choice = input("    '1': Regular polygon\n    '2': Circle\n    '3': Settings\n    '4': Quit\nMake a choice: ")

    if choice == "1": #Regular polygons
        sideCount = abs(int(input("\nNumber of sides (int): ")))
        sideLength = abs(float(input("Length of sides (float): ")))

        for i in range(int(len(variables)/4)):
            newPenColor, newPenSize, newTurtleSize, newBgColor = variables

        if settingsComplete:
            myFigure = RegularPolygon(sideCount, sideLength, newPenColor, newPenSize, newTurtleSize, newBgColor)
        else:
            myFigure = RegularPolygon(sideCount, sideLength, "white", 5, 2, "black")

        myFigure.draw()
        myFigure.getValues()

    elif choice == "2": #Circles
        radius = float(input("\nRadius of circle (float):"))
        
        if settingsComplete:
            myFigure = Circle(radius, newPenColor, newPenSize, newTurtleSize, newBgColor)
        else:
            myFigure = Circle(radius, "white", 5, 2, "black")
        
        myFigure.draw()
        myFigure.getValues()

    elif choice == "3": #Settings
        newPenColor, newPenSize, newTurtleSize, newBgColor, settingsComplete = settings()
        main(settingsComplete, newPenColor, newPenSize, newTurtleSize, newBgColor)
        
    elif choice == "4": #Exit
        pass

    else:
        print("\nForkert input - prøv igen\n\n")
        main(settingsComplete)    


if __name__ == '__main__':
    main(False)
    input("Press 'enter' to quit")
    

