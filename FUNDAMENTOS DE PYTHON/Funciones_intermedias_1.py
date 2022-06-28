
#Asignación: Funciones intermedias I

#1-- Actualizar valores en diccionarios y listas


x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)


estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes [ 0 ][ 'last_name' ] =  'Bryant'
print( estudiantes )


directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['fútbol'][0] = 'Andres'
print(directorio_deportes)


z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)



#2-- Iterar a través de una lista de diccionarios
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(dict):
    for estudiante in estudiantes:
        for key, val in estudiante.items():
            print(key, " - ", val)

iterateDictionary(estudiantes)



#3-- Obtener valores de una lista de diccionarios
#NOMBRES
def iterateDict2(lookup, dict):
    for estudiante  in estudiantes:
        print(estudiante [lookup])

iterateDict2('first_name', estudiantes)

#APELLIDOS
def iterateDict3(lookup, dict):
    for estudiante  in estudiantes:
        print(estudiante [lookup])

iterateDict3('last_name', estudiantes)



#4--Iterar a través de un diccionarios con valores de lista
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDojoInfo(list):
    for key in dojo:
        print(len(dojo[key]))
        print(key)
        for val in dojo[key]:
            print(val)

printDojoInfo(dojo)