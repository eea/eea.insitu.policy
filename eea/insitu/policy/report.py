"""insitu.report content type"""

from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobFile
from plone.restapi.behaviors import IBlocks
from plone.supermodel import model
from zope.interface import provider, implementer
from zope import schema


@provider(IFormFieldProvider)
class IInsituReport(model.Schema, IBlocks):
    """InsituReport Interface"""

    file = NamedBlobFile(
        title="File",
        description="File containing the report, example: pdf",
        required=False,
    )

    report_category = schema.List(
        title="Report category",
        description="Select the category of report",
        required=True,
        value_type=schema.Choice(
            vocabulary="eea.insitu.policy.report_categories"),
    )


@implementer(IInsituReport)
class InsituReport(Container):
    """insitu.report content type"""

    pass
