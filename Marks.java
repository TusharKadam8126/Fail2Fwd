import java.util.Scanner;
public class Marks
    {
        public static void main(String[] args) 
        {
            Scanner myobj = new  Scanner(System.in);
            System.out.println("ENTER YOUR MARKS :");
            int marks = myobj.nextInt();

                if (marks > 36)
            {
                System.out.println("YOU ARE PASSED.");
            }
                else
            {
                System.out.println("YOU ARE FAILED.");
            }
        myobj.close();
        }
    }        
        
    