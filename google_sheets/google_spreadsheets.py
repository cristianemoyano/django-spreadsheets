import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, os.getenv('TOKEN_FILE_NAME'))

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(filename, scope)

# work_sheets = gc.open('Test de Inteligencias Múltiples - Lic. Prof. Lucía Osorio (respuestas)').sheet1


def get_work_sheets(wrk_sheets_name):
    gc = gspread.authorize(credentials)
    # work_sheets.get_all_records()
    return gc.open(wrk_sheets_name).sheet1


def to_csv(filename, all_records):
    fieldnames = all_records[0].keys()
    with open(filename, 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(fieldnames)
        for data in all_records:
            writer.writerow(data.values())


# if __name__ == "__main__":
#     ws = get_work_sheets('Test de Inteligencias Múltiples - Lic. Prof. Lucía Osorio (respuestas)')
#     all_records = ws.get_all_records()
#     to_csv('records.csv', all_records)
