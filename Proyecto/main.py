from os import system
from lista_hash import ListaHash
import random
import re
TablaHash = []
for i in range(5):
  TablaHash.append(ListaHash())

# Crear un elemento para ejecutar la función hash
h = ListaHash()
file = open("prueba.txt")
#file = open("prueba2.txt")

blocks = {'{' : 'Inicia bloque de instrucciones', '}':'Fin de bloque de instrucciones'}
block_keys = blocks.keys()

operators = {'==' : 'Equal to op', '=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()

comments = {'//' : 'Comentario de línea','/*' : 'Inicia comentario multilinea', '*/' : 'Termina comentario multilinea', '/**/' : 'Comentario vacio'}
comment_keys = comments.keys()

data_type = {'int' : 'integer type', 'float': 'Floating point' , 'char' : 'Character type', 'long' : 'long int' }
data_type_key = data_type.keys()

reserved_word = {'pisco': 'print','absolutVodka' : 'abstract ', 'Voidka' : 'void', 'jose' : 'if' , 'cuervo' : 'else','whisky ' : 'while ', 'sake' : 'switch', 'jack' : 'case' , 'daniels' : 'break', 'forloko' : 'for', 'jagermeister' : 'return'}
reserved_word_key = reserved_word.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()

id = re.compile('([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*')
num = re.compile('([1-9][0-9])*[.,]?[1-9][0-9]*')
p_f = re.compile('([1-9][0-9])*[.,][1-9][0-9]*')
non_identifiers = ['_','-','+','/','*','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"','' '',':',';','{'
,'}','[',']','<','>','?','/']
#identifier = {id : 'id'}
#identifier_key = identifier.keys()
#("([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)", "id"),
# #("\d+*", "number"),
# ("", "empty")


dataFlag = False

a=file.read()
system("clear")
count=0
program = a.split("\n")
for line in program:
    count = count + 1
    #line[:-1] = ';'
    print("line#" , count, "\n" , line)

    tokens=line.split(' ')
    print("Tokens are " , tokens)
    print("Line#", count, "properties \n")
    for token in tokens:
        if token in block_keys:
            print (blocks[token])
            clave = h.funcionHash(random.randint(0,len(TablaHash)*5),len(TablaHash))
            TablaHash[clave].insertar(token, blocks[token])

        if token in operators_key:
            print("operator is ", operators[token])
            clave = h.funcionHash(random.randint(0,len(TablaHash)*5),len(TablaHash))
            TablaHash[clave].insertar(token, operators[token])

        if token in comment_keys:
            print ("Comentario: ", comments[token])
            clave = h.funcionHash(random.randint(0,len(TablaHash)*5),len(TablaHash))
            TablaHash[clave].insertar(token, comments[token])

        if token not in non_identifiers:
            tkn= token
            for x in non_identifiers:
                tkn.replace(x,'')

            if id.search(tkn) and tkn not in data_type_key and (tkn[0] == '/' and tkn[1] == '/'):
                print ("Line comment ",tkn)
                clave = h.funcionHash(random.randint(0,len(TablaHash))*5,len(TablaHash))
                TablaHash[clave].insertar(tkn,"Line comment") 
            
            if (id.search(tkn) and tkn not in data_type_key and tkn not in reserved_word_key) and (tkn[-1] not in non_identifiers) and (tkn[0] != '/' and tkn[0] != ' '):
                print ("Identificador: ",tkn)
                clave = h.funcionHash(random.randint(0,len(TablaHash))*5,len(TablaHash))
                TablaHash[clave].insertar(tkn,"id")    

        if token in data_type_key:
            print("datatype is", data_type[token])
            clave = h.funcionHash(random.randint(0,len(TablaHash)*5),len(TablaHash))
            TablaHash[clave].insertar(token, data_type[token])

        if token not in non_identifiers and token not in data_type_key and token[0] != '/' :
            tkn = token[:-1]
            if tkn in reserved_word_key :
                print (tkn, "Reserved word is" , reserved_word[tkn])
                clave = h.funcionHash(random.randint(0,len(TablaHash))*5,len(TablaHash))
                TablaHash[clave].insertar(tkn, reserved_word[tkn])
            if token in reserved_word_key :
                print (tkn, "Reserved word is" , reserved_word[token])
                clave = h.funcionHash(random.randint(0,len(TablaHash))*5,len(TablaHash))
                TablaHash[clave].insertar(token, reserved_word[token])

        if token in punctuation_symbol_key:
            print (token, "Punctuation symbol is" , punctuation_symbol[token])
            clave = h.funcionHash(random.randint(0,len(TablaHash))*5,len(TablaHash))
            TablaHash[clave].insertar(token, punctuation_symbol[token])
        if num.search(token):
            if p_f.search(token):
                tkn = token[:-1]
                print (tkn, "is a float")
                clave = h.funcionHash(random.randint(0,len(TablaHash))*5,len(TablaHash))
                TablaHash[clave].insertar(tkn, "Float")
            else:
                tkn = token[:-1]
                print (tkn, "is a number")
                clave = h.funcionHash(random.randint(0,len(TablaHash))*5,len(TablaHash))
                TablaHash[clave].insertar(tkn, "Number")
    dataFlag=False
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _") 

for i in range(5):
    print("ListaHash[" + str(i) + "] = ",end = "")
    TablaHash[i].recorrer()
    print("")
