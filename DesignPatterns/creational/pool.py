"""
Preinstantiate and maintain a group of instances of the same type.

This pattern is used when creating an object is costly (and they are
created frequently) but only a few are used at a time. With a Pool we
can manage those instances we have as of now by caching them. Now it
is possible to skip the costly creation of an object if one is
available in the pool.
A pool allows to 'check out' an inactive object and then to return it.
If none are available the pool creates one to provide without wait.

In this example queue.Queue is used to create the pool (wrapped in a
custom ObjectPool object to use with the with statement), and it is
populated with strings.
As we can see, the first string object put in "yam" is USED by the
with statement. But because it is released back into the pool
afterwards it is reused by the explicit call to sample_queue.get().
Same thing happens with "sam", when the ObjectPool created inside the
function is deleted (by the GC) and the object is returned.
"""
import queue


class ObjectPool:

    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def test_object(queue):
    pool = ObjectPool(queue, True)
    print(f'Inside func: {pool.item}')


if __name__ == '__main__':
    sample_queue = queue.Queue()
    sample_queue.put('yam')

    with ObjectPool(sample_queue) as obj:
        print(f'Inside with: {obj}')

    print(f'Outside with: {sample_queue.get()}')

    sample_queue.put('sam')
    test_object(sample_queue)

    print(f'Outside func: {sample_queue.get()}')

    if not sample_queue.empty():
        print(sample_queue.get())
