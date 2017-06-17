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

int sum_A=0;
int sum_B=0;


int * cluster_min[2];
// cluster_min= new int*[2];
for(int i=0;i<2;i++)
{
cluster_min[i]= new int[N];

}

for(int i=0;i<N;i++)
{
	int min_A=A-S[i];
	int min_B=B-S[i];
   
   if(min_A<0)
	min_A*=-1;
   
cluster_min[0][i]=min_A;
sum_A = sum_A + min_A;

if(min_B<0)
	min_B*=-1;
   
cluster_min[1][i]=min_B;
sum_B = sum_B + min_B;

}

// for(int i=0;i<2;i++)
// {
// 	for(int j=0;j<N;j++)
// 	{
// 		cout<<cluster_min[i][j];
// 	}
// 	cout<<endl;
// }
printf("%d",sum_A);
printf("%d\n",sum_B);


 }











	return 0;
}