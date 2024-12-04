"""Annotations for CIS2"""

import logging
from zope.annotation.interfaces import IAnnotations
from plone import api
from eea.insitu.policy.config import CIS2_ANNOT_KEY
from eea.insitu.policy.config import DATA_PROVIDERS_TABLE_ANNOT_KEY

logger = logging.getLogger("eea.insitu.policy")


def get_annot_container():
    """We use portal as annotations container"""
    return api.portal.get()


def create_annot(annot_container, annot_key):
    """Create annotations"""
    annot = IAnnotations(annot_container)
    annot[annot_key] = {}


def init_annot(annot_key):
    """Make sure annotations exists"""
    container = get_annot_container()
    annot = IAnnotations(container)
    if annot.get(annot_key, None) is None:
        create_annot(container, annot_key)


def save_annot(json_data, a_key=None, refresh_data_providers_cache=False):
    """Save json data into annotations"""

    logger.info("ANNOT: Saving...")
    # Config
    if a_key is not None:
        annot_key = a_key
    else:
        annot_key = CIS2_ANNOT_KEY
    container = get_annot_container()

    # Make sure annot exists
    init_annot(annot_key)

    # Save data
    annotations = IAnnotations(container)
    annotations[annot_key] = json_data
    logger.info("ANNOT: Saved")

    # Refresh cached data table
    if refresh_data_providers_cache is True:
        save_data_providers_table_annot()
        logger.info("ANNOT: TABLE CACHE REFRESH")


def get_annot(a_key=None):
    """Get json data from annotations"""

    # Config
    if a_key is not None:
        annot_key = a_key
    else:
        annot_key = CIS2_ANNOT_KEY
    container = get_annot_container()

    # Make sure annot exists
    init_annot(annot_key)

    # Get data
    annotations = IAnnotations(container)
    return annotations[annot_key]


def get_data_providers_table_annot():
    """Data providers table (as prepared for table listing) is saved into
    annotations in order to optimize the page load (prevent preparing the same
    table again and again with each page request)"""

    return get_annot(a_key=DATA_PROVIDERS_TABLE_ANNOT_KEY)


def save_data_providers_table_annot():
    """Save table as cache"""
    json_data = prepare_data_providers_table()
    save_annot(json_data, a_key=DATA_PROVIDERS_TABLE_ANNOT_KEY)


def extract_services_and_components(components):
    """Prepare services table column"""
    """
        Inoput:
        "components": [
          {
            "id": 2,
            "name": "Component 1",
            "service_id": 3,
            "service_name": "Service A"
          },
          {
            "id": 5,
            ...
          },
          ...
        ],

        Output:
        {
            'Service A': ['Component 1', 'Component 2'],
            'Service B': ['Component 4', 'Component 3'],
        }
    """
    services = {}
    for component in components:
        service = component["service_name"]
        if service not in services:
            services[service] = []
        services[service].append(component["name"])

    return services


def prepare_data_providers_table():
    """Prepare data for data providers table"""
    data_providers = get_annot()
    simple_providers = []
    network_providers = []

    for provider in data_providers:
        if provider["is_network"]:
            network_providers.append({
                "id":
                provider["id"],
                "acronym":
                provider["acronym"],
                "name": {
                    "title": provider["name"],
                    "link": provider["link"]
                },
                "provider_type":
                provider["provider_type"],
                "countries": [x["name"] for x in provider["countries"]],
                "link":
                provider["website"],
                "members":
                simplified_data_providers_list(provider["members"]),
                "services": extract_services_and_components(
                    provider["components"]),
                "is_network":
                provider["is_network"],
                "native_name":
                provider.get("native_name", ""),
            })
        else:
            simple_providers.append({
                "id":
                provider["id"],
                "acronym":
                provider["acronym"],
                "name": {
                    "title": provider["name"],
                    "link": provider["link"]
                },
                "provider_type":
                provider["provider_type"],
                "countries": [x["name"] for x in provider["countries"]],
                "link":
                provider["website"],
                "members":
                simplified_data_providers_list(provider["members"]),
                "services": extract_services_and_components(
                    provider["components"]),
                "is_network":
                provider["is_network"],
                "native_name":
                provider.get("native_name", ""),
            })

    return {
        "simple": simple_providers,
        "network": network_providers,
    }


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

    return [{
        "name": x["name"],
        "id": x["id"],
        "link": x["website"]
    } for x in members]
