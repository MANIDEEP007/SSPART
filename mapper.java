import java.util.*;
class Sample
{
  public String a,b,c,d,e;
}
public class mapper {
  public static void main(String[] args) {
    Map mapper = new HashMap();
    Sample arr[] = new Sample[5];
    Scanner s = new Scanner(System.in);
    for(int i=0;i<5;i++)
    {
      arr[i] = new Sample();
      System.out.println("Give Values for a,b,c,d,e for Sample["+(i+1)+"]");
      arr[i].a = s.nextLine();
      arr[i].b = s.nextLine();
      arr[i].c = s.nextLine();
      arr[i].d = s.nextLine();
      arr[i].e = s.nextLine();
    }
    for(int i=0;i<5;i++)
    {
      mapper.put( Integer.toString(i), arr[i]);
    }
    System.out.println("Enter Search String");
    String search = s.nextLine();
    System.out.println("The Keys are");
    Set set=mapper.entrySet();
    Iterator it=set.iterator();
    while(it.hasNext()){  
      Map.Entry entry_obj=(Map.Entry)it.next();  
      String key = (String)entry_obj.getKey();
      Sample value = (Sample)entry_obj.getValue();
      if(value.c.compareTo(search) == 0)
      {
        System.out.println(key);
      } 
    }  
  }
}
