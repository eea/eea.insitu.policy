"""insitu.report content type"""

from plone.autoform.interfaces import IFormFieldProvider
from plone.restapi.behaviors import IBlocks
from plone.supermodel import model
from zope.interface import provider, implementer
from plone.namedfile.field import NamedBlobFile


@provider(IFormFieldProvider)
class IInsituReport(model.Schema, IBlocks):
    """InsituReport Interface"""

    file = NamedBlobFile(
        title="File",
        description="File containing the report, example: pdf",
        required=False,
    )


@implementer(IInsituReport)
class InsituReport(object):
    """insitu.report content type"""

    pass
