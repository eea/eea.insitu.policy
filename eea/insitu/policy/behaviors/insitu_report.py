"""Behavior for insitu.report content type"""

from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IInsituReportBehavior(model.Schema):
    """InsituReport behavior"""

    file = NamedBlobFile(
        title="File",
        description="File containing the report, example: pdf",
        required=False,
    )
