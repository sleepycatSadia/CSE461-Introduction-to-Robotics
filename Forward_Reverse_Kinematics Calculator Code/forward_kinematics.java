import java.util.Scanner;
public class forward_kinematics {
     public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
          // put your  Theta of arms: th1*10=waist,th2*10=shoulder,th3*10=elbow
          System.out.println("Enter your waist in degree");
          double th1 = sc.nextDouble();
          System.out.println("Enter your Shoulder in degree");
          double th2 = sc.nextDouble();
          System.out.println("Enter your elbow in degree");
          double th3 = sc.nextDouble();
         
          double waist = 32,shoulder = 26, elbow = 20, wrist = 0;

          double thx = 180 - 90 - th2;
          System.out.printf("θx=180-90-θ2=(%.4f)\n", thx);
          double thy = th3 - thx;
          System.out.printf("θy=θ3-θx=(%.4f)\n", thy);
          double d3 = shoulder * (Math.sin(Math.toRadians(th2)));
          System.out.printf("d3=L1.sinθ2=(%.4f)\n", d3);
          double d4 = shoulder * (Math.cos(Math.toRadians(th2)));
          System.out.printf("d4=L1.cosθ2=(%.4f)\n", d4);
          double d5 = elbow * (Math.sin(Math.toRadians(thy)));
          System.out.printf("d5=L2.sinθy=(%.4f)\n", d5);
          double d6 = elbow * (Math.cos(Math.toRadians(thy)));
          System.out.printf("d6=L2.cosθy=(%.4f)\n", d6);
          double z = waist + d3 - d6;
          System.out.printf("z=d2+d3-d6=(%.4f)\n", z);
          double d1 = d4 + d5;
          System.out.printf("d1=d4+d5=(%.4f)\n", d1);
          double x = (d1 + wrist) * (Math.cos(Math.toRadians(th1)));
          System.out.printf("x=d1.cosθ1=(%.4f)\n", x);
          double y = (d1 + wrist) * (Math.sin(Math.toRadians(th1)));
          System.out.printf("y=d1.sinθ1=(%.4f)\n", y);
          System.out.printf("(x,y,z)=(%.4f,%.4f,%.4f)\n", x, y, z);
     }
}