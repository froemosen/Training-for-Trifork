package turtletest_docker;

import java.util.Scanner;
import java.lang.Math;
import edu.princeton.cs.introcs.StdDraw;


public class Main {   
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("| MAIN MENU |");

        System.out.println("    '1': Regular polygon\n    '2': Circle\n    '3': Quit\n\nMake a choice: ");
        int choice = scanner.nextInt();
        
        
        

        if (choice == 1) {
            System.out.println("Number of sides (int):");
            int sideCount = Math.abs(scanner.nextInt());
            
            System.out.println("Length of sides (double):");
            double sideLength = Math.abs(scanner.nextDouble());

            RegularPolygon myFigure = new RegularPolygon(StdDraw.BLUE, 0.0002, sideCount, sideLength);
            
            myFigure.draw();
        }

        else if (choice == 2) {
            System.out.println("Input Radius (double from 0,0-0,5):");
            double radius = Math.abs(scanner.nextDouble());

            Circle myCircle = new Circle(StdDraw.RED, 0.0002, radius);

            myCircle.draw();
        }

        else if (choice == 3) {
            System.out.println("Quitting program...");
        }

        else {
            System.out.println("Wrong input - Try again!");
            main(null);
        }

    scanner.close();    
    }
}