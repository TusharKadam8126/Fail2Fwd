import java.util.Scanner;
public class Calculator
{
    public static void main(String[] args)
    {
        Scanner myobj = new Scanner(System.in);
        System.out.println("Enter num1 :");
        int num1 = myobj.nextInt();
        System.out.println("Enter num2 :");
        int num2 = myobj.nextInt();
        System.out.println("Enter operator(+,-,*,/)");
        char operator = myobj.next().charAt(0);
        
        switch(operator)
        {
            case '+' :
            System.out.println("Addition is :" + (num1 + num2));
            break;
            case '-' :
            System.out.println("Subtraction is :" + (num1 -num2));
            break;
            case '*' :
            System.out.println("Multiplication is :" + (num1 * num2));
            break;
            case '/' :
            System.out.println("Division is :" + (num1/num2));
            break;
        }
        myobj.close();
    }
}
