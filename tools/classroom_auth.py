"""
Shared OAuth helper for the Classroom sync tools.

First run opens a browser for you to authorize your own personal Google
account. After that, a token is cached in token.json next to this file
so you are not re-prompted every run (Google may periodically expire it
while the OAuth consent screen is in "Testing" mode; just re-authorize
when that happens).

Requires credentials.json (the OAuth client you already created in
Cloud Console, type "Desktop app") to be present in the repo root, one
directory above this file, or set CLASSROOM_CREDENTIALS_PATH.
"""

import os
from pathlib import Path

from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/classroom.courses.readonly",
    "https://www.googleapis.com/auth/classroom.topics",
    "https://www.googleapis.com/auth/classroom.coursework.students",
    # Materials (the syllabus) are a separate resource from coursework and
    # need their own scope. Adding a scope invalidates any cached token,
    # so the next run re-opens the browser once.
    "https://www.googleapis.com/auth/classroom.courseworkmaterials",
    "https://www.googleapis.com/auth/drive.file",
]

TOOLS_DIR = Path(__file__).resolve().parent
DEFAULT_CREDENTIALS = TOOLS_DIR.parent / "credentials.json"
TOKEN_PATH = TOOLS_DIR / "token.json"


def get_credentials():
    creds_path = Path(os.environ.get("CLASSROOM_CREDENTIALS_PATH", DEFAULT_CREDENTIALS))
    creds = None

    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if not creds or not creds.valid:
        refreshed = False
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
                refreshed = True
            except RefreshError:
                # Expected roughly weekly: while the OAuth consent screen is
                # in "Testing" mode Google expires refresh tokens after seven
                # days. Falling through to a fresh browser flow is the whole
                # remedy, so it is not worth a traceback.
                print("Cached token has expired or been revoked. Re-authorizing.")
                TOKEN_PATH.unlink(missing_ok=True)
                creds = None

        if not refreshed:
            if not creds_path.exists():
                raise FileNotFoundError(
                    f"OAuth client file not found at {creds_path}. "
                    "Download it from Cloud Console (APIs & Services > Credentials) "
                    "and save it as credentials.json in the repo root, or set "
                    "CLASSROOM_CREDENTIALS_PATH."
                )
            flow = InstalledAppFlow.from_client_secrets_file(str(creds_path), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_PATH.write_text(creds.to_json())

    return creds


def get_services():
    creds = get_credentials()
    classroom = build("classroom", "v1", credentials=creds)
    drive = build("drive", "v3", credentials=creds)
    return classroom, drive


def get_docs_service():
    """
    Docs API client, used for the formatting that HTML import cannot
    express: real (clickable) checkbox list bullets and page margins.

    No extra OAuth scope is needed; drive.file already covers documents
    this tool created. The Docs API does have to be enabled once for the
    Cloud project, though, or every call returns 403 SERVICE_DISABLED.
    """
    return build("docs", "v1", credentials=get_credentials())
