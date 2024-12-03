"""Get JSON data from an uploaded file containing the CIS2 definitions"""

import json
from Products.Five import BrowserView
from eea.insitu.policy.cis2.cis2_annot import save_annot


class CIS2SaveJSON(BrowserView):
    """For testing, use this view to upload the new definitions from CIS2"""

    def _save_json_to_annot(self, json_data):
        """Save JSON data to annotations"""

    def __call__(self):
        """No validation, make sure you upload a good file."""
        if self.request.form:
            file_upload = self.request.form.get("fileToUpload", None)
            if file_upload is not None:
                json_file = file_upload.file
                json_file.seek(0)
                json_data = json.loads(json_file.read())

                save_annot(json_data, refresh_data_providers_cache=True)

                return "Saved."

            return "Upload a json file. Try: /cis2_upload_file"

        return "Missing file. Try: /cis2_upload_file"
