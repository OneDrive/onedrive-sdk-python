from ..http_provider import HttpProvider
from ..auth_provider import AuthProvider
from ..request.one_drive_client import OneDriveClient


def get_default_client(client_id, scopes):
    """Get a client using the default HttpProvider and
    AuthProvider classes

    Args:
        client_id (str): The client id for your application
        scopes (list of str): The scopes required for your
            application

    Returns:
        :class:`OneDriveClient<onedrivesdk.requests.one_drive_client.OneDriveClient>`:
            A OneDriveClient for making OneDrive requests.
    """
    http_provider = HttpProvider()
    auth_provider = AuthProvider(http_provider=http_provider,
                                 client_id=client_id,
                                 scopes=scopes)
    return OneDriveClient("https://api.onedrive.com/v1.0/",
                          auth_provider,
                          http_provider)
