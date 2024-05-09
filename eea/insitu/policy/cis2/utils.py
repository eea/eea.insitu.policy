"""CIS2 Utils"""

from eea.insitu.policy.config import (
    CIS2_IMPORT_TOKEN_ENV_VAR,
    CIS2_IMPORT_VIEW_TOKEN_ENV_VAR,
)
from eea.insitu.policy.browser.utils import get_env_var


def get_cis2_view_token():
    """The token that protects the view"""
    return get_env_var(CIS2_IMPORT_VIEW_TOKEN_ENV_VAR)


def get_cis2_token():
    """The token used to connect to CIS2"""
    return get_env_var(CIS2_IMPORT_TOKEN_ENV_VAR)
