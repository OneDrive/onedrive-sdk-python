# Getting started with the OneDrive SDK for Python

------------------------------------------------------------------------
[![Build status](https://ci.appveyor.com/api/projects/status/x1cjahp817w6r455?svg=true)](https://ci.appveyor.com/project/OneDrive/vroom-client-python)

## Installation

Once you've downloaded the OneDrive SDK for Python, open a command prompt and type the following to install it:

<pre><code>pip install onedrivesdk</code></pre>

Next, include the SDK in your Python project by adding:

<pre><code>import onedrivesdk</code></pre>

## Authentication

### OneDrive

To interact with the OneDrive API, your app must authenticate. You can use the following code sample to do so.

```python
import onedrivesdk

redirect_uri = 'http://localhost:8080/'
client_secret = 'your_client_secret'
client_id='your_client_id'
api_base_url='https://api.onedrive.com/v1.0/'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

http_provider = onedrivesdk.HttpProvider()
auth_provider = onedrivesdk.AuthProvider(
    http_provider=http_provider,
    client_id=client_id,
    scopes=scopes)

client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)
auth_url = client.auth_provider.get_auth_url(redirect_uri)
# Ask for the code
print('Paste this URL into your browser, approve the app\'s access.')
print('Copy everything in the address bar after "code=", and paste it below.')
print(auth_url)
code = raw_input('Paste code here: ')

client.auth_provider.authenticate(code, redirect_uri, client_secret)
```

The above code requires copy-pasting into your browser and back into your console. If you want to remove some of
that manual work, you can use the helper class `GetAuthCodeServer`. That helper class spins up a webserver, so
this method cannot be used on all environments.

```python
import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

redirect_uri = 'http://localhost:8080/'
client_secret = 'your_app_secret'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

client = onedrivesdk.get_default_client(
    client_id='your_client_id', scopes=scopes)

auth_url = client.auth_provider.get_auth_url(redirect_uri)

#this will block until we have the code
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

client.auth_provider.authenticate(code, redirect_uri, client_secret)
```

Once your app is authenticated, you should have access to the OneDrive API, and
can begin making calls using the SDK.

### OneDrive for Business

To interact with the OneDrive API, your app must authenticate for a specific resource. Your
app must first use the Resource Discovery helper to find out which service you can access.
Then, you can build a client to access those resources. This uses a slightly different
auth flow than the standard code flow - note the use of `redeem_refresh_token` with
the `service_resource_id` of the service you want to access.

```python
import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
from onedrivesdk.helpers.resource_discovery import ResourceDiscoveryRequest

redirect_uri = 'http://localhost:8080'
client_id = your_client_id
client_secret = your_client_secret
discovery_uri = 'https://api.office.com/discovery/'
auth_server_url='https://login.microsoftonline.com/common/oauth2/authorize'
auth_token_url='https://login.microsoftonline.com/common/oauth2/token'

http = onedrivesdk.HttpProvider()
auth = onedrivesdk.AuthProvider(http,
                                client_id,
                                auth_server_url=auth_server_url,
                                auth_token_url=auth_token_url)
auth_url = auth.get_auth_url(redirect_uri)
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
auth.authenticate(code, redirect_uri, client_secret, resource=discovery_uri)
# If you have access to more than one service, you'll need to decide
# which ServiceInfo to use instead of just using the first one, as below.
service_info = ResourceDiscoveryRequest().get_service_info(auth.access_token)[0]
auth.redeem_refresh_token(service_info.service_resource_id)
client = onedrivesdk.OneDriveClient(service_info.service_resource_id + '/_api/v2.0/', auth, http)
```

## About this form
This fork is maintained by Atakama, LLC.   This is not the official sdk but a number of pull requests have been incorporated:

- OrderedDict fix for python 3.5 (https://github.com/OneDrive/onedrive-sdk-python/pull/116)
- Socket linger fix (https://github.com/OneDrive/onedrive-sdk-python/pull/96)
- PyInstaller packaging fix

If you are looking for an alternative api, consider using one of:

- requests-oauthlib for OAuth and requests + .json() for the direct REST calls
- authomatic

(Personally, I believe that the onedrivesdk needs a replacement with less marshalling and more documentation.)

## Examples

**Note:** All examples assume that your app has already been
[Authenticated](#authentication).

### Upload an Item

```python
returned_item = client.item(drive='me', id='root').children['newfile.txt'].upload('./path_to_file.txt')
```

### Download an Item

```python
root_folder = client.item(drive='me', id='root').children.get()
id_of_file = root_folder[0].id

client.item(drive='me', id=id_of_file).download('./path_to_download_to.txt')
```

### Add a folder

```python
f = onedrivesdk.Folder()
i = onedrivesdk.Item()
i.name = 'New Folder'
i.folder = f

returned_item = client.item(drive='me', id='root').children.add(i)
```

### Copy an Item

```python
from onedrivesdk.item_reference import ItemReference

ref = ItemReference()
ref.id = 'yourparent!id' #path also supported

copy_operation = client.item(drive='me', id='youritemtocopy!id').copy(name='new copied name', parent_reference=ref).post()

#copy_operation.item will return None until the copy has completed.
#If you would like to block until the operation has been completed
#and copy_operation.item is no longer None
copy_operation.poll_until_complete()

```

### Rename an Item

```python
renamed_item = onedrivesdk.Item()
renamed_item.name = 'NewItemName'
renamed_item.id = 'youritemtorename!id'

new_item = client.item(drive='me', id=renamed_item.id).update(renamed_item)
```

### Paging through a collection

```python
#get the top three elements of root, leaving the next page for more elements
collection = client.item(drive='me', id='root').children.request(top=3).get()

#get the first item in the collection
item = collection[0]

#get the next page of three elements, if none exist, returns None
collection2 = onedrivesdk.ChildrenCollectionRequest.get_next_page_request(collection, client).get()
```

### Async operations

For async operations, you create an `asyncio.coroutine` which
implements `asyncio.ascompleted`, and execute it with
`loop.run\_until\_complete`.

```python
import asyncio

@asyncio.coroutine
def run_gets(client):
    coroutines = [client.drive('me').request().get_async() for i in range(3)]
    for future in asyncio.as_completed(coroutines):
        drive = yield from future
        print(drive.id)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_gets(client))   
```

## Saving and Loading a Session

You can save your OAuth session details so that you don't have to go through the full
OAuth flow every time you start your app. To do so, follow these steps:

```python
auth_provider = onedrivesdk.AuthProvider(http_provider,
                                         client_id,
                                         scopes)
auth_provider.authenticate(code, redirect_uri, client_secret)

# Save the session for later
auth_provider.save_session()

#### Next time you start the app ####
auth_provider = onedrivesdk.AuthProvider(http_provider,
                                         client_id,
                                         scopes)
auth_provider.load_session()
auth_provider.refresh_token()
client = onedrivesdk.OneDriveClient(base_url, auth_provider, http_provider)
```

After the call to `refresh_token()` your `AuthProvider` will be ready to authenticate calls
to the OneDrive API. This implementation is not complete, though.

1. The default implementation of [Session](\src\onedrivesdk\session.py) saves the session
information in a Pickle file. Session data should be treated with equal protection as a
password, so this is not safe for deployment to real users. You should re-implement
`Session` to fit your app's needs.
2. Calling `.load_session()` may throw an exception, depending on your implementation
of `Session`. For example, the default implementation tries to open the file `session.pickle`,
 which may not exist and will raise `FileNotFoundError`. You will need to account for that here
 (or, even better, in your implementation of `Session`).

## Using a Proxy
If you need to proxy your requests, you can use the helper class `HttpProviderWithProxy`.
```python
import onedrivesdk
from onedrivesdk.helpers import http_provider_with_proxy

proxy = {
    'http': 'http://localhost:8888',
    'https': 'https://localhost:8888'
}
http = http_provider_with_proxy.HttpProviderWithProxy(proxy, verify_ssl=True)
auth = onedrivesdk.AuthProvider(http, my_client_id, ['onedrive.readwrite'])
client = onedrivesdk.OneDriveClient(my_base_url, auth, http)
```

All requests using that client will be proxied.

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
