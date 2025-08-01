import gspread
from oauth2client.service_account import ServiceAccountCredentials


def update_google_sheet(df, sheet_name, worksheet_name="Sheet1"):
    # Google Sheets API scope
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)

    # Open the sheet
    sheet = client.open(sheet_name)
    try:
        worksheet = sheet.worksheet(worksheet_name)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sheet.add_worksheet(title=worksheet_name, rows="100", cols="20")

    # Reset index and flatten column headers
    df = df.reset_index()

    # Convert datetime columns to string
    for col in df.columns:
        if df[col].dtype == 'datetime64[ns]' or str(df[col].dtype).startswith("datetime") or str(type(df[col].iloc[0])) == "<class 'pandas._libs.tslibs.timestamps.Timestamp'>":
            df[col] = df[col].astype(str)

    # Flatten multi-level columns (if any)
    df.columns = [' '.join(col).strip() if isinstance(col, tuple) else col for col in df.columns]

    # Convert to list of lists
    data = [df.columns.tolist()] + df.values.tolist()

    # Clear old data and upload
    worksheet.clear()
    worksheet.update("A1", data)

    print("✅ Google Sheet updated successfully!")


def update_backtest_summary(sheet_name, summary_data):
    # Setup credentials
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)

    # Sheet and worksheet
    sheet = client.open(sheet_name)
    try:
        worksheet = sheet.worksheet("Summary")
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sheet.add_worksheet(title="Summary", rows="100", cols="10")

    # Clear old data
    worksheet.clear()

    # Add headers
    headers = ["Ticker", "Total Days", "Buy Signals", "Buy Signal %", "ML Accuracy"]
    worksheet.update("A1", [headers] + summary_data)

    print("✅ Summary worksheet updated successfully!")
