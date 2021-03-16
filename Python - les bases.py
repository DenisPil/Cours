        TYPE D'OBJET EN PYTHON :
        


Nombres (int and float) = """ Il existe deux grands types de nombres en Python : les entiers (integers) et 
                                    les décimaux (floats). Tous deux n’ont besoin ni de guillemets, de parenthèses ou de crochets. """
 
Chaînes de caractères (strings) = """ Il s’agit d’un ensemble de signes (lettres, chiffres, ponctuation, caractères spéciaux, …) 
                                      délimités par "  "   . """

Booléens = """ Un booléen est une information True ou False. Ce type est très utilepour comparer des valeurs entre elles. """
               
Listes = """ Une liste contient une succession de plusieurs objets. On les reconnaît aisément 
             car elles sont entourées de crochets [ ] et comprennent des valeurs séparées par des virgules.
             Une liste contenant des flottants, une liste contenant des chaînes de caractères, ou d'autre listes...
             et une liste mélangeant ces objets de différents types."""
 
Tuples = """ Les tuples servent à créer des structures dont le nombre d'éléments ne bouge pas. On dit qu’ils sont immuables. 
             On ne peut ajouter ou supprimer un élément.
             Elles commencent par () , un ensemble d’objets séparés par des virgules.
             On définit le contenu d'un tuple (les objets qu'il doit contenir) lors de sa création, 
             mais on ne peut en ajouter ou en retirer par la suite."""

Dictionnaires = """ Un dictionnaire est un ensemble de valeurs auxquelles vous pouvez accéder grâce d’autres objets.
                    Définir un dictionnaire commence par écrire une accolade { }. Puis nous indiquons  la clé, 
                    deux points et la valeur associée. """
 
 
 


 
        MOTS CLES :
        
        


        

if   =      """ Commencez par écrire if, puis vous indiquez la condition à remplir et terminez la ligne par deux points """
                ex : >>> if user_answer == "":
                
elif =      """ Intégrer une condition à la suite d'une autre condition """
                ex : >>> elif user_answer != "":
                
else =      """ Définir ce qu'il se passe si la condition n’est pas remplie """
                ex : >>> else:
pass =      """ Ne sert pas vraiment à quitter un programme. Nous l'utilisons quand aucune action n'est requise.
                Par défaut, si vous n'indiquez rien, Python considèrera qu'il y a une erreur. Il considèrera que vous avez dû oublier un élément. En écrivant 
                pass , vous lui dites : je te demande de ne rien faire. Et Python passera son chemin, tout simplement. """
                ex : >>> pass

type  =     """ La fonction "type" renvoie le type de la variable passée en paramètre (nom_d_une_variable). """
                ex : type(nom_de_la_variable)

def  =      """ Une fonction est un ensemble de commandes regroupées sous un seul nom unique. Pour définir une fonction,
                vous utilisez le mot-clé “def”, suivi d’un nom, de parenthèses(les paramètres) et de deux points. Puis vous indentez 
                tout ce qui se trouve à l’intérieur. """  
                ex : >>> def get_random_quote(): 
               
                ex 2:>>> def table(nb, max=10):  #"nb" et "max=10" sont des paramètres
                     # J'ai accès aux "nb" et "max" puisque je les ai passées en paramètre en lançant ma fonction.
         
return =    """ Pour que votre fonction "def" renvoie une certaine valeur.Il existe des fonctions comme "print" qui
                ne renvoient rien (attention, « renvoyer » et « afficher » sont deux choses différentes) et des fonctions telles que
                "input" ou "type" qui renvoient une valeur. Vous pouvez capturer cette valeur en plaçant une variable devant. En effet,
                les fonctions travaillent en général sur des données et renvoient le résultat obtenu, suite à un calcul par exemple. """ 
                ex : >>> def decomposer(entier, divise_par):
                            p_e = entier // divise_par
                            reste = entier % divise_par
                         return p_e, reste
                # Et on peut ensuite capturer la partie entière et le reste dans deux variables, au retour de la fonction
                     >>> partie_entiere, reste = decomposer(20, 3)
                     >>> partie_entiere
                     6
                     >>> reste
                     2

input() =   """ permet de “demander” son avis à l’utilisateur ! Le message affiché est passé en paramètre à la fonction.
                Quand elle est exécutée, elle renvoie la valeur saisie par l’utilisateur. 
                Pour l’utiliser vous devez l’assigner à une variable. """
                ex : >>> user_answer = input("")
               
while =     """ While est la traduction de “tant que...”. Concrètement, la boucle s’exécutera tant qu’une condition est remplie 
                (donc tant qu’elle renverra la valeur True) """          
                ex : >>>i = 0
                        while i < max:
                            print(i + 1, "*", nb, "=", (i + 1) * nb)
                            i += 1
           
print =     """ La fonction "print" est dédiée à l'affichage uniquement. Le nombre de ses paramètres est variable, c'est-à-dire
                que vous pouvez lui demander d'afficher une ou plusieurs variables.  """           
                ex : >>> print("a =", a, "et b =", b ) 

and =       """ Signifie « et » en anglais qui va nous rendre ici un fier service. En effet, on cherche à tester à la fois si "a" est 
                supérieur ou égal à 2 et inférieur ou égal à 8. On peut donc réduire ainsi les conditions imbriquées. """ 
                ex : >>> if a>=2 and a<=8:
                
or =        """ Evaluer notre condition différemment ( de "and" ). Nous allons chercher à savoir si "a" n'est pas dans l'intervalle. 
                La variable ne se trouve pas dans l'intervalle si elle est inférieure à 2 ou supérieure à 8. """
                ex : >>> if a<2 or a>8:

in =  """ Un autre opérateur logique utile en Python est l’opérateur  in. Cela renvoie  True  lorsqu’une valeur est trouvée dans une séquence (un string ou une liste) ;False,  sinon. """
          ex : maListe = [4, 2, 3, 2, 10]
               maListeDeString = ["a", "b", "c", "d"]
               monString = "La météo est vraiment bien aujourd'hui !"
               
               4 in maListe # True
               0 in maListe # False
               0 in maListeDeString # False
               "c" in maListeDeString # True
               "e" in maListeDeString # False
               "météo" in monString # True
               "vraiment" in monString # True
               "pluie ?" in monString # False 

del =       """ L'utilisation de "del" supprime une variable """
                ex : >>> del varialbe 


for/in =    """ L'instruction "for" travaille sur des séquences. Elle est en fait spécialisée dans le parcours d'une séquence de plusieurs
                données. 
                Les chaînes de caractères sont des séquences… de caractères ! Vous pouvez parcourir une chaîne de caractères 
                ce qui est également possible avec "while"."""
                ex : >>> chaine = "Bonjour les ZER0S"
                         for lettre in chaine:
                             print(lettre)
            """ Si l’on veut vraiment boucler via une valeur itérative entière en Python pour revenir à une boucle for plus classique en termes de programmation, on va en réalité devoir contourner 
                le problème. Vous  allez itérer au travers d’une liste qui contiendra les différentes valeurs de votre entier itératif. Pour cela, 
                vous utiliserez la fonction  range(début, fin, pas), qui va générer une liste de nombres selon trois paramètres.
                début  : le premier nombre de la  séquence;
                fin  : correspond au dernier nombre de la séquence non inclus. La fonction va générer des nombres de  début  à  fin- 1;
                pas  : le pas entre chaque nombre généré.
                La variable itérative peut prendre n’importe quel nom. Lorsque l’on itère sur un nombre entier, on utilise généralement des valeurs comme  i,  j  ou  k. 
                Sinon, il est préférable d’utiliser des noms explicites, comme vu ci-dessus (elt  étant l’abréviation d’élément)."""
                ex : for i in range(0, 5, 1):
                         print(i) # -> affiche de 0 à 4 par pas de 1 (fin - 1)
                     
                     for i in range(0, 5):
                          print(i) # -> affiche de 0 à 4 également (le pas par défaut est 1)
                     
                     for i in range(5):
                          print(i) # -> affiche de 0 à 4 également (le début par défaut est 0)
                     
                     for i in range(0, 5, 2):
                          print(i) # -> affiche 0, 2 puis 4  


"""Comme avec les opérations numériques, les opérateurs logiques respectent les priorités d’opérations : 
   l’opérateur not  est réalisé en premier, ensuite l’opérateur and  puis l’opérateur  or. """
   ex : False or True and True # True
        not(False) and True or False # True
""" Vous pouvez également utiliser des parenthèses pour changer l’ordre. """
    ex : (True and False) or True # True
         not(True and False or not(True)) # True


break =     """ Permet tout simplement d'interrompre une boucle. """ 
                ex : >>> break
               
continue =  """ Permet de… continuer une boucle, en repartant directement à la ligne du "while" ou "for". """
                ex : >>> continue

lambda =    """ Un autre moyen de créer des fonctions, des fonctions extrêmement courtes car limitées à une seule instruction. """
                ex : >>> lambda x: x * x    
                     >>> f = lambda x: x * x  # pour appeler la fonction 
                     >>> f(x)
                
import =    """ La méthode "import" est utilisé pour importer un module" """
                ex : >>> import math 
                     >>> math.sqrt(16)  
                 
import/as = """ Vouloir changer le nom de l'espace de noms dans lequel sera stocké le module importé. """
                ex : >>> import math as mathematiques
                     >>> mathematiques.sqrt(25)
                
from/import=""" Besoin, dans notre programme, que de la fonction renvoyant la valeur absolue d'une variable.
                Dans ce cas, nous n'allons importer que la fonction, au lieu d'importer tout le module. """
                ex : >>> from math import fabs
                     >>> fabs(-5)

                                   
                
try =       """ Le bloc d'instructions à essayer. """
                ex : >>> try :
                
except =    """ Le mot-clé "except" suivi, une fois encore, des deux points « : ». Il se trouve au même niveau d'indentation que le "try".
                Le bloc d'instructions qui sera exécuté si une erreur est trouvée dans le premier bloc. """
                ex : >>> except:         //       
                     >>>   print("")
                
                ex2: >>> except TypeError:

finally =   """ Permet d'exécuter du code après un bloc "try", quel que soit le résultat de l'exécution dudit bloc. Le bloc "finally"
                est exécuté dans tous les cas de figures. Quand bien même Python trouverait une instruction "return" dans votre bloc
                "except" par exemple, il exécutera le bloc "finally". """              
                ex :>>> try:
                        # Test d'instruction(s)
                    >>> except type_de_l_exception:
                        # Traitement en cas d'erreur
                    >>> finally:
                        # Instruction(s) exécutée(s) qu'il y ait eu des erreurs ou non
                
raise =     """ On lève une exception que l'on intercepte immédiatement ou presque. """
                ex : >>> raise ValueError ("")

assert =    """ Les assertions sont un moyen simple de s'assurer, avant de continuer, qu'une condition est respectée. 
                En général, on les utilise dans des blocs "try" … "except". Si le test renvoie "True", l'exécution se poursuit normalement.
                Sinon, une exception "AssertionErrorest" levée. """                 
                ex : >>> assert test

class =     """ Chaque objet est une "classe" en programmation.  En écrivant le mot-clé  class, son nom puis deux points,                
                la premiere lettres en MAJUSCULE. Une instance est un objet créé à partir d'une classe. Elle partage avec les autres instances 
                de sa classe les mêmes attributs (variable) et méthodes(focntion). Les valeurs de ces attributs varient en fonction des instances."""
                ex : >>> class Agent :    
                ex2 :>>> first_agent = Agent()    #création d'une instance 

sum =      """ La fonction sum() ajoute la valeur de départ(start) et les éléments de l’itérable donné de gauche à droite.
               iterable – itérable (liste, tuple, dictionnaire, etc.) dont la somme de l’élément doit être trouvée. Normalement, 
               les éléments de l’itérable doivent être des nombres.
               start(facultatif) – cette valeur est ajoutée à la somme des éléments de l’itérable. La valeur par défaut de start est 0."""
               ex : >>> sum([1, 2, 3, 4]) # somme des valeurs dans une liste
                    10
                    >>> 
                    >>> sum((1, 2, 3, 4)) # somme des valeurs dans un tuple
                    10
                    >>> 
                    >>> sum({1, 2, 3, 4}) # somme des valeurs dans une ensemble
                    10
                    >>> 
                    >>> sum({1: "blue", 2: "green", 3: "red"}) # somme des valeurs dans un dictionnaire
                    6 
               ex2: >>> sum([1, 2, 3, 4], 10)
                    20 

set =      """ Unset(ensemble) est un objet conteneur (lui aussi), très semblable aux listes sauf 
               qu'il ne peut contenir deux objets identiques. Vous ne pouvez pas trouver deux fois dans unsetl'entier3par exemple."""
               ex :  >>>mon_du_set = {'pseudo', 'mot de passe'}
      
sep="" =  """  Ca va être ce qui est entre les string que tu mets dans ton print """
               ex : >>> parametres = {"sep":" >> ", "end":" -\n"}
                    >>> print("Voici", "un", "exemple", "d'appel", **parametres)
                    Voici >> un >> exemple >> d'appel - 

id() =     """ Pour approcher de plus près les références, vous avez la fonctionidqui prend en paramètre un objet. 
               Elle renvoie la position de l'objet dans la mémoire Python sous la forme d'un entier""" 
               ex : >>> malist = [4, 5, 6]
                    >>> id(malist)
                    3073716802056

is =       """ Compare les ID des objets de part et d'autre."""
               ex :  >>> ma_liste1 = [1, 2]
                     >>> ma_liste2 = [1, 2]
                     >>> ma_liste1 == ma_liste2 # On compare le contenu des listes
                     True
                     >>> ma_liste1 is ma_liste2 # On compare leur référence
                     False   

global =   """ On le place généralement après la définition de la fonction, juste en-dessous de la "docstring" , 
               cela permet de retrouver rapidement les variables globales On précise derrière ce mot-clé 
               le nom de la variable à considérer comme globale.  En précisantglobal i, Python permet l'accès 
               en lecture et en écriture à cette variable, ce qui signifie que vous pouvez changer sa valeur par affectation.""" 
               ex : >>> i = 4 # Une variable, nommée i, contenant un entier
                    >>> def inc_i():
                    ...     """Fonction chargée d'incrémenter i de 1"""
                    ...     global i # Python recherche i en dehors de l'espace local de la fonction
                    ...     i += 1                                     
                                    









      
        METHODE :  """ Chaque type d’objet dispose de différentes méthodes qui nous permettent d’interagir avec lui. Une méthode est une fonction
                       associée à un type d’objet bien précis. En d’autres termes, une action que seul ce type d’objet peut faire. 
                       Les objets, que j'ai présentés comme des variables, pouvant contenir d'autres variables ou fonctions 
                       (que l'on appelle méthodes). On appelle une méthode d'un objet grâce à "objet.methode()"."""
        



                     
            Méthode pour "CHAINE DE CHARACTER" :             
            """Ceci est extrêmement important. Aucune des méthodes de chaînes ne modifie l'objet d'origine mais
               qu'elles renvoient toutes un nouvel objet, qui est la chaîne modifiée.""" 




.lower() =  """ Every word in lower case. La fonction "lower" est une fonction de la variable "chaine".
               Notez que "chaine.lower() "renvoie la chaîne en minuscules mais ne modifie pas la chaîne.
               Dans lower() les () représente les parametres  """
            ex: >>> "HELLO WORLD".lower()
                "hello world!"

.split() =  """ Pour « convertir » une chaîne en liste. Quand on appelle la méthode "split" , celle-ci découpe 
                la chaîne en fonction du paramètre donné. Ici la première case de la liste va donc du début de 
                la chaîne au premier espace (non inclus), la deuxième case va du premier espace au second, 
                et ainsi de suite jusqu'à la fin de la chaîne."""
            ex: >>> “hello world!”.split()
                ['hello', 'world!']
            ex2:>>> “hello world!”.split(" ") #On passe en paramètre de la méthode "split" une chaîne contenant un unique espace.
                ['hello', 'world!']

.strip() =  """ Remove all white spaces at the beginning and the end of a string."""
            ex: >>> “       hello world!      “.strip()
                “hello world!”

.capitalize()= """ First letter in the first word in capital letters."""
                   ex: >>> "hello world!".capitalize()
                       "Hello world!"

.upper() =  """ Every word in upper case."""
            ex: >>> "hello world!".upper()
                "HELLO WORLD!"

.find() =  """ retourne soit l’indice de la première occurrence de la chaîne passée en argument, soit -1 si elle ne la trouve pas."""
               ex : texte = "voici un exemple"
                    print (texte.find('un'))
                    6  # c'est le 6 caracteres  

.startswith = """ "startswith"  est une méthode de la classe string, qui retourne  True  lorsque la chaîne de caractères commence exactement par le string passé en paramètre ;
                   False, sinon. Vous pourriez par exemple utiliser cette expression pour réaliser une action si une phrase commence bien par un mot en particulier.""" 
                   ex : meteo = "La météo est chouette !"
                        meteo.startswith("La météo") # -> True                                

.format() = """  Permet de remplacer des valeurs à l’intérieur d’une chaîne à la manière d’un texte à trous."""   
            ex : >>> "{} a dit : {}".format("George Abitbol", "Monde de merde.")
                 >>> "George Abitbol a dit : Monde de merde."
            
            ex2: >>> "{character} a dit : {quote}".format(character="George Abitbol", quote="Monde de merde.") 
                 >>> "George Abitbol a dit : Monde de merde."

            ex3: >>> "Je m'appelle {0} {1} ({3} {0} pour l'administration) et j'ai {2}  "ans.".format(prenom, nom, age, nom.upper())) 

            """  On peut également nommer les variables que l'on va afficher, c'est souvent plus intuitif que d'utiliser leur indice.""" 
            ex4: # formatage d'une adresse
                >>> adresse = """
                {no_rue}, {nom_rue}
                {code_postal} {nom_ville} ({pays})
                """.format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
                >>> print(adresse)

.center(20)=""" Permet de centrer une chaîne. On lui passe en paramètre la taille de la chaîne que l'on souhaite obtenir."""
                ex :>>> titre = "introduction"
                    >>> titre.upper().center(20)
                    '    INTRODUCTION    '
                #. Dans cet exemple,"titre" contient la chaîne'introduction', chaîne qui (en minuscules ou en majuscules)
                #  mesure 12 caractères. On demande à "center" de centrer cette chaîne dans un espace de 20 caractères.                

titre.upper().center(20) = """ Sur quel objet travaille "center" ? Sur "titre" ? Non. Sur la chaîne renvoyée par "titre.upper()", 
                               c'est-à-dire le titre en majuscules. C'est pourquoi on peut « chaîner » ces deux méthodes : "upper", 
                               comme la plupart des méthodes de chaînes, travaille sur une chaîne et renvoie une chaîne… 
                               qui elle aussi va posséder les méthodes propres à une chaîne de caractères. """

chaine[] =   """ On précise entre crochets[]l'indice (la position du caractère auquel on souhaite accéder). """ 
                 ex : >>> chaine = "Salut les ZER0S !"
                      >>> chaine[0] # Première lettre de la chaîne
                      'S' 

