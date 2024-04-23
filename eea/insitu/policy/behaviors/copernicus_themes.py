"""Copernicus Themes behavior"""

from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class ICopernicusThemes(model.Schema):
    """Copernicus Themes behavior"""

    directives.widget(
        "copernicus_themes", vocabulary="eea.insitu.policy.copernicus_themes"
    )
    copernicus_themes = schema.Tuple(
        title="Copernicus Themes",
        value_type=schema.TextLine(
            title="Copernicus Theme",
            required=False,
        ),
    )
