import tkinter.filedialog
ruta_fitxer = tkinter.filedialog.askopenfilename()

#ruta fitxer = '\\Users\\Roser\\Desktop\\dates.txt'

def guardar_dates(ruta_fitxer, dia, mes, ano):
    '''
    
    '''
    
    #obrir fitxer en mode append
    dates_fitxer = open(ruta_fitxer, 'a')
    
    data= str(datatime.date(ano, mes, dia))
    dates_fitxer.write(data+'\n')
    dates_fitxer.close
    
#ppal

data = input("Introdueix una data en format DD/MM/AAAA: ")
while data !='':