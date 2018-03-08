import re
import codecs
import ply.lex as lex
from time import sleep

tokens = ['ID','NUMBER','PLUS','MINUS','MULTI','DIVIDE','ODD','ASSIGN','NE','LT','LTE','GT','GTE','LPARENT','RPARENT','COMMA','SEMMICOLOM','DOT','UPDATE']


reservadas={'start':'START', 
'ende':'ENDE', 
'ob':'OB', 
'dann':'DANN', 
'wahrend':'WAHREND', 
'machen':'MACHEN', 
'anruf':'ANRUF', 
'const':'CONST', 
'zahl':'ZAHL', 
'verfahren':'VERFAHREN', 
'aus':'AUS', 
'im':'IM', 
'sonst':'SONST' 
}

tokens = tokens+list(reservadas.values())


t_ignore = '\t'
t_PLUS = r'\+'
t_ASSIGN = r'='
t_MINUS = r'\-'
t_MULTI = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='

def t_ID(t):
	r'1-9[a-zA-Z_][a-zA-Z0-9_]*1-9'
	if t.value.upper() in tokens:
 		t.value = t.value.upper()
 		t.type = t.value
	return t
def t_TOKEN(t):
	r'\~token'
	if t.value.upper() in tokens:
 		t.value = t.value.upper()
 		t.type = t.value
	return t

def t_COOMENT(t):
	r'\#-*'

def t_ESPACE(t):
	r'\ '

def t_ENDLINE(t):
	r'\n'


def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print ("Carácter ilegal en la linea ",t.lineno)
	t.lexer.skip(1)
	
	
class hernan:
	
	def compilar(self,fileName):
		fp=codecs.open(fileName, 'r')
		file_text = fp.read()
		analizador = lex.lex()
		#i=0
		analizador.input(file_text)
		for i in range(11):			
			print('['+'/'*i+'|'*(10-i)+ ']',(i*10),'%', end='\r')
			sleep(0.2)
		print("analisis terminado")
		while True:
			tok = analizador.token()
			if not tok:
				break
			else:			
				#i=i+1
				print('\n',tok)
		fp.close()

	
fileName ="archivo.txt"
lexico=hernan()
lexico.compilar(fileName)
