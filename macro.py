# open input file
f = open("input.txt","r")
lines = f.readlines()
i=0
k=0
j=0
elseFlag=0
ifCond=0
ifFlag=0
args=[]
names=[]
definitions=[]
def getline():
	global i
	global k,j
	if expanding==True:
		j=j+1
		# return corresponding line from deftab
		return definitions[k][j-1]
	else:
		if i>=len(lines):
			return None
		i=i+1
		return lines[i-1]
def processline(line):
	global ifFlag
	global elseFlag
	global ifCond
	if line==None:
		return
	#print(line)
	line.strip()
	if ' ' in line:
		OPCODE=line[:line.find(' ')]
	else:
		OPCODE=line[:-1]
	# check for a macro definition
	if OPCODE=="MACDEF":
		define(line)
	elif OPCODE=="MSDEF":
		# add single line definitions
		name=[]
		line=line[line.find(' ')+1:]
		name.append(line[:line.find(' ')])
		name.append(0)
		name.append(None)
		names.append(name)
		line=line[line.find(' ')+1:]
		definition=[]
		definition.append(line.strip()+'\n')
		definitions.append(definition)
	# expand macro call
	elif OPCODE=="MCALL":
		expand(line)
	elif OPCODE=="_IF":
		if "|=" in line:
				line=line[0:line.find("|=")]
				line=line+'\n'
		ifFlag=1
		line=line[line.find(' ')+1:].strip()
		line=line[1:-1]
		elements=line.split(' ')
		# check the if condition
		if elements[1]=='EQ':
			if elements[0].startswith('#')==True:
				elements[0]=elements[0][1:]
				elements[0]=args[int(elements[0])-1]
			if elements[2].startswith('#')==True:
				elements[2]=elements[2][1:]
				elements[2]=args[int(elements[2])-1]	
			if elements[0]==elements[2]:
				ifCond=1
	elif OPCODE=="_ELSE":
		ifFlag=0
		elseFlag=1
	elif OPCODE=="_ENDIF":
		ifCond=0
		elseFlag=0
	else:
		if (elseFlag==1 and ifCond==0) or (ifFlag==0 and elseFlag==0) or (ifCond==1 and ifFlag==1):
			# comment removal
			if "|=" in line:
				line=line[0:line.find("|=")]
				line=line+'\n'
			i=0
			#for i in range(len(line)):
			while i<len(line):
				k=0
				# parameter substitution
				if line[i]=='#':
					i=i+1
					j=0
					k=i
					while(line[k]>='0' and line[k]<='9'):
						j=j*10+(int(line[k])-int('0'))
						k=k+1
						#print(j)
					print(args[j-1],end='')
					i=k
					print(line[i],end='')
				else:
					print(line[i],end='')
				i=i+1
			#print(line,end='')
def define(line):
	line=line[line.find(' ')+1:]
	line=line.strip()
	name=[]
	# add macro name to nametab
	if ' ' in line:
		name.append(line[0:line.find(' ')])
		line=line[line.find(' ')+1:]
		line=line.strip()
		line=line[1:-1]
		params=line.split(',')
		for i in range(len(params)):
			params[i]=params[i].strip()
		name.append(len(params))
		name.append(params)
	else:
		name.append(line)
		name.append(0)
		name.append(None)
	names.append(name)
	#print(name)
	# levels for nested definitions
	level=1
	definition=[]
	while level>0:
		line=getline()
		if "|=" in line:
			line=line[0:line.find("|=")]
			line.append('\n')
		OPCODE=line[:line.find(' ')]
		if OPCODE == "MACDEF":
			level=level+1
		elif OPCODE == "DEFEND":
			level=level-1
		if level==0:
			definitions.append(definition)
			break;
		definition.append(line)
	# print(definition)
def expand(line):
	global expanding
	global k
	global j
	expanding=True
	line=line[line.find(' ')+1:]
	k=0
	if ' ' in line:
		for k in range(len(names)):
			if names[k][0]==line[0:line.find(' ')]:
				break;
		line=line[line.find(' ')+1:]
		line=line.strip()
		line=line[1:-1]
		params=line.split(',')
		#print(params)
		for i in range(len(args)):
			args.pop()
		# load arguments into argtab
		for i in range(len(params)):
			params[i]=params[i].strip()
			if(params[i]==''):
				args.append(names[k][2][i])
			else:
				args.append(params[i])
		#print(params)
	else:
		for k in range(len(names)):
			if names[k][0]==line[0:-1]:
				break;
	j=0
	while(j<len(definitions[k])):
		line=getline()
		processline(line)
	expanding=False

expanding=False
while i<len(lines):
	line=getline()
	processline(line)
#print(names)
#print(definitions)
#print(names, definitions)
