import java.util.*;
public class SumOfDigits {
    public static void main(String[] args) {
        Scanner obj =new Scanner(System.in);
        int a= obj.nextInt();
        int temp,b,sum=0;
        temp=a;
        while(temp>0)
        {
            b=temp%10;
            sum=sum+b;
            temp=temp/10;
        } 
        System.out.println(+sum);
        }
}
