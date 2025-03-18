def enigma(text,ref,rot1,shift1,rot2,shift2,rot3,shift3):
		
	def rotor(symbol, n, puksamuksa, reverse=False):
		ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
				  1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
				  2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
				  3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
				  4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
				  5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
				  6: 'JPGVOUMFYQBENHZRDKASXLICTW',
				  7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT', 
				  8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
				  'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
				  'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
				  }	
		symbol=symbol.replace(' ','')
		def change(symbol,first_rotor,second_rotor,puksamuksa):
			
			text_change=''
			for i in symbol:
				r=i
				if reverse:
					s=(ROTORS[second_rotor]).index(i)+puksamuksa
					#print('s',s)
					k=0
					if s>25:
						#k=-1
						s=s%26
					elif s<0:
						#k=26
						s=s+26
					#b=((ROTORS[second_rotor]).index(i)+puksamuksa)//26+k
					b=s
					#print(ROTORS[second_rotor][b],b)
					r=ROTORS[second_rotor][b]
					b=(list(ROTORS[first_rotor])).index(r)
					c=ROTORS[second_rotor][b]
					text_change=text_change+c
				else:
					
					b=(list(ROTORS[first_rotor])).index(r)
					b=b+puksamuksa
					#print('b',b)
					s=b
					if s>25:
						#k=-1
						s=s%26
					elif s<0:
						#k=26
						s=s+26
					#b=((ROTORS[second_rotor]).index(i)+puksamuksa)//26+k
					b=s					
					
					c=ROTORS[second_rotor][b]				
					text_change=text_change+c
			return text_change				
			
		first_rotor=0
		second_rotor=n
		if reverse:
			first_rotor=n
			second_rotor=0
		
		text_change=change(symbol,first_rotor,second_rotor,puksamuksa)	
		
		return text_change
	
	def reflector(symbol,n,puksamuksa):
		REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',					  
					  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
					  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
					  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
					  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
					  }
		
		def change(symbol,reflector,puksamuksa):			
			symbol=symbol.replace(' ','')
			text_change=''
			for i in symbol:
				b=(list(REFLECTORS[0])).index(i)
				b=b+puksamuksa
				c=REFLECTORS[n][b]				
				text_change=text_change+c
			return text_change			
	
		text_change=change(symbol,n,puksamuksa)	
		return text_change		

	rel_shift3=shift3
	rel_shift2=shift2-shift3
	rel_shift1=shift1-shift2
	#rel_shift1=shift1-rel_shift2    	
	shift_ref=shift1*(-1)
	puksamuksa=[rel_shift3,rel_shift2,rel_shift1,shift_ref]
	#print(puksamuksa,'1')
	prom=[]
	for i in reversed(puksamuksa):
		#print('2')
		#print(i)
		#prom.append(puksamuksa[i]*(-1))
		prom.append(i*(-1))
	#print(prom)
	puksamuksa=puksamuksa+prom
	#puksamuksa=[-1,3,-3,0,0,-3,3,-1]
	#print(puksamuksa)
	
	text=text.upper()
	tumbajumba=[ref,rot1,rot2,rot3]	
	way_flag=False
	
	k=0
	for i in range(3,-4,-1):
		if i!=0:
			if i<0:
				way_flag=True
			text=rotor(text,tumbajumba[abs(i)],puksamuksa[k],way_flag)		
		else:
			text=reflector(text,ref,puksamuksa[k])
		k=k+1
		
	t=''	
	for i in text:		
		a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		b=a.index(i)+puksamuksa[7]
		#print(b)
		s=b
		if s>25:
			#k=-1
			s=s%26
		elif s<0:
			#k=26
			s=s+26
		b=s
		t=t+a[b]	
	text=t				
	return text

text='AYIQQLXZMFHQUHQCH'
ref=1
rot1=1
shift1=-1
rot2=2
shift2=2
rot3=3
shift3=-1
#text=text.upper()
print(enigma(text,ref,rot1,shift1,rot2,shift2,rot3,shift3))
