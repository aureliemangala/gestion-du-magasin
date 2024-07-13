import json
import os

articles =[]
global dicto



def validationid(idArticle):
    test=idArticle.isnumeric()
    if test == True:
        return True
    else:
        return False

def validationNomArticle(nomArticle):
    test=nomArticle.isalpha()
    if test==True:
        return True
    else:
        return False



def validationPrixArticle(prixArticle):
    test=prixArticle.isnumeric()
    """ print(test)
    while test ==False:
        test=prixArticle.isnumeric()
        if test==True:
            break """
    if test==True:
        return True
    else:
        return False
    

def validationQteArticle(qteArticle):
    test=qteArticle.isnumeric()
    """ print(test)
    while test==False:
        prixArt=input("entrez un prix")
        test= prixArt.isnumeric()
        if test == True:
            break """
    if test==True:
        return True
    else:
        return False
    
#importation json
def saveDataArticle(nouveauArticle):
    """temp=[]
    if os.path.exists('database.json'):
        with open('database.json','r')as f:
            articles=json.load(f)
            articles.append(nouveauArticle)
    
        with open('database.json','w')as db:
            json.dump(articles,  db, indent=4)
    
try:
    with open("database.json","r") as f:
        articles=json.load(f)
except FileNotFoundError:
    articles[]
articles.append(dicto)"""

     
def printDataFromJson():
    file='database.json'
    if os.path.exists(file):
        with open(file,'r') as f:
            articles=json.load(f)
        for el in articles:
            print(el)
    else:
        articles=[]

def printArticles():
    for article in articles:
        print(article)
 
    
def affichageArticle():
    print(articles)

def ajoutArticle():
    global articles
    idArticle=""
    nomArt=""
    prixArt=""
    qteArt=""
    
    
    #validationNomArticle(nomArt)
   
    while True:
        idArticle=input("saisir l'id: ")
        if validationid(idArticle):
            break
    while True:
        nomArt=input("saisir le nom de l'articles :")
        if validationNomArticle(nomArt):
            break
    
    while True:
        prixArt=(input("saisir le prix de l'article :"))
        if validationPrixArticle(prixArt):
            break
    
    while True:
        qteArt=(input("saisir la quantite de l'article :"))
        if validationQteArticle(qteArt):
            break

        
    
    dicto={'idArticle':int(idArticle),"nomArt":nomArt,"prixArt":float(prixArt),"qte":int(qteArt)}
    
    articles.append(dicto)
    try:
        with open("database.json","r") as f:
            articles =json.load(f)
    except FileNotFoundError:
        articles = []
    articles.append(dicto)

    with open("database.json","w") as f:
        json.dump(articles,f,indent=1)


    
"""def rechercherArticleid(database,idArticle):
    idArticle=""
    
    try:
        with open("nom_fichier","r") as fichier:
            donnes =json.load(fichier)
        for article in donnes:
            if article.get("id")==idArticle:
                return donnes
            
        return None
    except FileNotFoundError:
        print(f"fichier '{database}'introvable")
        return None
    except json.JSONDecodeError:
        print(f"erreur lors du decoration du ficher json'{database}'.")
        return None

nom_fichier="database.json" 
article_trouve=rechercherArticleid(nom_fichier,idArticle)
if article_trouve:
    print("article trouve: ")
    print(article_trouve)
else:
    print(f"aucun article trouve avec l id'{idArticle}'.")"""

def rechercherArticle_par_nom():
    with open ('database.json','r')as f:
        articles=json.load(f)
    recherche_art=input("saisir le nom de l article: ")
    i=0
    while(i<=len(articles)-1):
        if recherche_art==articles[i]['nomArt']:
            print("le nom de l article :",articles[i]['nomArt'],"le prix de l'article:",articles[i]['prixArt'])
            return i-1
        elif(i != len(articles)-1):
            i +=1
        else:
            print("le nom de l'article n'est pas trouve")
            break


def enregistrer_vente() :
    global client
    global produit
    global quantite
    global date 
    client=input("saisir le nom du client :")  
    produit=input("saisir le nom du produit :") 
    quantite=input("saisir la quantite :") 
    date=input("saisir la data :")

    vente={"nom clent":client,"nom produit":produit,"quantite":quantite,"date":date}

    try:
        with open("ventes.json","r")as f:
            ventes=json.load(f)
    except FileNotFoundError:
        ventes=[]
    ventes.append(vente)

    with open("ventes.json","w")as f:
        json.dump(ventes, f,indent=1)

    

    


    
    
    
    



    
