import os
from typing import final
import pandas as pd
import codecs

def concat(rutaF):
    df = pd.DataFrame()
    finalEncoding = 'latin1'
    finalSep = ','
    
    for file in os.listdir(rutaF):
        if file.endswith('.csv'):
            try:
                df = df.append(pd.read_csv(rutaF+file, encoding='latin1'))
            except:
                #Files with different delimiters than , or ;
                try:
                    doc = codecs.open(rutaF+file,'rU','UTF-16')
                    df = df.append(pd.read_csv(doc, sep='\t', encoding='latin1'))
                    finalEncoding = 'UTF-16'
                except:
                    pass
        elif file.endswith('.xlsx'):
            df = df.append(pd.read_excel(rutaF+file))

    df.to_csv('output_sheet.csv', index=False, sep='\t', encoding=finalEncoding)
    
    print('\n\n****** SPREADSHEETS JOINED CORRECTLY ******\nA file named "output_sheets.csv" has been created in this directory with the output result.')

if __name__ == "__main__":
    
    while True:
        fichero = input('----------\n[1] Introduce the path to of sheets folder: ')
        if(fichero == '.' or fichero == ''):
            fichero = os.getcwd()+'\\'
            break
        elif(os.path.isdir(fichero) == False):
            print("----------\n** Error ** That is not a valid folder. Enter a valid folder\n")
            continue
        else:
            caracter = fichero[len(fichero)-1]
            if(caracter != '/' or caracter != '\\'):
                fichero = fichero.replace('/','\\')+'\\'
            break
    
    concat(fichero)