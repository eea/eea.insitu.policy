"""plone.restapi customizations"""

from eea.insitu.policy.behaviors.cis2_data_providers import ICIS2DataProvidersList
from eea.insitu.policy.interfaces import IEeaInsituPolicyLayer
from plone.restapi.interfaces import IFieldSerializer
from plone.restapi.serializer.converters import json_compatible
from plone.restapi.serializer.dxfields import DefaultFieldSerializer
from zope.component import adapter
from zope.interface import implementer
from zope.schema.interfaces import IList
from eea.insitu.policy.cis2.utils import data_providers_list


@adapter(IList, ICIS2DataProvidersList, IEeaInsituPolicyLayer)
@implementer(IFieldSerializer)
class DataProvidersListFieldSerializer(DefaultFieldSerializer):
    """Data Providers List serializer"""

    def get_value(self, default=None):
        """Get value"""
        value = getattr(
            self.field.interface(self.context), self.field.__name__, default
        )
        if self.field.__name__ == "data_providers_list":
            if (
                self.request.get("HTTP_REFERER", None)
                and "/edit" in self.request["HTTP_REFERER"]
            ):
                return value  # ['1', '2']

            # In view mode we convert to list of data providers objects
            data_providers_ids = value
            return data_providers_list(data_providers_ids)
        return value
