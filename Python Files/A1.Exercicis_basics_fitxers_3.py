#Exercici 3
import tkinter.filedialog
ruta_fitxer = tkinter.filedialog.askopenfilename()
#ruta fitxer = '\\Users\\Roser\\Desktop\\dates.txt'

def majuscules(ruta_fitxes, cadena):
    '''
      Retorna el número de registres de data que conté el fitxer ruta_fitxer
    '''
    #readlines ens retorna llista amb el contingut del fitxer
    #obrir fitxer en mode append
    dates_fitxer = open(ruta_fitxer, 'a')
    
    cad_app= cadena.upper()
    fitxer.write(cad.upper)
    