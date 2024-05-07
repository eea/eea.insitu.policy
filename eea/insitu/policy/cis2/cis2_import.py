"""CIS2 importer"""

import logging
import requests
from eea.insitu.policy.cis2.cis2_annot import save_annot

# from plone import api
from zope.component.hooks import setSite

logger = logging.getLogger("eea.insitu.policy")
TEST_URL = "https://raw.githubusercontent.com/GhitaB/sandbox/main/test2.json"


def download_json(url):
    """Download json file"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        return json_data
    except requests.exceptions.RequestException as e:
        logger.error("CIS2 import - error:")
        logger.error(e)
        return None


def main(app, *args):
    """Importer"""
    import pdb

    pdb.set_trace()
    setSite(app.Plone)
    json_data = download_json(TEST_URL)

    if json_data:
        save_annot(json_data)

        logger.info("CIS2 import - Success.")
    else:
        logger.error("CIS2 import - Fail.")
