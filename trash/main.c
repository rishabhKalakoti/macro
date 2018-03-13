#include<stdio.h>
#include<stdlib.h>
#include<string.h>
// function prototypes
char* getLine(FILE* f);
void define();
void processline();
void expand();
// variables
int expanding=0;
int lineNo=0;
// functions
char* getLine(FILE* f)
{
	printf("line %d\n",lineNo);
	lineNo++;
	char* line;
	line=(char*)malloc(1000*sizeof(char));
	if(expanding==0)
	{
		if(fgets(line, sizeof(line), (FILE*)f)!=NULL)
		{
			//printf("%s",line);
			return line;
		}
		else
			return NULL;
	}
	else
	{
		// get next line from DEFTAB
		// substitute if arguments
		return NULL;
	}
}

void define()
{

}
void processLine(char* line)
{
	// comment
	// '|= this is a macro comment'
	int i;
	int l=strlen(line);
	printf("x%dx",l);
	for(i=0; i<l-1;i++)
	{
		if(line[i]=='|' && line[i+1]=='=')
		{
			line[i]='\0';
			break;
		}
	}
	l=strlen(line);
	// strip space from left
	while(line[0]==' ')
		for(i=0;i<l;i++)
			line[i]=line[i+1];
	// search OPCODE
	char OPCODE[100];
	i=0;
	while(i<l && ((line[i]>='A' && line[i]<='Z')
	  || (line[i]>='a' && line[i]<='z')
	  || (line[i]>='0' && line[i]<='9')
	  || line[i]=='_'))
	{
		OPCODE[i]=line[i];
		i++;
	}
	OPCODE[i]='\0';
	// if OPCODE = MACDEF
	if(strcmp(OPCODE,"MACDEF")==0)
	{
		printf("def");
		// call define
	}
	// if OPCODE = MCALL
	else if(strcmp(OPCODE,"MCALL")==0)
	{
		printf("call");
		// call expand
	}
	// else print the line
	else
	{
		printf("%s",line);
	}
}
void expand()
{

}
int main()
{
	FILE* f;
	f=fopen("input.txt","r");
	char* line;
	line=(char*)malloc(255*sizeof(char));
	while((line=getLine(f))!=NULL)
	{
		processLine(line);	
	}
	fclose(f);
	return 0;
}
