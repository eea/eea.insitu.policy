"""insitu.report content type - TODO delete - we keep it to prevent error"""

from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import provider, implementer


@provider(IFormFieldProvider)
class IInsituReport(model.Schema):
    """TODO Delete this"""


@implementer(IInsituReport)
class InsituReport(Container):
    """insitu.report content type"""

    pass
