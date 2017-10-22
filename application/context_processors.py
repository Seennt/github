# -*- coding: utf-8 -*-
""" Module: context_processors as part of: application

Created by: Reinier on 5-2-2017.Context processors makes project wide data availability.

Examples:
    Should be defined in a later state.

Attributes:
    All module attributes defined to understand there meaning.

TODO:
    - Add additional explanation.
    
"""
from application.packages import Labels, Sites


def labels_processor(request):
    """22-10-2017: The function: "labels_processor".

    Generate context data that holds labels for the navbar.

    Returns:
        dict: Labels.

    """
    #: labels(str): List of label objects.
    labels = Labels()

    return {
        'labels': labels.process(),
    }


def sites_processor(request):
    """22-10-2017: The function: "sites_processor".

    Generate context data that holds sites for the navbar.

    Returns:
        dict: Sites.

    """
    #: sites(str): List of site objects.
    sites = Sites()

    return {
        'sites': sites.process(),
    }
