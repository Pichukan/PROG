
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
	
	#---------------------------------------------------------------
	
	
	
	#----------------------------------------------------------
	def rotate_rotor(tumbajumba,shift):		
		
		ROTORS_ROTATE = {0: 0, 1: 17, 2: 5, 3: 22, 4: 10, 5: 0, 6: 0, 
						 7: 0, 8: 0, 'beta': 0, 'gamma': 0}	
		#{0: 0, 1: 17, 2: 5, 3: 22, 4: 10, 5: 0, 6: 0, 
						 	
		#k=k+1
		#puksamuksa_bias=puksamuksa.copy()
		#print(puksamuksa)		
		#shift_ref=[]
		
		for i in reversed(range(2,len(tumbajumba))):
			#print(i)
			#print(shift[i],'shift[i]',i)
			if i==(len(tumbajumba)-1):
				shift[i]=shift[i]+1
				#print('jjj')
				continue
			
			if (shift[i]+1)%ROTORS_ROTATE[tumbajumba[i]] == 0:
				shift[i]=shift[i]+1
				shift[i-1]=shift[i-1]+1
			
			if shift[i+1]%ROTORS_ROTATE[tumbajumba[i+1]] == 0:
				shift[i]=shift[i]+1
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
		print(shift,'shift')
		print(shift_ref,'shift_ref')
		return(shift_ref)
	
	#-------------------------------------------------------------
	'''
	rel_shift3=shift3
	rel_shift2=shift2-rel_shift3
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
	print(puksamuksa,'puksamuksa')	
	shift=[0,-1,2,-1]
	tumbajumba=[ref,rot1,rot2,rot3]
	shift_rel(shift,len(tumbajumba))	
	'''
	#-------------------------------------------------------------
	'''
	shift0=0
	shift=[0,0,0,0] #shift=[shift0,shift1,shift2,shift3]
	#shift_rel=[]
	text=text.upper()	
	tumbajumba=[ref,rot1,rot2,rot3]		
	text_out=''	
	n=0	
	print(rotate_rotor(tumbajumba,shift),'rotate rotor func',puksamuksa)
	'''
	'''
	for i in range(100):
		print(rotate_rotor(tumbajumba,shift),'rotate rotor func')
	'''
	#--------------------------------------------------------------
	
		
	text=text.upper()	
	text=text.replace(' ','')
	tumbajumba=[ref,rot1,rot2,rot3]	
	len_tumba=len(tumbajumba)
	shift=[0,shift1,shift2,shift3]
	text_out=''		
	
	for text_symbol in text:
		#n=0     #proba
		#n=rotate_rotor(tumbajumba,shift)         

		shift1=rotate_rotor(tumbajumba,shift)
		#shift1=[0, 4, 6, 10]
		
		puksamuksa=shift_rel(shift1,len_tumba)
		#puksamuksa=[10, -4, -2, -4, 4, 2, 4, -10]
		
		way_flag=False	
		k=0		
		for i in range(3,-4,-1):
			if i!=0:
				if i<0:
					way_flag=True
				text_symbol=rotor(text_symbol,tumbajumba[abs(i)],puksamuksa[k],way_flag)	
			else:
				text_symbol=reflector(text_symbol,ref,puksamuksa[k])
			k=k+1
			
			#n=rotate_rotor(puksamuksa,tumbajumba,n)
			
		#------------------------------------------------------------
								
		a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		b=a.index(text_symbol)+puksamuksa[7]
		#print(b)		
		if b>25:
			#k=-1
			b=b%26
		elif b<0:
			#k=26
			b=b+26				
		text_symbol=a[b]
		print(text_symbol)
		text_out=text_out+text_symbol
	
	#-----------------------------------------------------------
	#print(n)    #proba
	return text_out

text='AAAAAAA'     #BGDMBTZ=AAAAAAA
ref=1                  #BGDMBTZUONCIZMORCPNVLGOVLMURTNZNDROPETXLPL
rot1=2
shift1=3
rot2=2
shift2=3
rot3=2  
shift3=3
#text=text.upper()
print(enigma(text,ref,rot1,shift1,rot2,shift2,rot3,shift3))