package turtletest_docker;

import java.awt.Color;

abstract class Figure {
    protected Color penColor;
    protected double penRadius;
    protected Turtle pen;

    public Figure(Color inputPenColor, double inputPenRadius) {
        penColor = inputPenColor;
        penRadius = inputPenRadius;

        pen = new Turtle(0.5, 0.5, 0.0);
        System.out.println(pen);
        pen.setPenRadius(penRadius);
        pen.setCanvasSize(800, 800);
    }
}


