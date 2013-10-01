templer.affinitic
=================

http://www.affinitic.be/
info@affinitic.be

Summary
-------

The package templer.affinitic allow to create new packages the simpliest possible and corresponding to Affinitic needs.


Available templates
-------------------

Affinitic templer templates :

* affinitic\_basic\_plone\_buildout : A basic Plone buildout skeleton
* affinitic\_diazo\_theme : A basic Diazo theme package skeleton (with buildout)


Installation
------------

To use this product, you need to clone and install his buildout:

        cd buildouts
        git clone git@github.com:affinitic/templer.affinitic.git
        cd templer.affinitic
        virtualenv -p python2.6 --no-site-packages .
        bin/python bootstrap.py
        bin/buildout

Now that the templer.affinitic tool is installed, the script allowing you to create new package is:

        bin/templer

Do not hesitate to make an alias of the script to use it easily use it anywhere on your computer.


Script usage
------------

The script needs a template as argument, the list of available templates is showed when launching the script without argument or with '--list'

        bin/templer
        bin/templer --list

This will show:

        Affinitic

        affinitic_basic_plone_buildout: A basic Plone buildout skeleton
        affinitic_diazo_theme:          A basic Diazo theme package skeleton

... and some other zope/plone templates. We are of course interested by the Affinitic's ones.

To finally create a new package, you first need to be in the folder where you want the package to be created:

        cd buildouts

And to execute the script with the desired template:

        ../templer.affinitic/bin/templer affinitic_diazo_theme

You can also pass the name of the project in the arguments:

        ../templer.affinitic/bin/templer affinitic_diazo_theme my.package

Next, just answer the questions. They are the most simplified with good default answers:

        Enter project name: my.package
        Namespace Package Name (Name of outer namespace package) ['my']:
        Package Name (Name of the inner namespace package) ['package']:
        Web hosting service (If public, choose github. If private, choose bitbucket (github/bitbucket)) ['github']:
        Description (One-line description of the project) ['']: Description de mon package
        Project URL (URL of the homepage for this project) ['https://github.com/affinitic/my.package']:
        Zope port (Specify a port for your zope) ['8080']:
        Creating directory ./my.package

For example, this template will create a plone with a diazo and it buildout.

There is still some issues, you can follow them in the github issues of the package.
