from random import *

class Film:
    def __init__(self,name,year,act,gen,country,dir,min):
        self.name=name
        self.year=year
        self.act=act
        self.gen=gen
        self.cou=country
        self.dir=dir
        self.min=min
        
    def __repr__(self):
        if self.name[-10:-1]=="(Trilogia)":
            return "(Nome: "+self.name+", Periodo: "+str(self.year[0][0])+", "+self.year[1][0]+", "+self.year[2][0]+", Attori: "+str(self.act)+", Genere: "+str(self.gen)+", Paese: "+str(self.cou)+", Regista: "+str(self.dir)+", Minutaggio medio: "+str(self.min)+" minuti)"
        else:
            return "(Nome: "+self.name+", Anno: "+str(self.year[0][0])+", Attori: "+str(self.act)+", Genere: "+str(self.gen)+", Paese: "+str(self.cou)+", Regista: "+str(self.dir)+", Minutaggio: "+str(self.min)+" minuti)" 
        
class l_film:
    def __init__(self):
        self.l=[]
        self.y=None
        self.a=None
        self.g=None
        self.c=None
        self.d=None
    
    def start(self):
        dy={}
        ky=set()
        da={}
        ka=set()
        dg={}
        kg=set()
        dc={}
        kc=set()
        dd={}
        kd=set()
        for i in self.l:
            if len(i.year)>1:
                for q in i.year:
                    if q[0] in ky:
                        dy[q[0]].append(i.name+" "+str(q[1]))
                    else:
                        vy=[]
                        ky.add(q[0])
                        vy.append(i.name+" "+str(q[1]))
                        dy[q[0]]=vy                   
            else:
                if ky.__contains__(i.year[0][0]):
                    dy[i.year[0][0]].append(i.name)                    
                else:
                    vy=[]
                    ky.add(i.year[0][0])
                    vy.append(i.name)
                    dy[i.year[0][0]]=vy
            for a in i.act:
                if a in ka:
                    da[a].append(i.name)
                else:
                    va=[]
                    ka.add(a)
                    va.append(i.name)
                    da[a]=va
            for g in i.gen:
                if g in kg:
                    dg[g].append(i.name)
                else:
                    vg=[]
                    kg.add(g)
                    vg.append(i.name)
                    dg[g]=vg
            for c in i.cou:
                if c in kc:
                    dc[c].append(i.name)
                else:
                    vc=[]
                    kc.add(c)
                    vc.append(i.name)
                    dc[c]=vc
            for d in i.dir:
                if d in kd:
                    dd[d].append(i.name)
                else:
                    vd=[]
                    kd.add(d)
                    vd.append(i.name)
                    dd[d]=vd   
        self.y=dy
        self.a=da
        self.c=dc
        self.g=dg
        self.d=dd
        return None
    
    def get_by_name(self,name):
        for i in self.l:
            if i.name==name:
                return i
        return None
            
    def get_by_year(self,year):
        return self.y[year]
    
    def get_by_actor(self,act):
        return self.a[act]
    
    def get_by_genre(self, gen):
        return self.g[gen]
    
    def get_by_country(self,cou):
        return self.c[cou]
    
    def get_by_director(self,dir):
        return self.d[dir]
    
    def range_year(self,ind,year):
        l=[]
        k=self.y.keys()
        if ind>0:
            for i in k:
                if i>=year:
                    el=[i,self.y[i]]
                    j=0
                    while j<len(l) and el[0]<l[j][0]:
                        j+=1
                    l=l[:j]+[el]+l[j:] 
        else:
            for i in k:
                if i<=year:
                    el=[i,self.y[i]]
                    j=0
                    while j<len(l) and el[0]<l[j][0]:
                        j+=1
                    l=l[:j]+[el]+l[j:]     
        return l
    
    def range_min(self,ind,min):
        l=[]
        if ind>0:
            for i in self.l:
                if int(i.min)>=min:
                    j=0
                    if len(l)==0:
                        l.append(i)
                    else:
                        while int(i.min)<int(l[j].min) and j<len(l)-1:
                            j+=1
                        l=l[:j]+[i]+l[j:]
        else:
            for i in self.l:
                if int(i.min)<=int(min):
                    j=0
                    if len(l)==0:
                        l.append(i)
                    else:                    
                        while int(i.min)<int(l[j].min) and j<len(l)-1:
                            j+=1
                        l=l[:j]+[i]+l[j:]            
        lista=[]
        for ff in l:
            lista.append([ff.name,ff.min])
        return lista
    
    def get_cas_film(self):
        n=randint(0,len(self.l))
        return self.l[n]
        
