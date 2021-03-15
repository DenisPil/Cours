                              GitHub





Information sur la page :

 Pull requests = """ permet de réaliser des demandes de pull. Les demandes de pull (extractions) vous permettent d'informer 
                     les autres sur les modifications que vous avez appliquées à une branche d'un référentiel sur GitHub. 
                     Une fois qu'une demande d'extraction est ouverte, vous pouvez discuter et examiner les modifications 
                     éventuelles avec les collaborateurs, et ajouter des validations de suivi avant que vos modifications 
                     ne soient fusionnées dans la branche de base."""

Issue =          """  la section "Activité récente" de votre fil d’actualité, vous pouvez rapidement rechercher et suivre les problèmes 
                        récemment mis à jour, et extraire les demandes sur lesquelles vous travaillez. Sous "Activité récente", 
                        vous pouvez prévisualiser jusqu'à 12 mises à jour récentes effectuées au cours des deux dernières semaines.
                        Une activité est récente lorsque :
                        - vous avez ouvert un problème ou une demande d'extraction ;
                        - quelqu'un a commenté un problème ou tiré une demande que vous avez ouverte ;
                        - votre problème ou demande d'extraction a été rouvert ;
                        - votre avis a été demandé sur une demande de tirage ;
                        - vous avez été affecté à un problème ou à une demande d'extraction ;
                        - vous avez référencé un problème ou une requête d'extraction via un commit ;
                        - vous avez commenté un problème ou une demande d'extraction. """                     

Explore  =     """ Via Explore, vous pourrez trouver de nouveaux projets open source intéressants sur lesquels travailler, 
                   en parcourant les projets recommandés, en vous connectant à la communauté GitHub et en recherchant des référentiels 
                   par sujet ou par libellé."""
















                                        Git (bach)
                                """ Git gère les versions de vos travaux locaux à travers 3 zones locales majeures :
                                    le répertoire de travail (working directory/WD) ;
                                    l’index, ou stage (nous préférerons le second terme) ;
                                    le dépôt local (Git directory/repository).
                                    L'index, ou stage, désigne tous les fichiers modifiés que vous souhaitez voir apparaître dans votre 
                                    prochain commit. C'est avec la fonction  git add  que l'on ajoute un fichier au stage. 
                                    Le dépôt local est l'historique de l'ensemble de vos actions (commits, configurations...). 
                                    L'archivage se fait principalement avec la commande  git commit.  Il est possible d'accéder à 
                                    cet historique en faisant un  git reflog  qui affichera toutes vos actions et leurs SHA. Le SHA, 
                                    c'est ce grand code qui vous permettra de revenir à un commit exact. C'est l’identifiant de votre action"""         

 Git et sa structure = """ Les trois principaux types d'objets sont :
                           - le "tree" ou l'arbre Git qui est une forme de répertoire. 
                           Il va référencer une liste de trees et de blobs (sous-répertoires et fichiers) ;
                           - le "commit" qui va pointer vers un arbre spécifique et le marquer, 
                           afin de représenter son état à un instant donné.
                           - Le "blob" qui représente en général un fichier (Binary Large Object).
                           * le "tag" Le tag va représenter un commit d'une version spécifique.""" 
                           
hash SHA-1 = """ Toutes les informations nécessaires pour décrire l’historique d’un projet sont stockées dans des fichiers 
                 référencés par un identifiant de 40 caractères. Pour chacun des objets dans Git, vous trouverez cette 
                 chaîne de 40 caractères que nous appelons le hash SHA-1. Celui-ci représente le contenu de l'objet.
                 Git peut tout de suite reconnaître deux objets identiques (pas le meme sha). 
                 Le commit étant un objet, lui aussi a son empreinte SHA-1. Il est donc tout à fait possible d'appeler 
                 n'importe quel commit à n'importe quel moment grâce à cet identifiant unique."""

user.name = """ ton nom d'utilisateur. Si vous souhaitez par contre, pour un projet spécifique, changer votre nom d’utilisateur, 
                vous devrez repasser cette ligne mais sans le --global. """
                ex : git config --global user.name "Denis Pil"

user.email = """ ton email """
                 ex : git config --global user.email "denis.pilongery@gmail.com"

--global = """ Grâce à l’option --global, vous n’aurez besoin de le faire qu'une fois."""

git config --list = """ info sur la configuration de Git"""

activer les couleurs = """ Il est recommandé d’activer les couleurs afin d’améliorer la lisibilité des différentes branches.
                           Pour cela, passez ces trois lignes dans Git Bash """
                           ex : git config --global color.diff auto
                                git config --global color.status auto
                                git config --global color.branch auto

modifier éditeur = """ Par défaut, Git utilisera Vim comme éditeur et Vimdiff comme outil de merge. Vous pouvez les modifier en utilisant.
                       J'ai config de base VSC"""
                       ex : git config --global core.editor notepad++
                            git config --global merge.tool vimdiff

git init = """ créer un dépôt vide. On va créer, dans un premier temps, un dossier sur notre disque.
               Permet d'initialiser son projet dans Git Bash"""
               ex : DaltonX@DX-PC MINGW64 /c/OpenClassrooms/Git/PremierProject
                    $ git init
                    Initialized empty Git repository in C:/OpenClassrooms/Git/PremierProject/.git/
            """ solution plus complete création projet sur git ensuite"""
                …or create a new repository on the command line
                echo "# test" >> README.md
                git init
                git add README.md
                git commit -m "first commit"
                git branch -M main
                git remote add origin https://github.com/DenisPil/test.git "test.git le nom du repertoire il va donc changer"
                git push -u origin main   "ou" git push --set-upstream origin main
                
                …or push an existing repository from the command line
                git remote add origin https://github.com/DenisPil/test.git
                git branch -M main
                git push -u origin main



