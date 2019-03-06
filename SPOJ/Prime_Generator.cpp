// Problem link -     https://www.spoj.com/problems/PRIME1/

#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t, m, n, count;
	cin>>t;
	while(t>0)
	{
		cin>>m>>n;
		
		for (int i = m; i<=n; i++)
		{
			count = 0;
			int x=2;
			while(x*x<=i)
			{
				if(i%x == 0)
				{
					count++;
					if (count>0)
					{
						break;
					}
				}
				x++;
			}
			if (count==0 && i>1)
			{
				cout<<i<<endl;
			}
		}
		cout<<endl;
		t--;
	}
	return 0;
}
