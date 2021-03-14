~  =  """  signifie que je n’ai pas encore changé de répertoire : je suis dans le répertoire de l’utilisateur “DaltonX”, à savoir /home/DaltonX. 
           Je peux taper mes instructions derrière le $."""

Comprenez les arguments de la ligne de commande

""" La plupart des instructions de la ligne de commande prennent en compte des “paramètres” (ou “arguments”) qui vont venir “compléter” 
    l’instruction et modifier son comportement. Par exemple, avec pwd. Au lieu de taper simplement l’instruction “pwd", vous allez 
    rajouter le paramètre “--help”. Cette commande avec l’argument --help n’affiche plus le répertoire 
    dans lequel vous vous trouvez, mais l’aide associée à la commande."""

raccourcis utiles 

- """ la flèche haut et la flèche bas permettent de naviguer dans l'historique du terminal 
      et de relancer des commandes déjà tapées précédemment. """

- """ "tab" permet de faire de l'autocomplétion, c’est-à-dire compléter automatiquement une commande ou un chemin 
      si on a commencé à en taper le début. Si plusieurs options sont disponibles, taper une deuxième fois 
      sur cette touche affichera la liste des options possibles"""

- """ ctrl + r: cette combinaison permet de faire une recherche dans l'historique des commandes. 
      Faites d’abord ctrl+r pour passer en mode “recherche”, puis tapez une partie de la commande 
      que vous voulez rejouer. Lorsque votre recherche a porté ses fruits, vous n’avez plus qu’à valider en appuyant sur Entrée."""

- """ ctrl + a et ctrl + e : ces deux combinaison permettent respectivement d'aller automatiquement au 
      tout début ou à la toute fin de la ligne de commande que vous êtes en train de taper, 
      ce qui peut être pratique lorsque vous êtes en train d'écrire une commande particulièrement longue."""



pwd = """  signifie en réalité « Print Working Directory » (ou, en français, « afficher le répertoire de travail »).
           La commande pwd demande au terminal d’indiquer l’endroit où vous vous trouvez dans l’arborescence de fichiers.  """          
           ex : DaltonX@DX-PC ~
                $ pwd
                /home/DaltonX

cd =  """ pour changer de repertoire commence par cd !!!!!!"""
          ex : cd c:/blabla/blabla

ls = """  La commande ls (qui est le raccourci pour "list" en anglais) permet de lister le contenu d'un répertoire."""
          ex : DaltonX@DX-PC /cygdrive/c/users/ptibu/desktop/programmation
               $ ls
               C                     Project1        'Projet en cours'
               ConsoleApplication1  'Projet Python'  'les cours - les bases etc' 

ls -l = """ Pour plus de précision. 
            l : ce paramètre précise à la commande ls d’afficher plus d’informations sur chacun des éléments présents
            Chaque ligne possède beaucoup d’informations. Vous pouvez par exemple repérer que chaque ligne commence par un 
            “d” ou un “-”. Lorsque la ligne commence par un “d”, pour “directory”, cela signifie 
            que l’élément correspondant est un dossier. Sinon, c’est un fichier."""

ls -a = """ -a : ce paramètre indique que tous les dossiers et fichiers devront apparaître, y compris les dossiers et fichiers cachés. """


ls -la = """ Il est également possible de combiner ces deux commandes. Cela s’écrira ls -l -a ou plus simplement : ls -la"""

ls nomDuRepertoire = """ afficher le contenu d’un autre répertoire contenue dans le dossier"""
                         ex : ls c  # je me base sur le dossier programmation donc le "C" = nom de dossier

ls .  """ Dossier cachés“.” : ce dossier désigne toujours le répertoire dans lequel on se trouve. Autrement dit, 
          si “pwd” vous dit que vous êtes dans /cygdrive/c/OpenClassrooms, alors le terminal remplacera automatiquement “.” 
          par “/cygdrive/c/OpenClassrooms” ;"""
          ex : ls .                

ls .. """ Dossier cachés “..” : ce dossier désigne toujours le répertoire parent (c’est-à-dire le dossier qui contient 
          le dossier dans lequel vous êtes actuellement)."""
          ex : ls .. 

ls -la répertoire = """ es paramètres peuvent être combinés. ls -la C va afficher le contenu du répertoire “C”, 
                        avec les dossiers et fichiers cachés (option “a”) et sous forme de liste détaillée (option “l”). """