git remote add 'name' = """ comment accéder à un dépôt distant et le cloner en local. Il va falloir tout d’abord 
                            récupérer l’URL du dépôt distant, et là cela se passe sur GitHub !
                            "name" représente le nom court que vous utiliserez ensuite pour appeler votre dépôt. 
                            Appelez-le comme bon vous semble, mais un nom court et simple est toujours plus facile.
                            Cette ligne ne permet pas de cloner le dépôt, mais permet de dire au dépôt que l’on pointe vers le dépôt distant."""
                            ex : DaltonX@DX-PC MINGW64 /c/OpenClassrooms/Git/PremierProject (master)
                                 $ git remote add OC https://github.com/OpenClassrooms-Student-Center/projetOpenSource.git

git clone = """ notre dépôt local pointe sur le dépôt distant, nous allons cloner son contenu et le dupliquer en local. 
                Afin de réaliser le clonage, nous allons utiliser la commande."""
                ex : DaltonX@DX-PC MINGW64 /c/OpenClassrooms/Git/PremierProject (master)
                     $ git clone https://github.com/OpenClassrooms-Student-Center/ProjetOpenSource.git
                     Cloning into 'ProjetOpenSource'...
                     remote: Enumerating objects: 7, done.
                     remote: Total 7 (delta 0), reused 0 (delta 0), pack-reused 7
                     Receiving objects: 100% (7/7), done.

système de branches = """ C’est sur ces branches que repose toute la magie de GIT ! Les différentes branches correspondent à 
                          des copies de votre code principal à un instant T, où vous pourrez tester toutes vos idées 
                          sans que cela impacte votre code principal."""         

git branch = """ Connaître les branches présentes dans notre projet.  L’étoile signifie que c’est la branche 
                 sur laquelle vous vous situez et que c’est sur celle-ci qu'actuellement vous réalisez vos modifications."""
                 ex : $ git branch
                      * master
             """ Cette commande va créer la branche Cagnotte en local (elle ne va pas être dupliquée sur le dépôt distant). """
                 ex : $ git branch cagnotte
             """ ajouter une branch local sur github"""
                 ex : $ git push test test1 #test1 le nom de la branch a envoyer
                 #(correspond a OC dans un exemple au dessus la j'ai mi test mais je crois que la convension est "origin")    
 
git branch -d = """ supprime une branche """
                    ex : git branch -d nomBrachASupprimer


git checkout = """  Pour basculer d'une branche a une autres La branche va fonctionner comme un dossier virtuel. Avec Git checkout, 
                    on va être téléporté dans le dossier virtuel Cagnotte. On reste dans le dossier OC physiquement. 
                    Vous pouvez désormais réaliser votre évolution sans toucher à la branche master qui abrite votre code principal 
                    qui fonctionne. Vous pouvez rebasculer si besoin à tout moment sur la branche master, sans impacter 
                    les modifications de la branche Cagnotte."""
                    ex : DaltonX@DX-PC MINGW64 /c/OpenClassrooms/Git/PremierProject/ProjetOpenSource (master)
                         $ git checkout cagnotte
                         Switched to branch 'cagnotte'
                         DaltonX@DX-PC MINGW64 /c/OpenClassrooms/Git/PremierProject/ProjetOpenSource (cagnotte)
                         $ git branch
                         * cagnotte
                           master

git add = """ La commande git-add indexe les modifications qui ont été faites dans les fichiers du répertoire de 
              travail et prépare ainsi le prochain commit."""
              ex : "crée un fichier ou en avoir un sous le coude"
                   git add fichierExemple 

git commit = """ Un commit est tout simplement un enregistrement de votre travail à un instant T sur la branche courante où vous êtes.
                 La description est très importante pour retrouver le fil de vos commits, et revenir sur un commit en particulier."""
                 ex : $ git commit -m “Réalisation de la partie cagnotte côté front end”    

git stash = """ La remise va permettre de mettre vos modifications de côté, le temps de créer votre nouvelle branche et ensuite appliquer 
                cette remise sur la nouvelle branche. """ # exemple dans "Modifier branche master par erreur SANS commit" 

git stash list = """ La liste des stash en attente """ # exemple dans "Modifier branche master par erreur SANS commit" 

git status = """ Permet de voir vos fichiers qui ont été modifiés mais qui n'ont pas encore été commités. """
                 # exemple dans "Modifier branche master par erreur SANS commit"    

git log = """ analyser vos derniers commits avec la fonction  git log, afin de pouvoir récupérer l'identifiant du commit que 
              l'on appelle couramment le hash. Par défaut, git log  va vous lister par ordre chronologique 
              inversé tous vos commits réalisés. Cette commande affiche chaque commit avec son identifiant SHA, 
              l'auteur du commit, la date et le message du commit. """
              # exemple dans "Modifier branche master par erreur AVEC commit"

git reflog = """ git reflog  va loguer les commits, mais aussi toutes les autres actions que vous avez pu faire en local. 
                 Git reflog va enregistrer vos commits, vos modifications de messages, vos merges, vos resets etc... 
                 Git reflog va afficher un identifiant SHA-1 pour chaque action. Il est donc très facile de revenir à 
                 une action donnée grâce au SHA (8 premiers caracteres)."""
                 ex : DaltonX@DX-PC MINGW64 /c/OpenClassrooms/git/Test (master)
                      $ git reflog
                      949b8c4 (HEAD -> master) HEAD@{0}: revert: Revert "ceci est un commit pour test revert"
                      320e67b HEAD@{1}: commit: ceci est un commit pour test revert
                      b66eaf9 HEAD@{2}: commit (amend): nouveau commit
                      7814b11 HEAD@{3}: commit (amend): nouveau commit
                      e5ae6c2 HEAD@{4}: commit: test
            """ Pour revenir à une action donnée, on prend les 8 premiers caractères de son SHA et on fait."""
                ex : $ git checkout b66eaf9
                     Note: switching to 'b66eaf9'.
                     texte.....blabla                

