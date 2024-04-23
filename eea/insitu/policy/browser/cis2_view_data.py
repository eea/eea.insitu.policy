"""Easy way to check existing definitions saved in annotations related to CIS2"""

from Products.Five import BrowserView
from eea.insitu.policy.cis2.cis2_annot import get_annot


class CIS2ViewData(BrowserView):
    """For testing, use this view to verify the definitions from CIS2"""

    def __call__(self):
        return get_annot()
