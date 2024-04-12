"""insitu.report content type"""

from plone.app.textfield import RichText
from plone.autoform.interfaces import IFormFieldProvider
from plone.restapi.behaviors import IBlocks
from plone.supermodel import model
from zope.interface import provider, implementer
from zope.schema import TextLine


@provider(IFormFieldProvider)
class IInsituReport(model.Schema, IBlocks):
    """InsituReport Interface"""

    testrichtext = RichText(
        title="Test richtext",
        required=False,
    )

    testtextline = TextLine(title="Test textline", required=False)
    testtextline2 = TextLine(title="Test textline2", required=False)


@implementer(IInsituReport)
class InsituReport(object):
    """insitu.report content type"""

    pass
