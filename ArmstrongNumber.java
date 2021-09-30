package pattern;

import java.util.Scanner;
import java.lang.Math;
public class ArmstrongNumber {
	static int Armstrong(int num)
	{
		String s=String.valueOf(num);
		int n = s.length();
		int x=0;
		while(num>0)
		{
			int temp = num%10;
			x+=(int)Math.pow(temp, n);
			num=num/10;
		}
			
		return x;
	}

	public static void main(String[] args) {
		Scanner sc  = new Scanner(System.in);
		int n1 = sc.nextInt();
		int n2 = sc.nextInt();
		//int f=0;
		int x=0;
		for(int i=n1;i<=n2;i++)
		{
			x = Armstrong(i);
			if(x==i)
			{
				System.out.println(x);
			}
		}
		/*if(f==1)
		{
			System.out.println(x);
		}
		else
		{
			System.out.println("0");
		}*/
		sc.close();
	}

}
