"""Copernicus Components behavior"""

from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class ICopernicusComponents(model.Schema):
    """Copernicus Components behavior"""

    copernicus_components = schema.List(
        title="Copernicus Components",
        description="Select Copernicus Components",
        required=False,
        value_type=schema.Choice(vocabulary="eea.insitu.policy.copernicus_components"),
    )
    directives.write_permission(copernicus_components="cmf.ManagePortal")