def leggi_file():
    file=open("Film.txt","r")
    L=l_film()
    i=0
    for line in file:
        if line=="\n":
            o=Film(n,y,a,g,c,d,m)
            L.l.append(o)
            i=0
        else:
            if i==0:
                n=line
                i+=1
                n=n[:-1]
            elif i==1:
                if len(line)>4:
                    j=0
                    c=1
                    l_y=[]
                    s=""
                    while j<len(line):
                        if line[j]!="/":
                            s+=line[j]
                            j+=1
                        else:
                            l_y.append([int(s),c])
                            s=""
                            c+=1
                            j+=1
                    l_y.append([int(s),c])
                    y=l_y
                    i+=1
                else:
                    y=int(line)
                    i+=1
            elif i==2:
                j=0
                l_a=[]
                s=""
                while j<len(line):
                    if line[j]!="/":
                        s+=line[j]
                        j+=1
                    else:
                        l_a.append(s)
                        s=""
                        j+=1
                l_a.append(s)
                l_a[-1]=l_a[-1][:-1]
                a=l_a
                i+=1            
            elif i==3:
                j=0
                l_g=[]
                s=""
                while j<len(line):
                    if line[j]!="/":
                        s+=line[j]
                        j+=1
                    else:
                        l_g.append(s)
                        s=""
                        j+=1
                l_g.append(s)
                l_g[-1]=l_g[-1][:-1]
                g=l_g
                i+=1
            elif i==4:
                j=0
                l_c=[]
                s=""
                while j<len(line):
                    if line[j]!="/":
                        s+=line[j]
                        j+=1
                    else:
                        l_c.append(s)
                        s=""
                        j+=1
                l_c.append(s)
                l_c[-1]=l_c[-1][:-1]
                c=l_c
                i+=1   
            elif i==5:
                j=0
                l_d=[]
                s=""
                while j<len(line):
                    if line[j]!="/":
                        s+=line[j]
                        j+=1
                    else:
                        l_d.append(s)
                        s=""
                        j+=1
                l_d.append(s)
                l_d[-1]=l_d[-1][:-1]
                d=l_d
                i+=1  
            else:
                m=line[:-1]
    L.start()
    return L
                    