dossier avec espace = """ Si vous souhaitez lister le contenu d'un dossier dont le nom contient un espace comme « mon dossier » 
                          cela peut poser des problèmes, car la commande « ls » croira que vous cherchez à lister le contenu 
                          deux dossiers distincts : "mon" et "dossier". Pour afficher le contenu d’un dossier dont le nom 
                          contient un espace, vous pouvez utiliser des guillemets""" 
                          
cd = """ la commande « cd », pour « Change Directory » (« changer de répertoire », en français) 
          vous permettra de naviguer d'un répertoire à l'autre."""
          ex : DaltonX@DX-PC /cygdrive/c/users/ptibu/desktop/programmation
               $ cd c
               DaltonX@DX-PC /cygdrive/c/users/ptibu/desktop/programmation/c

mkdir = """ mkdir est la contraction de “make directory”, c’est-à-dire “Créer un répertoire”, en français.
            La syntaxe de mkdir est simple : il suffit de taper "mkdir" suivi du nom du répertoire que l'on désire créer."""
            ex : mkdir test   # création du dossier test                         
            ex2: mkdir test test1 test2  # création de 3 dossiers
        """ créer un dossier dont le nom possède un espace,est d'entourer le nom du dossier avec des guillemets."""
            ex : mkdir "dossier test"    
            ex2: mkdir dossier\ test

** ni dans VSC
touch = """ crée un fichier exactement de la même manière que pour créer un dossier"""
            ex : touch test #création d'un fichier 
            ex2: touch test test1 test2 # création de plusieurs fichiers
            ex3: touch "test espace"
            ex4: touch test2\ espace

mv = """ Déplacer un fichier, la commande à utiliser est mv pour “move”, déplacer, en français. 
         La syntaxe sera donc : mv elementADeplacer destination."""
         ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
              $ mv test testdéplacement  # testdéplacement est un dossier dans test création dossier
     """ Faire l’opération inverse et remettre le fichier “fichier.txt” là où il était. On utilise dossier caché “.”, 
         celui qui indiquait quel est le dossier courant. C’est ici qu’il va prendre toute son utilité.
         “testdéplacement/test” sert ici à désigner le fichier “test.txt” qui se trouve à l’intérieur du répertoire “testdéplacement”, 
         et “.” signifie “ici”."""
         ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
              $ mv testdéplacement/test .
     """ rename """
          ex : mv fichierOldName  fichierNewName


cp = """ Copier du contenu, nous allons procéder exactement de la même manière que ce que nous avons fait pour la commande mv, 
         mais avec la commande “cp”."""
         ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
              $ cp test testdéplacement  #test nom du fichier a copier vers le dossier testdéplacement
     """ Pour copier le fichier “test” dans le même répertoire, mais avec un nouveau nom, ici “test22”."""
         ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
              $ cp test test22
     """ La copie d’un répertoire. Le terminal demande donc une confirmation avec l’option -r 
         (r pour “récursif” qui signifie au terminal qu’il va devoir aller à l’intérieur 
         du dossier, et des sous-dossiers, et ainsi de suite)."""
         ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
              $ cp -r testdéplacement testdépladossier

rm = """ La suppression se fait avec rm, remove, qui signifie tout simplement “supprimer”, en français."""
         ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
              $ rm test
     """ pour un répertoire"""
         ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
              $ rm -r testdépladossier

man = """ La commande “man” affiche l’aide associée à une commande. Pour cela, il suffit de taper man commande. 
          Pour naviguer dans cette aide, vous pouvez utiliser flèche haut et flèche bas. Et pour sortir de cette aide, 
          vous pouvez taper sur la touche q (q pour pour "quitter"). """
          ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
               $ man ls
           
cat / less / more = """ Ces trois commandes ont le même but, à savoir afficher le contenu d’un fichier. Pour “less”, la différence, 
                        c’est que cet affichage va être “paginé”. C’est-à-dire qu’au lieu d’afficher le contenu directement 
                        sous la commande, le terminal va utiliser le même mode de visualisation qu’avec la commande “man”."""
                        ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
                             $ cat test1
                             ceci n'est qu'un test !!
                        ex2: DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
                             $ less test1
                        ex3: DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
                             $ more test1
                             ceci n'est qu'un test !!
     
