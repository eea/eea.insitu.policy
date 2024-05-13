"""CIS2 Data Providers"""

from eea.insitu.policy.cis2.utils import data_providers_details
from plone.restapi.interfaces import IExpandableElement
from eea.insitu.policy.interfaces import IEeaInsituPolicyLayer
from eea.insitu.policy.behaviors.cis2_data_providers import ICIS2DataProvidersList
from zope.component import adapter
from zope.interface import implementer
from plone.restapi.services import Service
from zope.interface import Interface
from eea.insitu.policy.cis2.utils import data_providers_details


@implementer(IExpandableElement)
@adapter(ICIS2DataProvidersList, IEeaInsituPolicyLayer)
class DataProvidersDetails(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_data_providers(self):
        data_providers_ids = self.context.data_providers_list
        return data_providers_details(data_providers_ids)

    def __call__(self, expand=False):
        return {"data_providers_details": self.get_data_providers()}


class DataProvidersDetailsGet(Service):
    def reply(self):
        data_providers = DataProvidersDetails(self.context, self.request)
        return data_providers
