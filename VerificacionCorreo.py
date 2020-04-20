c=0
v=False


mail=input("Inserte su email de gmail: ")
for i in range(len(mail)):
	if mail[i]=="@":
		c=c+1
		if (mail[i+1]=="g" and mail[i+2]=="m"and mail[i+3]=="a" and mail[i+4]=="i" and mail[i+5]=="l" and mail[i+6]=="." and mail[i+7]=="c" and mail[i+8]=="o"and mail[i+9]=="m"):
			v=True

if c==1 and v==True:
	print("Email correcto")
else:
	print("Email incorrecto")	
print(c)