> = """ Une redirection consiste à prendre la “sortie” d’une commande (par exemple pour “ls”, la sortie est tout simplement :
        afficher la liste des répertoires à l’écran) et à la rediriger vers autre chose, ici vers un fichier.""" 
        ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
             $ ls -l
             total 5
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 11:17 'fichier test.txt'
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 11:17  fichiertest.txt
             -rw-rw-r--+ 1 DaltonX Aucun 24 Mar 10 14:51  test1
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 11:18  test2
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 12:05  test22
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 12:04  test24
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 11:18  test3
             drwxrwxr-x+ 1 DaltonX Aucun  0 Mar 10 12:02  testdéplacement
             
             DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
             $ ls -l > liste.txt
             
             DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
             $ cat liste.txt
             total 5
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 11:17 fichier test.txt
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 11:17 fichiertest.txt
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 14:58 liste.txt
             -rw-rw-r--+ 1 DaltonX Aucun 24 Mar 10 14:51 test1
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 11:18 test2
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 12:05 test22
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 12:04 test24
             -rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 11:18 test3
             drwxrwxr-x+ 1 DaltonX Aucun  0 Mar 10 12:02 testdéplacement
 
grep = """ Grep sert à chercher des éléments à l’intérieur d’un fichier sans même avoir besoin de les ouvrir."""
           DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
           $ grep ceci test1 #grep ceQueVousVoulezChercher làOùVousVoulezChercher 
           ceci n'est qu'un test !!
       """ Si nous voulons chercher par exemple “txt” dans l’intégralité des fichiers du répertoire courant, alors la commande 
           sera grep txt *. Comme grep fait ses recherches dans des fichiers, lorsqu’il rencontre un élément qui est un répertoire, 
           il affiche un message pour préciser que cet élément est un répertoire et qu'il ne peut donc pas vérifier si la chaîne 
           se trouve bien à l'intérieur. Lorsque grep rencontre des fichiers, il les vérifie et soit il reste silencieux quand il n'y a rien 
           à l'intérieur qui corresponde à la recherche, soit il affiche le contenu qui correspond (par exemple “liste.txt” contient 
           trois lignes avec “txt” dedans, et ces lignes sont bien affichées). """ 
           ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
                $ grep test *
                liste.txt:-rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 11:17 fichier test.txt
                liste.txt:-rw-rw-r--+ 1 DaltonX Aucun  0 Mar 10 11:17 fichiertest.txt
                liste.txt:-rw-rw-r--+ 1 DaltonX Aucun 24 Mar 10 14:51 test1
                liste.txt:drwxrwxr-x+ 1 DaltonX Aucun  0 Mar 10 12:02 testdéplacement
                test1:ceci n'est qu'un test !!
                grep: testdéplacement: Is a directory
  


wildcards """ déplacer beaucoup de fichiers d’un coup C’est pour cette raison que l’on a créé des “wildcards” ou “jokers”. 
              Ce sont des caractères qui “remplacent” une partie du nom d’un fichier. Il en existe plusieurs, 
              mais le plus connu d’entre eux est probablement le caractère *. Ce caractère peut être utilisé comme substitut 
              pour n’importe quelle autre chaîne de caractères dans une recherche. cela fonctionne avec toutes les commandes  (mv etc....)""" 
              ex : DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier
                   $ ls t*  "tu peux aussi"  $ ls -la t*
                   test  test1  test2  test3
                   testdéplacement:
              ex2: DaltonX@DX-PC /cygdrive/c/OpenClassrooms/test création dossier # déplace tous les dossiers et fichiers 
                   $ mv * testdéplacement
              




                            package


pip install  = """ Installez et utilisez un paquet Python"""
                   ex : pip install matplotlib # matplotlib crée des graphique

pip list    =  """ Pour vérifier les paquets Python que vous avez installés répertorie tous les paquets 
                   que vous avez installés (et leurs dépendances)  """
pip freeze  =  """ répertorie les paquets que vous avez installés (mais pas leurs dépendances) 
                   dans un format adapté au stockage dans un fichier (souvent appelé fichier requirements.txt )"""

pip show  = """ vous montre des informations utiles sur un ou plusieurs paquets que vous avez installés"""
                ex : pip show requests
            """ obtenir des informations sur plusieurs paquets, en séparant les noms des paquets par des espaces"""
                ex : pip show requests matplotlib    

pip install package==0.0.0 = """ installer une version de paquet Python """

pip install package~=2.2 = """ installera la version la plus élevée disponible au-dessus de 2.2!, mais pas 3.0  ni les versions ultérieures."""

