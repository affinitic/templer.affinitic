# -*- coding: utf-8 -*-
"""
templer.affinitic

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from templer.core.base import BaseTemplate


class BasicBuildout(BaseTemplate):
    _template_dir = 'templates/basic_plone_buildout'
    summary = "A basic Plone buildout skeleton"
    help = "This creates a basic skeleton for a Plone buildout."
    category = "Buildout"
    required_templates = []
    default_required_structures = ['bootstrap', ]
    use_cheetah = True
