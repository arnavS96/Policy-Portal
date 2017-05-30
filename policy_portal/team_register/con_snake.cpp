#include<stdio.h>
#include "iostream"
#include "/usr/local/include/bits/stdc++.h"
// #include <bits/stdc++.h>
using namespace std;


int main()
{


 int T, N,L,A,B;
 scanf("%d",&T);
 scanf("%d",&N);
 scanf("%d",&L);
 scanf("%d",&A);
 scanf("%d",&B);
for(int t=0;t<T;t++)
{
int * S;
S= new int[N];

for(int i=0;i<N;i++)
	scanf("%d",&S[i]);

int ** cluster_min;
cluster_min= new int*[2];
for(int i=0;i<2;i++)
{
cluster_min[i]= new int[N];

}

for(int i=0;i<N;i++)
{
	int min_A=0;
	int min_B=0;
   
   if(A-S[i]>=0)
	min_A=A-S[i];
   else
	min_A=-1*(A-S[i]);
cluster_min[0][i]=A-S[i];

if(B-S[i]>=0)
	min_B=B-S[i];
   else
	min_B=-1*(B-S[i]);

cluster_min[1][i]=B-S[i];

}

for(int i=0;i<N;i++)
{
	for(int j=0;j<2;j++)
	{
		cout<<cluster_min[i][j];
	}
	cout<<endl;
}


}











	return 0;
}