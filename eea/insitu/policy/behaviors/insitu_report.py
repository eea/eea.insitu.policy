"""Behavior for insitu.report content type"""

from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider
from plone.namedfile.field import NamedBlobFile


@provider(IFormFieldProvider)
class IInsituReportBehavior(model.Schema):
    """InsituReport behavior"""

    file = NamedBlobFile(
        title="File",
        description="File containing the report, example: pdf",
        required=False,
    )

    report_category = schema.List(
        title="Report category",
        description="Select the category of report",
        required=True,
        value_type=schema.Choice(vocabulary="eea.insitu.policy.report_categories"),
    )
