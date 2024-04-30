"""Admin views"""

from Products.Five.browser import BrowserView


class GoPDB(BrowserView):
    """Debug pdb"""

    def __call__(self):
        import pdb

        pdb.set_trace()