def menu(L):
    print("")
    print("Menu: ")
    print("0 - Visualizza film ")
    print("1 - Ricerca ")
    print("2 - Vedi categorie ")
    print("3 - Scegli un film casuale ")
    print("4 - Esci ")
    print("")
    u=int(input("Inserire un carattere valido: "))
    while int(u)<0 or int(u)>4:
        print("")
        
        u=int(input("Inserire un valore valido!!! "))
    if u==0:
        for film in L.l: 
            print(film)
            print("")
        menu(L)
    elif u==1:
        print("")        
        print("Menu ricerca: ")
        print("0 - Ricerca per nome ")
        print("1 - Ricerca per anno ")
        print("2 - Ricerca per attori ")
        print("3 - Ricerca per generi ")
        print("4 - Ricerca per paesi ")
        print("5 - Ricerca per regista ")
        print("6 - Ricerca per minutaggio ")
        print("7 - Indietro ")
        print("")        
        r=int(input("Inserire un carattere valido. "))
        while int(r)<0 or int(r)>7:
            print("")            
            r=int(input("Inserire un valore valido!!! "))
        if r==0:
            print("")            
            name=input("Inserire il nome da ricercare o 0 per uscire: ")
            if name==0:
                menu(L)
            else:
                ris=L.get_by_name(name)
                if ris==None:
                    print("")                    
                    print("Nessuna corrispondenza. ")
                    menu(L)
                else:
                    print(ris)
                    menu(L)
        elif r==1:
            print("")            
            print("Menu ricerca per anno: ")
            print("0 - Ricerca anno singolo ")
            print("1 - Ricerca da un anno in poi ")
            print("2 - Ricerca fino a un anno ")
            print("3 - Menu ")
            print("")            
            a=int(input("Inserire un carattere valido. "))
            while int(a)<0 or int(a)>3:
                print("")                
                a=int(input("Inserire un valore valido!!! "))  
            print("")            
            y=int(input("Inserire un anno: "))
            if a==0:
                
                la=L.get_by_year(y)
                if la==None:
                    print("")                    
                    print("Anno non presente. ")
                    menu(L)
                else:
                    print("")                    
                    for f in la:
                        print(f)
                    menu(L)
            elif a==1:
                ret=L.range_year(1,y)
                print("")                
                for t in ret:
                    print(t)
                menu(L)
            elif a==2:
                ret=L.range_year(-1,y)
                print("")                
                for t in ret:
                    print(t)
                menu(L)
            elif a==3:
                menu(L)
        elif r==2:
            A=list(L.a.keys())
            k=1
            print("")           
            for aa in A:
                print(k," - ",aa)
                k+=1
            print("")            
            act=int(input("Inserire un valore valido o 0 per uscire: "))
            while act>len(A) or act<0:
                print("")                
                act=int(input("Inserire un valore valido o 0 per uscire!!! "))
            if act==0:
                menu(L)
            else:
                aa=A[act-1]
                p=L.get_by_actor(aa)
                print("")          
                print(aa,": ")
                for fi in p:
                    print(fi)
                menu(L)
        elif r==3:
            G=list(L.g.keys())
            k=1
            print("")            
            for gg in G:
                print(k," - ",gg)
                k+=1
            print("")            
            gen=int(input("Inserire un valore o 0 per uscire: "))
            while gen>len(G) or gen<0:
                print("")                
                gen=int(input("Inserire un valore o 0 per uscire!!! "))
            if gen==0:
                menu(L)
            else:
                gg=G[gen-1]
                p=L.get_by_genre(gg)
                print("")     
                print(gg,": ")
                for fi in p:
                    print(fi)
                menu(L)            
        elif r==4:     
            C=list(L.c.keys())
            k=1
            print("")            
            for cc in C:
                print(k," - ",cc)
                k+=1
            print("")            
            cou=int(input("Inserire un valore o 0 per uscire: "))
            while cou>len(C) or cou<0:
                print("")                
                cou=int(input("Inserire un valore o 0 per uscire!!! "))
            if cou==0:
                menu(L)
            else:
                cc=C[cou-1]
                p=L.get_by_country(cc)
                print("")
                print(cc,": ")
                for fi in p:
                    print(fi)
                menu(L)            
        elif r==5:
            D=list(L.d.keys())
            k=1
            print("")            
            for dd in D:
                print(k," - ",dd)
                k+=1
            print("")            
            dir=int(input("Inserire un valore o 0 per uscire: "))
            while dir>len(D) or dir<0:
                print("")                
                dir=int(input("Inserire un valore o 0 per uscire!!! "))
            if dir==0:
                menu(L)
            else:
                dd=D[dir-1]
                p=L.get_by_director(dd)
                print("")
                print(dd,": ")
                for fi in p:
                    print(fi)
                menu(L)  
        elif r==6:
            print("")            
            print("Menu ricerca per minutaggio ")
            print("0 - Ricerca minutaggi superiori a... ")
            print("1 - Ricerca minutaggi inferiori a... ")
            print("2 - Menu")
            print("")            
            m=int(input("Inserire un valore valido: "))
            while m<0 or m>2:
                print("")                
                m=int(input("Inserire un valore valido!!! "))
            if m==0:
                print("")                
                minut=int(input("Inserire un minutaggio: "))
                mm=L.range_min(1,minut)
                print("")                
                for M in mm:
                    print(M)
                menu(L)
            elif m==1:
                print("")                
                minut=int(input("Inserire un minutaggio: "))
                mm=L.range_min(-1,minut)
                print("")                
                for M in mm:
                    print(M)
                menu(L)
            elif m==2:
                menu(L)
        elif r==7:
            menu(L)
    elif u==2:
        print("")        
        print("Menu di visualizzazione ")
        print("0 - Attori ")
        print("1 - Generi ")
        print("2 - Paesi ")
        print("3 - Registi ")
        print("4 - Menu ")
        print("")        
        v=int(input("Inserire un valore valido: "))
        while v<0 or v>4:
            print("")            
            v=int(input("Inserire un valore valido!!! "))
        if v==0:
            att=L.a.keys()
            print("")            
            for a in att:
                n=len(L.a[a])
                print(a, " (",n,")")
            menu(L)
        elif v==1:
            gen=L.g.keys()
            print("")            
            for g in gen:
                n=len(L.g[g])
                print(g," (",n,")")
            menu(L)
        elif v==2:
            pae=L.c.keys()
            print("")            
            for p in pae:
                n=len(L.c[p])
                print(p," (",n,")")
            menu(L) 
        elif v==3:
            reg=L.d.keys()
            print("")            
            for r in reg:
                n=len(L.d[r])
                print(r, " (",n,")")
            menu(L)
        elif v==4:
            menu(L)
    elif u==4:
        fine()
    
    elif u==3:
        print(L.get_cas_film())
        menu(L)
        
def fine():
    pass

def main():
    L=leggi_file()
    menu(L)
main()