len() =     """ On peut obtenir la longueur de la chaîne (le nombre de caractères qu'elle contient)."""
                ex : >>> chaine = "Salut"
                     >>> len(chaine)
                     5

La concaténation de chaînes = """  Le signe « + » utilisé pour ajouter des nombres est ici utilisé pour concaténer deux chaînes."""
                                   ex : >>> prenom = "Paul"
                                        >>> message = "Bonjour"
                                        >>> chaine_complete = message + " " + prenom # les "" c est pour ajouter l'espace.
                                        >>> print(chaine_complete) # Résultat :
                                        Bonjour Paul

Concaténer, chaînes + nombres = """ On appelle "str" pour convertir un objet en une chaîne de caractères """
                                    ex: >>> age = 21
                                        >>> message = "J'ai " + str(age) + " ans."
                                        >>> print(message)
                                        J'ai 21 ans.
                    
Méthode de parcours par while = """Pour parcourir une chaîne grâce à la boucle "while" ."""
                ex : chaine = "Salut"
                     i = 0 # On appelle l'indice 'i' par convention
                     while i < len(chaine):
                         print(chaine[i]) # On affiche le caractère à chaque tour de boucle
                         i += 1 

Sélection de chaînes = """ Comment sélectionner une partie de la chaîne."""
                           ex : >>> presentation = "salut"
                                >>> presentation[0:2] # On sélectionne les deux premières lettres
                                'sa'                   

                           ex2: >>> presentation[2:len(presentation)] # On sélectionne la chaîne sauf les deux premières lettres
                                'lut' 

                       """ on peut sélectionner du début de la chaîne jusqu'à un indice, ou d'un indice jusqu'à la fin de la chaîne."""
                           ex : >>> presentation[:2] # Du début jusqu'à la troisième lettre non comprise
                                'sa'
                                >>> presentation[2:] # De la troisième lettre (comprise) à la fin
                                'lut'            










            Méthode pour "INT ET FLOAT" : 
        



.is_integer = """ Permet de vérifier si un nombre est un entier ou un décimal."""
                  ex : >>> (2.5).is_integer()
                  False  

pow =   """   permet de calculer a puissance b. Elle est équivalente à l’écriture  a**b"""
              ex : print (pow(4, 2)) 
                   
abs() =  """  retourne la valeur absolue d’un nombre."""
              ex : print (abs(-100))                    







             Méthode pour " LES LISTES [] " 





             """Ceci est extrêmement important. Dans le chapitre précédent, nous avons vu qu'aucune des méthodes de chaînes ne modifie 
                l'objet d'origine mais qu'elles renvoient toutes un nouvel objet, qui est la chaîne modifiée. Ici c'est le contraire :
                les méthodes de listes ne renvoient rien mais modifient l'objet d'origine."""
                ex : >>> liste1 = [1, 5.5, 18]
                     >>> liste2 = liste1.append(-15) # On ajoute -15 à liste1
                     >>> liste1                      # On affiche liste1
                     [1, 5.5, 18, -15]
                     >>> # Cette fois, l'appel de la méthode a modifié l'objet d'origine (liste1)
                     ... # Voyons ce que contient liste2
                     ... liste2
                     >>> # Rien ? Vérifions avec print
                     ... print(liste2)
                     None
           
            ex : ma_liste ["George Abitbol", "Zyke", "Bernard Friot", "Goku"]    
                 ma_liste2 [] 

ma_liste[]= """ Permet d'accéder aux différents éléments, indiquez son index entre crochets."""                
                ex : >>> my_list[3]
                     "Goku"
                 
.index  =   """ Pour connaitre l'index d'un élément. """                     
                ex : >>> ma_liste.index("Zyke")    
                     1
                    
.append =   """ On passe en paramètre de la méthode "append" l'objet que l'on souhaite ajouter à la fin de la liste. """                                                                   
                ex : >>> ma_liste.append("Tuan")    
                    
.insert =   """ Ajouter un élément à un certain index. Le premier argument est l’index, le second la valeur à insérer."""                   
                ex : >>> ma_liste.insert(2, "Gandalf")  

ma_liste[]= """ Modifier un élément : y accéder grâce à son index et lui donner une nouvelle valeur."""
                ex : >>> ma_liste[1] = "Sauron"

.extend =   """ On peut également agrandir des listes en les concaténant avec d'autres."""
                ex : ma_liste.extend(ma_liste2)  

                ex2 : ma_liste += ma_liste2 # Identique à extend

.pop()  =   """ Supprimer le dernier élément de la liste et renvoyer sa valeur. 
                De manière optionnelle, vous pouvez passer en paramètre l'index de l'élément à supprimer."""                    
                ex : >>> ma_liste.pop()      
                     "Tuan"
               
                ex2: >>> ma_liste.pop(0)     
                     "George Abitbol"   
                    
.remove=   """ Permet de supprimer des éléments de la liste grâce à la méthode "remove" qui
               prend en paramètre non pas l'indice de l'élément à supprimer, mais l'élément lui-même."""                    
               ex : >>> ma_liste.remove("Zyke")    

del =      """ On peut également utiliser "del" pour supprimer des éléments d'une séquence, comme une liste,
               et c'est ce qui nous intéresse ici. Prend en paramètre l'indice de l'élément à supprimer"""
               ex : >>> del ma_liste[0]             
                    
len()   =   """ Connaitre le nombre d’éléments dans une liste."""                 
                ex : >>> len(ma_liste)    
                   
[-1]    =   """ Accéder au dernier élément d’une liste."""
                ex : >>> ma_liste[-1]

= list() =  """ demandé à Python de créer un nouvel objet basé surma_liste1. Du coup, 
                les deux variables ne contiennent plus la même référence : elles modifient des objets différents."""
                ex : >>> ma_liste1 = [1, 2, 3]
                     >>> ma_liste2 = list(ma_liste1) # Cela revient à copier le contenu de ma_liste1
                     >>> ma_liste2.append(4)
                     >>> print(ma_liste2)
                     [1, 2, 3, 4]
                     >>> print(ma_liste1)
                     [1, 2, 3]

.join =     """ Des listes aux chaînes, c'est-à-dire si on a une liste contenant plusieurs chaînes 
                de caractères que l'on souhaite fusionner en une seule. En paramètre de la méthode "join" , 
                on passe la liste des chaînes que l'on souhaite « ressouder ». La méthode va travailler 
                sur l'objet qui l'appelle, ici une chaîne de caractères contenant un unique espace."""
                ex: >>> ma_liste = ['Bonjour', 'à', 'tous']
                    >>> " ".join(ma_liste)
                    'Bonjour à tous'   
Parcourir une list = ex : >>> i = 0 # Notre indice pour la boucle while
                          >>> while i < len(ma_liste):
                          ...     print(ma_liste[i])
                          ...     i += 1 # On incrémente i, ne pas oublier ! 

            """ Cette méthode est cependant préférable """
                     ex : >>> for elt in ma_liste: # elt va prendre les valeurs successives des éléments de ma_liste
                          ...     print(elt)           

enumerate = """ Prend en paramètre une liste et renvoie un objet qui peut être associé à une liste contenant deux valeurs 
                par élément : l'indice et l'élément de la liste parcouru. Quand on parcourt chaque élément de 
                l'objet renvoyé par "enumerate", on voit des tuples qui contiennent deux éléments :
                d'abord l'indice, puis l'objet se trouvant à cet indice dans la liste passée en argument à la fonction "enumerate".
                Quand on utilise "enumerate", on capture l'indice et l'élément dans deux variables distinctes.  """
                ex : >>> for i, elt in enumerate(ma_liste):
                     ...     print("À l'indice {} se trouve {}.".format(i, elt))  # i = l'indice (le num de la place dans la liste) et elt = element de la liste

                ex2: >>> for elt in enumerate(ma_liste):
                     ...     print(elt) 

.sort() =   """ Permet de trier une liste. """
                ex : >>> malist = (1,45,87,2,385,27) 
                     >>> malist.sort(reverse=False) #False
                     >>> malist
                     [1, 2, 27, 45, 87, 385]
                ex2: >>> malist = (1,45,87,2,385,27)
                     >>> malist.sort(reverse=True)  #True
                     >>> malist 
                     [385, 87, 45, 27, 2, 1]

sorted()=   """ Permet de trier une liste. Avec la fonction sorted n'a pas modifié la liste, elle a juste retournée une 
                nouvelle liste triée. La méthode de liste sort, elle, a travaillée sur notre liste et l'a modifiée. """
                ex : >>> malist = (1,45,87,2,385,27) 
                     >>> sorted (malist)
                     [1, 2, 27, 45, 87, 385]

key =      """ La méthode list.sort ou la fonction sorted ont tous deux un paramètre optionnel, appelé "key". Cet argument attend... 
               une fonction. La fonction à passer en paramètre prend un élément de la liste et retourne ce sur quoi doit s'effectuer le tri. """                      
               ex : >>> sorted(etudiants, key=lambda colonnes: colonnes[2])
                    [('Thomas', 11, 12), ('Charles', 12, 15), ('Damien', 12, 15), ('Clément', 14, 16),('Oriane', 14, 18)]
               """ D'abord, après le mot clé lambda, les arguments de la fonction à créer, séparés par une virgule si il y en a plusieurs 
               ;Ensuite, les deux points (:) ;Et ensuite le retour de la fonction."""


 list comprehension = """ Une liste dans laquelle vous effectuez une opération pour créer cette même liste. 
                          Les compréhensions de liste permettent de parcourir une liste en en renvoyant une seconde, modifiée ou filtrée. """
                         ex : >>> liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                              >>> [nb for nb in liste_origine if nb % 2 == 0]
                              [2, 4, 6, 8, 10]
                        
                         ex2:>>> liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                             >>> liste2 = [nb for nb in liste_origine if nb % 2 == 0]
                             [2, 4, 6, 8, 10]
                      """ On rajoute à la fin de l'instruction une condition qui va déterminer quelles valeurs seront transférées 
                          dans la nouvelle liste. Ici, on ne transfère que les valeurs paires. Au final, on se retrouve donc avec 
                          une liste deux fois plus petite que celle d'origine.""" 
                      
                      """ Mélangeons un peu tout cela"""
                          ex : >>># On change le sens de l'inventaire, la quantité avant le nom
                                  inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]
                                  # On trie l'inventaire inversé dans l'ordre décroissant
                                  inventaire_inverse.sort(reverse=True)
                                  # Et on reconstitue l'inventaire
                                  inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in inventaire_inverse]
                                    
                                                       



        def LES_LISTES_ET_PARAMETRES_DE_FONCTIONS()  



Les fonctions dont on ne connaît pas à l avance le nombre de paramètres =
             """ On place une étoile "*" devant le nom du paramètre qui accueillera la liste des arguments.
                 On peut appeler la "fonction_inconnue" avec un nombre indéterminé de paramètres, allant de 0 
                 à l'infini (enfin, théoriquement). Le fait de préciser une étoile "*" devant le nom du 
                 paramètre fait que Python va placer tous les paramètres de la fonction dans un tuple, 
                 que l'on peut ensuite traiter comme on le souhaite."""
                 ex :>>> def fonction_inconnue(*parametres):
                 #On place une étoile "*" devant le nom du paramètre qui accueillera la liste des arguments
                 #Le fait de préciser une étoile "*" devant le nom du paramètre fait que Python va placer tous 
                 #les paramètres de la fonction dans un tuple, que l'on peut ensuite traiter comme on le souhaite.
                     ...     """Test d'une fonction pouvant être appelée avec un nombre variable de paramètres"""
                     ...     
                     ...     print("J'ai reçu : {}.".format(parametres))
                     ... 
                     >>> fonction_inconnue() # On appelle la fonction sans paramètre
                     Jai reçu : ().
                     >>> fonction_inconnue(33)
                     Jai reçu : (33,).
                     >>> fonction_inconnue('a', 'e', 'f')
                     Jai reçu : ('a', 'e', 'f').
                     >>> var = 3.5
                     >>> fonction_inconnue(var, [4], "...")
                     Jai reçu : (3.5, [4], '...').
                 ex2: def fonction_inconnue(nom, prenom, *commentaires):
                 #Si on définit une liste variable de paramètres, elle doit se trouver après la liste des paramètres standard.  


Transformer une liste en paramètres de fonction =
             """ Si vous avez un tuple ou une liste contenant des paramètres qui doivent être passés à une fonction, 
                 vous pouvez très simplement les transformer en paramètres lors de l'appel. Là, on a une liste contenant 
                 des paramètres et on la transforme en une liste de paramètres de la fonction "print". Donc, au lieu d'afficher 
                 la liste proprement dite, on affiche tous les nombres, séparés par des espaces.
                 Si on ne connaît pas la fonction que l'on appelle, c'est très pratique.
                 Essayez de garder à l'esprit ce mécanisme de transformation.
                 On utilise une étoile * dans les deux cas. Si c'est dans une définition de fonction, cela signifie que les paramètres 
                 fournis non attendus lors de l'appel seront capturés dans la variable, sous la forme d'un tuple. Si c'est dans un appel de fonction,
                 au contraire, cela signifie que la variable sera décomposée en plusieurs paramètres envoyés à la fonction."""
                 ex : >>> liste_des_parametres = [1, 4, 9, 16, 25, 36]
                      >>> print(*liste_des_parametres)
                      1 4 9 16 25 36











            Méthode pour "DICTIONNAIRES"
            

        

          
            ex : >>> nom_dico = {"quotes": ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",n\ 
                                "On doit pouvoir choisir entre s'écouter parler et se faire entendre."],n\ 
                                "characters": ["alvin et les Chipmunks","Babar", "betty boop", "balimero", "casper","le chat potté", "Kirikou"]}
        
dict() =         """ Création d'un dictionnaire. """                   
                    ex : >>> mon_dictionnaire = dict()

                    ex2: >>> mon_dictionnaire = {}

nom_dico["la_clé"] = "la_valeur" = """ Nous indiquons entre crochets la clé à laquelle nous souhaitons accéder. Si la clé n'existe pas, 
                                       elle est ajoutée au dictionnaire avec la valeur spécifiée après le signe "=".Sinon, l'ancienne 
                                       valeur à l'emplacement indiqué est remplacée par la nouvelle :"""                   
                     ex : >>> mon_dictionnaire = {}
                          >>> mon_dictionnaire["pseudo"] = "Prolixe"
                          >>> mon_dictionnaire["mot de passe"] = "*"
                          >>> mon_dictionnaire
                          {'mot de passe': '*', 'pseudo': 'Prolixe'} 

nom_dico[la_clé]=""" Pour accéder à la valeur d'une clé précise """ 

nom_dico[""]=    """ Accéder à la valeur d’un élément stocké dans un dictionnaire : grâce à sa clé. """               
                     ex : >>> program["characters"]      
                        [“alvin et les Chipmunks”, “Babar”, “betty boop”, “balimero”, “casper”, “le chat potté”, “Kirikou”]

nom_dico[""][] = """En ajoutant l’index de l’élément souhaité à la suite, entre crochets ."""         
                    ex : >>> program["characters"][0]
                        "alvin et les Chipmunks"
                        
nom_dico[""] =   """ Remplacer ou ajouter une valeur : même méthode que pour une liste. """
                     ex : >>> program["characters"] = "Un nouveau nom"        
                        
.update =       """  Mettre à jour ou ajouter plusieurs valeurs en même temps."""          
                      ex : >>> program.update({"characters" : ["Alvin", "Père Noël"], "quotes": ["Une citation unique qui sera sauvegardée"]})
   
.pop() =        """  Supprimer une clé et renvoyer sa valeur. Vous pouvez utiliser cette même méthode sur une liste ! """       
                     ex : >>> program.pop("quotes")
                     "quotes"

.keys() =       """ La méthode "keys" (« clés » en anglais) renvoie la liste des clés contenues dans le dictionnaire. En vérité, 
                    ce n'est pas tout à fait une liste mais c'est une séquence qui se parcourt comme une liste. Les dictionnaires 
                    n'ont pas de structure ordonnée, gardez-le à l'esprit."""  
                    ex : >>> fruits = {"pommes":21, "melons":3, "poires":31}
                         >>> for cle in fruits.keys():
                         ...     print(cle)
 
                    ex2: >>> fruits = {"pommes":21, "melons":3, "poires":31}
                         >>> for cle in fruits:
                         ...     print(cle) 

.values() =     """ On peut aussi parcourir les valeurs contenues dans un dictionnaire. Pour ce faire, on utilise la méthode "values"."""
                    ex : >>> fruits = {"pommes":21, "melons":3, "poires":31}
                         >>> for valeur in fruits.values():
                         ...     print(valeur)
                """ Cette méthode est peu utilisée pour un parcours car il est plus pratique de parcourir la liste des clés, 
                    cela suffit pour avoir les valeurs correspondantes. Mais on peut aussi, bien entendu, l'utiliser dans une condition."""
                    ex: >>> if 21 in fruits.values():
                        ...     print("Un des fruits se trouve dans la quantité 21.")
                        ... 
                        Un des fruits se trouve dans la quantité 21.

.items() =      """  Permet de renvoyer une liste, contenant les couples clé : valeur, sous la forme d'un tuple."""  
                     ex : >>> fruits = {"pommes":21, "melons":3, "poires":31}
                          >>> for cle, valeur in fruits.items():
                          ...     print("La clé {} contient la valeur {}.".format(cle, valeur))                         

Les dictionnaires et paramètres de fonction = """ Pour capturer tous les paramètres nommés non précisés dans un dictionnaire, 
                                                  il faut mettre deux étoiles ** avant le nom du paramètre.Si vous passez des paramètres 
                                                  non nommés à cette fonction, Python lèvera une exception. """
                                                  ex : >>> def fonction_inconnue(**parametres_nommes):
                                                       ...     """Fonction permettant de voir comment récupérer les paramètres nommés
                                                       ...     dans un dictionnaire"""    
                                                       ...     print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))
                                                       >>> fonction_inconnue() # Aucun paramètre
                                                       J'ai reçu en paramètres nommés : {}
                                                       >>> fonction_inconnue(p=4, j=8)
                                                       J'ai reçu en paramètres nommés : {'p': 4, 'j': 8}

"""Si vous passez des paramètres non nommés à cette fonction, Python lèvera une exception.Ainsi, 
pour avoir une fonction qui accepte n'importe quel type de paramètres, nommés ou non, dans n'importe quel ordre, 
dans n'importe quelle quantité, il faut la déclarer de cette manière """
ex: def fonction_inconnue(*en_liste, **en_dictionnaire):
"""Tous les paramètres non nommés se retrouveront dans la variableen_listeet les paramètres nommés dans la variableen_dictionnaire."""

Transformer un dictionnaire en paramètres nommés d une fonction = """ Les paramètres nommés sont transmis à la fonction par un dictionnaire.
 Pour indiquer à Python que le dictionnaire doit être transmis comme des paramètres nommés, on place deux étoiles avant son nom ** dans 
 l'appel de la fonction."""
 ex : >>> parametres = {"sep":" >> ", "end":" -\n"}
      >>> print("Voici", "un", "exemple", "d'appel", **parametres)
      Voici >> un >> exemple >> d'appel - 





            Methode pour "LES CLASSES" :





