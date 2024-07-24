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


def data_providers_details(data_providers_ids):
    """Input: list of data providers ids (ids must be string!)
    Output: list of data providers (including details from annotations)"""
    data_providers = get_annot()
    res = []
    if data_providers_ids is None:
        return res

    for data_provider in data_providers:
        if data_provider.get("id", None) is not None:
            if str(data_provider["id"]) in data_providers_ids:
                res.append(data_provider)
    return res


def simplified_data_providers_list(data_providers_ids):
    """Input: list of data providers ids
    Output: [{id, name, link} for each one]
    """
    providers_ids = [str(x) for x in data_providers_ids]
    members = data_providers_details(providers_ids)

    return [
        {"name": x["name"], "id": x["id"],
         "link": x["website"]} for x in members]


def data_providers_table():
    """Prepare data for data providers table"""
    data_providers = get_annot()
    simple_providers = []
    network_providers = []

    for provider in data_providers:
        if provider["is_network"]:
            network_providers.append(
                {
                    "id": provider["id"],
                    "acronym": provider["acronym"],
                    "name": {
                        "title": provider["name"], "link": provider["link"]},
                    "provider_type": provider["provider_type"],
                    "countries": [x["name"] for x in provider["countries"]],
                    "link": provider["website"],
                    "members": simplified_data_providers_list(
                        provider["members"]),
                    "requirement_groups": [
                        x["name"] for x in provider["requirement_groups"]
                    ],
                    "is_network": provider["is_network"],
                    "native_name": provider["native_name"],
                }
            )
        else:
            simple_providers.append(
                {
                    "id": provider["id"],
                    "acronym": provider["acronym"],
                    "name": {
                        "title": provider["name"],
                        "link": provider["link"]
                    },
                    "provider_type": provider["provider_type"],
                    "countries": [x["name"] for x in provider["countries"]],
                    "link": provider["website"],
                    "members": simplified_data_providers_list(
                        provider["members"]),
                    "requirement_groups": [
                        x["name"] for x in provider["requirement_groups"]
                    ],
                    "is_network": provider["is_network"],
                    "native_name": provider["native_name"],                    
                }
            )

    return {
        "simple": simple_providers,
        "network": network_providers,
    }
