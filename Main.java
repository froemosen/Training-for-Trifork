// Java Hello World
/* 
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
*/

// Java simple method with parameter
public class Main {
    public static String john(String name) {
        return name;
    }

    public static void main(String[] args) {
        String name = john("John");
        System.out.println(name);
    }
}