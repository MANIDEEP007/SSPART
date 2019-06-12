import java.util.*;
public class Main {
  public static void search(String str_arr[],String ser_str)
  {
    int mid;
    int low = 0, high = str_arr.length-1;
    while(low<=high)
    {
      mid = (low+high)/2;
      int status = ser_str.compareTo(str_arr[mid]);
      if(status == 0)
      {
        System.out.println("String found at "+mid+" index");
        return;
      }
      if(status > 0)
      {
        low = mid +1;
      }
      else
      {
        high = mid -1;
      }
    }
    System.out.println("Not Found");
  }
  public static void main(String[] args) {
    String str_arr[] = {"apple","banana","citrus","orange","peach","pear"};//Sample Array
    Scanner s= new Scanner(System.in);
    String ser_str = s.nextLine();
    search(str_arr,ser_str);
  }
}
