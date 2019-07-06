string = 'A*-B-***C-*-*D-**E*F**-*G--*H****I**J*---K-*-L*-**M--N-*O---P*--*Q--*-R*-*S***T-U**-V***-W*--X-**-Y-*--Z--**'
i=0
for x in string:
	if (ord(x)>65)&(ord(x)<90):
		str1 = ''
		for j in range(1,6):
			if (ord(string[i+j])>65)&(ord(string[i+j])<90):
				break
			elif string[i+j] =='*':
				str1+='morse.dot();'
			else:
				str1+='morse.dash();'
		print("        case '{}':{}break;".format(x.lower(),str1))
	i=i+1