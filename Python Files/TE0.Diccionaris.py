#Metodes per a la creació de diccionaris a partir de llistes

def diccionari(animals,pes):
    '''
    
    '''
    
    animals= ['gos','gat','elefant']
    pes=(25,3,500)

    dct={}

    for x in range(len(animals)):
        dct[animals[x]]= pes[x]
        
    return dct

def dictionary2(lst_animal_pes):
    '''
    
    '''
    
    animals= ['gos','gat','elefant']
    pes=(25,3,500)    
    
    dec_an_pes= {}
    
    for i in range(len(lst_animal_pes)):
        dct_an_pes[lst_animals_pes[i][0]] = lst_animals_pes[i][1]
        
    return dct_an_pes
    
  
    
##Ordenar diccionari

lst=[]

for key in afr_animals_pes:
    
    lst.append(key)
    
##Guradem en una llista totes les claus 

    lst.sort()
    
    print(lst)
    
##Modificar un pes del diccionari

afr_animals_pes['elefant']=350

print(afr_animals_pes)



city_to_temp={'Toronto':'7', 'Sidney':'11', 'Algiers': '15'}

#per accedir als valors del diccionari
city_to_temp['Toronto'] < city_to_temp['Sidney']
    
    