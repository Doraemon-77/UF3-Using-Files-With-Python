import tkinter.filedialog
##Podem obrir el fitxer d'aquesta forma. 
##Això ens obrira una finestra per indicar on es troba el fitxer.
##ruta_fitxer = tkinter.filedialog.askopenfilename()


def read_grades(gradefile):
    '''(files open for reading) -> dict of {float: list of str}
    
    Read the grades from gradefile and return a dictionary where
    each grade is a key and each value is the list of ids of students
    
    Precondition: gradefile starts with a header that contains
    no blank lines, then has a blank line, an then lines containing
    a student number and a grade.
    
    '''
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()
        
#Creem un diccionari buit on guardarem les claus i els valors del fitxer

    grade_dic = {}
    
    line = gradefile.readline()
    while line !='':
        #tractar linia
        id_student = line[:4]
        nota = line[4:].strip()
              
        if nota not in grade_dic:
        
            grade_dic[nota] = [id_student]
        else:
            grade_dic[nota].append(id_student)
            
        #llegir següent linia
        line = gradefile.readline()
        
    return grade_dic

    


#prog. ppal
#ruta_fitxer = tkinter.filedialog.askopenfilename()
gradefile = open('grades.txt', 'r')
dic = read_grades(gradefile)
print(dic)
gradefile.close()