git blame = """ La commande  git blame  permet d’examiner le contenu d’un fichier ligne par ligne et de déterminer la date à 
                laquelle chaque ligne a été modifiée, et le nom de l’auteur des modifications. """
                ex : $ git blame test3.txt
                     DaltonX@DX-PC MINGW64 /c/OpenClassrooms/git/Test ((b8d9c03...))
                     $ git blame test3.txt
                     b8d9c032 (DenisPil 2021-03-13 10:40:38 +0100 1) test321654321654

git cherry-pick = """ Git cherry-pick n'est pas très apprécié dans la communauté des développeurs ! En effet, cette commande 
                      va dupliquer des commits existants. Il sera préférable, si possible, de réaliser un merge. 
                      Cette commande va permettre de sélectionner un ou plusieurs commits grâce à leurs SHA 
                      et de les migrer sur la branche master, sans pour autant fusionner toute la branche "Mes évolutions"."""
                      ex : faire un git log ou autre pour avoir le SHA du commit voulu.
                           DaltonX@DX-PC MINGW64 /c/OpenClassrooms/git/Test ((b8d9c03...))
                           $ git checkout master # revenir sur la branche master
                           DaltonX@DX-PC MINGW64 /c/OpenClassrooms/git/Test (master)
                           $ git cherry-pick b8d9c03
                           [master 9c808aa] commit test de  git blame
                           Date: Sat Mar 13 10:40:38 2021 +0100
                           1 file changed, 1 insertion(+)

git merge = """ Un  git merge  ne devrait être utilisé que pour la récupération fonctionnelle, intégrale et finale d’une
                branche dans une autre, afin de préserver un graphe d’historique sémantiquement cohérent et utile, 
                lequel représente une véritable valeur ajoutée. Comme son nom l’indique,  merge  réalise une fusion.  
                git merge  va combiner plusieurs séquences de commits en un historique unifié. Le plus souvent,   
                git merge  est utilisé pour combiner deux branches.  git merge  va créer un nouveau commit de merge."""
                
            """ Il faut toujours préparer le terrain avant de réaliser un merge ! Vous devez toujours vous assurer 
                d'être sur la bonne branche. Pour cela, vous pouvez réaliser un  git status. 
                Si vous n'êtes pas sur la bonne, réalisez un  git checkout, pour changer de branche."""
                ex : DaltonX@DX-PC MINGW64 /c/OpenClassrooms/git/Test (master)
                $ git merge brancheCommit2
                CONFLICT (add/add): Merge conflict in test2.txt
                Auto-merging test2.txt
                hint: Waiting for your editor to close the file...
                Merge made by the 'recursive' strategy.
                test2.txt | 5 +++++
                1 file changed, 5 insertions(+)
            """ Si les deux branches que vous essayez de fusionner modifient toutes les deux la même partie du même fichier, 
            Git ne peut pas déterminer la version à utiliser. Lorsqu'une telle situation se produit, 
            Git s'arrête avant le commit de merge, afin que vous puissiez résoudre manuellement les conflits."""
                            
git pull = """ La commande Git pull permet de télécharger les modifications qui ont eu lieu sur le dépôt distant, dans 
               le but de les rapatrier sur le dépôt local. Git pull est en réalité la fusion de deux commandes Git :  
               git merge  que nous venons de voir et  git fetch  que nous verrons juste après.  
               git pull va créer un nouveau commit de fusion comme le fait  git merge. La commande  git pull  exécute d'abord  
               git fetch  qui télécharge le contenu du référentiel distant spécifié. Ensuite, un git merge  
               est exécuté pour fusionner les modifications du dépôt distant et créer un nouveau commit de merge en local."""
               ex : $ git pull
                    remote: Enumerating objects: 4, done.
                    remote: Counting objects: 100% (4/4), done.
                    remote: Compressing objects: 100% (2/2), done.
                    remote: Total 2 (delta 1), reused 0 (delta 0), pack-reused 0
                    Unpacking objects: 100% (2/2), 707 bytes | 70.00 KiB/s, done.
                    From https://github.com/DenisPil/OpenclassrommProject
                    a7edcf9..d2fd0f6  main       -> origin/main
                    Updating a7edcf9..d2fd0f6
                    Fast-forward
                    testpulll        | 1 +
                    testpullllllllae | 1 +
                    2 files changed, 2 insertions(+)
                    create mode 100644 testpulll
 
git push = """ la commande Git push permet d'envoyer des modifications que l'on a réalisées en local sur le dépôt à distance.""" 
               ex : $ git push
                    Enumerating objects: 3, done.
                    Counting objects: 100% (3/3), done.
                    Delta compression using up to 8 threads
                    Compressing objects: 100% (2/2), done.
                    Writing objects: 100% (2/2), 246 bytes | 246.00 KiB/s, done.
                    Total 2 (delta 1), reused 0 (delta 0), pack-reused 0
                    remote: Resolving deltas: 100% (1/1), completed with 1 local object.
                    To https://github.com/DenisPil/OpenclassrommProject.git
                    d2fd0f6..03ae523  main -> main

