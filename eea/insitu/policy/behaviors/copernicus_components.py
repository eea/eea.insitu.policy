"""Copernicus Components behavior"""

from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class ICopernicusComponents(model.Schema):
    """Copernicus Components behavior"""

    directives.widget(
        "copernicus_components", vocabulary="eea.insitu.policy.copernicus_components"
    )
    copernicus_components = schema.Tuple(
        title="Copernicus Components",
        value_type=schema.TextLine(
            title="Copernicus Component",
            required=False,
        ),
    )
