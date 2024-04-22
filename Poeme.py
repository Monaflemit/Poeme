import streamlit as st 
# cd C:\Users\quewa\Documents\pyzo\Poeme
#streamlit run Poeme.py


with open('1.txt', 'r', encoding='utf-8') as f:
    data1 = f.read()

with open('2.txt', 'r', encoding='utf-8') as f:#Harry potter
    data2 = f.read()

def wq(e,contenu=data1):
    rep=e+"\n"



    phrase='\n'


    mini=0
    for i in str(e):
        mini+= int(i) +10*(int(i)==0)



    e=str(e)
    for i in range(1,len(contenu)-11):
        if contenu[i-1]==' ' or  contenu[i-1]=='\n' :
            j=0 #num decimal
            err=0
            while err == 0:
                lon=0 #longueur mot dans le livre
                while i+lon<len(contenu)    and contenu[i+lon]!='\n'  and  not(contenu[i+lon] in "?!-.,']’ —:;*)(") :
                    lon +=1
                if  j<len(e) and ( ( int(e[j]) == lon ) or ( int(e[j])==0 and lon == 10) ):
                    j+=1
                    phrase+= contenu[i:i+lon+1]
                    i=i+lon+1
                    if contenu[i] in " ":
                        phrase+=" "                        
                elif lon != 0:
                    err=1
                else :
                    i+=1
            phrase+= '\n\n'
    p=''
    for i in range(len(phrase)):
        if phrase[i]=='\n':
            j=1
            paslettre=0
            while i+j<len(phrase) and phrase[i+j] != '\n':
                j+=1
                if phrase[i+j] in "?!-.']’ —:;*)(":
                    paslettre+=1#+10 * (phrase[i+j] in "?!;." )
            if j>mini +paslettre:
                p+=phrase[i:i+j]+'\n'



#     phrase=''
# 
# 
#     mini=0
#     for i in str(e):
#         mini+= int(i) +10*(int(i)==0)
# 
# 
# 
#     e=str(e)
#     for i in range(1,len(contenu)-11):
#         if contenu[i-1]==' ' :
#             j=0 #num decimal
#             err=0
#             while err == 0:
#                 lon=0 #longueur mot dans le livre
#                 while i+lon<len(contenu)    and contenu[i+lon]!='\n'  and  not(contenu[i+lon] in "?!-.,']’ —:;*)(") :
#                     lon +=1
#                 if  j<len(e) and ( ( int(e[j]) == lon ) or ( int(e[j])==0 and lon == 10) ):
#                     j+=1
#                     phrase+= contenu[i:i+lon+1]
#                     i=i+lon+1
#                 elif lon != 0:
#                     err=1
#                 else :
#                     i+=1
#             phrase+= '\n\n'
#     p=''
#     for i in range(len(phrase)):
#         if phrase[i]=='\n':
#             j=1
#             paslettre=0
#             while i+j<len(phrase) and phrase[i+j] != '\n':
#                 j+=1
#                 if phrase[i+j] in "?!-.']’ —:;*)(":
#                     paslettre+=1+10 * (phrase[i+j] in "?!;." )
#             if j>mini +paslettre:
#                 p+=phrase[i:i+j]+'\n'


    return(rep+p)



    
def wq1(e,contenu=data1):
    """Début de la phrase"""
    rep=e+"\n"

    phrase='\n'

    mini=0
    for i in str(e):
        mini+= int(i) +10*(int(i)==0)

    e=str(e)
    for i in range(1,len(contenu)-11):
        if contenu[i-1]==' ' or  contenu[i-1]=='\n' :
            j=0 #num decimal
            err=0
            while err == 0:
                lon=0 #longueur mot dans le livre
                while i+lon<len(contenu)    and contenu[i+lon]!='\n'  and  not(contenu[i+lon] in "?!-.,']’ —:;*)(") :
                    lon += 1
                if  j<len(e) and ( ( int(e[j]) == lon ) or ( int(e[j])==0 and lon == 10) ):
                    j += 1
                    phrase += contenu[i:i+lon+1]
                    i = i+lon+1
                    if contenu[i] in " ":
                        phrase+=" "    
                elif lon != 0:
                    err=1
                else :
                    i+=1
            phrase+= '\n\n'
    p=''
    for i in range(len(phrase)-1):#and contenu[i-2] in "?!.;"
        if phrase[i]=='\n' and phrase[i+1] in "AZERTYUIOPQSDFGHJKLMWXCVBN" :
            j=1
            paslettre=0
            while i+j<len(phrase) and phrase[i+j] != '\n':
                j+=1
                if phrase[i+j] in "?!-.']’ —:;*)(":
                    paslettre+=1#+10 * (phrase[i+j] in "?!;." )
            if j>mini +paslettre:
                p+=phrase[i:i+j]+'\n'

    return(rep+p)
    

