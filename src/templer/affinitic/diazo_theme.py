# -*- coding: utf-8 -*-
"""
templer.affinitic

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""

from templer.affinitic.base import AffiniticBaseBuildoutTemplate


class DiazoTheme(AffiniticBaseBuildoutTemplate):
    _template_dir = 'templates/diazo_theme'
    summary = "A basic Diazo theme package skeleton"
    help = "This creates a basic skeleton for a Plone Buildout Diazo theme."
