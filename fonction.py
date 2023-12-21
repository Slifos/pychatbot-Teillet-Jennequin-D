import os
import math


def extraire_noms(directory : str):
    """extraire les noms des présidents à partir des noms des fichiers"""
    noms_fichiers = list_of_files(directory, ".txt")
    noms_presidents=[]
    for nom_fichier in noms_fichiers:
        nom_president = nom_fichier.replace("Nomination_", "", 1)
        nom_president = nom_president.replace(".txt", "", 1)
        for i in range(10):
            nom_president = nom_president.replace(str(i), "", 1)
        
        if not(nom_president in noms_presidents):
            noms_presidents.append(nom_president)
    return noms_presidents

def cleaned(char):
    """récupère une chaine de caractère pour la rendre en minuscule et séparer chaque mot par des espaces tout en remplaçant les caractères spéciaux"""
    n= len(char)
    n_char=-1
    s=""

    for elt in char:
        if elt == "§" : #ç
            s+= "c"
            n_char+=1
        elif elt in "©ª¨ë" : #éêè
            s += "e"
            n_char+=1
        elif elt in "â" : #à
            s += "a"
            n_char+=1
        elif elt == "¹" : #ù
            s += "u"
            n_char+=1
        elif elt in "Ã":
            s=s
        elif ord(elt)>=65 and ord(elt)<=90:
            s+=chr(ord(elt)+32)
            n_char+=1
            
        elif ord(elt)>=97 and ord(elt)<=122:
            s+=elt
            n_char+=1
        elif s!="" and s[n_char]!=" ":
            s+=" "
            n_char+=1
            
        
    #print(s)
    return s

def list_of_files(directory, extension):
    """récupère tous les noms de fichier d'une extension donnée à partir de son dossier"""
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def f_cleaned(directory):
    """Transfère les données d'un fichier à partir de son nom dans un autre tout en séparant chaque mot par des espaces"""
    directory_f="./cleaned/"
    T_president=extraire_noms(directory)
    file=list_of_files(directory, ".txt")
    for elt in T_president:
        f2= open(directory_f+elt+".txt",'w')
        for i in file:
            if elt in i:
                f = open(directory+i,'r')
                lines = f.readlines()
                for line in lines:
                    ajout=cleaned(line)
                    f2.write(ajout)
            f.close()
        f2.close()



def mot(char):
    """retourne un tableau de mot unique dans une chaine de caractère avec des mots séparés"""
    T=[]
    s=""
    
    for elt in char:
        if elt==" ":
            if not(s in T):
                T.append(s)
            s=""
        else:
            s+=elt
    if s!="":
        T.append(s)
    
    return T
def tf(char):
    """retourne un dictionnaire avec le nb de chaque occurence pour chaque mot unique dans une chaine de caractère avec des mots séparés"""
    d={}
    T=[]
    s=""
    for elt in char:
        if elt==" ":
            if s in T:
                d[s]=d[s]+1
            else:
                T.append(s)
                d[s]=1
            s=""
        else:
            s+=elt
    if s!="":
        T.append(s)
    #print(d)
    return d
def teste_occ(mot,list_T):
    """retourne le nb de fois qu'apparait un mot dans une liste 2D contenant des mots"""
    s=0
    for i in list_T:
        for j in i:
            if j==mot:
                s+=1
    return s
    
def idf(directory):
    files=list_of_files(directory, ".txt")
    matrice_mot=[]
    for elt in files:
        f=open(directory+elt,"r")
        line=f.read()
        T=mot(line)
        matrice_mot.append(T)
    d={}
    n=len(matrice_mot)
    for i in matrice_mot:
        for j in i:
            d[j]=math.log(n/teste_occ(j,matrice_mot))
    #print(d)
    return d
    
def m_mot(directory):
    files=list_of_files(directory, ".txt")
    matrice_mot=[]
    for elt in files:
        f=open(directory+elt,"r")
        line=f.read()
        T=mot(line)
        matrice_mot.append(T)
    return matrice_mot
    
def mot_2D(matrice_mot):
    """retourne un tableau de mot unique à partir d un tableau 2D remplie de mot"""
    T=[]
    s=""
    
    for elt in matrice_mot:
        for i in elt:
            if not(i in T):
                T.append(i)
                
    
    return T
    
def tf_idf(directory):
    """retourne une liste tf idf de chaque mot (qui correspond au colonne) dans chaque document(qui correspond à la ligne)"""
    matrice_mot=m_mot(directory)
    liste_mot=mot_2D(matrice_mot)
    T_president=extraire_noms(directory)
    d_idf=idf(directory)
    tfidf=[[0]]
    for elt in (liste_mot):
        tfidf[0].append(elt)
    for i in range(len(T_president)):
        tfidf.append([])
        tfidf[1+i].append(T_president[i])
    
    for i in range(1,len(tfidf)):
        f = open(directory+tfidf[i][0]+".txt",'r')
        line=f.read()
        d_tf=tf(line)
        T=mot(line)
        for j in range(1,len(tfidf[0])):
            if tfidf[0][j] in T:
                res=d_tf[tfidf[0][j]]*d_idf[tfidf[0][j]]
                tfidf[i].append(res)
            else:
                tfidf[i].append(res)
        f.close()
    return tfidf
    