parametres = """ Le premier paramètre doit être "self". En dehors de cela, un constructeur est une fonction plutôt classique : 
                 vous pouvez définir des paramètres, par défaut ou non, nommés ou non. Quand vous voudrez créer votre objet, 
                 vous appellerez le nom de la classe en passant entre parenthèses les paramètres à utiliser."""
                 ex : def __init__(self, nom, prenom):
                         """Constructeur de notre classe"""
                         self.nom = nom
                         self.prenom = prenom
                         self.age = 33
                         self.lieu_residence = "Paris"
                     >>> bernard = Personne("Micado", "Bernard")
                     >>> bernard.nom
                     'Micado'
                     >>> bernard.prenom
                     >>> bernard = Personne("Micado", "Bernard")
                     'Bernard'

attribut =   """ On définit notre attribut de classe directement dans le corps de la classe, sous la définition et la "docstring", 
                 avant la définition du constructeur. Quand on veut l'appeler dans le constructeur, on préfixe le nom de l'attribut 
                 de classe par le nom de la classe. Et on y accède de cette façon également, en dehors de la classe.
                 Les attributs sont des variables propres à notre objet, qui servent à le caractériser. """
                 ex : class Compteur:
                      """Cette classe possède un attribut de classe qui s'incrémente à chaque
                      fois que l'on crée un objet de ce type"""   
                         objets_crees = 0 # Le compteur vaut 0 au départ
                         def __init__(self):
                      """À chaque fois qu'on crée un objet, on incrémente le compteur"""
                         Compteur.objets_crees += 1 
                     >>> Compteur.objets_crees
                     0
                     >>> a = Compteur() # On crée un premier objet
                     >>> Compteur.objets_crees
                     1
                     >>> b = Compteur()
                     >>> Compteur.objets_crees
                     2

méthode =    """ Les méthodes sont plutôt des actions, agissant sur l'objet. Pour créer nos premières méthodes, 
                 nous allons modéliser… un tableau. Notre tableau va posséder une surface (un attribut) sur laquelle on 
                 pourra écrire, que l'on pourra lire et effacer. Pour créer notre 
                 classe "TableauNoir" et notre attribut "surface".
                 Les méthodes se définissent comme des fonctions, sauf qu'elles se trouvent dans le corps de la classe."""
                 ex : class TableauNoir:
                      """Classe définissant une surface sur laquelle on peut écrire,
                      que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
                      est 'surface'"""  
                         def __init__(self):
                     """Par défaut, notre surface est vide"""
                         self.surface = ""
                       def ecrire(self, message_a_ecrire):
                     """Méthode permettant d'écrire sur la surface du tableau.
                     Si la surface n'est pas vide, on saute une ligne avant de rajouter
                     le message à écrire"""
                         if self.surface != "":
                         self.surface += "\n"    
                         self.surface += message_a_ecrire
                     >>> tab = TableauNoir()
                     >>> tab.surface
                     ''
                     >>> tab.ecrire("Coooool ! Ce sont les vacances !")
                     >>> tab.surface
                     "Coooool ! Ce sont les vacances !"
                     >>> tab.ecrire("Joyeux Noël !") #Quand vous tapez "tab.ecrire(…)", Python va chercher la méthode "ecrire " 
                     >>> tab.surface                 #non pas dans l'objet "tab", mais dans la classe "TableauNoir"
                     "Coooool ! Ce sont les vacances !\nJoyeux Noël !"
                     >>> print(tab.surface)
                     Coooool ! Ce sont les vacances !
                     Joyeux Noël !


 

Méthodes de classe = """ Comme on trouve des attributs propres à la classe, on trouve aussi des méthodes de classe, qui ne travaillent 
                         pas sur l'instance "self " mais sur la classe même. Notre méthode de classe se définit exactement comme 
                         une méthode d'instance, à la différence qu'elle ne prend pas en premier paramètre 
                         "self" (l'instance de l'objet) mais "cls "(la classe de l'objet).Python reconnait une méthode de classe, 
                         il faut appeler la fonction "classmethod" qui prend en paramètre la méthode que l'on veut convertir 
                         et renvoie la méthode convertie."""                    
                         ex : class Compteur:
                                   objets_crees = 0 # Le compteur vaut 0 au départ
                                   def __init__(self):
                                   """À chaque fois qu'on crée un objet, on incrémente le compteur"""
                                   Compteur.objets_crees += 1
                                   def combien(cls):
                                   """Méthode de classe affichant combien d'objets ont été créés"""
                                   print("Jusqu'à présent, {} objets ont été créés.".format(cls.objets_crees))
                                   combien = classmethod(combien)
                                   >>> Compteur.combien()
                                   Jusqu à présent, 0 objets ont été créés.
                                   >>> a = Compteur()
                                   >>> Compteur.combien()
                                   Jusqu à présent, 1 objets ont été créés.           

self =     """  L'instance est représentée par le mot-clé self que nous passons en paramètre. Si nous reprenons
                la métaphore de la gaufre, la classe est le moule et  self  est la gaufre qui est en train de cuire dans le moule.
                Pour y associer un attribut, nous utiliserons un point.dès qu'on voitself, on sait que c'est un attribut ou 
                une méthode interne à l'objet qui va être appelé. """
                ex : def init(self):
                         self.agreeableness = 0                        

objet.attribut = nouvelle_valeur = """ Modifier un attribut d'un objet. """

.items() = """ De connaître tous les éléments d'un dictionnaire """
               ex : def __init__(self, agent_attributes):
                         for attr_name, attr_value in agent_attributes.items(): 

range()  = """ La méthode range() permet justement de créer une liste à partir d'une valeur minimale,
               d'une valeur maximale et d'un intervalle."""
               ex : class Zone
                    ...
                    def initialize_zones(self):
                          for longitude in range(self.MIN_LONGITUDE_DEGREES, self.MAX_LONGITUDE_DEGREES, self.WIDTH_DEGREES):        

dir  =     """ La fonction "dir" renvoie une liste comprenant le nom des attributs et méthodes de l'objet qu'on lui passe en paramètre.   
               La fonction "dir" se contente de renvoyer tout ce qu'il y a dans l'objet, sans distinction."""
               ex : # il faut crée un objet d'une class  un_test = Test()
                    >>> dir(un_test)

underscore =""" La convention veut qu'on n'accède pas, depuis l'extérieur de la classe, à un attribut commençant par un souligné "_".
encapsulation   On définit une première méthode, commençant elle aussi par un souligné "_", nommée "_get_lieu_residence". 
                C'est la même règle que pour les attributs : on n'accède pas, depuis l'extérieur de la classe, 
                à une méthode commençant par un souligné _."""
                ex: def __init__(self, nom, prenom):
                         """Constructeur de notre classe"""
                         self.nom = nom
                         self.prenom = prenom
                         self.age = 33
                         self._lieu_residence = "Paris" # Notez le souligné _ devant le nom
                    def _get_lieu_residence(self):
                         """Méthode qui sera appelée quand on souhaitera accéder en lecture
                         à l'attribut 'lieu_residence'"""       
                         print("On accède à l'attribut lieu_residence !")
                         return self._lieu_residence #Comme on est dans la classe, on a le droit de le (_) manipuler.
                    def _set_lieu_residence(self, nouvelle_residence):
                         """Méthode appelée quand on souhaite modifier le lieu de résidence"""
                         print("Attention, il semble que {} déménage à {}.".format(self.prenom, nouvelle_residence))
                         self._lieu_residence = nouvelle_residence
                    # On va dire à Python que notre attribut lieu_residence pointe vers une
                    # propriété
                    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)
                    # On définit dans notre propriété, dans l'ordre, 
                    # la méthode d'accès (l'accesseur) et celle de modification (le mutateur). 
                    >>> jean.lieu_residence
                    On accède à l'attribut lieu_residence !
                    'Paris'
                    >>> jean.lieu_residence = "Berlin"
                    Attention, il semble que Jean déménage à Berlin.
                    >>> jean.lieu_residence
                    On accède à l'attribut lieu_residence !
                    'Berlin'


_get_  =   """  Accesseur  On définit une première méthode, commençant elle aussi par un souligné "_", nommée "_get_lieu_residence".
                C'est la même règle que pour les attributs : on n'accède pas, depuis l'extérieur de la classe, à une méthode 
                commençant par un souligné "_". Si vous avez compris ma petite explication sur les accesseurs et mutateurs, 
                vous devriez comprendre rapidement à quoi sert cette méthode : elle se contente de renvoyer le lieu de résidence. 
                Là encore, l'attribut manipulé n'est pas "lieu_residence" mais "_lieu_residence". Comme on est dans la classe, 
                on a le droit de le manipuler."""
                ex : # le code "underscore"

set   =    """  Mutateur À la différence de l'accesseur, elle prend un paramètre : le nouveau lieu de résidence. 
                En effet, c'est une méthode qui doit être appelée quand on cherche à modifier le lieu de résidence, 
                il lui faut donc le nouveau lieu de résidence qu'on souhaite voir affecté à l'objet."""
                ex : #le code  de "underscore"

property = """  Enfin, la dernière ligne de la classe est très intéressante. Il s'agit de la définition d'une propriété. 
                On lui dit que l'attribut "lieu_residence" (cette fois, sans signe souligné _) doit être une propriété. 
                On définit dans notre propriété, dans l'ordre, la méthode d'accès (l'accesseur) et celle de modification (le mutateur)."""
                ex : # le code de "underscore"

issubclass =""" Comme son nom l'indique, elle vérifie si une classe est une sous-classe d'une autre classe. 
                Elle renvoie True si c'est le cas, False sinon."""
                ex : >>> issubclass(AgentSpecial, Personne) # AgentSpecial hérite de Personne
                     True
                     >>> issubclass(AgentSpecial, object)
                     True
                     >>> issubclass(Personne, object)
                     True
                     >>> issubclass(Personne, AgentSpecial) # Personne n'hérite pas d'AgentSpecial
                     False   

isinstance =""" Permet de savoir si un objet est issu d'une classe ou de ses classes filles."""  
                ex : >>> agent = AgentSpecial("Fisher", "18327-121")
                     >>> isinstance(agent, AgentSpecial) # Agent est une instance d'AgentSpecial
                     True
                     >>> isinstance(agent, Personne) # Agent est une instance héritée de Personne
                     True




                                                  __methodespeciale__
                      """ Les méthodes que nous allons voir permettent de travailler sur l'objet. 
                          Elles interviennent au moment de le créer et au moment de le supprimer."""


                          

__init__() = """ Python utilise une méthode spéciale pour créer votre instance. On l'appelle un constructeur car,
                 comme son nom l'indique, la méthode a pour responsabilité de construire une nouvelle instance à partir de votre classe.  
                 Heureusement, vous n'avez pas à créer cette méthode. Elle est déjà écrite en Python et vous n'avez qu'à l'appeler ! """
                 ex : def __init__():   # Par défaut, le constructeur crée une instance sans attribut = ()
                         self.nom = "Dupont"
                     >>> jean = Personne() # la Classe Personne
                     >>> jean.nom
                     'Dupont'

__dict__ = """ Par défaut, quand vous développez une classe, tous les objets construits depuis cette classe posséderont un attribut 
               spécial "__dict__" . Cet attribut est un dictionnaire qui contient en guise de clés les noms des attributs et, 
               en tant que valeurs, les valeurs des attributs. C'est un attribut un peu particulier 
               car ce n'est pas vous qui le créez, c'est Python."""
               ex : # il faut crée un objet d'une class  un_test = Test()
                    >>> un_test = Test()
                    >>> un_test.__dict__ 

__del__ =  """ vous voulez le supprimer explicitement, grâce au mot-clé "del"(del mon_objet). 
               Si l'espace de noms contenant l'objet est détruit, l'objet l'est également. 
               Si vous instanciez l'objet dans le corps d'une fonction : à la fin de l'appel à la fonction, 
               la méthode "__del__" de l'objet sera appelée. Enfin, si votre objet résiste envers et contre tout pendant 
               l'exécution du programme, il sera supprimé à la fin de l'exécution.si vous instanciez l'objet dans le corps d'une fonction : 
               à la fin de l'appel à la fonction, la méthode__del__de l'objet sera appelée. Enfin, 
               si votre objet résiste envers et contre tout pendant l'exécution du programme, il sera supprimé à la fin de l'exécution."""
               ex : def __del__(self):
                         """Méthode appelée quand l'objet est supprimé"""
                         print("C'est la fin ! On me supprime !")                    

 __lt__ =  """ C'est en effet cette méthode (utilisée pour la comparaison) qui est utilisée par Python pour trier une liste, 
               en comparant chacun de ses éléments. La méthode "__lt__" (lower than) correspond à l'opérateur "<". 
               On peut aussi utiliser l'argument key. Redéfinir la méthode "__lt__" est une bonne idée si notre objet 
               est un nombre (par exemple une durée ou bien une heure). Dans ce cas précis, il est préférable d'utiliser 
               l'argument key de la fonction sorted (ou de la méthode list.sort).  """
               ex : # il faut une class de départ et une liste
                    >>> sorted(etudiants, key=lambda etudiant: etudiant.moyenne)  #on peut classer par age ou par le nom   
                    <Étudiant Thomas (âge=11, moyenne=12)>
               """ Il arrive souvent que l'on veuille trier dans l'ordre inverse. Par exemple, que l'on veuille trier 
                   nos étudiants par ordre inverse d'âge (du plus grand au plus petit). Une solution est de trier et ensuite 
                   d'inverser la liste, mais là encore, il existe plus rapide : l'argument reverse.C'est un argument booléen 
                   que l'on peut passer à la méthode de liste sort ou à la fonction sorted. """
               ex : >>> sorted(etudiants, key=lambda etudiant: etudiant.age, reverse=True)   

__repr__ =   """  la méthode "__repr__" ne prend aucun paramètre (sauf, bien entendu,self) et renvoie une chaîne de caractères : 
                  la chaîne à afficher quand on entre l'objet directement dans l'interpréteur. 
                  On peut également obtenir cette chaîne grâce à la fonction "repr", qui se contente d'appeler 
                  la méthode spéciale "__repr__" de l'objet passé en paramètre"""
                  ex : class Personne:
                         """Classe représentant une personne"""
                         def __init__(self, nom, prenom):
                              """Constructeur de notre classe"""
                              self.nom = nom
                              self.prenom = prenom
                              self.age = 33
                         def __repr__(self):
                              """Quand on entre notre objet dans l'interpréteur"""
                              return "Personne: nom({}), prénom({}), âge({})".format(self.nom, self.prenom, self.age)                           
                      >>> p1 = Personne("Micado", "Jean")
                      >>> p1
                      Personne: nom(Micado), prénom(Jean), âge(33)
                      #ou
                      >>> p1 = Personne("Micado", "Jean")
                      >>> repr(p1)
                      'Personne: nom(Micado), prénom(Jean), âge(33)'

__str__ =    """  Il existe une seconde méthode spéciale, "__str__ ", spécialement utilisée pour afficher l'objet avec "print". 
                 Par défaut, si aucune méthode "__str__" n'est définie, Python appelle la méthode "__repr__" de l'objet. 
                 La méthode "__str__" est également appelée si vous désirez convertir votre objet en chaîne avec le constructeur "str". """
                 ex : # la classe du dessus  class Personne
                      def __str__(self):
                         """Méthode permettant d'afficher plus joliment notre objet"""
                              return "{} {}, âgé de {} ans".format(self.prenom, self.nom, self.age) 
                      >>> p1 = Personne("Micado", "Jean")
                      >>> print(p1)
                      Jean Micado, âgé de 33 ans
                      >>> chaine = str(p1)
                      >>> chaine
                      'Jean Micado, âgé de 33 ans'

__getattr__ = """ Python recherche l'attribut et, s'il ne le trouve pas dans l'objet et si une méthode "__getattr__" existe, 
                  il va l'appeler en lui passant en paramètre le nom de l'attribut recherché, sous la forme d'une chaîne de caractères.
                  Si l'attribut auquel on souhaite accéder existe, notre méthode n'est pas appelée. En revanche, 
                  si l'attribut n'existe pas, notre méthode "__getattr__ "est appelée."""
                  ex : >>> class Protege:
                         """Classe possédant une méthode particulière d'accès à ses attributs :
                         Si l'attribut n'est pas trouvé, on affiche une alerte et renvoie None"""   
                         def __init__(self):
                         """On crée quelques attributs par défaut"""
                              self.a = 1
                              self.b = 2
                              self.c = 3
                         def __getattr__(self, nom):
                              """Si Python ne trouve pas l'attribut nommé nom, il appelle
                              cette méthode. On affiche une alerte"""        
                              print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))
                      >>> pro = Protege()
                      >>>pro.a
                      1
                      >>> pro.e
                      Alerte ! Il n'y a pas d'attribut e ici !

__setattr__ = """ Cette méthode définit l'accès à un attribut destiné à être modifié. Si vous écrivez "objet.nom_attribut = nouvelle_valeur", 
                  la méthode spéciale "__setattr__" sera appelée ainsi : "objet.__setattr__("nom_attribut", nouvelle_valeur)". 
                  Là encore, le nom de l'attribut recherché est passé sous la forme d'une chaîne de caractères. 
                  Cette méthode permet de déclencher une action dès qu'un attribut est modifié."""
                  ex : def __setattr__(self, nom_attr, val_attr):
                         """Méthode appelée quand on fait "objet.nom_attr = val_attr".
                         On se charge d'enregistrer l'objet"""
                         object.__setattr__(self, nom_attr, val_attr)
                         self.enregistrer() 

__delattr__ =""" Cette méthode spéciale est appelée quand on souhaite supprimer un attribut de l'objet, en faisant "del objet.attribut"
                 Là encore, si vous voulez supprimer un attribut, n'utilisez pas dans votre méthode "del self.attribut". Sinon, vous 
                 risquez de mettre Python très en colère ! Passez par "object.__delattr__" qui sait mieux que nous comment tout cela fonctionne."""
                 ex : def __delattr__(self, nom_attr):
                         """On ne peut supprimer d'attribut, on lève l'exception
                         AttributeError"""
                         raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")   

__new__ = """ C'est une méthode statique, ce qui signifie qu'elle ne prend pas "self" en paramètre. 
              C'est logique, d'ailleurs : son but est de créer une nouvelle instance de classe, l'instance n'existe pas encore.
              Elle ne prend donc pas "self" en premier paramètre (l'instance d'objet). Cependant, elle prend la classe manipulée "cls".
              Autrement dit, quand on souhaite créer un objet de la classePersonne, la méthode "__new__" de la classe "Personne" est appelée et prend comme 
              premier paramètre la classe "Personne " elle-même. Les autres paramètres passés à la méthode__new__seront transmis au constructeur.     
              Redéfinir "__new__" peut permettre, par exemple, de créer une instance d'une autre classe. Elle est principalement utilisée par Python 
              pour produire des types immuables (en anglais, immutable), que l'on ne peut modifier, comme le sont les chaînes de caractères, les tuples, les entiers, les flottants…
              La méthode__new__est parfois redéfinie dans le corps d'une métaclasse."""
              ex : class Personne:
                   Le nom et le prénom doivent être passés au constructeur.
                         def __new__(cls, nom, prenom):
                              print("Appel de la méthode __new__ de la classe {}".format(cls))
                              # On laisse le travail à object
                              return object.__new__(cls, nom, prenom)
    
                         def __init__(self, nom, prenom):
                                   """Constructeur de notre personne."""
                              print("Appel de la méthode __init__")
                              self.nom = nom
                              self.prenom = prenom
                              self.age = 23
                              self.lieu_residence = "Lyon"
                  >>> personne = Personne("Doe", "John")
                  Appel de la méthode __new__ de la classe <class '__main__.Personne'>
                  Appel de la méthode __init__



