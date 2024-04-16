"""Copernicus Services behavior"""

from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class ICopernicusServices(model.Schema):
    """Copernicus Services behavior"""

    copernicus_services = schema.List(
        title="Copernicus Services",
        description="Select Copernicus Services",
        required=False,
        value_type=schema.Choice(
            vocabulary="eea.insitu.policy.copernicus_services"),
    )
    directives.write_permission(copernicus_services="cmf.ManagePortal")
