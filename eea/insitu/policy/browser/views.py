"""Views"""

# import csv
import logging

import transaction
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

# from eea.insitu.policy.migration.insitu_reports import INSITU_REPORTS_CSV
from eea.insitu.policy.migration.insitu_reports_date import INSITU_REPORTS_DATE
from eea.insitu.policy.vocabulary import _report_categories
from eea.insitu.policy.browser.utils import normalized
from plone import api
from DateTime import DateTime

logger = logging.getLogger("eea.insitu.policy")


class ImportInsituReports(BrowserView):
    """Import insitu reports from csv file"""

    def get_report_category(self, text_categ):
        """Get category as vocabulary key"""
        categs = {}
        for categ in _report_categories:
            categs[categ[1]] = categ[0]

        res = categs.get(text_categ, text_categ)

        return [res]

    def get_copernicus_service(self, text):
        """Get copernicus service as vocabulary key"""
        services = {
            # OK
            "Atmosphere": ["CAMS"],
            "Land": ["CLSM"],
            "Marine": ["CMEMS"],
            "Space": ["CSC"],
            # Not OK, to be edited and clarified manually
            "Artic": ["CSC"],
            "Cross cutting": ["CSC"],
            "Water": ["CSC"],
        }
        return services.get(text, text)

    def __call__(self):
        # Already imported
        """
        report_index = 0
        for csv_line in INSITU_REPORTS_CSV.splitlines():
            if len(csv_line) > 2:
                csv_list = csv.reader([csv_line])
                data_row = next(csv_list)

                report_title = data_row[0]
                report_url = data_row[1]
                report_publisher = [data_row[7]]
                report_category = self.get_report_category(data_row[11])
                copernicus_services = self.get_copernicus_service(data_row[12])

                print("TITLE: ", report_title)
                print("URL: ", report_url)
                print("PUBLISHER: ", report_publisher)
                print("CATEG", report_category)
                print("SERVICE", copernicus_services)

                api.content.create(
                    type="insitu.report",
                    container=self.context,
                    title=report_title,
                    report_category=report_category,
                    copernicus_services=copernicus_services,
                    publisher=report_publisher,
                )
                report_index += 1
                if report_index % 10 == 0:
                    transaction.commit()
        """


class ImportInsituReportsDates(BrowserView):
    """We need the publishing date copied from the old website for each file"""

    def _fix_date_for_report(self, report):
        """Update publication date for report"""

        def updateEffective(obj, value):
            """Update publication date for obj"""
            obj.setEffectiveDate(value)
            obj.reindexObject()
            transaction.commit()

        if report.file is None:
            return

        lines = [x for x in INSITU_REPORTS_DATE.splitlines()]
        filename = report.file.filename
        found = [x for x in lines if normalized(filename) in normalized(x)]
        if found:
            report_data = found[0]
            date = report_data.split(",")[0]
            date_time = DateTime(date)
            updateEffective(report, date_time)
            logger.info("Updated: %s <-- %s", report.absolute_url(), date)
        else:
            logger.info("Not found: %s", report.absolute_url())

    def __call__(self):
        site = api.portal.get()
        catalog = getToolByName(site, "portal_catalog")
        brains = catalog.searchResults(portal_type="insitu.report")

        for brain in brains:
            report = brain.getObject()
            self._fix_date_for_report(report)