git fetch = """ Git fetch, contrairement à Git pull, va aller chercher les modifications sur le dépôt distant mais ne va 
                pas les fusionner avec nos modifications locales. Git isole le contenu récupéré en tant que contenu local 
                existant, cela n'a absolument aucun effet sur votre travail de développement local. 
                La commande Git fetch va récupérer toutes les données des commits effectués sur la branche courante 
                qui n'existent pas encore dans votre version en local. Ces données seront stockées dans 
                le répertoire de travail local, mais ne seront pas fusionnées avec votre branche locale. 
                Si vous souhaitez fusionner ces données pour que votre branche soit à jour, 
                vous devez utiliser ensuite la commande Git merge. La commande Git pull automatise la mise à jour des données, 
                mais peut entraîner de nombreux conflits si vous avez modifié beaucoup de fichiers. 
                Utiliser la commande Git fetch permet de garder son répertoire de travail à jour et de contrôler 
                le moment où l'on souhaite fusionner les données.""" 

git rebase = """ Git rebase a le même objectif que Git merge. Ces deux commandes permettent de transférer les changements 
                 d'une branche à une autre. Le rebase dispose de puissantes fonctionnalités de réécriture de l'historique. 
                 Il existe deux types de rebase : le rebase manuel et le rebase interactif. Au niveau du contenu, 
                 le rebase consiste à changer la base de votre branche d'un commit vers un autre, donnant l'illusion 
                 que vous avez créé votre branche à partir d'un commit différent. 
                 Attention ! Vous ne devez jamais rebaser des commits pushés sur le dépôt public ! Cela remplacerait 
                 les anciens commits du dépôt public, et cela  serait comme si votre historique avait brusquement disparu !"""                  

git rebase -i = """ démarre une session de rebasage interactive. Cette fonctionnalité permet de déplacer les commits un à un 
                    en ayant la possibilité de les modifier. Vous avez donc la possibilité de supprimer certains commits
                    ou de les modifier. Cette action ouvre un éditeur dans lequel vous pouvez entrer des commandes  
                    pour chaque commit à rebaser.
                    les commdes possibles :
                    # p, pick = utilisez le commit
                    # # r, reword = utilisez le commit, mais éditez le message de commit
                    # # e, edit = utilisez le commit, mais arrêtez-vous pour apporter des changements
                    # # s, squash = utilisez le commit, mais intégrez-le au commit précédent
                    # # f, fixup = commande similaire à "squash", mais qui permet d'annuler le message de log de ce commit
                    # # x, exec = exécutez la commande (le reste de la ligne) à l'aide de Shell 
                    # # d, drop = supprimez le commit """
                    ex : commence par un git log pour avoir la liste des commit et leur SHA
                         DaltonX@DX-PC MINGW64 /c/OpenClassrooms/git/testPullPush/OpenclassrommProject (main)
                         $ git rebase -i ba12eb7 # ba12eb7 corespond au 5eme commit de mon git log je vais donc modifier 
                         # tous les commit depuis celui la donc 4
                         hint: Waiting for your editor to close the file...
                         Successfully rebased and updated refs/heads/main.
               """ autre solution """
                   ex : $ git rebase -i HEAD~3  # le 3 dit que l'on veut rebase les 3 derniers commit    

git rebase -i HEAD^ = """ La commande Git rebase interactif permet aussi de modifier les messages de commit. """
                          ex : git rebase -i HEAD^
                      """ fenetre s'ouvre change le premier mot "pick" part "edit" save et ferme"""
                          $ git rebase -i HEAD^
                          hint: Waiting for your editor to close the file...
                          Stopped at 67615da...  encore un changement
                          You can amend the commit now, with
                          git commit --amend
                          Once you are satisfied with your changes, run
                          git rebase --continue
                      """ faire un git commit --amend modifier le msg save et fermer"""
                          $ git commit --amend
                          hint: Waiting for your editor to close the file...
                          [detached HEAD 0483e72] changement msg encore
                          Date: Sat Mar 13 12:09:38 2021 +0100
                          1 file changed, 0 insertions(+), 0 deletions(-)
                          create mode 100644 testpush.txt
                      """ puis validé avec la commande"""
                          $ git rebase --continue   # tu peux controler avec un git log
                          Successfully rebased and updated refs/heads/main.

Squash = """  Un squash est un regroupement de plusieurs commits. Le but est de les fusionner en un seul pour avoir 
              un historique Git plus propre. Il est notamment conseillé de le faire dans le cadre des envois sur le dépôt 
              à distance, pour simplifier la relecture des modifications effectuées. Non seulement Squash va fusionner 
              vos modifications, mais il va aussi fusionner vos messages de commit !"""
              ex : $ git rebase -i HEAD~2
                   # quand la fenetre s'ouvre changer pick par squash sur le ou les commit a fusionner
                   # valide la fenetre de commit. tu peux check avec un git log 

git bisect = """ Trouvez l’origine d’un bug avec Git bisect. Vous indiquez à Git que vous cherchez un bug, il se déplace de 
                 commit en commit, vous testez la version et vous lui dites si le bug est présent dans le commit courant ou pas. 
                 Le but est de retrouver le premier commit où le bug est apparu. Grâce à cela, vous saurez que l'une 
                 des modifications faites dans ce commit a causé le bug. git bisect start [bad] [good]
                 Au lieu de bad, vous devrez mettre le hash d'un commit où le bug est présent. À la place de good, 
                 vous devrez mettre le hash d'un commit où le bug n'était pas présent !"""
                 ex : $ git bisect start 52711531 7d9a178a
                      52711531af14fd8e1fb1abd28640bc18df6ec884 is the first bad commit
                      commit 52711531af14fd8e1fb1abd28640bc18df6ec884
                      Author: DenisPil <80517781+DenisPil@users.noreply.github.com>
                      etc...
             """ Si le commit ne présente pas le bug """
                 $ git bisect good # a la chaine selon le nb de commit a verif
             """ Si le commit présente un bug"""
                 $ git bisect bad 
             """ Une fois chaque commit vérifié, Git va vous indiquer le commit qui a provoqué le bug. Il va l'indiquer """
                 fvsd54g5s5d4g5f34g5dfg47df578q9qdff6 is first bad commit
                 commit fvsd54g5s5d4g5f34g5dfg47df578q9qdff6
                 Author: Moi <Moi@example.com>
                 Date: Tue mar 27 16:28:38 2019 -0800
                 Add fonctionnality AB                   