bonus = """ Voici quelques fonctions qui font à peu près ce que nous avons fait mais en utilisant des chaînes de caractères 
            pour les noms d'attributs. prennent toutes, en premier paramètre, l'objet sur lequel travailler et en second 
            le nom de l'attribut (sous la forme d'une chaîne). Toutefois, cela peut être très pratique parfois de travailler 
            avec des chaînes de caractères plutôt qu'avec des noms d'attributs.""" 
            ex : objet = MaClasse() # On crée une instance de notre classe
                getattr(objet, "nom") # Semblable à objet.nom
                setattr(objet, "nom", val) # = objet.nom = val ou objet.__setattr__("nom", val)
                delattr(objet, "nom") # = del objet.nom ou objet.__delattr__("nom")
                hasattr(objet, "nom") # Renvoie True si l'attribut "nom" existe, False sinon









                                        Les méthodes de conteneur:
          """ Les objets conteneurs, ce sont les chaînes de caractères, les listes et les dictionnaires, entre autres. 
              Tous ont un point commun : ils contiennent d'autres objets, auxquels on peut accéder grâce à l'opérateur[]."""

__getitem__ =   objet[index]
__setitem__ =   objet[index] = valeur
__delitem__ =   del objet[index] """elle ne prend qu'un seul paramètre qui est l'index que l'on souhaite supprimer."""
                ex : class ZDict:
                          """Classe enveloppe d'un dictionnaire"""
                         def __init__(self):
                              """Notre classe n'accepte aucun paramètre"""
                              self._dictionnaire = {}
                         def __getitem__(self, index):
                              """Cette méthode spéciale est appelée quand on fait objet[index]
                              Elle redirige vers self._dictionnaire[index]"""       
                              return self._dictionnaire[index]
                         def __setitem__(self, index, valeur):
                              """Cette méthode est appelée quand on écrit objet[index] = valeur
                              On redirige vers self._dictionnaire[index] = valeur"""       
                              self._dictionnaire[index] = valeur 

__contains__ = """  si vous voulez que votre classe enveloppe puisse utiliser le mot-clé "in" comme une liste ou un dictionnaire, 
                    vous devez redéfinir cette méthode "__contains__" qui prend en paramètre, outre "self", l'objet qui nous intéresse. 
                    Si l'objet est dans le conteneur, on doit renvoyer "True" ; sinon "False"."""
                    ex : class Mot:    
                          def __init__(self):
                               self._liste = [1,2,3,4,5,6]
                          def __contains__(self, demande):
                               return demande in self._liste
                        var = Mot()
                        >>> 7 in var
                        False
                        >>> 5 in var
                        True

__len__ =   """ "len" (objet) équivaut à "objet.__len__()" . Cette méthode spéciale ne prend aucun paramètre et renvoie une taille sous la forme d'un entier. """
                class MyObject:
                    def len(self):
                         return len(self)

__iter__ = """ L'itérateur est créé dans la méthode spéciale "__iter__" de l'objet. Ici, c'est donc la méthode "__iter__" 
               de la classe list qui est appelée et qui renvoie un itérateur permettant de parcourir la liste. Quand Python 
               tombe sur une ligne du type for element in ma_liste:, il va appeler l'itérateur de ma_liste. L'itérateur, 
               c'est un objet qui va être chargé de parcourir l'objet conteneur, ici une liste."""
               ex : >>> ma_chaine = "test"
                    """On appelle ensuite la fonction iter en lui passant en paramètre la chaîne. Cette fonction appelle 
                    la méthode spéciale __iter__ de la chaîne, qui renvoie l'itérateur permettant de parcourir ma_chaine."""
                    >>> iterateur_de_ma_chaine = iter(ma_chaine)
                    """ On va ensuite appeler plusieurs fois la fonction next en lui passant en paramètre l'itérateur. 
                    Cette fonction appelle la méthode spéciale __next__ de l'itérateur.""" 
                    >>> next(iterateur_de_ma_chaine)
                    't'
                    >>> next(iterateur_de_ma_chaine)
                    'e'
                    >>> next(iterateur_de_ma_chaine)
                    's'
                    >>> next(iterateur_de_ma_chaine)
                    't'
                    >>> next(iterateur_de_ma_chaine)
                    """ StopIteration quand la chaîne a été parcourue entièrement. """
                    StopIteration

__next__ = """ À chaque tour de boucle, Python appelle la méthode spéciale __next__ de l'itérateur, qui doit renvoyer l'élément suivant 
               du parcours ou lever l'exception StopIteration si le parcours touche à sa fin. Python utilise deux fonctions pour 
               appeler et manipuler les itérateurs : iter permet d'appeler la méthode spéciale __iter__ de l'objet passé en paramètre 
               et next appelle la méthode spéciale __next__ de l'itérateur passé en paramètre."""
               ex : # le code de __iter__

yield =   """ Pour créer des générateurs, nous allons découvrir "yield". Ce mot-clé ne peut s'utiliser que dans le corps d'une 
              fonction et il est suivi d'une valeur à renvoyer.  L'idée consiste à définir une fonction pour un type de parcours. 
              Quand on demande le premier élément du parcours (grâce à next), la fonction commence son exécution. Dès qu'elle 
              rencontre une instruction yield, elle renvoie la valeur qui suit et se met en pause. Quand on demande l'élément 
              suivant de l'objet (grâce, une nouvelle fois, à next), l'exécution reprend à l'endroit où elle s'était arrêtée 
              et s'interrompt au yield suivant. système des co-routines en Python est contenu dans le mot-clé yield."""
              ex :  def intervalle(borne_inf, borne_sup):
                         """Générateur parcourant la série des entiers entre borne_inf et borne_sup.
                         Note: borne_inf doit être inférieure à borne_sup"""
                         borne_inf += 1
                         while borne_inf < borne_sup:
                              yield borne_inf
                              borne_inf += 1
                    # pour activer le code voir a .close()
.close() =""" Interrompre la boucle. Comme vous le voyez, pour appeler les méthodes du générateur, 
              on doit le stocker dans une variable avant la boucle. Si vous aviez écrit directement "for nombre in intervalle(5, 20)", 
              vous n'auriez pas pu appeler la méthode close du générateur."""
              ex : generateur = intervalle(5, 20)
                   for nombre in generateur:
                         if nombre > 17:
                         generateur.close() # Interruption de la boucle

Envoyer des données à notre générateur =
          """ Le point d'échange de données se fait au mot-clé yield. yield valeur « renvoie » valeur qui deviendra donc la valeur 
              courante du parcours. La fonction se met ensuite en pause. On peut, à cet instant, envoyer une valeur à notre générateur. 
              Cela permet d'altérer le fonctionnement de notre générateur pendant le parcours.""" 
              ex : def intervalle(borne_inf, borne_sup):
                    """Générateur parcourant la série des entiers entre borne_inf et borne_sup.
                    Notre générateur doit pouvoir "sauter" une certaine plage de nombres
                    en fonction d'une valeur qu'on lui donne pendant le parcours. La
                    valeur qu'on lui passe est la nouvelle valeur de borne_inf.
                    Note: borne_inf doit être inférieure à borne_sup"""
                         borne_inf += 1
                         while borne_inf < borne_sup:
                              """Tout se passe à partir de la ligne du yield. Au lieu de simplement renvoyer une valeur à notre boucle, 
                              on capture une éventuelle valeur dans valeur_recue."""
                              valeur_recue = (yield borne_inf)
                              """Si aucune valeur n'a été passée à notre générateur, notre valeur_recue vaudra None."""
                              if valeur_recue is not None: # Notre générateur a reçu quelque chose
                                   """On vérifie donc si elle ne vaut pas None et, dans ce cas, on affecte la nouvelle valeur à borne_inf."""
                                   borne_inf = valeur_recue
                              borne_inf += 1
                   """Voici le code permettant d'interagir avec notre générateur. 
                   On utilise la méthode "send" pour envoyer une valeur à notre générateur"""
                   generateur = intervalle(10, 25)
                   for nombre in generateur:
                         if nombre == 15: # On saute à 20
                              generateur.send(20)
                         print(nombre, end=" ") 



 
                                        Les méthodes mathématiques : 

                    ex : class Duree:
                              """Classe contenant des durées sous la forme d'un nombre de minutes
                              et de secondes"""    
                              def __init__(self, min=0, sec=0):
                                   """Constructeur de la classe"""
                                   self.min = min # Nombre de minutes
                                   self.sec = sec # Nombre de secondes
                              def __str__(self):
                                   """Affichage un peu plus joli de nos objets"""
                                   return "{0:02}:{1:02}".format(self.min, self.sec)
                         >>> d1 = Duree(3, 5)
                         >>> print(d1)
                         03:05

__add__ =   """ quand vous utilisez le symbole+ainsi, c'est en fait la méthode__add__de l'objetDureequi est appelée. 
                Elle prend en paramètre l'objet que l'on souhaite ajouter, peu importe le type de l'objet en question. 
                Et elle doit renvoyer un objet exploitable, ici il serait plus logique que ce soit une nouvelle durée.
                Pour mieux comprendre, remplacezd2 = d1 + 54pard2 = d1.__add__(54): cela revient au même. 
                Ce remplacement ne sert qu'à bien comprendre le mécanisme.""" 
                ex : def __add__(self, objet_a_ajouter):
                         """L'objet à ajouter est un entier, le nombre de secondes"""
                         nouvelle_duree = Duree()
                         # On va copier self dans l'objet créé pour avoir la même durée
                         nouvelle_duree.min = self.min
                         nouvelle_duree.sec = self.sec
                         # On ajoute la durée
                         nouvelle_duree.sec += objet_a_ajouter
                         # Si le nombre de secondes >= 60
                         if nouvelle_duree.sec >= 60:
                              nouvelle_duree.min += nouvelle_duree.sec // 60
                              nouvelle_duree.sec = nouvelle_duree.sec % 60
                         # On renvoie la nouvelle durée
                         return nouvelle_duree
                         >>> d1 = Duree(12, 8)
                         >>> print(d1)
                         12:08
                         >>> d2 = d1 + 54 # d1 + 54 secondes
                         >>> print(d2)
                         13:02
__sub__ =     """ Surcharge de l'opérateur "-" """

__mul__=      """ Surcharge de l'opérateur "*" ."""

__truediv__=  """ Surcharge de l'opérateur" /" ."""

__floordiv__= """ Surcharge de l'opérateur "//" (division entière) ."""

__mod__=      """ Surcharge de l'opérateur "%" (modulo) ."""

__pow__=      """ Surcharge de l'opérateur "**" (puissance)."""

__radd__=    """  écrire "objet1 + objet2" ne revient pas au même qu'écrire "objet2 + objet1" si les deux objets ont des types différents.
                  En effet, suivant le cas, c'est la méthode "__add__" de l'un ou l'autre des objets qui est appelée. Cela signifie que, 
                  lorsqu'on utilise la classe Duree, si on écrit "d1 + 4" cela fonctionne, alors que "4 + d1" ne marche pas. En effet, 
                  la class "int" ne sait pas quoi faire de votre objet Duree. Il existe cependant une panoplie de méthodes spéciales 
                  pour faire le travail de "__add__" si vous écrivez l'opération dans l'autre sens. Il suffit de préfixer le nom 
                  des méthodes spéciales par un "r". """
                  ex : def __radd__(self, objet_a_ajouter):
                         """Cette méthode est appelée si on écrit 4 + objet et que
                         le premier objet (4 dans cet exemple) ne sait pas comment ajouter
                         le second. On se contente de rediriger sur __add__ puisque,
                         ici, cela revient au même : l'opération doit avoir le même résultat,
                         posée dans un sens ou dans l'autre"""       
                          return self + objet_a_ajouter

__iadd__ =   """ Il est également possible de surcharger les opérateurs "+=" , "-=" , etc. On préfixe cette fois-ci les noms de 
                 méthode que nous avons vus par un "i" ."""
                 ex : def __iadd__(self, objet_a_ajouter):
                         """L'objet à ajouter est un entier, le nombre de secondes"""
                         # On travaille directement sur self cette fois
                         # On ajoute la durée
                         self.sec += objet_a_ajouter
                         # Si le nombre de secondes >= 60
                         if self.sec >= 60:
                              self.min += self.sec // 60
                              self.sec = self.sec % 60
                              # On renvoie self
                          return self 
                                     


                                     
                                     
                                      Les méthodes de comparaison
               """ Ces méthodes sont donc appelées si vous tentez de comparer deux objets entre eux. Comment Python sait-il que 3 
                   est inférieur à 18 ? Une méthode spéciale de la classeintle permet, en simplifiant. Donc si vous voulez comparer 
                   des durées, par exemple, vous allez devoir redéfinir certaines méthodes que je vais présenter plus bas. 
                   Elles devront prendre en paramètre l'objet à comparer à  "self" , et doivent renvoyer un booléen (True ou False). """    

 == =   """ Opérateur d'égalité (equal). Renvoie "True" si "self" et "objet_a_comparer" sont égaux, "False" sinon. """
            ex : def __eq__(self, objet_a_comparer):

!= =   """ Différent de (non equal). Renvoie "True" si "self" et "objet_a_comparer" sont différents, "False" sinon. """
           ex : def __ne__(self, objet_a_comparer):

>  =   """ Teste si "self" est strictement supérieur (greater than) à "objet_a_comparer"."""
           ex : def __gt__(self, objet_a_comparer):

>= =   """ Teste si "self" est supérieur ou égal (greater or equal) à "objet_a_comparer"."""
           ex : def __ge__(self, objet_a_comparer):

< =   """ Teste si "self" est strictement inférieur (lower than) à "objet_a_comparer"."""
          ex : def __lt__(self, objet_a_comparer):

<= =   """ Teste si "self" est inférieur ou égal (lower or equal) à "objet_a_comparer"."""
           ex : def __le__(self, objet_a_comparer):




                                   Des méthodes spéciales utiles à pickle
          """ Deux méthodes qui sont utilisées par ce module pour influencer la façon dont nos objets sont enregistrés dans des fichiers."""        

__getstate__ = """ La méthode "__getstate__" est appelée au moment de sérialiser l'objet. Quand vous voulez enregistrer l'objet
                   à l'aide du module "pickle" , "__getstate__" va être appelée juste avant l'enregistrement.Si aucune méthode
                   "__getstate__" n'est définie,"pickle" enregistre le dictionnaire des attributs de l'objet à enregistrer. 
                   Il est contenu dans objet. "__dict__" . """
                   ex :  class Temp:
                         """Classe contenant plusieurs attributs, dont un temporaire"""
                              def __init__(self):
                                   """Constructeur de notre objet"""
                                   self.attribut_1 = "une valeur"
                                   self.attribut_2 = "une autre valeur"
                                   self.attribut_temporaire = 5
                              def __getstate__(self):
                                   """Renvoie le dictionnaire d'attributs à sérialiser"""
                                   dict_attr = dict(self.__dict__)
                                   dict_attr["attribut_temporaire"] = 0
                                   return dict_attr
               """ Voyons le code de "__getstate__". La méthode ne prend aucun argument (excepté "self" puisque c'est une méthode d'instance).
                   Elle enregistre le dictionnaire des attributs dans une variable locale "dict_attr". Ce dictionnaire a le même contenu 
                   que "self.__dict__"(le dictionnaire des attributs de l'objet). En revanche, il a une référence différente. 
                   Sans cela, à la ligne suivante, au moment de modifier "attribut_temporaire", le changement aurait été également appliqué 
                   à l'objet, ce que l'on veut éviter. À la ligne suivante, donc, on change la valeur de l'attribut "attribut_temporaire". 
                    Étant donné que "dict_attr" et "self.__dict__" n'ont pas la même référence, l'attribut n'est changé que dans "dict_attr "
                   et le dictionnaire de "self" n'est pas modifié. Enfin, on renvoie "dict_attr" . Au lieu d'enregistrer
                   dans notre fichier "self.__dict__" ,pickle enregistre notre dictionnaire modifié,"dict_attr"."""

__setstate__ = """ À la différence de "__getstate__" , la méthode "__setstate__" est appelée au moment de désérialiser l'objet. 
                   Concrètement, si vous récupérez un objet à partir d'un fichier sérialisé, "__setstate__" sera appelée après 
                   la récupération du dictionnaire des attributs."""
                   ex : def __setstate__(self, dict_attr):
                              """Méthode appelée lors de la désérialisation de l'objet"""
                              dict_attr["attribut_temporaire"] = 0
                              self.__dict__ = dict_attr
               """ on modifie le dictionnaire d'attributs après la désérialisation. Le dictionnaire que l'on récupère contient un 
                   attribut "attribut_temporaire" avec une valeur quelconque (on ne sait pas laquelle) mais après avoir récupéré 
                   l'objet qui est déjà instancié (et avant le retour de la désérialisation !), on met cette valeur à 0."""

@property = """ Une propriété est une méthode qui est accessible comme un attribut Si nous voulons accéder à la longitude, nous
            """ devons écrire position.longitude(). Or nous voulons plutôt écrire position.longitude, afin que la longitude 
               soit utilisée comme un attribut et non comme une méthode """
               ex: @property
                    def longitude(self):

@classmethod = """ pouvoir lancer ma méthode maintenant ! Mais si j'essaie de la lancer, je suis pris moi-même dans une boucle infinie. 
                    """Le seul moyen que nous connaissions pour lancer une méthode, jusqu'à maintenant, est de créer une instance et
                    de l'utiliser pour exécuter la méthode. """
                    ex: @classmethod
                         def initialize_zones(self):
                              
ATTRIBUT DE CLASS = """ Un attribut de classe est une variable dont le champ d'action s'étend à l'ensemble d'une classe. 
                         Ils sont très utilisés pour compter le nombre d'instances d'une classe par exemple. 
                         Par convention, un attribut de classe s'indique en majuscules, avant les méthodes. """
                        ex : class Zone:
                               MIN_LONGITUDE_DEGREES = -180
                               def __init__(self, corner1, corner2): 
                    """ Pour y accéder par la suite """                              
                        ex: print(Zone.MIN_LONGITUDE_DEGREES)
                    """ Vous pouvez également y accéder via une instance de la classe"""
                        ex:   def __init__(self, corner1, corner2):
                                   ...
                                   longitude = self.MIN_LONGITUDE_DEGREES

