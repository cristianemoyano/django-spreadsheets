import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, os.getenv('TOKEN_FILE_NAME'))

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(filename, scope)


def get_work_sheets(wrk_sheets_name):
    gc = gspread.authorize(credentials)
    return gc.open(wrk_sheets_name).sheet1


def to_csv(filename, all_records):
    fieldnames = all_records[0].keys()
    with open(filename, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)
        for data in all_records:
            writer.writerow(data.values())
