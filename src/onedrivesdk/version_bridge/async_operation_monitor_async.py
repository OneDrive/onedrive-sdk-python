'''
------------------------------------------------------------------------------
 Copyright (c) 2015 Microsoft Corporation

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
------------------------------------------------------------------------------
'''
import asyncio
from ..async_operation_monitor import AsyncOperationMonitor


@asyncio.coroutine
def poll_until_done_async(self):
    """Yielding this method blocks until done polling for
    the result of the async operation is returned

    Yields:
        :class:`Item<onedrivesdk.models.item.Item>`: item from the async operation
    """
    future = self._client._loop.run_in_executor(None,
                                                self.poll_until_done)
    item = yield from future
    return item

AsyncOperationMonitor.poll_until_done_async = poll_until_done_async