HEAD = """ Le HEAD, si vous n'êtes pas sûr d'avoir bien compris , est un pointeur, une référence sur notre position actuelle 
           dans notre répertoire de travail Git. le HEAD représente le dernier commit.
           Par défaut, HEAD pointe sur la branche courante, master, et peut être déplacé vers une autre branche ou un autre commit."""

git reset = """ La commande  git reset  est un outil complexe et polyvalent pour annuler les changements. Elle peut être appelée 
                de trois façons différentes qui correspondent aux arguments de ligne de commande --soft, --mixed et --hard. """
                --hard = """ Cette commande va permettre de revenir à n'importe quel commit mais en oubliant absolument 
                              tout ce qu'il s'est passé après ! Que vous ayez fait des modifications après ou d'autres commits, 
                              tout sera effacé ! C'est pourquoi il est extrêmement important de revérifier 
                              plusieurs fois avant de la lancer Cette utilisation de  git reset  constitue une manière 
                              simple d'annuler des changements qui n'ont pas encore été partagés."""
                              ex : $ git reset notreCommitCible  --hard  
                --mixed =""" Le  git reset --mixed  va permettre de revenir juste après votre dernier commit ou le commit spécifié, 
                             sans supprimer vos modifications en cours. Il va par contre créer un HEAD détaché. Il permet aussi, 
                             dans le cas de fichiers indexés mais pas encore commités, de désindexer les fichiers."""
                             ex : $ git reset --mixed
                             ex2: $ git reset HEAD~ # Si rien n'est spécifié après  git reset, par défaut il exécutera un  
                                                    # git reset --mixed HEAD~.     
                --soft = """ Le git reset --Soft permet juste de se placer sur un commit spécifique afin de voir le code à 
                             un instant donné ou créer une branche partant d'un ancien commit. Il ne supprime aucun fichier, 
                             aucun commit, et ne crée pas de HEAD détaché."""


git reset --hard HEAD^ = """ Cette ligne de commande va permettre de supprimer de la branche master votre dernier commit.  
                             Le Head^ indique que c'est bien le dernier commit que nous voulons supprimer."""
                             # exemple dans "Modifier branche master par erreur AVEC commit"

git  commit --amend = """ Pour résumer, git commit --amend vous permet de sélectionner le dernier commit afin d'y ajouter 
                          de nouveaux changements en attente. Vous pouvez ajouter ou supprimer des changements  
                          afin de les appliquer avec  commit --amend. Votre fichier a été ajouté à votre commit et
                          grâce à la commande --no-edit que nous avons ajoutée, nous n'avons pas modifié le message du commit. """
                          ex : "avoir une modif a faire sur le commit exemple ajouter un fichier"                               
                               $ git add test3.txt # l'ajout du fichier
                               DaltonX@DX-PC MINGW64 /c/OpenClassrooms/git/Test (master)
                               $ git commit --amend --no-edit # modifie le dernier commit (ajoute le fichier test3.txt) 
                               [master b66eaf9] nouveau commit
                               Date: Fri Mar 12 18:18:23 2021 +0100
                               2 files changed, 0 insertions(+), 0 deletions(-)
                               create mode 100644 test2.txt
                               create mode 100644 test3.txt
 
git revert = """ Au lieu de supprimer le commit de l'historique du projet, elle détermine comment annuler les changements introduits 
                 par le commit et ajoute un nouveau commit avec le contenu ainsi obtenu. Vous allez donc revenir à l'état précédent 
                 mais avec un nouveau commit. Ainsi, Git ne perd pas l'historique, lequel est important pour l'intégrité de votre 
                 historique de révision et pour une collaboration fiable.
                 La différence entre Revert et Reset est que Reset va revenir à l'état précédent sans créer un nouveau commit, 
                 alors que Revert va créer un nouveau commit.  """
                 ex : DaltonX@DX-PC MINGW64 /c/OpenClassrooms/git/Test (master)
                      $ git add test3.txt # j'ajoute un fichier

                      DaltonX@DX-PC MINGW64 /c/OpenClassrooms/git/Test (master)
                      $ git commit # je fais le commit du fichier ajouter
                      hint: Waiting for your editor to close the file...
                      [master 320e67b] ceci est un commit pour test revert
                      1 file changed, 1 insertion(+)

                      DaltonX@DX-PC MINGW64 /c/OpenClassrooms/git/Test (master)
                      $ git revert HEAD # vire le fichier ajouter et crée un nouveau commit. vérifie avec git log
                      hint: Waiting for your editor to close the file...
                      [master 949b8c4] Revert "ceci est un commit pour test revert" virer le fichier text3.txt This reverts 
                      commit 320e67bc9603b0bbeeb6a27dfa9e2951a90b8ca2.
                      1 file changed, 1 deletion(-)


                                 

