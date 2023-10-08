# Bibliotecas 
import pandas as pd 
d = {
       'Nome': ["Pablo", 'Thais'],
       'Idade':[43, 40],
       'Altura': [180, 170]       
}
dados = pd.DataFrame(d)
print(dados)
dados.to_excel("teste.xlsx", index = False)
