import os
import sys

import requests


def get_google_sheet(spreadsheet_id, out_dir, out_file):
    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv"
    response = requests.get(url)
    if response.status_code == 200:
        filepath = os.path.join(out_dir, out_file)
        with open(filepath, "wb") as f:
            f.write(response.content)
            print("CSV file saved to: {}".format(filepath))
    else:
        print(f"Error downloading Google Sheet: {response.status_code}")
        sys.exit(0)
