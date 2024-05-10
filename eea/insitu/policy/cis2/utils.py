"""CIS2 Utils"""

from eea.insitu.policy.config import (
    CIS2_IMPORT_TOKEN_ENV_VAR,
    CIS2_IMPORT_VIEW_TOKEN_ENV_VAR,
    CIS2_URL_ENV_VAR,
)
from eea.insitu.policy.browser.utils import get_env_var
from eea.insitu.policy.cis2.cis2_annot import get_annot


def get_cis2_view_token():
    """The token that protects the view"""
    return get_env_var(CIS2_IMPORT_VIEW_TOKEN_ENV_VAR)


def get_cis2_token():
    """The token used to connect to CIS2"""
    return get_env_var(CIS2_IMPORT_TOKEN_ENV_VAR)


def get_cis2_url():
    """The url used to connect to CIS2"""
    return get_env_var(CIS2_URL_ENV_VAR)


def data_providers_list(data_providers_ids):
    """Input: list of data providers ids
    Output: list of data providers (including details from annotations)"""
    data_providers = get_annot()
    res = []

    for data_provider in data_providers:
        if data_provider.get("id", None) is not None:
            if str(data_provider["id"]) in data_providers_ids:
                res.append(data_provider)
    return res
