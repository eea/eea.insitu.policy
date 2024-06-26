"""CIS2 Data Providers"""

from plone.restapi.interfaces import IExpandableElement
from plone.restapi.services import Service
from plone.memoize.view import memoize
from eea.insitu.policy.cis2.utils import data_providers_details
from eea.insitu.policy.cis2.utils import data_providers_table
from eea.insitu.policy.interfaces import IEeaInsituPolicyLayer
from eea.insitu.policy.behaviors.cis2_data_providers import (
    ICIS2DataProvidersList)
from eea.insitu.policy.interfaces import ICIS2DataProvidersTable
from zope.component import adapter
from zope.interface import implementer


@implementer(IExpandableElement)
@adapter(ICIS2DataProvidersList, IEeaInsituPolicyLayer)
class DataProvidersDetails(object):
    """Data providers details from CIS2 json file"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_data_providers(self):
        """Data providers details list"""
        data_providers_ids = self.context.data_providers_list
        return data_providers_details(data_providers_ids)

    def __call__(self, expand=False):
        return {"data_providers_details": self.get_data_providers()}


class DataProvidersDetailsGet(Service):
    """Data providers details"""

    def reply(self):
        """Data providers"""
        data_providers = DataProvidersDetails(self.context, self.request)
        return data_providers


@implementer(IExpandableElement)
@adapter(ICIS2DataProvidersTable, IEeaInsituPolicyLayer)
class DataProvidersTable(object):
    """Data providers table"""

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @memoize
    def data_providers_table(self):
        """cached table data"""
        return data_providers_table()

    def __call__(self, expand=False):
        return {"data_providers_table": self.data_providers_table()}


class DataProvidersTableGet(Service):
    """Data providers table"""

    def reply(self):
        """Data providers table"""
        return DataProvidersTable(self.context, self.request)
