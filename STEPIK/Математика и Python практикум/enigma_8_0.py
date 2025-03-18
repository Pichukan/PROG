
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
				#print(reverse,'inside')
				if reverse:
					#print('index first rotor',ROTORS[first_rotor].index(i))
					b=(ROTORS[first_rotor]).index(i)+puksamuksa
					s=b
					#print('s+puksamuksa',ROTORS[first_rotor][s],s)
					k=0
					
					if s>25:
						#k=-1
						s=s%26
					elif s<0:
						#k=26
						#s=s+26
						s=s-(s//26+1)*26+26
					#b=((ROTORS[second_rotor]).index(i)+puksamuksa)//26+k
					b=s
					#print(ROTORS[first_rotor][b],b)
					r=ROTORS[first_rotor][b]
					b=(list(ROTORS[second_rotor])).index(r)
					c=ROTORS[first_rotor][b]
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
						#s=s+26
						s=s-(s//26+1)*26+26
					#b=((ROTORS[second_rotor]).index(i)+puksamuksa)//26+k
					b=s					
					
					c=ROTORS[second_rotor][b]				
					text_change=text_change+c
			return text_change				
			
		first_rotor=0
		second_rotor=n		
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
				
				s=b
				if s>25:					
					s=s%26
				elif s<0:					
					#s=s+26		#b=b-(b//26+1)*26+26
					s=s-(s//26+1)*26+26
				b=s								
				c=REFLECTORS[n][b]				
				text_change=text_change+c
			return text_change			
	
		text_change=change(symbol,n,puksamuksa)	
		return text_change			
	
	#----------------------------------------------------------
	def rotate_rotor(tumbajumba,shift):		
		
		ROTORS_ROTATE = {0: 0, 1: 17, 2: 5, 3: 22, 4: 10, 5: 0, 6: 0, 
						 7: 0, 8: 0, 'beta': 0, 'gamma': 0}			
		
		for i in reversed(range(2,len(tumbajumba))):
			#print(i,'i')
			#print(shift[i],'shift[i]',i)			
			if i==(len(tumbajumba)-1):
				shift[i]=shift[i]+1
				A=((shift[i]-shift[i]//26*26)%ROTORS_ROTATE[tumbajumba[i]] == 0) and		((shift[i]-shift[i]//26*26)//ROTORS_ROTATE[tumbajumba[i]] == 1)
				if A:
					shift[i-1]=shift[i-1]+1								
				#print('jjj')
				continue
			A=((shift[i+1]-shift[i+1]//26*26)%ROTORS_ROTATE[tumbajumba[i+1]] == 0) and		((shift[i+1]-shift[i+1]//26*26)//ROTORS_ROTATE[tumbajumba[i+1]] == 1)
			B=((shift[i]+1-shift[i]//26*26)%ROTORS_ROTATE[tumbajumba[i]] == 0) and		((shift[i]+1-shift[i]//26*26)//ROTORS_ROTATE[tumbajumba[i]] == 1)
			
			if B and (not A):
				shift[i]=shift[i]+1
				if B:
					shift[i-1]=shift[i-1]+1	
				continue			
			#print(i)
			#pass
			#shift=[0,-1,2,-1]
			#shift_rel(shift,len(tumbajumba))
		return shift
	
	#--------------------------------------------------------
	
	def shift_rel(shift,num):

		shift_ref=[]
		for i in range(num):
			shift_ref.append(0)

		shift_ref[num-1]=shift[num-1]
		#print(shift_ref,'1 stage')
		for i in reversed(range(1,num-1)):
			#print(i)
			shift_ref[i]=shift[i]-shift[i+1]
		shift_ref[0]=shift[1]*(-1)
		shift_ref.reverse()
		prom=[]
		for i in reversed(shift_ref):
			prom.append(i*(-1))
		shift_ref=shift_ref+prom
		#print(shift,'shift')
		#print(shift_ref,'shift_ref')
		return(shift_ref)	
	#-------------------------------------------------------------
			
	text=text.upper()	
	text=text.replace(' ','')
	tumbajumba=[ref,rot1,rot2,rot3]	
	len_tumba=len(tumbajumba)
	shift=[0,shift1,shift2,shift3]    #------
	text_out=''		
	
	for text_symbol in text:
		#n=0     #proba
		#n=rotate_rotor(tumbajumba,shift)  
		shift1=rotate_rotor(tumbajumba,shift)
		#shift1=[0, 4, 5, 10]
		#shift1=shift            #----------		
		puksamuksa=shift_rel(shift1,len_tumba)
		#puksamuksa=[2, 0, 0, 0, 0, 0, -2, 0]
		
		way_flag=False	
		k=0		
		for i in range(3,-4,-1):
			if i!=0:
				if i<0:
					way_flag=True
				#print(text_symbol,'before ',way_flag,puksamuksa[k],end='\n')
				text_symbol=rotor(text_symbol,tumbajumba[abs(i)],puksamuksa[k],way_flag)
				#print(text_symbol,'after ',way_flag,puksamuksa[k],end='\n')
			else:
				#print(text_symbol,'  before ref',end='\n')
				text_symbol=reflector(text_symbol,ref,puksamuksa[k])
				#print(text_symbol,'after ref',end='\n')
			k=k+1			
		#------------------------------------------------------------
		a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		b=a.index(text_symbol)+puksamuksa[7]
		#print(b,'b')		
		if b>25:
			#k=-1
			b=b%26
		elif b<0:
			#k=26
			b=b-(b//26+1)*26+26			
		text_symbol=a[b]
		#print(text_symbol)
		text_out=text_out+text_symbol	
	#-----------------------------------------------------------
	#print(n)    #proba	
	return text_out

text='AAAAA AAAAA'     #BGDMBTZ=AAAAAAA
ref=1                  #BGDMBTZUON=AAAAA AAAAA
rot1=2
shift1=3
rot2=2
shift2=3
rot3=2
shift3=3
#text=text.upper()
print(enigma(text,ref,rot1,shift1,rot2,shift2,rot3,shift3))