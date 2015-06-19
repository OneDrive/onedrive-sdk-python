**Getting Started with the OneDrive Python SDK**

------------------------------------------------------------------------
[![Build status](https://ci.appveyor.com/api/projects/status/x1cjahp817w6r455?svg=true)](https://ci.appveyor.com/project/OneDrive/vroom-client-python)

Installation
============

To install the OneDrive Python SDK, open a command prompt and type:

<pre><code>pip install onedrivesdk
</code></pre>
Next, include the SDK in your python project by adding

<pre><code>import onedrivesdk</code></pre>

Authentication
==============

To interact with the OneDrive API, you must authenticate. You can use the following code sample to do so.

<pre><code>import onedrivesdk
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
</code></pre>

Once you are authenticated, you should have access to the OneDrive API, and
can begin making calls using the SDK!

Examples
========

NOTE: All examples assume that the
[Authentication](#authentication) has already occured.

Upload an Item
--------------

<pre><code>returned_item = client.item(drive="me", id="root").children["newfile.txt"].upload("./path_to_file.txt")</code></pre>

Download an Item
----------------

<pre><code>root_folder = client.item(drive="me", id="root").children.get()
id_of_file = root_folder[0].id

client.item(drive="me", id=id_of_file).download("./path_to_download_to.txt")
</code></pre>

Add a Folder
------------

<pre><code>f = onedrivesdk.Folder()
i = onedrivesdk.Item()
i.name = "New Folder"
i.folder = f

returned_item = client.item(drive="me", id="root").children.add(i)
</code></pre>

Copying an Item
---------------

<pre><code>from onedrivesdk.item_reference import ItemReference

ref = ItemReference()
ref.id = "yourparent!id" #path also supported

copy_operation = client.item(drive="me", id="youritemtocopy!id").copy(name="new copied name", parent_reference=ref).post()

#copy_operation.item will return None until the copy has completed.
#If you would like to block until the operation has been completed
#and copy_operation.item is no longer None
copy_operation.poll_until_complete()

</code></pre>

Renaming an Item
----------------

<pre><code>renamed_item = onedrivesdk.Item()
renamed_item.name = "NewItemName"
renamed_item.id = "youritemtorename!id"

new_item = client.item(drive="me", id=renamed_item.id).update(renamed_item)
</code></pre>

Paging through a Collection
---------------------------

<pre><code>#get the top 3 elements of root, leaving the next page for more elements
collection = client.item(drive="me", id="root").children.request(top=3).get()

#get the first item in the collection
item = collection[0]

#get next page of 3 elements, if none exist, returns None
collection2 = collection.next_page_request.get()
</code></pre>

Async operations
----------------

<p>
For async operations, you create an asyncio.coroutine which
implements asyncio.ascompleted, and execute it with
loop.run\_until\_complete.

<pre><code>import asyncio

@asyncio.coroutine
def run_gets(client):
    coroutines = [client.drive("me").request().get_async() for i in range(3)]
    for future in asyncio.as_completed(coroutines):
        drive = yield from future
        print(drive.id)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_gets(client))   
</code></pre>
