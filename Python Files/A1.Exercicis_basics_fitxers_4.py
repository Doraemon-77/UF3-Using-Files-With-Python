#Exercici 4
import tkinter.filedialog
##ruta_fitxer = tkinter.filedialog.askopenfilename()

def swap_fitxer(ruta_fitxer_in, ruta_fitxer_out):
    '''
    
    '''
    
    f_in= open(ruta_fitxer_in, 'r')
    content = f_in.read()
    f_in.close()
    
    #tractar contingut
    
    swap_content = ''
    for c in content:
        if c.isupper():
            swap_content += c.lower()
            
        elif c.islower():
            swap_content += c.upper()
        else:
            swap_content += c
            
    #obrir fitxer en mode escriptura
    f_out = open(ruta_fitxer_out, 'w')
    
