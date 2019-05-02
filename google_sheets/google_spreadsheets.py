from django.conf import settings
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import os
from autotest.models import DataFile

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, os.getenv('TOKEN_FILE_NAME'))

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


def get_service_account_credentials():
    token_file = DataFile.objects.get(key_file='token')
    token_file_path = os.path.join(settings.MEDIA_ROOT, token_file.data.name)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(token_file_path, scope)
    return credentials


def get_work_sheets(wrk_sheets_name):
    gc = gspread.authorize(get_service_account_credentials())
    return gc.open(wrk_sheets_name).sheet1


def to_csv(filename, all_records):
    fieldnames = all_records[0].keys()
    with open(filename, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)
        for data in all_records:
            writer.writerow(data.values())
