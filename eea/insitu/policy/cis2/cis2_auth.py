"""CIS2 auth"""

from eea.insitu.policy.cis2.utils import get_cis2_token, get_cis2_url


def cis2_auth():
    """return url and headers"""
    url = get_cis2_url()
    token = get_cis2_token()

    if token and url:
        auth = "Bearer " + token
        headers = {"Authorization": auth}
        return {"url": url, "headers": headers}

    return None
