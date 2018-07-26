Initial config instructions

1. Went through installation documentation provided by google online
2. Installed on Windows 10
3. Installed GCP SDK using all the default settings. Required installation of Python 2 (needed for the SDK to run) but not Python 3 (already installed)
4. Activated needed APIs in my cloud (Translation, etc.)
5. Installed google-cloud-vision into python anaconda virtualenv
6. Via the cloud console created an account and gave it permissions
7. Created a JSON with the credentials, downloaded to local project folder
8. Set env var GOOGLE_APPLICATION_CREDENTIALS to point to the JSON with the creds


set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\dunca\Desktop\CanonGoogleVisionOCR_Test\creds.json