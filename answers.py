import pandas as pd
import os

# GENERAL RESOURSES
listOfCoutry = []
listOfThemes = []
arquivo = os.path.realpath('Data/NECP.csv')
def lerDados():
    arq = pd.read_csv(arquivo)
    indice = pd.Series(data=arq["index"])
    paises = pd.Series(data=arq["country"])
    secoes = pd.Series(data=arq["subsection"])
    dimensoes = pd.Series(data=arq["energy_union_dimension"])
    data = {"index": indice, "country": paises, "sections": secoes, "dimension": dimensoes}
    tabela = pd.DataFrame(data)
    tabela.fillna("Others", inplace=True)
    
    return tabela

def listCountry():
    data = lerDados()
    for i in range(len(data)-1):
        if data['country'][i] != data['country'][i+1]:
            aux = data['country'][i]
            listOfCoutry.append(aux)
            
    return listOfCoutry

# FIRST QUESTION

def listEngagement():
    data = lerDados()
    for i in range(len(data)-1):
        if data['country'][i] != data['country'][i+1]:
            aux = data['country'][i]
            listOfCoutry.append(aux)
            
    print(listOfCoutry)
    for i in range(len(data)-1):
        if data['dimension'][i] != data['dimension'][i+1]:
            if data['dimension'][i] in listOfThemes:
                continue
            else: 
                aux = data['dimension'][i]
                listOfThemes.append(aux)
    print(listOfThemes)
    print(data.groupby(['country', 'dimension']).count())

# THE SECOND QUESTION:
def engagementsforcountry():
    data = lerDados()
    return data.groupby(['country', 'dimension']).value_counts()

# THE THIRD QUESTION:
def percentageEngagementforcountry():
    data = lerDados()
    return data.groupby(['country', 'dimension']).mean()

# THE FOURTH QUESTION:
def contryforproposalEE():
    data = lerDados()
    lsofco = listCountry()
    for i in lsofco:
        print(data[(data["country"] == i) & (data["dimension"] == "energy efficiency")].value_counts())
    
# THE FIFTH QUESTION:
def contryforproposalD():
    data = lerDados()
    lsofco = listCountry()
    for i in lsofco:
        print(data[(data["country"] == i) & (data["dimension"] == "Decarbonisation")].value_counts())
    
# THE SIXTH QUESTION:
def contryforproposalES():
    data = lerDados()
    lsofco = listCountry()
    for i in lsofco:
        print(data[(data["country"] == i) & (data["dimension"] == "Energy security")].value_counts())

# THE SEVENTH QUESTION:
def contryforproposalI():
    data = lerDados()
    lsofco = listCountry()
    for i in lsofco:
        print(data[(data["country"] == i) & (data["dimension"] == "Internal market")]['country'].value_counts())

# THE EIGHTH QUESTION:
def contryforproposalRI():
    data = lerDados()
    lsofco = listCountry()
    for i in lsofco:
        print(data[(data["country"] == i) & (data["dimension"] == "R&I and Competitiveness")].value_counts())