def wq2(e,contenu=data1):
    """fin de la phrase"""
    rep=e+"\n"
    phrase='\n'
    mini=0
    for i in str(e):
        mini+= int(i) +10*(int(i)==0)

    e=str(e)
    for i in range(2,len(contenu)-11):
        if contenu[i-1]==' '  :
            j=0 #num decimal
            err=0
            while err == 0:
                lon=0 #longueur mot dans le livre
                while i+lon<len(contenu)    and contenu[i+lon]!='\n'  and  not(contenu[i+lon] in "?!-.,']’ —:;*)(") :
                    lon +=1
                if  j<len(e) and ( ( int(e[j]) == lon ) or ( int(e[j])==0 and lon == 10) ):
                    j+=1
                    phrase+= contenu[i:i+lon+1]
                    i=i+lon+1
                    if contenu[i] in " ":
                        phrase+=" "    
                elif lon != 0:
                    err=1
                else :
                    i+=1
            #phrase+=contenu[i-2:i+5]#.
            phrase+= '\n\n'
    #print(' \n',phrase,' \n')
    p=''
    for i in range(len(phrase)-1):#and contenu[i-2] in "?!.;"
        if phrase[i]=='\n'  :
            j=1
            paslettre=0
            while i+j<len(phrase) and phrase[i+j] != '\n':
                j+=1
                if phrase[i+j] in "?!-.']’ —:;*)(":
                    paslettre+=1#+10 * (phrase[i+j] in "?!;." )
            if j>mini +paslettre and phrase[i+j-1]==".":
                p+=phrase[i:i+j]+'\n'

    return(rep+p)
    



# Ajouter un titre
st.title("Poème")

st.write('Site qui aide à la mémorisation de nombres. ')

st.write('Comment faire pour retenir plus facilement les nombres ?')

st.write('Par exemple, pour retenir le nombre pi,  il existe un poème :')

#st.write('3  $~~$ 1 $~~$ 4 $~~$ 1 $~~$ 5')
#st.write('Que j\'aime à faire')
from matplotlib.pyplot import imread
pi_im=imread("pi.png")
# Affichez l'image dans votre application
st.image(pi_im, caption="Poème de pi")


#texte.isdigit()

st.write("J'ai donc créé ce site qui prend en entrer un nombre. Il cherche dans un texte les mots avec le bon nombre de lettres. Il renvoie un poème comme ci-dessus.")



# Créer une zone de texte
texte = st.text_input("Entrez un nombre", value="", key=None, type='default')



# Créer les onglets
onglet_selectionne = st.radio("Sélectionnez un mode", ["Poème","Personnaliser"])

# Début ou fin de phrase ?
place = st.radio("Début ou fin de phrase ?", ["Tous","Début","Fin"])



# Afficher le contenu de l'onglet sélectionné
if onglet_selectionne == 'Poème':
    col1, col2,col3,col4 = st.columns(4)
    with st.spinner("Calcul en cours..."):

        if col1.button('Poème'):
            if place=="Tous":
                poeme=wq(texte)
            elif place=="Début":
                poeme=wq1(texte)
            else:
                poeme=wq2(texte) 
            #st.write(poeme)
            st.session_state.texte_prec=poeme
    
        if col2.button('Harry Potter'):
            if place=="Tous":
                poeme2=wq(texte,data2)
            elif place=="Début":
                poeme2=wq1(texte,data2)
            else:
                poeme2=wq2(texte,data2) 
            #st.write(poeme2) 
            st.session_state.texte_prec=poeme2
else:    
    # Créer une zone de texte de plusieurs lignes
    texte3 = st.text_area("Entrez votre livre", value="", height=200)    


    with st.spinner("Calcul en cours..."):
        if st.button('Texte personnalisé'):
            if place=="Tous":
                poeme3=wq(texte,texte3)
            elif place=="Début":
                poeme3=wq1(texte,texte3)
            else:
                poeme3=wq2(texte,texte3) 
            #poeme3=wq(texte,texte3)
            #st.write(poeme3) 
            st.session_state.texte_prec=poeme3

try:
    st.write( st.session_state.texte_prec)
except:
    a=1    
