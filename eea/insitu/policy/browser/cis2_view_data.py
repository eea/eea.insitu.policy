"""Easy way to check definitions saved in annotations related to CIS2"""

from Products.Five import BrowserView
from eea.insitu.policy.cis2.cis2_annot import get_annot
from eea.insitu.policy.cis2.utils import data_providers_table


class CIS2ViewData(BrowserView):
    """For testing, use this view to verify the definitions from CIS2"""

    def __call__(self):
        return get_annot()


class CIS2ViewTable(BrowserView):
    """For testing, use this view to verify the data providers table data"""

    def __call__(self):
        return data_providers_table()
