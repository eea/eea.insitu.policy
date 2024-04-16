# -*- coding: utf-8 -*-
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