L encapsulation =  """ Le fait que les attributs et les méthodes d un objet lui sont spécifiquement associés. 
                       Le champ d action des attributs et des méthodes est par défaut l objet lui-même et non tout autre objet.                 
                       Une méthode protégée est accessible à l'intérieur d'une classe mais ne doit pas être aisément accessible de l'extérieur.
                       Vous ajoutez pour cela un underscore au début du nom. 
                       Ajouter des underscores pour transformer nos méthodes en méthodes privées ou protégées.
                       On peut bel et bien accéder à cette méthode privée. Tout est question de syntaxe ! En écrivant _MaClasse__methode_privee(), 
                       je peux quand même l'exécuter."""                                  
                       ex : class CoffeeMachine():
                           
                                def _start_machine(self):
                                   .......

                                def __boil_water(self):
                                    return "boiling..."

                                def make_coffee(self):
                                    if self._start_machine(): #Pour continuer à utiliser cette méthode, ajoutez le underscore.
                                        self.water_level -= 20
                                        print(self.__boil_water()) #Et pour les méthodes privées ? Vous ajoutez deux underscores ! Ainsi :
                                        print("Coffee is ready!")

                                machine = CoffeeMachine()                            
                                print("Make Coffee: Public", machine.make_coffee())
                                print("Start Machine: Protected", machine._start_machine())        #On peut bel et bien accéderà cette méthode
                                print("Boil Water: Private", machine._CoffeeMachine__boil_water() )#ICI # privée avec _ devant la CLASS 
                        
Héritage =   """ L'héritage est un mécanisme qui nous permet d'étendre les fonctionnalités d'une classe parent à travers une classe enfant.
                 Il nous permet de réutiliser du code de manière simple et efficace. De manière générale, nous disons qu'une classe enfant
                 hérite d'une classe parent et que la classe parent étend la classe enfant.La classe enfant a accès à tous les attributs
                 et à toutes les méthodes de sa classe parent mais l'inverse n'est pas vrai  
                 Une classe abstraite (parent) est une classe qui ne peut pas être instanciée sans renvoyer une erreur. 
                 Elle doit être héritée par une classe enfant qui elle-même créera des instances. 
                 L'inverse est appelé une classe concrète (enfant) : on ne s'attend pas à ce qu'elle étende d'autres classes."""                     
                 ex : class Personne:    # constructeur
                         """Classe représentant une personne"""
                         def __init__(self, nom):
                              """Constructeur de notre classe"""
                              self.nom = nom   # attribut
                              self.prenom = "Martin" #attribut
                         def __str__(self):
                              """Méthode appelée lors d'une conversion de l'objet en chaîne"""
                              return "{0} {1}".format(self.prenom, self.nom)

                     class AgentSpecial(Personne):
                         """Classe définissant un agent spécial.
                         Elle hérite de la classe Personne"""
                         def __init__(self, nom, matricule):
                              """Un agent se définit par son nom et son matricule"""
                              # On appelle explicitement le constructeur de Personne :
                              Personne.__init__(self, nom) #prend les meme parametre que dans la class Personne
                              self.matricule = matricule
                         def __str__(self):
                              """Méthode appelée lors d'une conversion de l'objet en chaîne"""
                              return "Agent {0}, matricule {1}".format(self.nom, self.matricule)
                     >>> agent = AgentSpecial("Fisher", "18327-121")
                     >>> agent.nom
                     'Fisher'
                     >>> print(agent)
                     Agent Fisher, matricule 18327-121
                     >>> agent.prenom
                     'Martin'

Heritage Multiple = """ La recherche des méthodes se fait dans l'ordre de la définition de la classe. Dans l'exemple ci-dessus, 
                        si on appelle une méthode d'un objet issu de MaClasseHeritee, on va d'abord chercher dans la classe MaClasseHeritee. 
                        Si la méthode n'est pas trouvée, on la cherche d'abord dans MaClasseMere1. Encore une fois, si la méthode 
                        n'est pas trouvée, on cherche dans toutes les classes mères de la classe MaClasseMere1, si elle en a, 
                        et selon le même système. Si, encore et toujours, on ne trouve pas la méthode, on la recherche dans 
                        MaClasseMere2 et ses classes mères successives."""
                        ex : class MaClasseHeritee(MaClasseMere1, MaClasseMere2):  

super(). =   """ La méthode  super()  appelle la méthode correspondante de la classe parent. 
                 Cela vous permet d'en changer une partie sans pour autant tout remplacer ! """  
                  ex : def __init__(self):
                            super().__init__()       


Exceptions personnalisées = """ Que doit contenir notre classe exception ? Deux choses : un constructeur et une méthode "__str__" 
                                car, au moment où l'exception est levée, elle doit être affichée. Souvent, votre constructeur 
                                ne prend en paramètre que le message d'erreur et la méthode "__str__" renvoie ce message.
                                Vous pourrez les lever avec raise, les intercepter avec except."""
                                ex : class ErreurAnalyseFichier(Exception):
                                        """Cette exception est levée quand un fichier (de configuration)
                                        n'a pas pu être analysé.
                                        Attributs :
                                             fichier -- le nom du fichier posant problème
                                             ligne -- le numéro de la ligne posant problème
                                             message -- le problème proprement dit"""
                                        def __init__(self, fichier, ligne, message):
                                             """Constructeur de notre exception"""
                                             self.fichier = fichier
                                             self.ligne = ligne
                                             self.message = message
                                        def __str__(self):
                                             """Affichage de l'exception"""
                                             return "[{}:{}]: {}".format(self.fichier, self.ligne,self.message)
                                    >>> raise ErreurAnalyseFichier("plop.conf", 34,
                                    "Il manque une parenthèse à la fin de l'expression")
                                    Traceback (most recent call last):
                                    File "<stdin>", line 2, in <module>
                                    __main__.ErreurAnalyseFichier: [plop.conf:34]: il manque une parenthèse à la fin de l'expression

                                   







          LES MODULES : 





os.chdir = """ Permet de changer de repertoire de travail Pour cela, vous devez utiliser une fonction du module "os", 
               qui s'appelle "chdir" (Change Directory). """
               ex : >>> import os
                    >>> os.chdir("C:\\tests python")          




