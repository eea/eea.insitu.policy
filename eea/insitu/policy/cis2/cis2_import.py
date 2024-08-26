"""Import definitions from CIS2"""

import logging
import requests
from eea.insitu.policy.cis2.cis2_annot import save_annot
from eea.insitu.policy.cis2.cis2_auth import cis2_auth

logger = logging.getLogger("eea.insitu.policy")


def cis2_importer():
    """Import json from CIS2"""

    auth = cis2_auth()
    if auth:
        try:
            response = requests.get(auth["url"], headers=auth["headers"])
            response.raise_for_status()
            json_data = response.json()

            if json_data:
                save_annot(json_data, refresh_data_providers_cache=True)
                logger.info("CIS2 import - Success.")
            else:
                logger.error("CIS2 import - Fail.")

        except requests.exceptions.RequestException as e:
            logger.error("CIS2 import - error:")
            logger.error(e)
    else:
        logger.error("CIS2 import - missing auth")