git commit --amend -m  = """ L'exécution de cette commande, lorsqu'aucun élément n'est encore modifié, vous permet de modifier 
                             le message du commit précédent sans modifier son instantané. L'option -m 
                             permet de transmettre le nouveau message."""
                             ex : $ git log  # juste un git log pour voir le msg de mon commit
                                 commit e5ae6c29ebc069c19adaa7a51b0c7821aaa536cf (HEAD -> master)
                                 Author: DenisPil <denis.pilongery@gmail.com>
                                 Date:   Fri Mar 12 18:18:23 2021 +0100
                                 test # le msg de mon commit
                         """ la modif"""
                             ex : $ git commit --amend -m "nouveau commit"
                                  [master 7814b11] nouveau commit
                                  Date: Fri Mar 12 18:18:23 2021 +0100
                                  1 file changed, 0 insertions(+), 0 deletions(-)
                                  create mode 100644 test2.txt
                                  nouveau commit  # la modif du commit
                         """ Si besoin tu controle avec un git log"""
 


Création dépôt Git = """ Créé un dossier """
                         ex : mkdir Test
                     """ Initialiser le dépôt dans le dossier créé"""
                         ex : cd Test
                              git init
                     """ création branche principale (master), il faut crée un fichier et le commit"""
                         ex : touch PremierFichier.txt  # utilise touch et pas ni 
                              git add PremierFichier.txt
                              git commit
                     """ une fenetre va s'ouvrir (pour moi uine fenetre VSC) taper le msg du commit save et fermer.
                         ensuite possible de crée d'autre branche"""
                         ex : git branch brancheTest         

Supprimer une branche = """ exemple nous voulions ajouter nos fichiers avant de la créer et nous sommes maintenant bloqués 
                            avec cette branche. Notre branche est supprimée et nous pouvons ajouter dans 
                            un premier temps nos fichiers avant de créer la branche."""
                            ex : git branch -d brancheTest
                        """ Attention, si toutefois vous avez déjà fait des modifications dans la branche que vous souhaitez supprimer, 
                            il faudra soit faire un commit de vos modifications, soit mettre vos modifications de côté,
                            soit forcer la suppression en faisant """
                            ex : git branch -D brancheTest   

Modifier branche master par erreur SANS commit !!
     1 =  """ le cas où vous avez modifié votre branche master mais que vous n'avez pas encore fait le commit.
              Nous allons faire ce qu'on appelle une remise. La remise va permettre de mettre vos modifications de côté, 
              le temps de créer votre nouvelle branche et ensuite appliquer cette remise sur la nouvelle branche. """
              ex : $ git checkout master #important etre dans la branche master
                   $ git status   #controler le statut des fichier (commit unstage....)
                   On branch master
                   Changes to be committed:
                   (use "git restore --staged <file>..." to unstage)
                   new file:   test2.txt
                   Changes not staged for commit:
                   (use "git add <file>..." to update what will be committed)
                   (use "git restore <file>..." to discard changes in working directory)
                   modified:   test2.txt
          """ Créé la remise """
              ex : $ git stash
                   Saved working directory and index state WIP on master: eded1f3 commit test je pige rien pour l'instant
          """ Possibiliter de controler le statut des fichier voir sur le stash est good"""
              ex : $ git status
                   On branch master
                   nothing to commit, working tree clean.
          """ Si pas deja fait création d'une branche et on bascule sur la branche"""
          """ Et finalement, nous allons pouvoir appliquer la remise, afin de récupérer nos modifications sur notre nouvelle branche."""
              ex : $ git stash apply  
                   On branch brancheCommit
                   Changes to be committed:
                   (use "git restore --staged <file>..." to unstage)
                   new file:   test2.txt

          """ Si pour une raison ou une autre, vous avez créé plusieurs remises, et que la dernière n'est pas celle que vous souhaitiez
              appliquer, pas de panique, il est possible d'appliquer une autre remise. Nous allons d'abord regarder la liste de nos remises."""      
              ex : $ git stash list
                   stash@{0}: WIP on master: eded1f3 commit test je pige rien pour l'instant
                   stash@{1}: WIP on master: eded1f3 commit test je pige rien pour l'instant
          """ Il suffira alors d'appeler la commande git stash  en indiquant l'identifiant."""
              ex : $ git stash apply stash@{0} 
                   Changes to be committed:
                   (use "git restore --staged <file>..." to unstage)
                   new file:   test2.txt
        
Modifier branche master par erreur AVEC commit !! 
          """ Le cas est plus complexe, puisque vous avez enregistré vos modifications sur la branche master, alors que vous ne deviez pas."""
          """ Nous allons devoir aller analyser vos derniers commits avec la fonction  git log, afin de pouvoir récupérer 
              l'identifiant du commit que l'on appelle couramment le hash. Par défaut, git log  va vous lister par 
              ordre chronologique inversé tous vos commits réalisés."""
              ex : $ git log
                   commit 100d91a76c9c324cda0f15db6770cc544b5ea5fa (HEAD -> master)
                   Author: DenisPil <denis.pilongery@gmail.com>
                   Date:   Fri Mar 12 17:48:43 2021 +0100
                   ceci est un commit dangereux fdp
          """ Maintenant que vous disposez de votre identifiant, gardez-le bien de côté. 
              Vérifiez bien que vous êtes sur votre branche master et réalisez la commande 
              Cette ligne de commande va permettre de supprimer de la branche master votre dernier commit.  
              Le Head^ indique que c'est bien le dernier commit que nous voulons supprimer."""
              ex : $ git reset --hard HEAD^
                   HEAD is now at eded1f3 commit test je pige rien pour l'instant
          """ Création de la nouvelle branche ou bien et basculer sur la bonne branche"""
          """ Maintenant que nous sommes sur la bonne branche, nous allons de nouveau faire un  git reset, mais celui-ci 
              va permettre d'appliquer ce commit sur notre nouvelle branche ! Il n'est pas nécessaire d'écrire 
              l'identifiant en entier. Seuls les 8 premiers caractères sont nécessaires.""" 
              ex : $ git reset --hard 100d91a76
                   HEAD is now at 100d91a ceci est un commit dangereux fdp
  
