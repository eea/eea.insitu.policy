"""Annotations for CIS2"""

import logging
from plone import api
from zope.annotation.interfaces import IAnnotations

logger = logging.getLogger("eea.insitu.policy")

CIS2_ANNOT_KEY = "CIS2_data_providers"


def get_annot_container():
    """We use portal as annotations container"""
    logger.info("ANNOT: Get container")
    return api.portal.get()


def create_annot(annot_container, annot_key):
    """Create annotations"""
    logger.info("ANNOT: Create annot")
    annot = IAnnotations(annot_container)
    annot[annot_key] = {}


def init_annot(annot_key):
    """Make sure annotations exists"""
    logger.info("ANNOT: Init")
    container = get_annot_container()
    annot = IAnnotations(container)
    if annot.get(CIS2_ANNOT_KEY, None) is None:
        create_annot(container, CIS2_ANNOT_KEY)


def save_annot(json_data):
    """Save json data into annotations"""

    logger.info("ANNOT: Saving...")
    # Config
    annot_key = CIS2_ANNOT_KEY
    container = get_annot_container()

    # Make sure annot exists
    init_annot(annot_key)

    # Save data
    annotations = IAnnotations(container)
    annotations[annot_key] = json_data
    logger.info("ANNOT: Saved")


def get_annot():
    """Get json data from annotations"""

    # Config
    annot_key = CIS2_ANNOT_KEY
    container = get_annot_container()

    # Make sure annot exists
    init_annot(annot_key)

    # Get data
    annotations = IAnnotations(container)
    logger.info("ANNOT: Get")
    return annotations[annot_key]
