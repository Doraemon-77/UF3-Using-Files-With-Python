import tkinter.filedialog
ruta_fitxer = tkinter.filedialog.askopenfilename()
def comptarParaules(ruta_fitxer):
    
    historia_file = open('historia.txt', 'r')
    
    content = content.split()
    
    return len(content)

def afegir_paraula(ruta_fitxer):
    '''
    
    '''
    
    #obrir fitxer en mode append
    vaca_fitxer= 
    
def afegirParaula2(ruta_fitxer):
    '''
    
    '''
    
    #obrir fitxer en mode lectura
    vaca_fitxer = open(ruta_fitxer, 'r')
    #obtenir contingut del fitxer
    content = vaca_fitxer.read()
    #tancar fitxer
    vaca_fitxer.close()
    
    #obrir fitxer en mode write
    vaca_fitxer = open(ruta_fitxer, 'w')
    #tractar contingut
    paraula = input(