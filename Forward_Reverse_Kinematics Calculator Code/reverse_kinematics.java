import java.util.Scanner;
public class reverse_kinematics {
     public static void main(String[] args) {
          Scanner sc = new Scanner (System.in);
          System.out.println("Enter your A");
          double x = sc.nextDouble();
          System.out.println("Enter your B");
          double y = sc.nextDouble();
          System.out.println("Enter your C");
          double z = sc.nextDouble(); 
          
          double waist = 32,shoulder = 26, elbow = 20, wrist = 0;
          System.out.println();
          double d1 = Math.sqrt((Math.pow(x, 2) + Math.pow(y, 2))) - wrist;
          System.out.printf("d1=(%.4f)\n", d1);

          double th1 = Math.acos(x / (d1 + wrist));
          System.out.printf("θ1=(%.4f)\n", Math.toDegrees(th1));

          double d6 = Math.sqrt((Math.pow(d1, 2)) + (Math.pow((z - waist), 2)));
          System.out.printf("d6=(%.4f)\n", d6);

          double th7 = Math.acos(d1 / d6);
          System.out.printf("θ7=(%.4f)\n", Math.toDegrees(th7));

          double th3 = Math.acos(((Math.pow(shoulder, 2)) + (Math.pow(elbow, 2)) - (Math.pow(d6, 2))) / (2 * shoulder * elbow));
          System.out.printf("θ3=(%.4f)\n", Math.toDegrees(th3));

          double th6 = Math.asin((elbow * (Math.sin(th3))) / d6);
          System.out.printf("θ6=(%.4f)\n", Math.toDegrees(th6));

          double th2 = th6 + th7;
          System.out.printf("θ2=(%.4f)\n", Math.toDegrees(th2));
          System.out.printf("(waist,elbow,shoulder)=(%.4f,%.4f,%.4f)\n", Math.toDegrees(th1), Math.toDegrees(th3), Math.toDegrees(th2));
     }
}