import java.util.*;
class arrayOp{
    public static void main(String args[]){
        int i;
        int flag=0;
        int[] a = new int[1000];
        System.out.print("How numbers in the array");
        Scanner obj =new Scanner(System.in);
        int n= obj.nextInt();
        for(i=0;i<n;i++)
        {   
            System.out.print("Enter the value for index "+i+ "=" );
            a[i]= obj.nextInt();
        }
        System.out.print("Check for a number in the array Y/N? ");
        char ch = obj.next().charAt(0);
        if(ch=='Y'|| ch=='y')
        {
            System.out.print("Enter the search element ");
            int se = obj.nextInt();
            for(i=0;i<n;i++) {
                if(se==a[i])
                {flag=1;
                System.out.println("The element is present at the position number "+ ++i+" in the array set");
                }
              }
              if(flag ==0)
              System.out.println("The Element is not present in the array");
        }
        else if(ch=='N'|| ch=='n')
        System.out.println("Well, Okay. Thanks for testing out this program");
        else
        System.out.println("Wrong Entry,anyways thanks for testing out the code.");
    }
}  
    