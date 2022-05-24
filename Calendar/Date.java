import java.util.Scanner;
public class Date {

	int mm,dd,yy;
	int arrDaysInMonths[]=new int[12];
	ConsoleIpOp objCI=new ConsoleIpOp();
	public void initDaysInMonths()
	{
		arrDaysInMonths[0]=31;//jan
		//arrDaysInMonths[1]=31;
		arrDaysInMonths[2]=31;//mar
		arrDaysInMonths[3]=30;
		arrDaysInMonths[4]=31;
		arrDaysInMonths[5]=30;
		arrDaysInMonths[6]=31;
		arrDaysInMonths[7]=31;//aug
		arrDaysInMonths[8]=30;
		arrDaysInMonths[9]=31;
		arrDaysInMonths[10]=30;
		arrDaysInMonths[11]=31;
		if(yy%4==0)
		{
			arrDaysInMonths[1]=29;
		}
		else
		{
			arrDaysInMonths[1]=28;
		}
		
		
	}
	public int getDaysInMonth(int m)
	{
		return arrDaysInMonths[m-1];
	}
	public void enterDate()
	{
		setYY();
		initDaysInMonths();
		setMM();
		setDD();
	}
	public void setDD()
	{
		int d;
		System.out.println("enter days");
		d=objCI.getInt();
		//
		//boolean res=isValidDays(d);
		//if(res)
		if(isValidDays(d))
		{
			dd=d;
		}
		else
		{
			System.out.println("please enter valid days");
			setDD();
		}
		
	}
	public void setMM()
	{
		int m;
		System.out.println("enter months");
		m=objCI.getInt();
		if(isValidMonths(m))
		{
			mm=m;
		}
		else
		{
			System.out.println("pls enter valid months");
			setMM();
		}
		
	}
	public void setYY()
	{
		int y;
		System.out.println("enter year");
		y=objCI.getInt();
		if(isValidYear(y))
		{
			yy=y;
		}
		else
		{
			System.out.println("pls enter valid year");
			setYY();
		}
	}
	public boolean isValidYear(int y)
	{
		if(y>=1600 && y<=9999)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	public boolean isValidMonths(int m)
	{
		if(m>=1 && m<=12)
		{
			return true;
		}
		else
		{
			return false;//invalid months
		}
	}
	public boolean isValidDays(int d)
	{
		if(d>=1 && d<=getDaysInMonth(mm))
		{
			return true;//valid days
		}
		else
		{
			return false;//invalid days
		}
	}
	
	public void dispDate()
	{
		System.out.println(dd+ " "+mm +" "+yy);
	}
	public void addDays()
	{
		int d;
		System.out.println("enter days you want to add");
		d=objCI.getInt();
		dd=dd+d;
		while(dd>=getDaysInMonth(mm))
		{
			dd=dd-getDaysInMonth(mm);
			mm++;
			if(mm>12)
			{
				mm=mm-12;
				yy++;
				initDaysInMonths();
			}
		}
		
	}
	public void addMonths()
	{
		int m;
		System.out.println("enter months you want to add");
		m=objCI.getInt();
		mm=mm+m;
		while(mm>12)
		{
			mm=mm-12;
			yy++;
		}
	}
	public void addYear()
	{
		int y;
		System.out.println("enter years you want to add");
		y=objCI.getInt();
		yy += y;
	}
}
