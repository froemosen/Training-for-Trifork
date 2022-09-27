package turtletest_docker;

import java.awt.Color;
import edu.princeton.cs.introcs.StdDraw;

class Circle extends Figure {
    protected double radius; 
    double precision = 200;

    double doublePauseTime = 2000/precision;
    int pauseTime = (int) doublePauseTime;

    public Circle(Color penColor, double penRadius, double inputRadius) {
        super(penColor, penRadius);
    
        radius = inputRadius;
    }

    public void draw() {
        //Set position
        pen.setPenColor(StdDraw.WHITE);
        pen.turnLeft(135);
        pen.goForward(radius);
        pen.turnLeft(90);
        pen.setPenColor(penColor);
        

        //Draw circle
        for (int i = 0; i < precision; i++){
            pen.goForward(2*radius*3.1415/precision);
            pen.turnLeft(360/precision);
            pen.pause(pauseTime);
            }
        }
    }

