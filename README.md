# Getting started with the OneDrive SDK for Python

------------------------------------------------------------------------
[![Build status](https://ci.appveyor.com/api/projects/status/x1cjahp817w6r455?svg=true)](https://ci.appveyor.com/project/OneDrive/vroom-client-python)

## Installation

Once you've downloaded the OneDrive SDK for Python, open a command prompt and type the following to install it:

<pre><code>pip install onedrivesdk</code></pre>

Next, include the SDK in your Python project by adding:

<pre><code>import onedrivesdk</code></pre>

## Authentication

To interact with the OneDrive API, your app must authenticate. You can use the following code sample to do so.

```python
import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

redirect_uri = "http://localhost:8080/"
client_secret = "your_app_secret"

client = onedrivesdk.get_default_client(client_id='your_client_id',
                                       	scopes=['wl.signin',
                                               	'wl.offline_access',
                                               	'onedrive.readwrite'])

auth_url = client.auth_provider.get_auth_url(redirect_uri)

#this will block until we have the code
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

client.auth_provider.authenticate(code, redirect_uri, client_secret)
```

Once your app is authenticated, you should have access to the OneDrive API, and
can begin making calls using the SDK.

## Examples

**Note:** All examples assume that your app has already been
[Authenticated](#authentication).

### Upload an Item

```python
returned_item = client.item(drive="me", id="root").children["newfile.txt"].upload("./path_to_file.txt")
```

### Download an Item

```python
root_folder = client.item(drive="me", id="root").children.get()
id_of_file = root_folder[0].id

client.item(drive="me", id=id_of_file).download("./path_to_download_to.txt")
```

### Add a folder

```python
f = onedrivesdk.Folder()
i = onedrivesdk.Item()
i.name = "New Folder"
i.folder = f

returned_item = client.item(drive="me", id="root").children.add(i)
```

### Copy an Item

```python
from onedrivesdk.item_reference import ItemReference

ref = ItemReference()
ref.id = "yourparent!id" #path also supported

copy_operation = client.item(drive="me", id="youritemtocopy!id").copy(name="new copied name", parent_reference=ref).post()

#copy_operation.item will return None until the copy has completed.
#If you would like to block until the operation has been completed
#and copy_operation.item is no longer None
copy_operation.poll_until_complete()

```

### Rename an Item

```python
renamed_item = onedrivesdk.Item()
renamed_item.name = "NewItemName"
renamed_item.id = "youritemtorename!id"

new_item = client.item(drive="me", id=renamed_item.id).update(renamed_item)
```

### Paging through a collection

```python
#get the top three elements of root, leaving the next page for more elements
collection = client.item(drive="me", id="root").children.request(top=3).get()

#get the first item in the collection
item = collection[0]

#get the next page of three elements, if none exist, returns None
collection2 = collection.next_page_request.get()
```

### Async operations

For async operations, you create an `asyncio.coroutine` which
implements `asyncio.ascompleted`, and execute it with
`loop.run\_until\_complete`.

```python
import asyncio

@asyncio.coroutine
def run_gets(client):
    coroutines = [client.drive("me").request().get_async() for i in range(3)]
    for future in asyncio.as_completed(coroutines):
        drive = yield from future
        print(drive.id)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_gets(client))   
```

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
