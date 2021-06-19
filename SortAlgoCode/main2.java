import java.util.*;
import java.lang.*;

class Rextester
{  
    
// Driver Code
public static void main(String[] args)
{
    Random random = new Random();

    int[] arr = random.ints(10000, 1,1000).toArray();
    //int[] arr = { 10, 7, 8, 9, 1, 5 };
     
    Arrays.sort(arr);
    //System.out.println("Sorted array: ");

}

}