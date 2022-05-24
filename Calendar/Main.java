import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	    ConsoleIpOp objCI=new ConsoleIpOp();
	    Date obj=new Date();
		while(true)
		{
			
		    int ch;
		    System.out.println("enter 1 to enter date ");
		    System.out.println("enter 2 to disp date");
		    System.out.println("enter 3 to add days");
		    System.out.println("enter 4 to add months");
		    System.out.println("enter 5 to add year");
		    System.out.println("enter 6 to exit");
		    System.out.println("enter your choice");
		    ch=objCI.getInt();
		    switch(ch)
		    {
		    case 1:
		    	obj.enterDate();
		    	break;
		    case 2:
		    	obj.dispDate();
		    	break;
		    case 3:
		    	obj.addDays();
		    	break;
		    case 4:
		    	obj.addMonths();
		    	break;
		    case 5:
		    	obj.addYear();
		    	break;
		    case 6:
		    	System.exit(0);
		    	break;
		    	default:
		    		System.out.println("pls enter val bw 1-6");
		    		
		    
		    }

		}
	}

}