git revert HEAD^ = """ Vous avez pushé des fichiers erronés (donc plus en local). Il est possible d'annuler son commit public avec 
                       la commande Git revert. L'opération Revert annule un commit en créant un nouveau commit. Cette commande 
                       n'a donc aucun impact sur l'historique ! Par conséquent, il vaut mieux utiliser  git revert  pour annuler 
                       des changements apportés à une branche publique, et git reset  pour faire de même, mais sur une branche privée.
                       attention, Git revert peut écraser vos fichiers dans votre répertoire de travail, il vous sera donc demandé de 
                       commiter vos modifications ou de les remiser."""   

clés SSH = """ Git base toute sa gestion d’authentification sur le mécanisme des clés SSH. Ce système est d’ailleurs immensément utile
               de façon générale sous Linux, Unix et OSX, dès qu’il s’agit de s’authentifier sur une machine tierce.
               Afin d’avoir un maximum de confort lorsqu’on accède à un dépôt nécessitant une identification 
               (lecture de dépôts privés ou écriture dans le cas général), il est donc important de bien maîtriser les clés SSH.""" 
               ex : $ ssh-keygen -t rsa -b 4096 -C "denis.pilongery@gmail.com"
           """ Vous pouvez soit appuyer sur Entrée, soit indiquer un nom de fichier. Un mot de passe vous est ensuite demandé.
               Vous avez obtenu votre clé SSH ! Pour la trouver, il suffit d'aller à l'adresse : C:\Users\VotreNomD'Utilisateur\, 
               et d'afficher les dossiers masqués. Dans ce dossier, vous avez donc deux fichiers, votre clé publique et votre clé privée.
               La clé id_rsa.txt est votre clé privée alors que la clé id_rsa.pub est votre clé publique.
               Premiere utilisation de la clé public dans github settings """                             

git submodule = """ Les sous-modules reposent sur l'imbrication de dépôts : vous avez des dépôts… dans des dépôts. 
                    vous développez deux projets totalement distincts, mais qui vont à un moment devoir se retrouver. 
                    C'est un cas typique d'utilisation des sous-modules Git, car ils vont vous permettre d'inclure 
                    un autre dépôt Git au sein de votre projet actuel. Il vous sera alors possible de gérer vos commits 
                    séparément pour chacun des dépôts. Cette commande va ajouter à notre dépôt courant le projet ProjetSubModule, 
                    comme sous-module dans le dossier Dossier/Destination. Vous noterez également qu'au travers de cette opération, 
                    Git a ajouté un nouveau fichier de configuration nommé .gitmodules contenant 
                    la description des sous-modules utilisés par le projet."""
                    ex : $ git submodule add https://github.com/etudiantOC/ProjetSubModule dossier/destination
 
git subtree = """ garder une fonctionnalité pour la réutiliser dans d'autres projets. Il pourrait être très facile de juste 
                  copier-coller les fichiers, et de les remettre plus tard dans les autres projets. Cependant, 
                  vous perdriez tout l'historique sur ces fonctionnalités. Heureusement, il existe les sous-arborescences Git ! 
                  Git subtree va vous permettre de créer un nouvel arbre de commits pour un sous-dossier de votre dépôt Git. 
                  Autrement dit, Git subtree régénère l’historique d’un dossier."""
                  ex : $ git subtree push -P monRépertoire git@mon-serveur-git:group/projet.git master
















                                WORKFLOW GIT :

                            """ Un workflow Git est une recommandation sur la façon d'utiliser Git pour effectuer un travail de 
                                manière cohérente et productive. Plusieurs workflows connus sont couramment utilisés par les développeurs 
                                pour des projets personnels, mais aussi par les entreprises. Pour que l'équipe soit sur la même page, 
                                un workflow Git convenu doit être développé ou sélectionné. Il existe plusieurs flux de travail 
                                Git connus qui conviendront peut-être à votre équipe """


workflow fork (duplication) = """ Au lieu d'utiliser un dépôt unique côté serveur pour agir en tant que base de code « centrale », 
                                  ce workflow fournit un dépôt côté serveur à chaque développeur. Par conséquent, chaque contributeur 
                                  dispose non pas d'un, mais de deux dépôts Git : un privé en local et un public côté serveur. """

workflow de fonctionnalités = """ Le principe de base du workflow de branche par fonctionnalité est que chaque fonctionnalité est 
                                  développée dans une branche prévue à cet effet plutôt que dans la branche master. 
                                  Grâce à cette encapsulation, plusieurs développeurs peuvent travailler aisément sur une même 
                                  fonctionnalité sans modifier la base de code principale. Il sera utilisé essentiellement 
                                  dans le cadre de l'intégration continue. """                                         

