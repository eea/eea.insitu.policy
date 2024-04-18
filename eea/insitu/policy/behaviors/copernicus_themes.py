"""Copernicus Themes behavior"""

from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class ICopernicusThemes(model.Schema):
    """Copernicus Themes behavior"""

    copernicus_themes = schema.List(
        title="Copernicus Themes",
        description="Select Copernicus Themes",
        required=False,
        value_type=schema.Choice(vocabulary="eea.insitu.policy.copernicus_themes"),
    )
    directives.write_permission(copernicus_themes="cmf.ManagePortal")
