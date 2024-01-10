import streamlit as st #streamlit run Poeme.py


with open('1.txt', 'r', encoding='utf-8') as f:
    data1 = f.read()

with open('2.txt', 'r', encoding='utf-8') as f:#Harry potter
    data2 = f.read()

def wq(e,contenu=data1):
    rep=e+"\n"


    phrase=''


    mini=0
    for i in str(e):
        mini+= int(i) +10*(int(i)==0)



    e=str(e)
    for i in range(1,len(contenu)-11):
        if contenu[i-1]==' ' :
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
                    paslettre+=1+10 * (phrase[i+j] in "?!;." )
            if j>mini +paslettre:
                p+=phrase[i:i+j]+'\n'


    return(rep+p)



# Ajouter un titre
st.title("Poème")

# Ajouter du texte
st.write('Exemple : ')
st.write('3  $~~$ 1 $~~$ 4 $~~$ 1 $~~$ 5')
st.write('Que j\'aime à faire')

#texte.isdigit()

# Créer une zone de texte
texte = st.text_input("Entrez un nombre", value="", key=None, type='default')



# Créer les onglets
onglet_selectionne = st.selectbox("Sélectionnez un mode", ["Poème","Personnaliser"])

# Afficher le contenu de l'onglet sélectionné
if onglet_selectionne == 'Poème':
    col1, col2,col3,col4 = st.columns(4)

    if col1.button('Poème'):
        poeme=wq(texte)
        st.write(poeme)

    if col2.button('Harry Potter'):
        poeme2=wq(texte,data2)
        st.write(poeme2) 
else:    
    # Créer une zone de texte de plusieurs lignes
    texte3 = st.text_area("Entrez votre livre", value="", height=200)    

    if st.button('Texte personnalisé'):
        poeme3=wq(texte,texte3)
        st.write(poeme3) 


    