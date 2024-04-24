"""CIS2 Data Providers List Behavior"""

from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider
from eea.insitu.policy.vocabulary import get_terms


@provider(IFormFieldProvider)
class ICIS2DataProvidersList(model.Schema):
    """CIS2 Data Providers List Behavior"""

    data_providers_list = schema.List(
        title="Data Providers",
        description="Select Data Providers",
        required=False,
        # value_type=schema.Choice(vocabulary="eea.insitu.policy.cis2_data_providers"),
        value_type=schema.Choice(source=get_terms),
    )
    directives.write_permission(data_providers_list="cmf.ManagePortal")
