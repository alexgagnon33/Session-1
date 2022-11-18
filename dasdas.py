def document():

    nom_doc = int(input('Écriver le nom du document'))
    nombre = int(input('Écriver les nombre à inscrire dans le document'))

données = nombre
def plus_grand():
    plus_grand_nb = données[0]
    for nb in données:
        if nb > plus_grand_nb:
            plus_grand_nb = nb

def large(nb):

    max_ = nb[0]
    for nombre in nb:
        if(nombre > max_):
           max_ = nombre
    return max_ 

list1 = nombre
result = large(list1)
    #https://www.codingem.com/python-how-to-find-the-largest-number-in-a-list/