pip install package~=2.1.0 = """ installera la version la plus élevée disponible au-dessus de 2.1.0  , mais pas la version 2.2.0  
                                  ni les versions ultérieures."""

pip install package>2.5.0  = """ installera la version la plus élevée disponible au-dessus de 2.5.0 """

pip install "package>2.4.0,<2.6.0" = """  installera la version la plus élevée disponible supérieure à 2.4.0, mais inférieure à 2.6.0.
                                           Notez que dans le dernier exemple, puisque nous utilisons une syntaxe plus compliquée, 
                                           nous encadrons le nom du paquet et nos exigences de versions avec des guillemets."""

pip uninstall <package> = """ désinstaller un package """









                            LES PAQUETS

matplotlib = """ création de graphique"""  

numpy = """  pour arrondir les nombres à l'entier inférieur ou supérieur. """  
             ex : import numpy
             
                  print(numpy.ceil(1.2))
                  print(numpy.ceil(1.933))
                  print(numpy.floor(1.2))                       +

                  



                         Environnement :
                    """  il est préférable de créer un environnement pour chacun des projets sur lesquels nous 
                         travaillons et d'installer les paquets localement, au sein de l'environnement."""



python -m venv <environment name> = """ Créer un environnement """

<environment name>/Scripts/activate.bat = """ Activer l'environnement. À ce stade, votre terminal (selon celui que vous utilisez) 
                .bat pas obligatoire          ajoutera probablement le nom de votre environnement au début de chaque ligne 
source env/bin/activate (linux)               de votre terminal (ici, ‘env’) """                                    
                                   ****** """ grosse galère cela ne fonctionne pas j'ai du ouvrir powershell en admin taper 
                                             "Set-ExecutionPolicy RemoteSigned" et valider ensuite aller dans le repertoire 
                                             "env" et taper "\Scripts\activate""""

<environment name>/Scripts/deactivate = """ Vous devrez « quitter » ou « désactiver » votre environnement virtuel à l'aide de 
                                            la commande deactivate  pendant que votre environnement virtuel est activé. 
                                            Selon le terminal que vous utilisez, le suffixe (env)  n’apparaîtra plus.
                                            vous pouvez en réalité désactiver votre environnement 
                                            virtuel depuis n'importe quel répertoire."""

Supprimer venv = ex : rm -r env                                             

requirements.txt = """ Pour garantir que tous les développeurs travaillant sur un projet utilisent le même environnement virtuel, 
                       nous utilisons un fichier requirements.txt  . Il s'agit de la liste des paquets Python dont l'installation 
                       est requise dans un environnement virtuel pour que l'application s'exécute correctement.""" 
                       ex : 
                            ni requirements.txt
                            env) PS C:\OpenClassrooms\demo--ap-2> pip freeze > .\requirements.txt "#faire dans l'environnement important"
                            (env) PS C:\OpenClassrooms\demo--ap-2> cat .\requirements.txt
                            cycler==0.10.0
                            kiwisolver==1.3.1
                            etc...                                            

                   """ install requirements.txt """
                       ex : pip install -r requirements.txt





Terminal linux 

sudo su = " admin"

apt = "gestion des paquets éco ubuntu"

$ (uname -r) = " retour d'une imformation du kernel = coeur de ton linux toute la partie entre  sortie  périph reseau etc..."

ll = "linux ls -a"

halt = "eteindre la machine"

history = "historique des commande passer"

Ctrl+R =  " gar en mémoire les derniere commande"

Ctrl+U = "efface toute la ligne"

Ctrl+A = "renvoie au tout debut de la ligne"

Ctrl+E = " renvoie a la fin de la ligne"

Ctrl+W = "efface le dernier mot"

Ctrl+N,T =  """ crée nouvelle fenetre ou nouvelle onglet"""

realpath "donne le chemin exact d'un dossier"

ajouter un user dans un groupe ="""c'est important!! """
                                 ex : usermod -aG vboxsf dalton-x # vboxsf est le grtoupe dans le quel dalton rentre uniquement en root

exemple installer git  =    sudo apt install git


 curl  = "recup fichier sur le net"  
esc :wq! = """sortir et sauvegarder d'un vi !!!"""

nano  Ctrl+o ="""nano afficher et modifier un fichier dans la console, sauvegarder  avec nano peut etre avec autre chose"""

alias cat="batcat -p" = """ créé un alias pour ganger du temps, on vire le -p pour ameliorer la mise en page"""                            