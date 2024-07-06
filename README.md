Ce script récupère la date de création des fichiers en .docx ou .odt contenus dans un dossier désigné par l'Utilisateur et ajoute cette date de création au titre de ces fichiers. Cette transformation se fait également dans les fichiers présents dans les sous-dossiers. 

Dans un dossier donné, un document intitulé texte.odt créé le 23 avril 2024 sera automatiquement renommé 20240423_texte.odt

Ce script a été créé avec l'aide du modèle de langage DeepSeek habergé par l'Université de Rennes le 3 juillet 2024

# comment faire fonctionner le script avec un ordinateur Windows

Python n'est pas installé par défaut sur le système d'exploitation de Windows. 

Télécharger au préalable la dernière version de Python sur votre ordinateur (ordinateurs de l'Université de Rennes : Python peut être téléchargé sans droits d'administrateur sur votre poste depuis le Centre Logiciel)

Télécharger, ou cloner avec Git, ce répertoire. 
Aller dans le répertoire. 
Ouvrir à cet endroit le terminal de Windows (maj+clic droit fait apparaître le menu dans lequel apparaît l'option "ouvrir la fenêtre powershell ici). Cliquer sur cette option.
Dans le terminal, entrer la commande suivante : 

```shell
python append_date_to_name.py 
```

Dans le terminal, on vous demande dans quel dossier opérer le changement. 
Choisir un nom de dossier, ou bien le chemin absolu vers le dossier dans lequel vous souhaitez procéder à ces changements. 
Par exemple, si c'est le dossier Unimarc dans le dossier catalogage sur votre disque S, entrer : 

S:/catalogage/Unimarc

Appuyer sur entrée. 

# Comment appliquer ce changement sur d'autres types de fichiers

Ouvrir le script dans un éditeur de texte (blocnote, VScode, notepad++)
Faire une recherche (Ctrl+F) sur ' dir, ext= ' dans la parenthèse qui suit, ajouter l'extension demandée. 


