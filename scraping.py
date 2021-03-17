Mot clé concept 

parser =  """parser se traduit en français par analyseur syntaxique. Il s'agit d'un concept beaucoup plus général que de l'appliquer 
             sur du XML ou du CSV. Puisque tu parles de "page", j'aurais tendance à croire que tu veux analyser une page HTML. 
             Mais effectivement, il s'agit bien de dégager une structure à partir de données brutes, presque toujours représentées 
             en texte brut (ASCII/ANSI/UTF8/etc. mais pas DOC par exemple). Cette structure peut être tabulaire comme avec le CSV, 
             mais est en général arborescente (en arbre) comme en XML ou HTML. Les techniques d'analyse de CSV sont très simples et
              peuvent être correctement mises en oeuvre sans connaissance théorique préalable. Pour des structures plus complexes 
              (mais plus puissantes) comme l'XML, l'HTML, ou même le langage Delphi, il faut recourir à des méthodes d'analyse 
              syntaxique éprouvées et performantes."""



Pour le scraping ( aller chercher des data sur un siteweb)
les modules de bases sont :
requests et bs4

"""premier test c'est de tester ton url avec requests.get(url)"""
ex: url = 'http://books.toscrape.com/'
    response = requests.get(url) #créa variable de requests.get()

    if response.ok:  #créé une condition répondre si cela fonctionne (le code est 200 si ok ) (facultatif je pense mais un +)
        print(response) ex2 print(reponse.text) = donne le code html de la page


"""possibiliter d'enregistrer ça dans un fichier et chercher des mots clés par itération mais pas pratique """           
    if response.ok:
        soup =  BeautifulSoup(response.text) #création objet soup pour utiliser une fonction
        print(soup)                          # cette objet sera le résultat du contenue de la réponse hmtl (response.txt)

    if response.ok:
        soup =  BeautifulSoup(response.text, 'html.parser' ) # on utilise un parser pour préciser le format évite les msg
        title = soup.find("title") # fonction .find permet de chercher des balises comme le titre ex <title>. 
            print (title.text) # le ".text" permet de virer les balise sur le titre


"""resultat sans le parser, et avec les balises sur le titre"""            
dalton-x@daltonx-VirtualBox:~$ /usr/bin/python3 /home/dalton-x/VirtualPartage/testScraping/testScraping.py
/home/dalton-x/VirtualPartage/testScraping/testScraping.py:9: GuessedAtParserWarning: No parser was explicitly specified, 
so I m using the best available HTML parser for this system ("html.parser"). This usually isn t a problem, but 
if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 9 of the file /home/dalton-x/VirtualPartage/testScraping/testScraping.py. 
To get rid of this warning, pass the additional argument 'features="html.parser"' to the BeautifulSoup constructor.

  soup =  BeautifulSoup(response.text)
<title>             #avec les balise  soup.find a bien trouver les balises avec title 
    All products | Books to Scrape - Sandbox
</title>    


"""résultat avec le parser et sans les balise sur le titre"""
dalton-x@daltonx-VirtualBox:~$ /usr/bin/python3 /home/dalton-x/VirtualPartage/testScraping/testScraping.py
                    # plus de balise perfect !  soup.find a bien trouver les balises avec title 
    All products | Books to Scrape - Sandbox


""" pour examiner une ligne image etc dans une page clic droit et inspecter (sur image, etc..). le code html s'ouvre et l'arborescence pointe
    vers l'objet pointé et le nom de la balise (ici des livres). Le test avec un print (len()"""
if response.ok:
    soup =  BeautifulSoup(response.text, 'html.parser' )
    article_class= soup.findAll("article") #soupfindAll = rechercher toute les itérations de la balise(le nombre de balise "article")    
    print (len(article_class))  # afficher le nombre de fois (len()) qu'il trouve la balise "article"


"""Si ton print(len()) affiche ce que tu veux ici 20 livres par pages on continue. Ensuite choper le nom de la balise
   a placer dans une boucle pour récup les url des livres"""
url = 'http://books.toscrape.com/'
response = requests.get(url)

if response.ok:
    links_books = [] # créa de la liste qui contient les urls (a href) des livres
    soup =  BeautifulSoup(response.text, 'html.parser' )
    article_class = soup.findAll("article")#findAll = rechercher toute les itérations d'article (donc chercher le nombre d'objet "article")
    for article in article_class: 
        a = article.find("a") #chercher les a avec .find (car une seul balise a part article(balise précedente. arborescence!!))
        link = a["href"] # dans la balise "a" on veut extraire l'attribue "href" on utilise des [important!] href = url d'un livre 
        links_books.append("http://books.toscrape.com/" + link)#ajoute les url avec la concanétation (http +) pour avoir l adresse compléte
    print(links_books)


""" Pour récup les urls de tous les livres du site on fait la meme chose (avec quelque modif ex déplacement de la liste, regarde bien !!) 
    mais on place ce code dans une boucle qui va itérer toutes les pages """
import requests 
from bs4 import BeautifulSoup

links_books = []# on déplace la liste avant la boucle important !!!
for i in range(51): #la boulce qui va itérer toute les pages le i représente les pages
    url = 'https://books.toscrape.com/catalogue/page-' + str(i) + '.html'#concaténation du i(num page)faut voir sur chaque site comt c'est foutu l'url
    response = requests.get(url)#on déplace request.get avant le if  
    if response.ok:
        soup =  BeautifulSoup(response.text, 'html.parser' )
        article_class = soup.findAll("article")
        for article in article_class:
            a = article.find("a")
            link = a["href"]
            links_books.append('https://books.toscrape.com/catalogue/' + link)
    print(links_books)    
    

"""Maintenant que nous avons récup toutes les urls (donc tout les livres) on va les copier dans un fichier"""
...   # je recopie pas tous le code !!
..
.
            links_books.append('https://books.toscrape.com/catalogue/' + link)
    print(links_books)
    with open ('urls.txt', 'w') as file: #ouverture fichier, avec fonc open  en parametre ('nom du fichier + w = écriture) sous le nom file
        for link in links_books: # petite séquence pour lui dire que tous les livres(link) dans la liste[links_books] doivent etre copier
            file.write(link + '\n')   # tu copie dans file(le fichier urls.txt) et tu va a la ligne (\n)

""" scraper les informations d'un livre le plus compliqué était "review_rating" car l'info etait dans le nom du code css a savoir le nombre 
    d'étoile. la solution ce trouve  "class_= 'star-rating')['class'][1]" je sais pas trop comment mais le fait de faire class_ ... me permet
    de prendre la donné que j'ai besoin. J'ai utiliser le meme procéder pour l'image """
url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser') #créa objet BeautifulSoup
    product_information = soup.find('table', {'class': 'table table-striped'}).findAll('td')#objet avec toutes les infos dans table-striped
    upc = product_information[0].text   
    book_name = soup.find('h1').text
    price_tax = product_information[3].text.replace('Â',"")
    price_no_tax = product_information[2].text.replace('Â',"")
    availability = product_information[5].text.replace('In stock', '')    
    product_description = soup.findAll('p')[3].text
    #category = soup.find()
    review_rating = soup.find('p', class_= 'star-rating')['class'][1]#le plus compliqué §§§ ce souvenir du mot_ underscore et pas de {}
    image_url = soup.find('img', src_= '')['src'][0:100]\
        .replace('../..','https://books.toscrape.com/')
    print(product_description,review_rating,image_url)
