"""insitu.report content type"""

from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobFile
from plone.restapi.behaviors import BLOCKS_SCHEMA, LAYOUT_SCHEMA, IBlocks
from plone.supermodel import model
from plone.schema import JSONField
from zope.interface import provider, implementer
from zope import schema
from eea.insitu.policy.behaviors.volto_layout import (
    insitu_report_layout_items,
    insitu_report_layout_blocks,
)


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

    blocks = JSONField(
        title="Blocks",
        description="The JSON representation of the object blocks.",
        schema=BLOCKS_SCHEMA,
        default=insitu_report_layout_blocks,
        required=False,
    )

    blocks_layout = JSONField(
        title="Blocks Layout",
        description="The JSON representation of the object blocks layout.",
        schema=LAYOUT_SCHEMA,
        default={
            "items": insitu_report_layout_items,
        },
        required=False,
    )


@implementer(IInsituReport)
class InsituReport(Container):
    """insitu.report content type"""

    pass
