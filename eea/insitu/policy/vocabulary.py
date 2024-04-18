# -*- coding: utf-8 -*-
"""Vocabularies"""

from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.interface import alsoProvides


def generic_vocabulary(_terms, sort=True):
    """Returns a zope vocabulary from a dict or a list"""

    if _terms and isinstance(_terms, dict):
        _terms = _terms.items()
    elif _terms and isinstance(_terms[0], str):
        _terms = [(x, x) for x in _terms]

    if sort:
        _terms = sorted(_terms, key=lambda x: x[0])

    def factory(context):
        """Simple Vocabulary factory"""
        return SimpleVocabulary(
            [SimpleTerm(n, n.encode("utf-8"), term) for n, term in _terms]
        )

    return factory


_copernicus_services = (
    ("CAMS", "Copernicus Atmosphere Monitoring Service"),
    ("CEMS", "Copernicus Emergency Management Service"),
    ("CLMS", "Copernicus Land Monitoring Service"),
    ("CMEMS", "Copernicus Marine Service"),
    ("C3S", "Copernicus Climate Change Service"),
    ("CSS", "Copernicus Security Service"),
    ("CSC", "Copernicus Space Component"),
)
copernicus_services = generic_vocabulary(_copernicus_services)
alsoProvides(copernicus_services, IVocabularyFactory)

_copernicus_components = (
    ("TESTC1", "Test Copernicus Component 1"),
    ("TESTC2", "Test Copernicus Component 2"),
)

copernicus_components = generic_vocabulary(_copernicus_components)
alsoProvides(copernicus_components, IVocabularyFactory)


_copernicus_themes = (
    ("TESTT1", "Test Copernicus Theme 1"),
    ("TESTT2", "Test Copernicus Theme 2"),
)

copernicus_themes = generic_vocabulary(_copernicus_themes)
alsoProvides(copernicus_themes, IVocabularyFactory)

_report_categories = (
    ("GENERAL", "General Reports on In Situ Data"),
    ("NOV23", "Copernicus Working Group on Geospatial Data meeting " "(November 2023)"),
    (
        "OCT23",
        "Copernicus Working Group on In Situ Observations meeting " "(October 2023)",
    ),
    (
        "APR18",
        "Evolution of the Copernicus In Situ component workshop " "(25 April 2018)",
    ),
    ("WORKSHOPPRES", "Workshop Presentations"),
    ("STATEOFPLAY", "State of Play"),
    ("WORKSHOPREP", "Workshop Reports"),
    ("BACKGROUND", "Background"),
)
report_categories = generic_vocabulary(_report_categories)
alsoProvides(report_categories, IVocabularyFactory)
