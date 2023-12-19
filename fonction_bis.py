from fonction import*
def pas_important(t_2D):
    T=[]
    for i in range(1,len(t_2D)):
        if t_2D[1][i]==0.0 and t_2D[2][i]==0.0 and t_2D[3][i]==0.0 and t_2D[4][i]==0.0 and t_2D[5][i]==0.0:
            T.append(t_2D[0][i])
    print(T)
def eleve(t_2D):
    T=[]
    max=-1
    for i in range(1,len(t_2D[0])):
        s=0
        for j in range (1,len(t_2D)):
            s+=t_2D[j][i]
        if s>max:
            max=s
            T=[t_2D[0][i]]
        elif s==max:
            T.append(t_2D[0][i])
    print(T)
def chirac_mot():
    T=[]
    max=-1
    f = open("./cleaned/Chirac.txt",'r')
    line = f.read()
    d=tf(line)
    T_unique=mot(line)
    f.close()
    for elt in T_unique:
        if d[elt]>max:
            max=d[elt]
            T=[elt]
        elif d[elt]==max:
            T.append(elt)
    print(T)
def nation(t_2D):
    T=[]
    i=1
    max=-1
    max_president="personne"
    while i<len(t_2D[0]) and t_2D[0][i-1]!="nation":
        if t_2D[0][i]=="nation":
            for j in range(1,len(t_2D)):
                
                f=open("./cleaned/"+t_2D[j][0]+".txt","r")
                line=f.read()
                d=tf(line)
                if t_2D[0][i] in d.keys() and d[t_2D[0][i]]>0:
                    T.append(t_2D[j][0])
                if t_2D[0][i] in d.keys() and d[t_2D[0][i]]>max:
                    max_president=t_2D[j][0]
        i+=1
    print(T,max_president)
def climat(t_2D):
    for i in range(1,len(t_2D)):
        f = open("./cleaned/"+t_2D[i][0]+".txt","r")
        line=f.read()
        d=tf(line)
        f.close()
        if "climat" in d.keys() or "ecologie" in d.keys():
            print(t_2D[i][0])
            return t_2D[i][0]
    