def affichage_matrice(L):
    f=open("réecriture.txt","w")
    for elt in L:
        print("[",end=" ")
        s="[ "
        
        for elt2 in elt:
            print(elt2,end=" ")
            s+= str(elt2)+" "
        
        print("]")
        s+="]"
        f.write(s)

    f.close()
        
def token(chain):
    new= chain
    new.lower()
    s=""
    L=[]
    for elt in chain:
        if ord(elt)>= ord("a") and ord(elt)<=ord("z"):
            s+=elt
        else:

            L.append(s)
            s=""
    if s!="":
        L.append(s)
    return L
    
def intersection(fichier,L_token):
    f = open("./cleaned/"+fichier+".txt","r")
    line = f.readlines()
    #print(line)
    

    L_fichier= mot(line[0])
    
    L_inter = []
    for i in L_fichier:
        for j in L_token:
            if i==j:
                L_inter.append(i)
    return L_inter

def tfidf_token(chain):
    """retourne un t2D des vecteurs tf idf de chaque mot en + des tokens dans chaque document"""
    L_token=token(chain)
    d_idf=idf("./cleaned/")
    
    
    tfidf=tf_idf("./cleaned/")
    char=""
    for elt in L_token:
            
            char+=elt+" "
    tf_token=tf(char)
    for i in range(1,len(tfidf)):
        L_inter=intersection(tfidf[i][0],L_token)
        #print(L_inter)
        
        
        for j in range(1,len(tfidf[0])):
            if tfidf[0][j] in L_inter:
                res=tf_token[tfidf[0][j]]*d_idf[tfidf[0][j]]
                tfidf[i][j]=res
                #print(res)
            else:
                tfidf[i][j]=0.0
    return tfidf
    
def scalaire(A,B):
    s=0
    for i in range(len(A)):
        s+=A[i]*B[i]
    return s
def norme(A):
    s=0
    for elt in A:
        s+=elt**2
    s=math.sqrt(s)
    return s
def similarite(A,B):
    scal = scalaire(A,B)
    normeA=norme(A)
    normeB=norme(B)
    if normeA==0 or normeB==0:
        res=0
    else:

        res=scal/(normeA*normeB)
    return res
def pertinent(tfidf,tfidf_token):
    maxi=0
    important =0
    for i in range(1,len(tfidf)):
        vec_ori=tfidf[i][1:]
        vec_tok=tfidf_token[i][1:]
        simi = similarite(vec_ori,vec_tok)
        if simi>maxi:
            maxi=simi
            important=tfidf[i][0]
    return important
    
def grand_tfidf(tfidf):
    maxi=0
    mot_important=""
    for i in range(1,len(tfidf)):
        for j in range(1,len(tfidf[0])):
            if tfidf[i][j]>maxi:
                maxi=tfidf[i][j]
                mot_important=tfidf[0][j]
    
    return mot_important
    
def starter(question):
    question.lower()
    question_starters = {"comment": "Après analyse, ","pourquoi": "Car, ","peux-tu": "Oui, bien sûr!"}
    T_question=["comment","pourquoi","peux-tu"]
    char=""
    for elt in question:
        if elt ==" ":
            if char in T_question:
                return question_starters[char]
        char+=elt
    return ""
    

def réponse(tfidf,tfidf_token,question):
    
    mot_imp=grand_tfidf(tfidf_token)

    if mot_imp=="":
        return "je n'ai pas compris votre phrase. Veuillez répéter."
    doc_imp=pertinent(tfidf,tfidf_token)
    T_speeches=list_of_files("./speeches/", ".txt")
    n=0
    name=[]
    for elt in T_speeches:
        if doc_imp in elt:
            n+=1
            name.append(elt)
    phrase_f=[]

    start = starter(question)
    for elt in name:
        phrase_f.append(phrase(mot_imp,elt))

    if phrase_f==[" "," "]:
        return "je n'ai pas compris votre phrase. Veuillez répéter."
    elif len(phrase_f)==1:
        return start+phrase_f[0]
    elif len(phrase_f[1])>len(phrase_f[0]):
        return start+phrase_f[1]
    
    return start+ phrase_f[0]


def phrase(mot,fichier):

    f = open("./speeches/"+fichier,"r",encoding="utf8")
    lines=f.readlines()
    
    for line in lines:
        i=0
        char=""
        index_p=0
        
        line.lower()
        for elt in line:
        
            if elt =="."or elt=="!" or elt=="?":
                index_p=i+1
            if elt ==" " or elt=="\n":
                if char==mot:
                    i=index_p
                    phrase_f=""
                    
                    while line[i]!="."and line[i]!="!" and line[i]!="?" and line[i]!="\n" and i<400:
                        phrase_f+=line[i]
                        
                        i+=1
                    return phrase_f+"."
                char=""
        

            else:
                char+=elt
    
    return " "
   
