"""A view to trigger CIS2 import. It uses a token saved as ENV VAR."""

import logging
import requests
from Products.Five import BrowserView
from eea.insitu.policy.cis2.cis2_annot import save_annot
from eea.insitu.policy.cis2.utils import get_cis2_token, get_cis2_view_token


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


class CIS2ImportData(BrowserView):
    """ "Import data from CIS2"""

    def __call__(self):
        cis2_view_token = get_cis2_view_token()
        cis2_token = get_cis2_token()

        if cis2_view_token is None:
            logger.info("CIS2 import - Canceled: missing view token ENV.")
            return "fail"

        if cis2_token is None:
            logger.info("CIS2 import - Canceled: missing CIS2 token ENV.")
            return "fail"

        view_token = self.request.form.get("token", None)
        if view_token is None:
            logger.info("CIS2 import - Canceled: missing view token.")
            return "missing view token"

        if view_token != cis2_view_token:
            logger.info("CIS2 import - Canceled: invalid view token.")
            return "invalid view token"

        json_data = download_json(TEST_URL)

        if json_data:
            save_annot(json_data)

            logger.info("CIS2 import - Success.")
        else:
            logger.error("CIS2 import - Fail.")

        return "ok"