workflow GitFlow = """ GitFlow est une méthode, une architecture Git permettant de séparer au maximum le travail et de toucher 
                       le moins possible à la branche master. Cette méthode représente donc une architecture en branches. 
                       GitFlow est une des architectures les plus connues. GitFlow n'ajoute aucun concept ni aucune commande, 
                       il attribue plutôt des rôles très spécifiques aux différentes branches et définit comment et quand elles doivent 
                       interagir.  GitFlow, il va falloir dans un premier temps l'installer.
                       
                       Fonctionnement : GitFlow va définir dans un premier temps deux branches distinctes dans lesquelles les développeurs 
                       n'auront aucunement le droit de développer. La branche master est la branche qui va correspondre 
                       à notre environnement de production. Il est donc logique que l'on ne puisse y pousser nos modifications directement. 
                       La branche Develop centralise toutes les nouvelles fonctionnalités qui seront livrées dans la prochaine version. 
                       Ici, il va falloir se forcer à ne pas y faire de modifications directement. Dans le cadre d'un gros projet, 
                       la branche Develop correspond en général à notre environnement de recette. 
                       L'environnement de recette est une copie du projet qui est censée partir en production et où 
                       les testeurs vont réaliser une batterie de tests afin d'être sûrs de ne pas envoyer de bugs en production. 
                       La branche master stocke l'historique officiel des versions, et la branche Develop sert de branche d'intégration 
                       pour les fonctionnalités.
                       GitFlow ne se contente bien sûr pas uniquement de deux branches. À ces deux branches vont venir s'ajouter 
                       trois autres types de branches : 
                       - Les branches Feature permettent de commencer à travailler sur une nouvelle fonctionnalité. 
                         La branche Feature est créée à partir de la branche Develop. Vous devrez créer pour chaque nouvelle 
                         fonctionnalité une branche Feature ! Lorsque nous avons fini de développer notre nouvelle fonctionnalité, 
                         il faudra alors la commiter puis la fusionner sur la branche Develop.
                       - La branche Hotfix, quant à elle, va permettre de corriger un bug en production. 
                         En ce sens, elle sera créée à partir de la branche master, car c'est la branche master qui correspond 
                         à l'environnement de production. Une fois la branche Hotfix terminée, elle est mergée dans la 
                         branche Develop et dans la branche master.
                       - La branche Release est créée à partir de la branche Develop en cas de livraison en production imminente. 
                         En effet, dans le cadre d'un projet un peu plus conséquent, il y a souvent plusieurs versions. 
                         Une fois que toutes les fonctionnalités d'une version ont été créées, c'est à ce moment que nous devons 
                         créer une branche Release. Elle va permettre de réaliser nos tests alors que d'autres développeurs 
                         pourront commencer à travailler sur la version suivante. Lorsque la branche Release est terminée, 
                         nous devons la merger dans la branche Develop et dans la branche master.
                         Il faut installer git flow avec la commande "$ sudo apt-get install git-flow"""  
                       ex : "création repertoire du flow et ce placer a l'interieur" 
                            $ mkdir gitflow  
                            $ git flow init
                            Dépôt Git vide initialisé dans /home/dalton-x/VirtualPartage/gitflow/.git/
                            No branches exist yet. Base branches must be created now.
                            Branch name for production releases: [master] main
                            Branch name for "next release" development: [develop] devlop
                   """ Créer une feature. Étant au tout début du projet, notre feature va correspondre à la base notre projet. 
                       Elle s’appellera donc main."""
                       ex : $ git flow feature start main
                   """ Avec l'exécution de cette commande, Git créera la branche Feature main et nous basculera dessus."""     
                               
     









                                marketplace de GitHub : 



WhiteSource Bolt = """ une application gratuite, qui analyse en permanence tous vos dépôts, détecte les vulnérabilités des 
                       composants open source et apporte des correctifs. Il prend en charge les référentiels privés et publics !"""

ZenHub = """ ZenHub est le seul outil de gestion de projet qui s'intègre de manière native dans l'interface utilisateur de GitHub. 
             ZenHub est un outil de gestion de projet agile fonctionnant par sprint et générant des rapports assez poussé """

Travis Ci = """ Dans le domaine de l'intégration continue, Travis CI permet à votre équipe de tester et déployer vos applications 
                en toute confiance. Très polyvalent, il s'adapte aux petits comme aux grands projets. """                                   

WinMerge et Meld = """Les deux ont exactement le même but, comparer simplement deux fichiers en indiquant les zones où votre code 
                      est différent ! En plus de vous indiquer les différences entre vos deux fichiers, vous allez pouvoir les 
                      fusionner de façon intelligente. Pour chaque ligne différente, l'outil de comparaison vous demandera 
                      quelle version vous souhaitez conserver. Il est donc indispensable en cas de conflit dans Git.""" 












                                GitLab : 
                                # Pas installé ou vue encore pour plus d'info
#https://openclassrooms.com/fr/courses/5641721-utilisez-git-et-github-pour-vos-projets-de-developpement/6113136-utilisez-le-gitlab-integration-continue-ic

                            """ GitLab est une plateforme permettant d'héberger et gérer des projets web. 
                                GitLab est considérée comme la plateforme des développeurs modernes ! Comparé à GitHub, 
                                la palette fonctionnelle de GitLab se veut nettement plus large. Au-delà de la compilation 
                                et de la gestion de dépôts de code source sur lesquels se concentre le premier, 
                                GitLab s'étend au test logiciel, au packaging d'applications, à l'intégration et au déploiement 
                                continus, à la configuration, jusqu'au monitoring et à la sécurité applicative."""   

intégration continue (CI) = """ permet d'intégrer le code de votre équipe dans un référentiel partagé. Les développeurs partagent 
                                leur nouveau code dans une demande de fusion (extraction), ce qui déclenche la création, 
                                le test et la validation par un pipeline, avant la fusion des modifications dans votre référentiel. 
                                GitLab CI/CD va vous permettre d’automatiser les builds, les tests, les déploiements, etc.  
                                de vos applications. L’ensemble de vos tâches peut être divisé en étapes et l’ensemble 
                                de vos tâches et étapes constituent un pipeline. Les outils d'intégration continue - CI,
                                et de déploiement continu - CD, permettent d'automatiser beaucoup de processus 

















