from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
cred = None
cred = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SAMPLE_SPREADSHEET_ID = '1sKpN9JY-t7EtuUmsoEg50O3Y256jRu6-KnmmqmtHz4Y'
service = build('sheets', 'v4', credentials=cred)
sheet = service.spreadsheets()
def indiegogo(list):
    value_range_body={
      "values": list
    }
    sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Indiegogo!A2:Z500", valueInputOption="USER_ENTERED", body=value_range_body).execute()
    # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Indiegogo").execute()
    # values = result.get('values', [])

def kickstarter(list):
    value_range_body={
      "values": list
    }
    sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Kickstarter!A2:Z500", valueInputOption="USER_ENTERED", body=value_range_body).execute()
    # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Indiegogo").execute()
    # values = result.get('values', [])

# clear_values_request_body ={}
# sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Indiegogo!A2:Z500", body=clear_values_request_body ).execute()

