from math import sqrt,floor
n_k=list(map(int,input().split()))

n=n_k[0]
k=n_k[1]



if((240-k)>= 2.5*((n*n)+n)):
	print(n)
else:
	print(floor((sqrt(9625- 40*k)-5)/10))
