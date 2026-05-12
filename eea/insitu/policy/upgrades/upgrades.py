"""Upgrades"""

from collective.taxonomy import PATH_SEPARATOR
from collective.taxonomy.interfaces import ITaxonomy
from logging import getLogger
from zope.component import queryUtility


logger = getLogger(__name__)


def add_sentinel2_copernicus_component(context):
    """Add Sentinel-2 to the Copernicus Components taxonomy."""
    taxonomy = queryUtility(
        ITaxonomy, name="collective.taxonomy.copernicus_components"
    )

    if taxonomy is None:
        logger.warning("Copernicus Components taxonomy was not found.")
        return

    language = taxonomy.default_language or "en"
    if language not in taxonomy.data:
        language = "en"

    identifier = "Sentinel-2"
    path = PATH_SEPARATOR + "Sentinel-2"
    existing_identifiers = taxonomy.inverted_data.get(language, {})

    if identifier in existing_identifiers:
        logger.info("Sentinel-2 already exists in Copernicus Components taxonomy.")
        return

    taxonomy.update(language, [(path, identifier)], clear=False)
    logger.info("Added Sentinel-2 to Copernicus Components taxonomy.")
