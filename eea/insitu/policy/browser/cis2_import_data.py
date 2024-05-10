"""A view to trigger CIS2 import. It uses a token saved as ENV VAR."""

import logging
from Products.Five import BrowserView
from eea.insitu.policy.cis2.utils import get_cis2_token, get_cis2_view_token
from eea.insitu.policy.cis2.cis2_import import cis2_importer

logger = logging.getLogger("eea.insitu.policy")


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

        # Trigger import
        cis2_importer()

        return "ok"
