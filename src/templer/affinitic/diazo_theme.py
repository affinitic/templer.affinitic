# -*- coding: utf-8 -*-
"""
templer.affinitic

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from templer.affinitic.base import AffiniticBaseTemplate


class DiazoTheme(AffiniticBaseTemplate):
    _template_dir = 'templates/diazo_theme'
    summary = "A basic Diazo theme package skeleton"
    help = "This creates a basic skeleton for a Plone Diazo theme."
    category = "Affinitic"
    required_templates = []
    default_required_structures = ['bootstrap', ]
    use_cheetah = True
