import requests

# Replace with your "Published to Web" CSV link
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS_66k9JHNj4a3At6WAhQ1tgiBtj4GoQdjmeqCL1nHty2aU2RRzviaN6O3_HJsQs2LkxMMiZBkYU86v/pub?output=csv"

def download_data():
    response = requests.get(SHEET_URL)
    if response.status_code == 200:
        with open("jentz_gig_dates_sheet_1.csv", "w") as f:
            f.write(response.text)
        print("Data updated successfully!")
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    download_data()