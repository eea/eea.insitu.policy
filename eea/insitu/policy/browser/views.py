from Products.Five import BrowserView
from eea.insitu.policy.migration.insitu_reports import INSITU_REPORTS_CSV
from plone import api
import csv
import logging

logger = logging.getLogger("eea.insitu.policy")


class ImportInsituReports(BrowserView):
    """Import insitu reports from csv file"""

    def __call__(self):
        # columns = [
        #     "REPORT Title",
        #     "URL",
        #     "Description",
        #     "Publishing date",
        #     "EEA Topics",
        #     "Country/Countries",
        #     "Region ",
        #     "Publisher",
        #     "Data provenance",
        #     "Other organisations involved",
        #     "Rights",
        #     "CATEG1",
        #     "CATEG2/Copernicus_service",
        #     "Copernicus Themes",
        # ]
        for csv_line in INSITU_REPORTS_CSV.splitlines():
            if len(csv_line) > 2:
                csv_list = csv.reader([csv_line])
                data_row = next(csv_list)
                api.content.create(
                    type="insitu.report", title=data_row[0], container=self.context
                )
                # import pdb
                #
                # pdb.set_trace()
