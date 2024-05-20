"""Prepare the data providers similar with eea.api.dataconnector method"""

from plone.restapi.interfaces import IExpandableElement
from plone.restapi.services import Service
from zope.component import adapter
from zope.component import getMultiAdapter
from zope.interface import Attribute
from zope.interface import Interface
from zope.interface import implementer
from zope.interface.interfaces import ComponentLookupError
from eea.insitu.policy.cis2.cis2_annot import get_annot


def data_providers_connector_data():
    """Prepare the data providers data in the expected format"""
    # example = {"col1": ["value1", "value2"], "col2": ["valueA", "valueB"]}
    data_providers = get_annot()
    cols = [
        # "id",
        # "acronym",
        "name",
        # "provider_type",
        "countries",
        "link",
        # "members",
        # "requirement_groups",
        # "is_network",
    ]

    results = {}
    for data_provider in data_providers:
        for col in cols:
            if col not in results.keys():
                results[col] = []
            results[col].append(str(data_provider.get(col, "---")))

    connector_data = {
        "@id": "some id",
        "data": {"metadata": {"readme": ""}, "results": results},
    }

    return connector_data


class IBasicDataProvider(Interface):
    """A data provider concept"""


class IDataProvider(IBasicDataProvider):
    """An export of data for remote purposes"""

    provided_data = Attribute("Data made available by this data provider")


@implementer(IExpandableElement)
@adapter(IBasicDataProvider, Interface)
class ConnectorData:
    """connector data"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, expand=False):
        return data_providers_connector_data()


class ConnectorDataGet(Service):
    """connector data - get"""

    def reply(self):
        return data_providers_connector_data()


class ConnectorDataPost(Service):
    """connector data - post"""

    def reply(self):
        return data_providers_connector_data()
