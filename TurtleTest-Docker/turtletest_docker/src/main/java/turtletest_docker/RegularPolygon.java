package turtletest_docker;

import java.awt.Color;
import edu.princeton.cs.introcs.StdDraw;

class RegularPolygon extends Figure {
    //Variables for the entire class
    int sides;
    double sideLength;
    double angle;
    double height;


    
    public RegularPolygon(Color penColor, double penRadius, int inputSides, double inputSideLength) {
        super(penColor, penRadius);
        //pen = super.pen;
        sides = inputSides;
        sideLength = inputSideLength;

        pen.setPenRadius(penRadius); //test

        angle = 180+((sides-2)*180)/(sides);

        if (sides % 2 == 0) {
            //Even amount of sides
            height = sideLength*(1+0.33*(sides-4));
        }
        else {
            //Uneven amount of sides
            height = sideLength*(0.87+0.33*(sides-3));
        }
    }

    public void draw() {
        double lengthMultiplier = 600/height; //limits height (and width) to about 600 pixels (size of window is 800)
        //In original program, the circumference and area of the polygon was calculated.
        //This is not the case here. Therefore sideLenght doesn't really matter.

        //Set position
        pen.setPenColor(StdDraw.WHITE);
        pen.turnLeft(90);
        pen.goForward((0.5*height*lengthMultiplier)/800);
        pen.turnLeft(90);
        pen.goForward((0.5*sideLength*lengthMultiplier)/800);
        pen.turnLeft(180);
        pen.setPenColor(penColor);

        //Draw
        for (int i = 0; i < sides; i++) {
            pen.goForward((sideLength*lengthMultiplier)/800);
            pen.turnLeft(angle);
        }
    }
}