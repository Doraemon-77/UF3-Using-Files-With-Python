#Exercici 2
import tkinter.filedialog
ruta_fitxer = tkinter.filedialog.askopenfilename()

#ruta fitxer = '\\Users\\Roser\\Desktop\\dates.txt'

def compta_registre(ruta_fitxes, data):
    '''
      Retorna el número de registres de data que conté el fitxer ruta_fitxer
    '''
    #readlines ens retorna llista amb el contingut del fitxer
    #obrir fitxer en mode append
    dates_fitxer = open(ruta_fitxer, 'r')
    
    content_lst= dates_fitxer.readlines()
    dates_fitxer.close()
    
    cont= 0
    
    for d in content_lst:
        
        if data == d.strip('\n'):
            cont+= 1
            
    return cont
    
#ppal

data = input("Introdueix una data en el format DD/MM/AAA: ")

print("El fitxer conté %d registres amb la data %s." %(compta_data(ruta_fitxer,)))