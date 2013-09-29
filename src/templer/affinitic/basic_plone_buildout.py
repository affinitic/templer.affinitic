# -*- coding: utf-8 -*-
"""
templer.affinitic

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from templer.affinitic.base import AffiniticBaseTemplate
from templer.core.vars import StringVar


class BasicPloneBuildout(AffiniticBaseTemplate):
    _template_dir = 'templates/basic_plone_buildout'
    summary = "A basic Plone buildout skeleton"
    help = "This creates a basic skeleton for a Plone buildout."
    category = "Affinitic"
    required_templates = []
    default_required_structures = ['bootstrap', ]

    use_cheetah = True

    def __init__(self, *args, **kw):
        super(BasicPloneBuildout, self).__init__(*args, **kw)

        # Add new var
        self.vars.append(StringVar(
            'port',
            title='Zope port',
            description='Specify a port for your zope',
            default='8080',
        ))
