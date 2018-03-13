f = open("input.txt","r")
lines = f.readlines()
i=0
k=0
j=0
args=[]
names=[]
definitions=[]
def getline():
	global i
	global k,j
	if expanding==True:
		j=j+1
		return definitions[k][j-1]
	else:
		if i>=len(lines):
			return None
		i=i+1
		return lines[i-1]
def processline(line):
	if line==None:
		return
	#print(line)
	line.strip()
	OPCODE=line[:line.find(' ')]
	if OPCODE=="MACDEF":
		define(line)
	elif OPCODE=="MCALL":
		expand(line)
	else:
		if "|=" in line:
			line=line[0:line.find("|=")]
			line.append('\n')
		i=0
		#for i in range(len(line)):
		while i<len(line):
			k=0
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
