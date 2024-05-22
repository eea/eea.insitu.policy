"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from zope.interface import Interface


class IEeaInsituPolicyLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICIS2DataProvidersTable(Interface):
    """Marker interface to be used in Data Providers context"""
