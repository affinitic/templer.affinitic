templer.affinitic
=================

Summary
-------

Le produit templer.affinitic permet de crééer des nouveaux packages le plus simplement possible et qui correspondent directement aux besoins d'affinitic.


Templates disponibles
---------------------

Affinitic templer templates :

* affinitic\_basic\_plone\_buildout : A basic Plone buildout skeleton
* affinitic\_diazo\_theme : A basic Diazo theme package skeleton (with buildout)


Installation
------------

Pour utiliser ce produit, il faut tout d'abord récupérer et installer son buildout:

        cd buildouts
        git clone git@github.com:affinitic/templer.affinitic.git
        cd templer.affinitic
        virtualenv -p python2.6 --no-site-packages .
        bin/python bootstrap.py
        bin/buildout

Voilà l'outil templer.affinitic est installé. Le script permettant de créer des nouveau package est

        bin/templer

N'hésitez pas à faire un alias de ce script afin de pouvoir l'utiliser partout.


Utilisation du script
---------------------

Le script a besoin qu'on lui indique la template du package que l'on veut installer, la liste s'affiche si on lance le script sans argument ou en lui indiquant '--list'

        bin/templer
        bin/templer --list

Ceci affichera:

        Affinitic

        affinitic_basic_plone_buildout: A basic Plone buildout skeleton
        affinitic_diazo_theme:          A basic Diazo theme package skeleton

Ainsi que d'autre templates de zope/plone. Celles qui nous intéressent principalement sont bien entendu les templates affinitic qui pourront s'étoffer au fil de notre amélioration de templer.affinitic.

Pour enfin lancer la création d'un package, il vous suffit de vous trouver dans le dossier là où vous voulez créer ce package:

        cd buildouts

Et de lancer le script avec la template désirée:

        ../templer.affinitic/bin/templer affinitic_diazo_theme

Vous pouvez également directement mettre le nom du projet:

        ../templer.affinitic/bin/templer affinitic_diazo_theme mon.package

Ensuite une série de questions vous seront posées suivant la template choisie, avec un maximum de réponses par défaut pour faciliter la tâche:

        Enter project name: mon.package
        Namespace Package Name (Name of outer namespace package) ['mon']:
        Package Name (Name of the inner namespace package) ['package']:
        Web hosting service (If public, choose github. If private, choose bitbucket (github/bitbucket)) ['github']:
        Description (One-line description of the project) ['']: Description de mon package
        Project URL (URL of the homepage for this project) ['https://github.com/affinitic/mon.package']:
        Zope port (Specify a port for your zope) ['8080']:
        Creating directory ./mon.package

Ce thème, par exemple, créera un plone avec un diazo et son buildout clé sur porte.

Il reste des issues concernant ce package qui peuvent être suivies dans le ticket: http://trac.affinitic.be/trac/ticket/5396
