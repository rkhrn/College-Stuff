package JavaPrograms;
import java.util.*;
import java.util.Arrays; 
class SortArray{
    public static void main(String args[]){
        int[] ArrayOfNumbers= new int[ ]{ 70, 65, 2, 36, 35, 55, 0, 89, 67, 33 };
        Arrays.sort(ArrayOfNumbers); 
        System.out.printf("The sorted array is : %s", Arrays.toString(ArrayOfNumbers));
        }
}  