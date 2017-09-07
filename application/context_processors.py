# -*- coding: utf-8 -*-
""" Module: context_processors as part of: applications

Created by: Reinier on 5-2-2017.Provide a module description here. A good explanation for a module provides
a higher readability and will improve implementation.

Examples:
    Should be defined in a later state.

Attributes:
    All module attributes defined to understand there meaning.

TODO:
    - Use TODO comments for code that is temporary, a short-term solution, or good-enough but not perfect.
    
"""
from applications.packages import Labels, Sites


def labels_processor(request):
    labels = Labels()

    return {
        'labels': labels.process(),
    }


def sites_processor(request):
    sites = Sites()

    return {
        'sites': sites.process(),
    }
