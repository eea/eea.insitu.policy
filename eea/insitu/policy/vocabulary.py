# -*- coding: utf-8 -*-
"""Vocabularies"""

from plone.app.vocabularies.catalog import KeywordsVocabulary as BKV
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.interface import alsoProvides
from zope.interface import implementer


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
    ("MWR", "Micro-Wave Radiometer"),
    ("SRAL", "Synthetic Aperture Radar Altimeter"),
    ("OLCI", "Ocean and Land Colour Instrument"),
    ("SLSTR", "Sea and Land Surface Temperature Radiometer"),
    (
        "SLSTROLCI",
        "Sea and Land Surface Temperature Radiometer/Ocean and Land "
        "Colour Instrument",
    ),
    ("TROPOMI", "TROPOspheric Monitoring Instrument"),
    ("SEN5", "Sentinel-5	Sentinel-5p"),
    ("SENOCEAN", "Se-3-Ocean	Sentinel-3-Ocean"),
    ("SENLAND", "Sen-3-Land	Sentinel-3-Land"),
    ("RM", "Rapid Mapping"),
    ("EWC", "Early Warning"),
    ("RR", "Risk and Recovery"),
    ("CCC", "Climate Change"),
    ("LLC", "Local Land"),
    ("PLC", "Pan-European Land"),
    ("GLC", "Global Land"),
    ("PRIOR", "Priority Area Monitoring"),
    ("LANDCOVER", "Land Cover and Land Use Mapping"),
    ("BIOGEO", "Bio-geophysical Parameters"),
    ("SATDATA", "Satellite Data"),
    ("REFVAL", "Reference and Validation Data"),
    ("GROUND", "Ground Motion Monitoring"),
    ("BSC", "Border Surveillance"),
    ("MSC", "Maritime Surveillance"),
    ("SESA", "Support to EU External and Security Actions"),
    ("AMC", "Atmosphere Monitoring"),
    ("MMC", "Marine Environment Monitoring"),
)

copernicus_components = generic_vocabulary(_copernicus_components)
alsoProvides(copernicus_components, IVocabularyFactory)


_copernicus_themes = (
    ("ADDRESSES", "Addresses"),
    ("ADMINISTRATIVEUNITS", "Administrative units"),
    ("CADASTRALPARCELS", "Cadastral parcels"),
    ("COORDINATEREFERENCE", "Coordinate reference systems"),
    ("GEOGRAPHICALGRID", "Geographical grid systems"),
    ("GEOGRAPHICALNAMES", "Geographical names"),
    ("HYDROGRAPHY", "Hydrography"),
    ("PROTECTEDSITES", "Protected sites"),
    ("TRANSPORTNETWORKS", "Transport networks"),
    ("ELEVATION", "Elevation"),
    ("GEOLOGY", "Geology"),
    ("LANDCOVER", "Land cover"),
    ("ORTHOIMAGERY", "Orthoimagery"),
    (
        "AGRICULTURALAQUACULTURE",
        "Agricultural and aquaculture facilities",
    ),
    (
        "AREAMANAGEMENT",
        "Area management/restriction/regulation zones & reporting units",
    ),
    ("ATMOSPHERICCONDITIONS", "Atmospheric conditions"),
    ("BIOGEOGRAPHICALREGIONS", "Bio-geographical regions"),
    ("BUILDINGS", "Buildings"),
    ("ENERGYRESOURCES", "Energy resources"),
    ("ENVIRONMENTALMONITORING", "Environmental monitoring facilities"),
    ("HABITATSANDBIOTOPES", "Habitats and biotopes"),
    ("HUMANHEALTHANDSAFETY", "Human health and safety"),
    ("LANDUSE", "Land use"),
    ("METEOROLOGICALGEOGRAPHICAL", "Meteorological geographical features"),
    ("MINERALRESOURCES", "Mineral resources"),
    ("NATURALRISK", "Natural risk zones"),
    ("OCEANOGRAPHICGEOGRAPHICAL", "Oceanographic geographical features"),
    (
        "POPULATIONDISTRIBUTION",
        "Population distribution and demography",
    ),
    ("PRODUCTIONINDUSTRIAL", "Production and industrial facilities"),
    ("SEAREGIONS", "Sea regions"),
    ("SOIL", "Soil"),
    ("SPECIESDISTRIBUTION", "Species distribution"),
    ("STATISTICALUNITS", "Statistical units"),
    ("UTILITYGOVERNMENTAL", "Utility and governmental services"),
    ("NA", "N/A"),
    ("TBD", "TBD"),
)

copernicus_themes = generic_vocabulary(_copernicus_themes)
alsoProvides(copernicus_themes, IVocabularyFactory)

_report_categories = (
    ("GENERAL", "General Reports on In Situ Data"),
    ("NOV23", "Copernicus Working Group on Geospatial Data meeting "
        "(November 2023)"),
    (
        "OCT23",
        "Copernicus Working Group on In Situ Observations meeting "
        "(October 2023)",
    ),
    (
        "APR18",
        "Evolution of the Copernicus In Situ component workshop "
        "(25 April 2018)",
    ),
    ("WORKSHOPPRES", "Workshop Presentations"),
    ("STATEOFPLAY", "State of Play"),
    ("WORKSHOPREP", "Workshop Reports"),
    ("BACKGROUND", "Background"),
)
report_categories = generic_vocabulary(_report_categories)
alsoProvides(report_categories, IVocabularyFactory)


@implementer(IVocabularyFactory)
class KeywordsVocabulary(BKV):
    """Keywords"""

    def __init__(self, index):
        """Kwywords"""
        self.keyword_index = index


CopernicusComponentsVocabularyFactory = KeywordsVocabulary(
    "copernicus_components")
CopernicusThemesVocabularyFactory = KeywordsVocabulary("copernicus_themes")
