import os.path
from mcp.server.fastmcp import FastMCP
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

mcp = FastMCP("email_triage")

# Define necessary scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'

def get_gmail_service():
    """Authenticates and returns a service object for Gmail API."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If there are no valid credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            # This is key: It will open a browser window for authentication
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

        service = build('gmail', 'v1', credentials=creds)

        # --- INSPECTION POINT 1: Print the service object ---
        print("\n--- GMAIL SERVICE OBJECT TYPE ---")
        # print(type(service))
        print("\n--- GMAIL SERVICE OBJECT DIR (methods) ---")
        print(dir(service), flush=True) # Shows available methods/attributes

#     # Build the Gmail service object
    service = build('gmail', 'v1', credentials=creds)
    return service


@mcp.tool()
# def list_emails(max_results: int = 10) -> list[dict]:
    # """
    # Lists a specific number of recent emails in the user's inbox.

    # Args:
    #     max_results: The maximum number of emails to retrieve. Defaults to 10.

    # Returns:
    #     A list of dictionaries, each containing an email ID and a snippet of its content.
    # """
    # try:
    #     service = get_gmail_service()
    #     # Call the Gmail API to fetch messages
    #     results = service.users().messages().list(
    #         userId='me',
    #         labelIds=['INBOX'],
    #         maxResults=max_results
    #     ).execute()

    #     messages = results.get('messages', [])
    #     email_list = []

    #     if not messages:
    #         print("No messages found.")
    #         return []

    #     # Optionally, fetch details for each message (snippet)
    #     for message in messages:
    #         msg = service.users().messages().get(userId='me', id=message['id'], format='minimal').execute()
    #         email_list.append({
    #             'id': msg['id'],
    #             'threadId': msg['threadId'],
    #             'snippet': msg.get('snippet', 'No snippet available.')
    #         })

    #     return email_list

    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     # In a real server, you might want to return an error object
    #     return [{"error": str(e)}]

@mcp.tool()
def list_emails(max_results: int = 1) -> list[dict]: # Reduced default results for easier inspection
    # ... (try/except block setup) ...
    service = get_gmail_service()
    # print(service)

        # --- INSPECTION POINT 2: Print the result of the list call ---
        # list_results = service.users().messages().list(
        #     userId='me',
        #     labelIds=['INBOX'],
        #     maxResults=max_results
        # ).execute()
        # print("\n--- LIST API CALL RESULTS ---")
        # print(type(list_results))
        # print(list_results)

        # messages = list_results.get('messages', [])

        # if messages:
        #     # --- INSPECTION POINT 3: Print a single message 'get' result ---
        #     msg = service.users().messages().get(userId='me', id=messages[0]['id'], format='minimal').execute()
        #     print("\n--- SINGLE MESSAGE GET RESULTS (FORMAT='minimal') ---")
        #     print(type(msg))
        #     print(msg)
        #     print("\n------------------------------------------------\n")

# If you run this script directly, you typically start the FastMCP server
# if __name__ == "__main__":
#     mcp.run()

print("--- Running manual test of list_emails function ---")
# Call the function directly here
# test_emails = list_emails(max_results=2)
get_gmail_service()
# print("\n--- FINAL FORMATTED OUTPUT (Return Value) ---")
# print(test_emails)
