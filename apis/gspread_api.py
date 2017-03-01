import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Driver(object):

    def __init__(self):

        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('apis/drive_secret.json', scope)
        self.client = gspread.authorize(credentials)

    def _get_content(self):
        sheet = self.client.open("direktbostader").sheet1
        return sheet.get_all_records()

    def get_emails(self):
        content = self._get_content()
        emails = [signup["Email-adress"] for signup in content if signup["Email-adress"]]
        return emails
