#from goto import goto,label
print("Lossy OR Lossless Finder")
a=input("Enter the relation :- ")
R=[]
c=0
for i in range(0,len(a)):
	if(a[i]!=" "):
		o=0
		for j in R:
			o=o+1
			if(a[i]==j):
				print("You cant Repeat a Letter")
				c=c+1
				break
		if(o==len(R)):
			R.append(a[i])
if(c==0):
	print(R)
n=int(input("Enter the Number of Decomposed Relation :- "))
rel=[]
i=0
while(i<n):
	print(i+1,"th")
	a=input("\tEnter R :- ")
	for j in range(0,len(a)):
		p=0
		#print(j,a[j])
		for k in range(0,len(R)):
			#print(k,R[k])
			if(a[j]==R[k]):
				p=p+1
				break

		if(p==0):
			i=i-1
			print("Not in Parent Relation \nRe-Enter")
			rel.pop()
			break
	rel.append(a)
	i=i+1
print(rel,R)