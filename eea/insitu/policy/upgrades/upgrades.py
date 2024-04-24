"""Upgrades"""

from plone import api
from zope.interface import noLongerProvides
import logging
from eea.insitu.policy.report import IInsituReport


logger = logging.getLogger("eea.insitu.policy")


def insitu_report_cleanup_interface(_):
    catalog = api.portal.get_tool(name="portal_catalog")
    reports = [b.getObject() for b in catalog(portal_type="insitu.report")]
    for report in reports:
        noLongerProvides(report, IInsituReport)
