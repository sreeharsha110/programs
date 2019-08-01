def subsets(s):
	n=len(s)
	for i in range(2**n):
		t=i
		count=0
		temp=""
		while(t>0):
			if(t&1):
				temp+=s[count]
			t//=2
			count+=1
		print(temp)


s=input("enter a string")
subsets(s)