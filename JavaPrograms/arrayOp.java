import java.util.*;
class arrayOp{
    public static void main(String args[ ]){
        int i;
        int flag=0;
        int[ ] a = new int[5];
        System.out.println("Enter 5 numbers in the array");
        Scanner obj =new Scanner(System.in);
        for(i=0;i<5;i++)
        {   
            System.out.println("Enter the value for index "+i );
            a[i]= obj.nextInt();
        }
        System.out.println("Check for a number in the array Y/N?");
        char ch = obj.next().charAt(0);
        if(ch=='Y'|| ch=='y')
        {
            System.out.println("Enter the search element ");
            int se = obj.nextInt();
            for(i=0;i<5;i++) {
                if(se==a[i])
                {flag=1;
                System.out.println("The element is present at the position number "+i+" in the array set");
                }
              }
              if(flag ==0)
              System.out.println("The Element is not present in the array");
        }
        else
        {System.out.println("Well, Okay. Thanks for testing out this program");}
        
    }
}  
    