open =    """ D'abord, il nous faut ouvrir le fichier avec Python. On utilise pour ce faire la fonctionopen, 
              disponible sans avoir besoin de rien importer. Elle prend en paramètre :le chemin (absolu ou relatif)
              menant au fichier à ouvrir ;le mode d'ouverture. """ 
          'r': ouverture en lecture (Read).
          'w': ouverture en écriture (Write). Le contenu du fichier est écrasé. Si le fichier n existe pas, il est créé.
          'a': ouverture en écriture en mode ajout (Append). On écrit à la fin du fichier sans écraser 
               l ancien contenu du fichier. Si le fichier n existe pas, il est créé
               ex : >>> mon_fichier = open("C:\\Users\\ptibu\\Desktop\\Projet_Python\\projet_python_dumoment\\fichier.txt, "r")
          'b': Pour ouvrir le fichier en mode binaire.
               ex : >>> mon_fichier = open("C:\\Users\\ptibu\\Desktop\\Projet_Python\\projet_python_dumoment\\fichier.txt, "wb") 
               

.close() = """  fermer un fichier après l'avoir ouvert. Si d'autres applications, ou d'autres morceaux de votre propre code, 
                souhaitent accéder à ce fichier, ils ne pourront pas car le fichier sera déjà ouvert. C'est surtout vrai en écriture  """                 
                ex : >>> mon_fichier.close()

.read() =  """ Pour ce faire, on utilise la méthode "read " de la classe "TextIoWrapper". Elle renvoie l'intégralité du fichier."""
               ex : >>> mon_fichier = open("fichier.txt", "r")
                    >>> contenu = mon_fichier.read()
                    >>> print(contenu)
                    # contenu du fichier......
                    >>> mon_fichier.close()

.write() =  """ Pour écrire dans un fichier, on utilise la méthode "write" en lui passant en paramètre la chaîne à écrire dans le fichier. 
                Elle renvoie le nombre de caractères qui ont été écrits. La méthode "write "n'accepte en paramètre que des chaînes de caractères."""
                ex : >>> mon_fichier = open("fichier.txt", "w") # Argh j'ai tout écrasé !
                     >>> mon_fichier.write("Premier test d'écriture dans un fichier via Python")
                     50
                     >>> mon_fichier.close()

with =     """ Le mot-clé "with" permet de créer un "context manager" (gestionnaire de contexte) qui vérifie que le fichier est ouvert et fermé,
               même si des erreurs se produisent pendant le bloc."""  
               ex : >>> with open('fichier.txt', 'r') as mon_fichier:
                    ...     texte = mon_fichier.read()    


                                    module pickle

pickle =  """ Grâce au module "pickle", on peut enregistrer n'importe quel objet et le récupérer par la suite, 
              au prochain lancement du programme, par exemple. En outre, le fichier résultant pourra être lu depuis 
              n'importe quel système d'exploitation (à condition, naturellement, que celui-ci prenne en charge Python).""" 
              ex : >>> import pickle

.Pickler = """ Pour créer notre objet "Pickler" (qui est une class), nous allons l'appeler en passant en paramètre le fichier dans 
               lequel nous allons enregistrer notre objet. Quand nous allons enregistrer nos objets, ce sera dans le fichier "donnees". """
               ex : >>> with open('donnees', 'wb') as fichier:
                    ...     mon_pickler = pickle.Pickler(fichier)                      

.dump =   """ On utilise la méthode "dump" du pickler pour enregistrer l'objet. Si vous voulez enregistrer plusieurs objets, 
              appelez de nouveau la méthode "dump" avec les objets à enregistrer. Ils seront ajoutés dans le fichier dans 
              l'ordre où vous les enregistrez. """
              ex : >>> score = {"joueur 1":    5,"joueur 2":   35,"joueur 3":   20,"joueur 4":    2,}
                   >>> with open('donnees', 'wb') as fichier:
                   ...     mon_pickler = pickle.Pickler(fichier)
                   ...     mon_pickler.dump(score) 

.Unpickler = """ Récupérer nos objets enregistrés, il faut commencer par crée notre objet. À sa création, 
                 on lui passe le fichier dans lequel on va lire les objets. Puisqu'on va lire, on change de mode, 
                 on repasse en moder, et même "rb" puisque le fichier est binaire."""
                 ex : >>> with open('donnees', 'rb') as fichier:
                      ...     mon_depickler = pickle.Unpickler(fichier)
                      ...     # Lecture des objets contenus dans le fichier...

.load =     """ Pour lire l'objet dans notre fichier, il faut appeler la méthode "load" de notre de "pickler"  . 
                Elle renvoie le premier objet qui a été lu (s'il y en a plusieurs, il faut l'appeler plusieurs fois)."""
               ex : >>> with open('donnees', 'rb') as fichier:
                    ...     mon_depickler = pickle.Unpickler(fichier)
                    ...     score_recupere = mon_depickler.load()
                         #Et après cet appel, si le fichier a pu être lu, dans votre variable "score_recupere", 
                         # vous récupérez votre dictionnaire contenant les scores.
                        


                                   module operator

itemgetter = """ On appelle la fonction itemgetter avec le paramètre 2(qui est dans l exemple la moyenne d'un étudiants). 
                 Un objet operator.itemgetter est créé et passé au paramètre key de la fonction sorted. Ensuite, 
                 pour chaque étudiant contenu dans notre liste, 
                 l'objet operator.itemgetter est appelé et retourne la note moyenne de l'étudiant."""                                   
                 ex : from operator import itemgetter # au début du code biensur
                      sorted(etudiants, key=itemgetter(2))  == ==   sorted(etudiants, key=lambda etudiant: etudiant[2])     
                        
attrgetter = """ On peut faire la même chose si on parcourt une liste d'objets, mais cette fois, on utilise la fonction attrgetter. 
                 Le système est le même, sauf que l'on travaille ici sur une liste d'objets et que le calcul est fait sur un attribut
                 de l'objet (ici "moyenne") au lieu d'un tuple. """
                 ex : #il faut une class avec une liste pour faire ça 
                      from operator import attrgetter # a début du code biensur 
                      sorted(etudiants, key=attrgetter("moyenne"))

            """ Trier selon un critère, c'est déjà très bien, mais trier selon plusieurs critères, ce peut être encore mieux. 
                Si nous voulons, disons, trier nos étudiants par âge et note moyenne. C'est-à-dire que le tri se fera par âge, 
                mais si deux étudiants ont le même âge, le tri se fera sur leur moyenne. il faut passer juste 
                un nouveau paramètre à la fonction attrgetter """          
                ex : >>> sorted(etudiants, key=attrgetter("age", "moyenne"))
                     [<Étudiant Thomas (âge=11, moyenne=12)>,<Étudiant Charles (âge=12, moyenne=15)>,
                     <Étudiant Damien (âge=12, moyenne=15)>,<Étudiant Clément (âge=14, moyenne=16)>,
                     <Étudiant Oriane (âge=14, moyenne=18)>]
            """ Vous avez peut-être remarqué que l'ordre de Charles et Damien dans la liste est identique à avant, 
                même si d'autres étudiants ont changé de place : en effet, Charles et Damien ont le même âge et la même 
                moyenne et leur ordre n'est pas modifié par Python.Cette propriété est appelée « stabilité ». 
                Si deux éléments de la séquence à comparer sont identiques, leur ordre est conservé. """

Chaînage de tris = """ si vous voulez trier par prix croissant et par quantité décroissante ? C'est-à-dire qu'on veut trier par 
                       prix croissant, mais que si deux lignes d'inventaires ont le même prix, alors on trie dans l'ordre décroissant 
                       de quantité. Le plus simple ici est de faire deux tris en utilisant la propriété de stabilité. La subtilité, 
                       c'est que l'on va trier d'abord par notre second critère et ensuite par notre premier."""   
                       ex : class LigneInventaire:
                              """Classe représentant une ligne d'un inventaire de vente."""
                              def __init__(self, produit, prix, quantite):
                                   self.produit = produit
                                   self.prix = prix
                                   self.quantite = quantite
                              def __repr__(self):
                                   return "<Ligne d'inventaire {} ({}X{})>".format(
                                        self.produit, self.prix, self.quantite)
                           # Création de l'inventaire
                            inventaire = [LigneInventaire("pomme rouge", 1.2, 19),LigneInventaire("orange", 1.4, 24),
                            LigneInventaire("banane", 0.9, 21),LigneInventaire("poire", 1.2, 24),]
                         """ On veut trier cette liste par prix et par quantité. Facile, c'est ce qu'on a fait un peu plus haut"""
                             from operator import attrgetter
                             sorted(inventaire, key=attrgetter("prix", "quantite")) 
                         """ si vous voulez trier par prix croissant et par quantité décroissante ? C'est-à-dire qu'on veut 
                         trier par prix croissant, mais que si deux lignes d'inventaires ont le même prix, alors on trie dans 
                         l'ordre décroissant de quantité ? Le plus simple ici est de faire deux tris en utilisant la propriété 
                         de stabilité. La subtilité, c'est que l'on va trier d'abord par notre second critère et ensuite par notre premier."""
                       ex : inventaire.sort(key=attrgetter("quantite"), reverse=True)
                            sorted(inventaire, key=attrgetter("prix"))   





                                   Module Time 


import time = """ Disposer d'une mesure du temps dans un programme peut avoir des applications variées : connaître la date et l'heure actuelles et faire remonter une erreur,
                  calculer depuis combien de temps le programme a été lancé, gérer des alarmes programmées, faire des tests de performance"""
                  ex : >>> debut = time.time()
                       >>> # On attend quelques secondes avant de taper la commande suivante
                       ... fin = time.time()
                       >>> print(debut, fin)
                       1297642195.45 1297642202.27
                       >>> debut < fin
                       True
                       >>> fin - debut # Combien de secondes entre debut et fin ?
                       6.812000036239624

fonction localtime = """ Nous allons découvrir tout au long de ce chapitre des moyens d'afficher nos temps de façon plus élégante et d'obtenir 
                         les diverses informations relatives à une date et une heure.  Elle prend un paramètre optionnel : le timestamp tel que 
                         nous l'avons découvert plus haut. Si ce paramètre n'est pas précisé, "localtime" utilisera automatiquement "time.time()" 
                         et renverra donc la date et l'heure actuelles. """
                         ex : time.localtime()
                              >>> time.struct_time(tm_year=2020, tm_mon=11, tm_mday=18, tm_hour=11, tm_min=9, tm_sec=5, tm_wday=2, tm_yday=323, tm_isdst=0)               
                              tm_year: l'année sous la forme d'un entier ;
                              tm_mon: le numéro du mois (entre 1 et 12) ;
                              tm_mday: le numéro du jour du mois (entre 1 et 31, variant d'un mois et d'une année à l'autre) ;
                              tm_hour: l'heure du jour (entre 0 et 23) ;
                              tm_min: le nombre de minutes (entre 0 et 59) ;
                              tm_sec: le nombre de secondes (entre 0 et 61, même si on n'utilisera ici que les valeurs de 0 à 59, c'est bien suffisant) ;
                              tm_wday: un entier représentant le jour de la semaine (entre 0 et 6, 0 correspond par défaut au lundi) ;
                              tm_yday: le jour de l'année, entre 1 et 366 ;
                              tm_isdst: un entier représentant le changement d'heure local.

fonction mktime =  """ Récupérer un timestamp depuis une date. L'idée est, à partir d'une structure représentant les date et heure telles que renvoyées 
                       par "localtime" , de récupérer le timestamp correspondant. On utilise pour ce faire la fonction "mktime"."""
                       ex : >>> print(debut)
                            1297642195.45
                            >>> temps = time.localtime(debut)
                            >>> print(temps)
                            time.struct_time(tm_year=2011, tm_mon=2, tm_mday=14, tm_hour=1, tm_min=9, tm_sec=55, tm_wday=0, tm_yday=45, tm_isdst=0)
                            >>> ts_debut = time.mktime(temps)
                            >>> print(ts_debut)
                            1297642195.0

fonction sleep =  """ Mettre en pause l'exécution du programme pendant un temps déterminé. 
                      prend en paramètre un nombre de secondes qui peut être sous la forme d'un entier ou d'un flottant.
                      Python se met en pause et vous devez attendre 3,5 secondes avant que les trois chevrons s'affichent à nouveau.  """
                      ex : >>> time.sleep(3.5) # Faire une pause pendant 3,5 secondes
                           >>>

fonction strftime = """ Elle permet de formater une date et heure en la représentant dans une chaîne de caractères.Elle prend deux paramètres :
                        La chaîne de formatage.
                        Un temps optionnel tel que le renvoie "localtime" . Si le temps n'est pas précisé, c'est la date et l'heure courantes qui sont utilisées par défaut.
                        Pour construire notre chaîne de formatage, nous allons utiliser plusieurs caractères spéciaux. 
                        Python va remplacer ces caractères par leur valeur (la valeur du temps passé en second paramètre ou du temps actuel sinon)."""
                        ex : time.strftime('%Y')
                             Symbole:       Signification:
                               %A            Nom du jour de la semaine  
                               %B            Nom du mois  
                               %d            Jour du mois (de 01 à 31)  
                               %H            Heure (de 00 à 23)  
                               %M            Minute (entre 00 et 59)  
                               %S            Seconde (de 00 à 59)  
                               %Y            Année  
                    """ Donc pour afficher la date telle qu'on y est habitué en France"""
                        ex : time.strftime("%A %d %B %Y %H:%M:%S")

 



                                   Module datetime

                         """Le module "datetime" propose plusieurs classes pour représenter des dates et heures.
                            nous nous avançons petit à petit vers une façon de gérer les dates et heures qui est davantage orientée objet.
                            Dans certains cas, on a juste besoin d'une date, c'est-à-dire un jour, un mois et une année.
                            Il est naturellement possible d'extraire cette information de notre timestamp. Le moduledatetimepropose une classedate, 
                            représentant une date, rien qu'une date. L'objet possède trois attributs :
                            year: l'année ; month: le mois ; day: le jour du mois.
                            Il y a plusieurs façons de procéder. Le constructeur de cette classe prend trois arguments qui sont, dans l'ordre, l'année, le mois et le jour du mois."""

date.today() = """ renvoie la date d'aujourd'hui """
                   ex  : >>> import time
                         >>> import datetime
                         >>> aujourdhui = datetime.date.today()
                         >>> aujourdhui
                         datetime.date(2011, 2, 14)

date.fromtimestamp(timestamp) = """ renvoie la date correspondant au timestamp passé en argument. """
                                    ex : >>> datetime.date.fromtimestamp(time.time()) # Équivalent à date.today
                                         datetime.date(2011, 2, 14)

Représenter une heure = """ C'est moins courant mais on peut également être amené à manipuler une heure, indépendamment de toute date. La classe "time" du module "datetime"est 
                            là pour cela. On construit une heure avec non pas trois mais cinq paramètres, tous optionnels :
                            hour(0 par défaut) : les heures, valeur comprise entre 0 et 23 ;
                            minute(0 par défaut) : les minutes, valeur comprise entre 0 et 59 ;
                            second(0 par défaut) : les secondes, valeur comprise entre 0 et 59 ;
                            microsecond(0 par défaut) : la précision de l'heure en micro-secondes, entre 0 et 1.000.000 ;
                            tzinfo(Nonepar défaut) : l'information de fuseau horaire (je ne détaillerai pas cette information ici)."""

Représenter des dates et heures = """ Représenter une date et une heure dans le même objet, ce sera probablement la classe que vous utiliserez le plus souvent. 
                                      Celle qui nous intéresse s'appelle "datetime" , comme son module. Elle prend d'abord les paramètres de "datetime.date(année, mois, jour)" 
                                      et ensuite les paramètres dedatetime.time(heures, minutes, secondes, micro-secondes et fuseau horaire).
                                      deux méthodes de classe que vous utiliserez le plus souvent :
                                      datetime.now(): renvoie l'objetdatetimeavec la date et l'heure actuelles ;
                                      datetime.fromtimestamp(timestamp): renvoie la date et l'heure d'un timestamp précis."""
                                      ex : >>> import datetime
                                           >>> datetime.datetime.now()
                                           datetime.datetime(2011, 2, 14, 5, 8, 22, 359000)





                                   module sys

                         """ Les flux standard quand vous appelez la fonction print, si le message s'affiche à l'écran, c'est parce que la sortie standard de votre programme est 
                             redirigée vers votre écran. On distingue trois flux standard :"""
                             - "sys.stdin" L entrée standard : elle est appelée quand vous utilisez input. C est elle qui est utilisée pour demander des informations à l utilisateur. 
                             Par défaut, l bentrée standard est votre clavier.
                             - "sys.stdout" La sortie standard : comme on l a vu, c est elle qui est utilisée pour afficher des messages. Par défaut, elle redirige vers l écran.
                             - "sys.stderr "L erreur standard : elle est notamment utilisée quand Python vous affiche le traceback d une exception. Par défaut, 
                             elle redirige également vers votre écran.

 import sys =    """ Accéder aux flux standard. On peut accéder aux objets représentant ces flux standard grâce au module sys qui propose plusieurs fonctions et 
                     variables permettant d'interagir avec le système. Classe que les fichiers ouverts grâce à la fonction open. Et il n'y a aucun hasard derrière cela.En effet, 
                     pour lire ou écrire dans les flux standard, on utilise les méthodes read et write.Naturellement, l'entrée standard stdin peut lire (méthode read) et 
                     les deux sorties stdout et stderr peuvent écrire (méthode write)."""
                     ex : >>> import sys
                          >>> sys.stdout.write("un test")
                          un test7
                 """  Là, ce que renvoie la méthode (le nombre de caractères écrits) est affiché juste après notre message."""   
                     ex2: >>> sys.stdout.write("Un test\n")
                     Un test
                     8

Modifier les flux standard = """ Vous pouvez modifier sys.stdin, sys.stdout et sys.stderr. """
                                 ex : >>> fichier = open('sortie.txt', 'w')
                                      >>> sys.stdout = fichier
                                      >>> print("Quelque chose...")
                                      >>>
                             """ rien ne s'affiche à l'écran. En revanche, si vous ouvrez le fichier sortie.txt, vous verrez le message que vous avez passé à print.
                                 Ou est le fichier sortie.txt ? Il doit se trouver dans le répertoire courant de Python. Pour connaître l'emplacement de ce répertoire, 
                                 utilisez le module os et la fonction getcwd (Get Current Working Directory).
                                 Une petite subtilité : si vous essayez de faire appel à getcwd directement, le résultat ne va pas s'afficher à l'écran… 
                                 il va être écrit dans le fichier. Pour rétablir l'ancienne sortie standard, tapez la ligne :"""
                                 sys.stdout = sys.__stdout__
                             """ Vous pouvez ensuite faire appel à la fonction getcwd :""" 
                                 import os
                                 os.getcwd()
                             """ Dans ce répertoire, vous devriez trouver votre fichier sortie.txt
                                 Si vous avez modifié les flux standard et que vous cherchez les objets d'origine, ceux redirigeant vers le clavier (pour l'entrée) et 
                                 vers l'écran (pour les sorties), vous pouvez les trouver dans sys.__stdin__, sys.__stdout__ et sys.__stderr__.La documentation de 
                                 Python nous conseille malgré tout de garder de préférence les objets d'origine sous la main plutôt que d'aller les chercher dans 
                                 sys.__stdin__, sys.__stdout__ et sys.__stderr__."""






                                   Module Signal

                     """ Les signaux sont un des moyens dont dispose le système pour communiquer avec votre programme. Typiquement, si le système doit arrêter votre programme, 
                         il va lui envoyer un signal. Les signaux peuvent être interceptés dans votre programme. Cela vous permet de déclencher une certaine action si le programme 
                         doit se fermer (enregistrer des objets dans des fichiers, fermer les connexions réseau établies avec des clients éventuels, …).
                         Les signaux sont également utilisés pour faire communiquer des programmes entre eux. Si votre programme est décomposé en plusieurs programmes s'exécutant 
                         indépendamment les uns des autres, cela permet de les synchroniser à certains moments clés.""" 


sigint =            """  le signal SIGINT envoyé à l'arrêt du programme. La plupart du temps, si votre programme renvoie 0, le système comprendra que tout s'est bien passé. 
                         Si c'est un entier autre que 0, le système interprétera cela comme une erreur ayant eu lieu pendant l'exécution de votre programme. 
                         Ici, notre programme s'arrête normalement, on passe donc à exit0. """
                         ex: import signal 
                             >>> signal.SIGINT
                             2
                    """   Pour intercepter ce signal, il va falloir créer une fonction qui sera appelée si le signal est envoyé. 
                          Cette fonction prend deux paramètres :
                          - le signal (plusieurs signaux peuvent être envoyés à la même fonction) ; 
                          - le frame qui ne nous intéresse pas ici."""
                          ex : import sys
                               def fermer_programme(signal, frame):
                                   """Fonction appelée quand vient l'heure de fermer notre programme"""
                                   print("C'est l'heure de la fermeture !")
                                   sys.exit(0) #On demande simplement à notre programme Python de se fermer Pour ce faire, on utilise la fonction exit du module sys. 
                                               #Elle prend en paramètre le code de retour du programme.
                    """ Connectons à présent notre fonction au signal SIGINT, sans quoi notre fonction ne serait jamais appelée.
                        On utilise pour cela la fonction signal. Elle prend en paramètre :
                        le signal à intercepter ;
                        la fonction que l'on doit connecter à ce signal.""" #Ne mettez pas les parenthèses à la fin du nom de la fonction.
                        ex : signal.signal(signal.SIGINT, fermer_programme) #On envoie la référence vers la fonction, on ne l'exécute pas.
                    """ Cette ligne va connecter le signal SIGINT à la fonction fermer_programme que vous avez définie plus haut. 
                        Dès que le système enverra ce signal pour fermer le programme, la fonction fermer_programme sera appelée."""
                        import signal
                        import sys
                        
                        def fermer_programme(signal, frame):
                             """Fonction appelée quand vient l'heure de fermer notre programme"""
                             print("C'est l'heure de la fermeture !")
                             sys.exit(0)
                         # Connexion du signal à notre fonction
                         signal.signal(signal.SIGINT, fermer_programme)
                         # Notre programme...
                         print("Le programme va boucler...")
                         while True:
                             continue                                                   
                    """ Quand vous lancez ce programme, vous voyez un message vous informant que le programme va boucler… et le programme continue de tourner. 
                        Il ne s'arrête pas. Il ne fait rien, il boucle simplement mais il va continuer de boucler tant que son exécution n'est pas interrompue.
                        Dans la fenêtre du programme, tapez CTRL + C Cette combinaison de touches va demander au programme de s'arrêter. Après l'avoir saisie, 
                        vous pouvez constater qu'effectivement, votre fonction fermer_programme est bien appelée et s'occupe de fermer le programme correctement. """        




                                  module math

                    """ Si bsoin d'une fonction chercher dans la documentation"""

math.pow() = """ Il y a bel et bien une différence entre l'opérateur "**" et la fonction "math.pow" . 
                 La fonction renvoie toujours un flottant alors que l'opérateur renvoie un entier quand cela est possible."""
                 ex : >>> math.pow(5, 2) # 5 au carré
                 25.0
                 >>> 5 ** 2 # Pratiquement identique à pow(5, 2)
                 25
                 >>> math.sqrt(25) # Racine carrée de 25 (square root)
                 5.0
                 >>> math.exp(5) # Exponentielle
                 148.4131591025766
                 >>> math.fabs(-3) # Valeur absolue
                 3.0

fonction de trigonométrie = """ Avant de voir les fonctions usuelles en trigonométrie, j'attire votre attention sur le fait que les angles, 
                                en Python, sont donnés et renvoyés en radians (rad). Pour rappel :1 rad = 57,29 degrés Cela étant dit, 
                                il existe déjà dans le modulemathles fonctions qui vont nous permettre de convertir simplement nos angles."""
                                ex : math.degrees(angle_en_radians) # Convertit en degrés
                                     math.radians(angle_en_degrés) # Convertit en radians 
math.cos =  cosinus 
math.sin =  sinus ;
math.tan = tangente 
math.acos = arc cosinus 
math.asin = arc sinus 
math.atan = arc tangente


Arrondir un nombre = """ Le modulemathnous propose plusieurs fonctions pour arrondir un nombre selon différents critères."""
                         ex : >>> math.ceil(2.3) # Renvoie le plus petit entier >= 2.3
                         3
                         >>> math.floor(5.8) # Renvoie le plus grand entier <= 5.8
                         5
                         >>> math.trunc(9.5) # Tronque 9.5
                         9





                                   module fraction

               """  Ce module propose, entre autres, de manipuler des objets modélisant des fractions. Le constructeur de la classeFractionaccepte plusieurs types de paramètres :
                    Deux entiers, le numérateur et le dénominateur (par défaut le numérateur vaut "0" et le dénominateur "1" ).
                    Si le dénominateur est "0" , une exception "ZeroDivisionError " est levée. Une autre fraction.Une chaîne sous la forme'numerateur/denominateur'. """
                    ex : from fractions import Fraction
                         >>> un_demi = Fraction(1, 2)
                         >>> un_demi
                         Fraction(1, 2)
                         >>> un_quart = Fraction('1/4')
                         >>> un_quart
                         Fraction(1, 4)
                         >>> autre_fraction = Fraction(-5, 30)
                         >>> autre_fraction
                         Fraction(-1, 6)
                  
fractions flottante = """  Pour créer une fraction depuis un flottant, on utilise la méthode de classefrom_float."""
                           ex : >>> Fraction.from_float(0.5)
                                Fraction(1, 2)
                      """  Et pour retomber sur un flottant """
                           ex : >>> float(un_quart)
                                0.25

Manipuler les fractions = """ Maintenant, quel intérêt d'avoir nos nombres sous cette forme ? Surtout pour la précision des calculs. Les fractions que nous venons de voir 
                              acceptent naturellement les opérateurs usuels ."""
                              ex : >>> un_dixieme = Fraction(1, 10)
                                   >>> un_dixieme + un_dixieme + un_dixieme
                                   Fraction(3, 10)
                          """ alors que """
                              ex : >>> 0.1 + 0.1 + 0.1
                                   0.30000000000000004
                          """ Bien sûr, la différence n'est pas énorme mais elle est là. Tout dépend de vos besoins en termes de précision.
                              D'autres calculs :"""
                              ex : >>> un_dixieme * un_quart
                                   Fraction(1, 40)
                                   >>> un_dixieme + 5
                                   Fraction(51, 10)
                                   >>> un_demi / un_quart
                                   Fraction(2, 1)
                                   >>> un_quart / un_demi
                                   Fraction(1, 2)





                               module random


fonction random =  """ Elle génère un nombre pseudo-aléatoire compris entre 0 et 1. Ce sera donc naturellement un flottant. """
                       ex : >>> import random
                            >>> random.random()
                            0.9565461152605507
                   """ La fonctionrandrangeprend trois paramètres :
                       - la marge inférieure de l'intervalle ;
                       - la marge supérieure de l'intervalle ;
                       - l'écart entre chaque valeur de l'intervalle (1par défaut)."""
                       ex : random.randrange(5, 10, 2)
                   """ Cette instruction va chercher à générer un nombre aléatoire entre "5" inclus et "10" non inclus, avec un écart de2entre chaque valeur. 
                       Elle va donc chercher dans la liste des valeurs[5, 7, 9].Si vous ne précisez pas de troisième paramètre, 
                       il vaudra1par défaut (c'est le comportement attendu la plupart du temps)."""

fonction randint = """ Elle génère un nombre pseudo-aléatoire. La fonctionrandintprend deux paramètres :
                       - là encore, la marge inférieure de l'intervalle ;
                       - la marge supérieure de l'intervalle, cette fois incluse."""
                       ex : random.randint(1, 6)

fonction choice =  """ Renvoie au hasard un élément d'une séquence passée en paramètre."""
                       ex : >>> random.choice(['a', 'b', 'k', 'p', 'i', 'w', 'z'])
                            'k'

fonction shuffle = """ Elle prend en paramètre une séquence et la mélange ; elle modifie donc la séquence qu'on lui passe et ne renvoie rien."""
                       ex : >>> liste = ['a', 'b', 'k', 'p', 'i', 'w', 'z']
                            >>> random.shuffle(liste)
                            >>> liste
                            ['p', 'k', 'w', 'z', 'i', 'b', 'a']

fonction sample =  """ fonction prend une séquence et un nombre en paramètres. Elle retourne une nouvelle séquence contenant autant d'éléments que 
                       le nombre indiqué, sélectionnés aléatoirement dans la séquence d'origine."""
                       ex : >>> liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
                            >>> random.sample(liste, 5)
                            ['b', 'a', 'c', 'j', 'e']
                            >>> # Ou peut-être que cet exemple sera plus clair
                            ... random.sample(range(1000), 10)
                            [389, 406, 890, 955, 837, 401, 971, 716, 954, 862]

fonction uniform() = """  va générer un float aléatoire compris entre  a  et  b"""
                          ex : for i in range(3):
                                   print(random.uniform(5,10))

fonction gauss() = """ La loi normale est l’une des lois de probabilité les plus adaptées pour modéliser des phénomènes naturels issus de plusieurs événements aléatoires. 
                       Ce sont l’ensemble de ces phénomènes où la majeure partie des individus se situent autour d’une moyenne, avec des proportions décroissantes 
                       en dessous et au-dessus de cette moyenne. Le module random vous permet de générer des nombres aléatoires selon cette loi : 
                       c’est-à-dire que l’on a beaucoup plus de chances d’avoir des valeurs proches de la moyenne.
                       Exemple avec une loi centrée en 0 et avec un écart-type de 1 (loi normale "classique") """
                       ex : for i in range(10):
                              print(random.gauss(0,1)) 








                              module getpass

                         """ Réceptionner un mot de passe saisi par l'utilisateur"""

getpass() =     """ La fonction qui nous intéresse porte le même nom que le module. Elle va réagir comme input, attendre 
                    une saisie de l'utilisateur et la renvoyer. Mais à la différence d'input, elle ne va pas afficher ce que l'utilisateur saisit.
                     Le mot de passe que l'on tape est invisible. Vous appuyez sur les touches de votre clavier mais rien ne s'affiche. Cependant, 
                     vous écrivez bel et bien et, quand vous appuyez sur Entrée, la fonction getpass renvoie ce que vous avez saisi."""
                    ex : >>> from getpass import getpass
                         >>> mot_de_passe = getpass()
                         Password:
                         >>> mot_de_passe
                         'un mot de passe'

                    ex2: >>> mot_de_passe = getpass("Tapez votre mot de passe : ") #mettre le msg en FR
                         Tapez votre mot de passe : 





                              module hashlib

                 """ Permet en partant d'un mot de passe, n'importe lequel, on arrive à une seconde chaîne de caractères, complètement incompréhensible. 
                     Le chiffrement fonctionne avec plusieurs techniques ou algorithmes de chiffrement. Chiffrer un mot de passe avec un certain 
                     algorithme ne donne pas le même résultat qu'avec un autre algorithme."""

choisir un algorithme = """ Pour nous aider dans notre choix, le module hashlib nous propose deux listes :
                            - algorithms_guaranteed : les algorithmes garantis par Python, les mêmes d'une plateforme à l'autre. 
                              Si vous voulez faire des programmes portables, il est préférable d'utiliser un de ces algorithmes.
                            - algorithms_available : les algorithmes disponibles sur votre plateforme. Tous les algorithmes garantis s'y trouvent, 
                              plus quelques autres propres à votre système."""
                                   import hashlib
                                   from getpass import getpass  
                              ex : >>> hashlib.algorithms_guaranteed
                                   {'sha1', 'sha224', 'sha384', 'sha256', 'sha512', 'md5'}

sha1 =    """ nous allons créer notre objet SHA1. On va utiliser le constructeur sha1 du module hashlib. Il prend en paramètre une chaîne, 
              mais une chaîne de bytes (octets). Pour obtenir une chaîne de bytes depuis une chaîne str, on peut utiliser la méthode encode. 
              Je ne vais pas rentrer dans le détail des encodages ici. Pour écrire directement une chaîne bytes sans passer par une chaîne str, 
              vous avez une autre possibilité consistant à mettre un b minuscule avant l'ouverture de votre chaîne ."""
                   import hashlib
                   from getpass import getpass
              ex : >>> b'test'
                   b'test'

          """ Générons notre mot de passe """
              ex : >>> mot_de_passe = hashlib.sha1(b"mot de passe")
                   >>> mot_de_passe
                   <sha1 HASH object @ 0x00BF0ED0>

          """ Pour obtenir le chiffrement associé à cet objet, on a deux possibilités :
              - la méthode "digest", qui renvoie un type bytes contenant notre mot de passe chiffré.
              - la méthode "hexdigest", qui renvoie une chaîne str contenant une suite de symboles hexadécimaux (de 0 à 9 et de A à F)."""
                ex : >>> mot_de_passe.hexdigest()
                     'b47ea832576a75814e13351dcc97eaa985b9c6b7'

          """ Et pour déchiffrer ce mot de passe, On ne le déchiffre pas. Si vous voulez savoir si le mot de passe saisi par l'utilisateur 
              correspond au chiffrement que vous avez conservé, chiffrez le mot de passe qui vient d'être saisi et comparez les deux chiffrements obtenus."""
              ex : import hashlib
                   from getpass import getpass
                   
                   chaine_mot_de_passe = b"azerty"
                   mot_de_passe_chiffre = hashlib.sha1(chaine_mot_de_passe).hexdigest()
                   
                   verrouille = True
                         while verrouille:
                              entre = getpass("Tapez le mot de passe : ") # azerty
                              # On encode la saisie pour avoir un type bytes
                              entre = entre.encode()
                              
                              entre_chiffre = hashlib.sha1(entre).hexdigest()
                              if entre_chiffre == mot_de_passe_chiffre:
                                   verrouille = False
                              else:
                                   print("Mot de passe incorrect")
                                   
                         print("Mot de passe accepté...")
          



                              module unittest

                    """ Le module unittest de la bibliothèque standard de Python inclut le mécanisme des tests unitaires. Voici la structure que vous rencontrerez le plus souvent :
                        - Une fonctionnalité codée grâce à un ensemble de fonctions, de classes, de modules, de packages et autre.
                        - Pour chaque fonctionnalité, un test qui vérifie que la fonctionnalité fait bien ce qu'on lui demande. 
                          Par exemple, que si une certaine fonction est appelée avec certains paramètres, elle retourne telle valeur."""

testCase =  """ la forme la plus simple du test unitaire. Pour créer un test unitaire, la première chose est de créer une classe héritant de "unittest.TestCase"."""
                ex : import random
                     import unittest

                     class RandomTest(unittest.TestCase):
            """ On peut définir ensuite un test dans une méthode dont le nom commence par test.
                Test de la fonction "random.choice".  """ 
                ex : class RandomTest(unittest.TestCase):
                     """Test case utilisé pour tester les fonctions du module 'random'."""
                     
                     def test_choice(self):
                          """Test le fonctionnement de la fonction 'random.choice'."""
                          liste = list(range(10))
                          elt = random.choice(liste)
                          # Vérifie que 'elt' est dans 'liste'
                          self.assertIn(elt, liste)               
            """  1 D'abord à la première ligne, on crée une liste de 0 à 9,
                 2 Ensuite on appelle la fonction random.choice sur notre liste et on récupère le retour,
                 3 Enfin, on vérifie que notre élément retourné par random.choice se trouve bien dans notre liste. On utilise pour ce faire une méthode assertIn 
                   et pas le mot clé assert. En fait, unittest.TestCase propose plusieurs méthodes d'assertion que nous utiliserons dans nos tests unitaires. 
                   Une assertion lève une exception qui serait considérée par unittest comme une erreur. Nous verrons plus loin comment les erreurs sont gérées.
                 Si vous exécutez ce code dans votre interpréteur... rien ne se passe ! Vous avez créé une classe mais vous n'avez pas demandé au test de se lancer. 
                 Pour ce faire vous pouvez exécuter l'instruction   """  
                 ex : unittest.main()
                      .
                      ----------------------------------------------------------------------
                      Ran 1 test in 0.003s
                      OK
            """ Le retour affiché se décompose en trois parties
                1 D'abord, la première ligne contient un caractère par test exécuté. Les principaux caractères sont un point (".") 
                  si le test s'est validé, la lettre F si le test n'a pas obtenu le bon résultat et la lettre E si le test a rencontré une erreur 
                  (si une exception a été levée pendant l'exécution de la méthode).
                2 Ensuite se trouve une ligne récapitulative du nombre de tests exécutés.
                3 Enfin, la dernière ligne récapitule le nombre de réussites ou échecs ou erreurs. Si tout va bien, cette dernière ligne devrait être simplement "OK".  """  

                Faire échouer le test : modifier le code pour provoquer un échec : 
                ex : class RandomTest(unittest.TestCase):
                     """Test case utilisé pour tester les fonctions du module 'random'."""
                     def test_choice(self):
                          """Test le fonctionnement de la fonction 'random.choice'."""
                          liste = list(range(10))
                          elt = random.choice(liste)
                          self.assertIn(elt, ('a', 'b', 'c'))

            """ Et après un appel à unittest.main()""" 
                ex : F
                ======================================================================
                FAIL: test_choice (__main__.RandomTest)
                Test le fonctionnement de la fonction 'random.choice'.
                ----------------------------------------------------------------------
                Traceback (most recent call last):
                    File "code.py", line 13, in test_choice
                         self.assertIn(elt, ('a', 'b', 'c'))
                AssertionError: 0 not found in ('a', 'b', 'c')
                ----------------------------------------------------------------------
                Ran 1 test in 0.004s
                FAILED (failures=1)  

            """ Ici, on parle d'échec (failure) et non pas d'erreur (error). Cela signifie que notre assertion 
                ne s'est pas vérifiée (regardez le traceback) mais que notre test s'est correctement exécuté.
                Le traceback est assez détaillé : il donne la ligne de l'erreur avec les appels successifs, si on a besoin de remonter la piste de l'erreur. 
                Le message d'erreur lui-même donne des informations plus précises sur pourquoi le test a échoué (0 not found in ('a', 'b', 'c')). """

Test de la fonction random.shuffle = """  elle prend une liste en paramètre et mélange cette liste aléatoirement. """
           ex : class RandomTest(unittest.TestCase):
                """Test case utilisé pour tester les fonctions du module 'random'."""
                # Autres méthodes de test
                def test_shuffle(self):
                     """Test le fonctionnement de la fonction 'random.shuffle'."""
                     liste = list(range(10))
                     random.shuffle(liste)
                     liste.sort()
                     self.assertEqual(liste, list(range(10)))                                 
                """  on appelle la fonction random.shuffle avant de trier de nouveau notre liste. Une fois la liste triée de nouveau, 
                     elle devra être identique à notre liste d'origine (list(range(10))).Ici, nous avons utilisé la méthode assertEqual 
                     qui sera sans doute celle que vous utiliserez le plus souvent.""" 

Test de la fonction random.sample = """ Cette fonction prend deux paramètres : une séquence et un nombre K. Elle retourne une liste 
                                        contenant K éléments sélectionnés aléatoirement dans notre séquence de base."""
                ex : class RandomTest(unittest.TestCase):
                     """Test case utilisé pour tester les fonctions du module 'random'."""
                     # Autres méthodes de test
                     def test_sample(self):
                          """Test le fonctionnement de la fonction 'random.sample'."""
                          liste = list(range(10))
                          extrait = random.sample(liste, 5)
                          for element in extrait:
                               self.assertIn(element, liste)
                          
                          self.assertRaises(ValueError, random.sample, liste, 20)
                """ La dernière ligne mérite quelques explications. On utilise encore une méthode d'assertion assert* (cette fois, assertRaises).
                    On peut utiliser cette méthode de deux façons :
                    Soit, comme on vient de le faire, en précisant d'abord le type de l'exception qui doit être levée, puis la fonction qui doit 
                    être appelée (la référence, sans parenthèses) et enfin les paramètres attendus par la fonction.
                    Soit en utilisant un context manager (gestionnaire de contexte) qui rend le code plus facile à lire."""

context manager =  ex :     def test_sample(self):
                            """Test le fonctionnement de la fonction 'random.sample'."""
                            liste = list(range(10))
                            extrait = random.sample(liste, 5)
                            for element in extrait:
                                 self.assertIn(element, liste)

                            with self.assertRaises(ValueError):
                                 random.sample(liste, 20)
                 """ On appelle un nouveau context manager grâce au mot-clé with ouvert sur le retour de la méthode assertRaises. 
                     Cette fois, on ne passe en paramètre de cette méthode que le type de notre exception ;À l'intérieur de notre bloc 
                     se trouve la ligne qui doit lever l'exception ValueError. Si le bloc dans le context manager lève bien l'exception, alors le test passe. Sinon il ne passe pas.
                     Cette seconde syntaxe est plus lisible, à mon sens, mais je vous montre les deux car vous pourriez trouver la première au cours de vos lectures d'autres codes."""   






                                   module "re"               
                                   Les expressions régulèrieres (regex (abréviation de Regular Expression))


Initialisation des tests = " toutes nos méthodes de test commencent par cette ligne de code " liste = list(range(10))
                         """ Il existe un moyen pour éviter de répéter cette ligne à chaque fois. Nos méthodes de test partagent un point commun : 
                             elles sont définies dans la même classe. Autant en profiter.unittest.TestCase nous propose une méthode qui est appelée 
                             avant chaque méthode de test. Il serait mieux que la création de notre liste (de 0 à 9) se trouve dans cette méthode.
                             Son nom est setUp. Créez-la dans votre classe."""
                             ex : class RandomTest(unittest.TestCase):
                                   def setUp(self):
                                        """Initialisation des tests."""
                                        self.liste = list(range(10))
                         """ Au lieu de créer la liste, on utilise l'attribut d'instance créé dans la méthode setUp. 
                             Il existe également une méthode tearDown qui est appelée après chaque test. """              

     Récapitulatif complet du code de test : 
     """ pour tester le code, vous pouvez ajouter l'instruction "unittest.main()" à la fin de votre module."""
import random
import unittest

class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def setUp(self):
        """Initialisation des tests."""
        self.liste = list(range(10))

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        elt = random.choice(self.liste)
        self.assertIn(elt, self.liste)

    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        random.shuffle(self.liste)
        self.liste.sort()
        self.assertEqual(self.liste, list(range(10)))

    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        extrait = random.sample(self.liste, 5)
        for element in extrait:
            self.assertIn(element, self.liste)

        with self.assertRaises(ValueError):
            random.sample(self.liste, 20)


Les principales méthodes d assertion : 

     Méthode                                                Explications

assertEqual(a, b)                                           a == b

assertNotEqual(a, b)                                        a != b

assertTrue(x)                                               x is True

assertFalse(x)                                              x is False

assertIs(a, b)                                              a is b

assertIsNot(a, b)                                           a is not b

assertIsNone(x)                                             x is None

assertIsNotNone(x)                                          x is not None

assertIn(a, b)                                              a in b

assertNotIn(a, b)                                           a not in b

assertIsInstance(a, b)                                      isinstance(a, b)

assertNotIsInstance(a, b)                                   not isinstance(a, b)

assertRaises(exception, fonction, *args, **kwargs)          Vérifie que la fonction lève l'exception attendue.





                              module Thread

                    """ Python nous propose dans sa bibiliothèque standard plusieurs modules pour faire de la « programmation parallèle », c'est-à-dire que plusieurs instructions 
                        de code s'exécuteront en même temps, ou presque en même temps.Nous allons regarder de plus près le module threading qui propose une interface simple pour
                        créer des threads, c'est-à-dire des portions de notre code qui seront exécutées en même temps."""

               ex :import random
                   import sys
                   from threading import Thread
                   import time
                   class Afficheur(Thread):
                        """Thread chargé simplement d'afficher une lettre dans la console."""
                        def __init__(self, lettre):
                             Thread.__init__(self)
                             self.lettre = lettre
                         def run(self):
                              """Code à exécuter pendant l'exécution du thread."""
                              i = 0
                              while i < 20:
                                   sys.stdout.write(self.lettre)
                                   sys.stdout.flush()
                                   attente = 0.2
                                   attente += random.randint(1, 60) / 100
                                   time.sleep(attente)
                                   i += 1
                    """ Le constructeur ne devrait pas trop vous surprendre. Il prend en paramètre la lettre à afficher (nous verrons des exemples plus loin). 
                        Il appelle le constructeur parent (Thread.__init__(self)) et c'est une étape importante, ne l'oubliez pas quand vous redéfinissez le constructeur de votre thread ;
                        la méthode run est également redéfinie. Le code qu'elle contient vous semble sans doute familier : c'est le code que nous avons utilisé dans notre 
                        exemple de programmation linéaire tout à l'heure."""

                    """ Vous avez défini le thread, mais il nous reste à le créer. Ou plutôt, à les créer, car nous allons essayer de faire deux threads s'exécutant en même temps."""
                    """ D'abord, on crée nos deux threads. Les objets Thread sont conservés dans nos variables thread_1 et thread_2. Notez qu'on passe en paramètre de nos deux threads des 
                        lettres différentes, pour pouvoir les différencier quand ils commenceront à afficher les informations dans la console.""" 
                   # Création des threads
                   thread_1 = Afficheur("1")
                   thread_2 = Afficheur("2")
                   """ ensuite, on appellethread_1.start(). Cette méthode va créer un thread (une partie du code qui va pouvoir s'exécuter en parallèle) et exécuter la méthode run. 
                       Nos chiffres 1 commencent ainsi à s'afficher dans notre console. Mais la méthodestartn'attend pas que tous les chiffres soient écrits avant de retourner et 
                       on passe tout de suite à la ligne suivante ;C'est au tour du second thread. Il est également lancé. Les deux threads s'exécutent en même temps."""
                   # Lancement des threads
                   thread_1.start()
                   thread_2.start()
                   """ Enfin, on appelle la méthodejoin()sur les deux threads. Cette méthode bloque et ne retourne que quand le thread est terminé. Si le programme se termine pendant 
                       que des threads tournent, les threads risquent d'être fermés brusquement."""
                   # Attend que les threads se terminent
                   thread_1.join()
                   thread_2.join()
                  

La synchronisation des threads = """ Il existe plusieurs moyens de « synchroniser » nos threads, c'est-à-dire de faire en sorte qu'une partie du code ne s'exécute que si personne 
                                     n'utilise la ressource partagée. Le mécanisme de synchronisation le plus simple est le lock (verrou en anglais).C'est un objet proposé par 
                                     threading qui est extrêmement simple à utiliser : au début de nos instructions qui utilisent notre ressource partagée, on dit au lock de 
                                     bloquer pour les autres threads. Si un autre thread veut faire appel à cette ressource, il doit patienter jusqu'à ce qu'elle soit libérée."""
                                     ex : import random
                                          import sys
                                          from threading import Thread, RLock  #On importe RLock du module threading
                                          import time
                                          
                                          verrou = RLock()    #on crée un lock que l'on place dans notre variable verrou
                                          class Afficheur(Thread):
                                               """Thread chargé simplement d'afficher un mot dans la console."""
                                               def __init__(self, mot):
                                                    Thread.__init__(self)
                                                    self.mot = mot
                                               def run(self):
                                                       """Code à exécuter pendant l'exécution du thread."""
                                                       i = 0
                                                       while i < 5:
                                                            with verrou:   #dans notre méthode run, on verrouille une partie de notre thread
                                                                 for lettre in self.mot:
                                                                      sys.stdout.write(lettre)
                                                                      sys.stdout.flush()
                                                                      attente = 0.2
                                                                      attente += random.randint(1, 60) / 100
                                                                      time.sleep(attente)
                                                            i += 1
                                """ On utilise là encore un context manager pour indiquer quand bloquer le lock. Le lock se débloque à la fin du bloc with. 
                                    La partie verrouillée de notre code ne s'exécute qu'un thread à la fois.D'abord, thread_1 est lancé. Il verrouille le lock 
                                    et commence à afficher les lettres de son mot ("canard") ;
                                    thread_2 est lancé entre temps, mais il bloque au moment d'afficher son propre mot, car le verrou est détenu par thread_1. 
                                    Ce n'est que quand thread_1 relâche le verrou (à la fin du bloc with) qu'il peut commencer à s'exécuter ;
                                    ... Et ainsi de suite jusqu'à la fin des deux threads."""





                              module Tkinter

                     """ Tkinter (Tk interface) est un module intégré à la bibliothèque standard de Python, bien qu'il ne soit pas maintenu directement par 
                         les développeurs de Python. Il offre un moyen de créer des interfaces graphiques via Python.Tkinter est disponible sur Windows 
                         et la plupart des systèmes Unix. Les interfaces que vous pourrez développer auront donc toutes les chances d'être portables 
                         d'un système à l'autre.Nous pour créer des interfaces graphiques. Tkinter a l'avantage d'être disponible par défaut, 
                         sans nécessiter une installation supplémentaire. """   
                         from tkinter import *

créer une fenêtre avec Tkinter = """On commence par importer Tkinter"""
                                   from tkinter import *

                                   """On crée ensuite un objet de la classeTk. La plupart du temps, cet objet sera la fenêtre principale de notre interface."""
                                   fenetre = Tk()

                                   """On crée unLabel, c'est-à-dire un objet graphique affichant du texte"""
                                   # # Note : le premier paramètre passé au constructeur de Label est notre
                                   # # interface racine
                                   champ_label = Label(fenetre, text="Salut les Zér0s !")

                                   """On appelle la méthodepackde notreLabel. Cette méthode permet de positionner l'objet dans notre fenêtre (et, par conséquent, de l'afficher)."""
                                   champ_label.pack()

                                   """Enfin, on appelle la méthodemainloopde notre fenêtre racine. Cette méthode ne retourne que lorsqu'on ferme la fenêtre."""
                                   fenetre.mainloop()

widget =    """ Nos objets graphiques (boutons, champs de texte, cases à cocher, barres de progression…) sont appelés des widgets. On peut préciser plusieurs options 
                lors de la construction de nos widgets. Ici, on définit l'optiontextde notreLabelà"Salut les Zér0s ! Il existe d'autres options communes à la plupart 
                des widgets (la couleur de fond "bg", la couleur du widget "fg", etc.) et d'autres plus spécifiques à un certain type de widget. 
                Le "Label" par exemple possède l'option text représentant le texte affiché par le Label. 
                Pour qu'un widget apparaisse, il faut : 
                qu'il prenne, en premier paramètre du constructeur, la fenêtre principale
                qu'il fasse appel à la méthode "pack". La méthode "pack" permet de positionner un objet dans une fenêtre ou dans un cadre"""

widget Label
Les labels =  """ On s'en sert pour afficher du texte dans notre fenêtre, du texte qui ne sera pas modifié par l'utilisateur."""
                  ex : champ_label = Label(fenetre, text="contenu de notre champ label")
                       champ_label.pack()

widget Button
Les boutons = """ Les boutons sont des widgets sur lesquels on peut cliquer et qui peuvent déclencher des actions ou commandes """
                  ex : bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
                       bouton_quitter.pack()
              """ le dernier paramètre passé à notre constructeur deButton. Il s'agit de l'action liée à un clic sur le bouton. 
                  Ici, c'est la méthodequitde notre fenêtre racine qui est appelée. Ainsi, quand vous cliquez sur le boutonQuitter, la fenêtre se ferme."""

widget Entry
Une ligne de saisie = """ Une zone de texte dans laquelle l'utilisateur peut écrire. En fait de zone, il s'agit d'une ligne simple.
                          On préférera créer une variable Tkinter associée au champ de texte."""
                          ex : var_texte = StringVar()
                               ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
                               ligne_texte.pack()
                      """ À la ligne 1, nous créons une variable Tkinter. En résumé, c'est une variable qui va ici contenir le texte de notreEntry. 
                          Il est possible de lier cette variable à une méthode de telle sorte que la méthode soit appelée quand la variable est modifiée 
                          (l'utilisateur écrit dans le champEntry)."""

widget Checkbutton
Les cases à cocher = """ Les cases à cocher sont définies dans la classeCheckbutton. Là encore, on utilise une variable pour surveiller la sélection de la case.
                         Pour surveiller l'état d'une case à cocher (qui peut être soit active soit inactive), on préférera créer 
                         une variable de type "IntVar" plutôt que "StringVar", bien que ce ne soit pas une obligation."""
                         ex : var_case = IntVar()
                              case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
                              case.pack()
                     """ Vous pouvez ensuite contrôler l'état de la case à cocher en interrogeant la variable."""
                         ex : var_case.get()
                     """ Si la case est cochée, la valeur renvoyée par la variable sera "1". Si elle n'est pas cochée, ce sera0.
                         Notez qu'à l'instar d'un bouton, vous pouvez lier la case à cocher à une commande qui sera appelée quand son état change.""" 

widget
Les boutons radio = """ Les boutons radio (radio buttons en anglais) sont des boutons généralement présentés en groupes. C'est, à proprement parler, 
                        un ensemble de cases à cocher mutuellement exclusives : quand vous cliquez sur l'un des boutons, celui-ci se sélectionne 
                        et tous les autres boutons du même groupe se désélectionnent.Ce type de bouton est donc surtout utile dans le cadre d'un regroupement.
                        Pour créer un groupe de boutons, il faut simplement qu'ils soient tous associés à la même variable (là encore, une variable Tkinter). 
                        La variable peut posséder le type que vous voulez."""
                        ex : var_choix = StringVar()
                        
                        choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")
                        choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
                        choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")
                        
                        choix_rouge.pack()
                        choix_vert.pack()
                        choix_bleu.pack()
                    """ Pour récupérer la valeur associée au bouton actuellement sélectionné, interrogez la variable."""
                        ex : var_choix.get()

widget
Les listes déroulantes = """ Ce widget permet de construire une liste dans laquelle on peut sélectionner un ou plusieurs éléments. Le fonctionnement 
                             n'est pas tout à fait identique aux boutons radio. Ici, la liste comprend plusieurs lignes et non un groupe de boutons."""  
                             ex : liste = Listbox(fenetre)
                                  liste.pack()
                              """ On insère ensuite des éléments. La méthodeinsertprend deux paramètres
                                  Si vous voulez insérer des éléments à la fin de la liste, utilisez la constanteENDdéfinie par Tkinter"""
                              ex : liste.insert(END, "Pierre") # 1 la position à laquelle insérer l'élément (END);
                                   liste.insert(END, "Feuille") # 2 l'élément même, sous la forme d'une chaîne de caractères ( Feuille)
                                   liste.insert(END, "Ciseau")     
                              """ Pour accéder à la sélection, utilisez la méthodecurselectionde la liste. Elle renvoie un tuple de chaînes de caractères, 
                                  chacune étant la position de l'élément sélectionné."""
                              ex : liste.curselection() # renvoie('2',), c'est le troisième élément de la liste qui est sélectionné (Ciseauen l'occurrence).

widget Frame
Organiser ses widgets dans la fenêtre = """ Il existe plusieurs widgets qui peuvent contenir d'autres widgets. L'un d'entre eux se nomme "Frame". 
                                            C'est un cadre rectangulaire dans lequel vous pouvez placer vos widgets... ainsi que d'autres objets "Frame" si besoin est. 
                                            Si vous voulez qu'un widget apparaisse dans un cadre, utilisez le "Frame" comme parent à la création du widget."""
                                            ex : cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
                                                cadre.pack(fill=BOTH)
                                                
                                                message = Label(cadre, text="Notre fenêtre")
                                                message.pack(side="top", fill=X)
                                        """ nous avons passé plusieurs arguments nommés à notre méthodepack. Cette méthode, je vous l'ai dit, sert à placer nos widgets 
                                            dans la fenêtre (ici, dans le cadre). En précisant "side="top"", on demande à ce que le widget soit placé en haut de son parent 
                                            (ici, notre cadre). Il existe aussi l'argument nomméfillqui permet au widget de remplir le widget parent, soit en largeur si 
                                            la valeur est "X", soit en hauteur si la valeur est "Y", soit en largeur et hauteur si la valeur est "BOTH"."""          

widget Labelframe =  """ un cadre avec un titre, ce qui nous évite d'avoir à placer un "label" en haut du cadre. Il se construit comme un "Frame" mais peut prendre en argument, 
                         à la construction, le texte représentant le titre """
                         ex : cadre = Labelframe(..., text="Titre du cadre")


Créer commandes personnalisées = """ Nous pouvons créer assez simplement des commandes personnalisées, en écrivant des méthodes. Cependant, il y a ici une petite subtilité : 
                                     la méthode que nous devons créer ne prend aucun paramètre. Si nous voulons qu'un clic sur le bouton modifie le bouton lui-même ou un autre objet, 
                                     nous devons placer nos widgets dans un corps de classe. D'ailleurs, à partir du moment où on sort du cadre d'un test, 
                                     il est préférable de mettre le code dans une classe. On peut la faire hériter deFrame, ce qui signifie que notre classe sera un widget elle aussi. """
                                     ex : from tkinter import *
                                          """ On crée une classe qui contiendra toute la fenêtre. Cette classe hérite deFrame, c'est-à-dire d'un cadre Tkinter."""
                                          class Interface(Frame):
                                               """ Notre fenêtre principale.
                                               Tous les widgets sont stockés comme attributs de cette fenêtre."""
                                               """ Dans le constructeur de la fenêtre, on appelle le constructeur du cadre et onpack(positionne et affiche) le cadre."""
                                               def __init__(self, fenetre, **kwargs):
                                                    Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
                                                    self.pack(fill=BOTH)
                                                    self.nb_clic = 0
                                               """ Toujours dans le constructeur, on crée les différents widgets de la fenêtre. On les positionne et les affiche également."""     
                                                    # Création de nos widgets
                                                    self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
                                                    self.message.pack()
                                                    
                                                    self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
                                                    self.bouton_quitter.pack(side="left")
                                                    
                                                    self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",command=self.cliquer)
                                                    self.bouton_cliquer.pack(side="right")
                                               """ On crée une méthode  bouton_cliquer, qui est appelée quand on clique sur lebouton_cliquer. Elle ne prend aucun paramètre. 
                                                   Elle va mettre à jour le texte contenu dans le labelself.messagepour afficher le nombre de clics enregistrés sur le bouton."""
                                               def cliquer(self):
                                                    """Il y a eu un clic sur le bouton.
                                                    On change la valeur du label message."""
                                                    self.nb_clic += 
                                                    self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

                                 """  Pour créer notre interface """
                                 """ On crée la fenêtreTkqui est l'objet parent de l'interface que l'on instancie ensuite."""
                                     ex : fenetre = Tk()
                                          interface = Interface(fenetre)
                                 """ On rentre dans la bouclemainloop. Elle s'interrompra quand on fermera la fenêtre."""        
                                          interface.mainloop()
                                 """ Ensuite, on détruit la fenêtre grâce à la méthode destroy."""         
                                          interface.destroy()







               """Le module "re", que nous allons découvrir un peu plus loin, nous permet de faire des recherches très précises dans des chaînes de caractères et de remplacer 
                  des éléments de nos chaînes, le tout en fonction de critères particuliers. Ces critères, ce sont nos expressions régulières. Pour nous, elles se présentent 
                  sous la forme de chaînes de caractères.
                  Epoch Unix. L'idée retenue a été de représenter une date et une heure en fonction du nombre de secondes écoulées depuis une date précise. La plupart du temps, 
                  cette date est l'Epoch Unix, le 1er janvier 1970 à 00:00:00.
                  "timestamp" comme on l'appelle généralement"""
 


^"..." = """ vous voulez rechercher la syllabe "cha" en début de votre chaîne, vous écrirez donc l'expression "^cha" . Cette expression sera trouvée dans la chaîne 'chaton'
             mais pas dans la chaîne 'achat'."""

"..."$ = """Pour matérialiser la fin de la chaîne, vous utiliserez le signe "$" . Ainsi, l'expression "q$" sera trouvée uniquement si votre chaîne se termine par la lettre q minuscule."""

"..."* = """ Cela signifie que notre lettretpourra se retrouver 0, 1, 2, … fois dans notre chaîne. Autrement dit, notre expressionchat*sera trouvée dans les chaînes suivantes :
             'chat','chaton','chateau','herbe à chat','chapeau','chatterton','chattttttttt'…
              On trouvera dans chacune de ces chaînes l'expression régulière "chat*". Traduite en français, cette expression signifie : « on recherche une lettre "c" suivie d'une 
              lettre "h" suivie d'une lettre "a" suivie, éventuellement, d'une lettre "t" qu'on peut trouver zéro, une ou plusieurs fois ». Peu importe que ces lettres soient trouvées au 
              début, à la fin ou au milieu de la chaîne."""

*   =    abc* =  0, 1 ou plus = 'ab','abc','abcc','abcccccc'

+   =    abc+ = 1 ou plus = 'abc','abcc','abccc'

?   =    abc?  0 ou 1  =  'ab','abc' 

"""Vous pouvez également contrôler précisément le nombre d'occurrences grâce aux accolades. """

E{4}: signifie 4 fois la lettre E majuscule ;

E{2,4}: signifie de 2 à 4 fois la lettre E majuscule ;

E{,5}: signifie de 0 à 5 fois la lettre E majuscule ;

E{8,}: signifie 8 fois minimum la lettre E majuscule.

Les classes de caractères = """Vous pouvez préciser entre crochets plusieurs caractères ou classes de caractères. Par exemple, si vous écrivez[abcd], 
                               cela signifie : l'une des lettres parmi "a,b,c " et "d" .Pour exprimer des classes, vous pouvez utiliser le tiret "-" entre deux lettres. 
                               Par exemple, l'expression [A-Z] signifie « une lettre majuscule ». Vous pouvez préciser plusieurs classes ou possibilités dans votre expression. 
                               Ainsi, l'expression [A-Za-z0-9] signifie « une lettre, majuscule ou minuscule, ou un chiffre ».Vous pouvez aussi contrôler l'occurrence des classes comme 
                               nous l'avons vu juste au-dessus. Si vous voulez par exemple rechercher 5 lettres majuscules qui se suivent dans une chaîne, votre expression sera[A-Z]{5}."""


Les groupes =  """ Cette expression sera vérifiée pour les chaînes contenant la séquence'cha'répétée entre deux et cinq fois. Les séquences'cha'doivent se suivre naturellement.
                   Les groupes sont également utiles pour remplacer des portions de notre chaîne."""
                   ex : (cha){2,5}                               

import re =  """ Le module "re" a été spécialement conçu pour travailler avec les expressions régulières (Regular Expressions). Il définit plusieurs fonctions utiles,  ainsi que des objets 
                 propres pour modéliser des expressions.Chercher dans une chaîne """

fonction search = """ Attend deux paramètres obligatoires : l'expression régulière, sous la forme d'une chaîne, et la chaîne de caractères dans laquelle on recherche cette expression.
                      Si l'expression est trouvée, la fonction renvoie un objet symbolisant l'expression recherchée. Sinon, elle renvoie "None" Pour symboliser les caractères spéciaux dans 
                      les expressions régulières, il est nécessaire d'échapper l'anti-slash en le faisant précéder d'un autre anti-slash. Cela veut dire que pour écrire le caractère spécial "\w", 
                      vous allez devoir écrire "\\w". C'est assez peu pratique et parfois gênant pour la lisibilité. C'est pourquoi je vous conseille d'utiliser un format de chaîne que nous 
                      n'avons pas vu jusqu'à présent : en plaçant un "r" avant le délimiteur qui ouvre notre chaîne, tous les caractères anti-slash qu'elle contient sont échappés.""" 
                      r'\n'    ==      '\\n'
                      ex : >>> re.search(r"abc", "abcdef")
                           <_sre.SRE_Match object at 0x00AC1640>
                           >>> re.search(r"abc", "abacadaeaf")
                           >>> re.search(r"abc*", "ab")
                           <_sre.SRE_Match object at 0x00AC1800>
                           
                           ex2: if re.match(expression, chaine) is not None:
                           # Si l'expression est dans la chaîne
                           # Ou alors, plus intuitivement
                           if re.match(expression, chaine):    

exemple regex numero de tel : ^0[0-9]([ .-]?[0-9]{2}){4}$
                              """ D'abord, on trouve un caractère accent circonflexe^qui veut dire qu'on cherche l'expression au début de la chaîne. 
                                  Vous pouvez aussi voir, à la fin de la regex, le symbole "$" qui veut dire que l'expression doit être à la fin de la chaîne. 
                                  Si l'expression doit être au début et à la fin de la chaîne, cela signifie que la chaîne dans laquelle on recherche ne doit rien contenir 
                                  d'autre que l'expression.Nous avons ensuite le "0" qui veut simplement dire que le premier caractère de notre chaîne doit être un "0" .
                                  Nous avons ensuite une classe de caractère[0-9]. Cela signifie qu'après le "0" , on doit trouver un chiffre compris entre 0 et 9 
                                  (peut-être 0, peut-être 1, peut-être 2…).Ensuite, cela se complique. Vous avez une parenthèse qui matérialise le début d'un groupe. 
                                  Dans ce groupe, nous trouvons, dans l'ordre :D'abord une classe[ .-]qui veut dire « soit un espace, soit un point, soit un tiret ». 
                                  Juste après cette classe, vous avez un signe?qui signifie que cette classe est optionnelle.Après la définition de notre délimiteur, 
                                  nous trouvons une classe[0-9]qui signifie encore une fois « un chiffre entre 0 et 9 ». Après cette classe, entre accolades, 
                                  vous pouvez voir le nombre de chiffres attendus (2).Ce groupe, contenant un séparateur optionnel et deux chiffres, doit se retrouver 
                                  quatre fois dans notre expression (après la parenthèse fermante, vous trouvez entre accolades le contrôle du nombre d'occurrences)."""
                                  ex2 : import re
                                        chaine = ""
                                        expression = r"^0[0-9]([ .-]?[0-9]{2}){4}$"
                                        while re.search(expression, chaine) is None:
                                             chaine = input("Saisissez un numéro de téléphone (valide) :")

fonction sub =  """ Elle prend trois paramètres :
                    l'expression à rechercher ;
                    par quoi remplacer cette expression ;
                    la chaîne d'origine.
                    Elle renvoie la chaîne modifiée. Des groupes numérotésPour remplacer une partie de l'expression, on doit d'abord utiliser des groupes. 
                    Si vous vous rappelez, les groupes sont indiqués entre parenthèses. """ 
                    ex : (a)b(cd)
                         >>> re.sub(r"(ab)", r" \1 ", "abcdef")
                         ' ab cdef'
                """ Dans cet exemple,(a)est le premier groupe et(cd)est le second. L'ordre des groupes est important dans cet exemple. Dans notre expression 
                    de remplacement, nous pouvons appeler nos groupes grâce à "\<numéro du groupe>". Pour une fois, on compte à partir de 1."""

Donner des noms à nos groupes =  """ Nous pouvons également donner des noms à nos groupes. Cela peut être plus clair que de compter sur des numéros. 
                                     Pour cela, il faut faire suivre la parenthèse ouvrant le groupe d'un point d'interrogation, d'un P majuscule et du nom du groupe entre chevrons <>. """                   
                                     (?P<id>[0-9]{2})
                                     ex : >>> texte = """
                                          ... nom='Task1', id=8
                                          ... nom='Task2', id=31
                                          ... nom='Task3', id=127"""
                                          ... ...
                                          >>> print(re.sub(r"id=(?P<id>[0-9]+)", r"id[\g<id>]", texte))
                                          nom='Task1', id[8]
                                          nom='Task2', id[31]
                                          nom='Task3', id[127]

Des expressions compilées = """ Si, dans votre programme, vous utilisez plusieurs fois les mêmes expressions régulières, il peut être utile de les compiler. Le module "re" 
                                propose en effet de conserver votre expression régulière sous la forme d'un objet que vous pouvez stocker dans votre programme. 
                                Si vous devez chercher cette expression dans une chaîne, vous passez par des méthodes de l'expression. Cela vous fait gagner en performances 
                                si vous faites souvent appel à cette expression.Par exemple, j'ai une expression qui est appelée quand l'utilisateur saisit son mot de passe. 
                                Je veux vérifier que son mot de passe fait bien six caractères au minimum et qu'il ne contient que des lettres majuscules, minuscules et des chiffres."""
                                ^[A-Za-z0-9]{6,}$ 
                            """ Pour conserver l'expression en mémoire.On utilise pour ce faire la méthodecompiledu modulere. On stocke la valeur renvoyée (une expression régulière compilée) 
                                dans une variable, c'est un objet standard pour le reste."""
                                ex : chn_mdp = r"^[A-Za-z0-9]{6,}$"
                                     exp_mdp = re.compile(chn_mdp)
                            """ Ensuite, vous pouvez utiliser directement cette expression compilée. Elle possède plusieurs méthodes utiles, dont "search" et "sub" 
                                que nous avons vu plus haut. À la différence des fonctions du modulereportant les mêmes noms, elles ne prennent pas en premier paramètre 
                                l'expression (celle-ci se trouve directement dans l'objet)."""
                                ex : chn_mdp = r"^[A-Za-z0-9]{6,}$"
                                     exp_mdp = re.compile(chn_mdp)
                                     mot_de_passe = ""
                                     while exp_mdp.search(mot_de_passe) is None:
                                          mot_de_passe = input("Tapez votre mot de passe : ")         





                    bs4, BeautifullSoup

soup.find() = """ fonction .find permet de chercher des balises "<>" comme le titre ex <title>. .find va chercher dans
                  le code html la balise avec le mot qui est en argument."""
                  ex : title = soup.find("title") # cherche la balise avec le mot title 

soup.findAll = """ rechercher toute les itérations de article (donc chercher le nombre d'objet "article" dans la page)"""
                   ex : article_class= soup.findAll("article")    







