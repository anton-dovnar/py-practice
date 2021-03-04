# TOC

* [Common Magic](#common-magic)
* [Basic Typing](#basic-typing)

## Common Magic

    __main__
    __name__
    __file__
    __module__
    __all__
    __dict__
    __class__
    __doc__
    __init__(self, [...)
    __str__(self)
    __repr__(self)
    __del__(self)

    # For Descriptor
    __get__(self, instance, owner)
    __set__(self, instance, value)
    __delete__(self, instance)

    # For Context Manager
    __enter__(self)
    __exit__(self, exc_ty, exc_val, tb)

    # Emulating container types
    __len__(self)
    __getitem__(self, key)
    __setitem__(self, key, value)
    __delitem__(self, key)
    __iter__(self)
    __contains__(self, value)

    # Controlling Attribute Access
    __getattr__(self, name)
    __setattr__(self, name, value)
    __delattr__(self, name)
    __getattribute__(self, name)

    # Callable object
    __call__(self, [args...])

    # Compare related
    __cmp__(self, other)
    __eq__(self, other)
    __ne__(self, other)
    __lt__(self, other)
    __gt__(self, other)
    __le__(self, other)
    __ge__(self, other)

    # Arithmetical operation related
    __add__(self, other)
    __sub__(self, other)
    __mul__(self, other)
    __div__(self, other)
    __mod__(self, other)
    __and__(self, other)
    __or__(self, other)
    __xor__(self, other)

## Basic Typing

    import io
    import re
    from collections import deque, namedtuple
    from typing import (
        IO,
        Any,
        Deque,
        Dict,
        Iterable,
        List,
        Mapping,
        Match,
        MutableMapping,
        NamedTuple,
        Optional,
        Pattern,
        Sequence,
        Set,
        Text,
        Tuple,
    )

    # Without initializing
    x: int

    # Any type
    y: Any
    y = 1
    y = "1"

    # Built-in
    var_int: int = 1
    var_str: str = "Hello Typing"
    var_byte: bytes = b"Hello Typing"
    var_bool: bool = True
    var_float: float = 1.
    var_unicode: Text = u'\u2713'

    # Cound be none
    var_could_be_none: Optional[int] = None
    var_could_be_none = 1

    # collections
    var_set: Set[int] = {i for i in range(3)}
    var_dict: Dict[str, str] = {"foo": "Foo"}
    var_list: List[int] = [i for i in range(3)]
    var_Tuple: Tuple = (1, 2, 3)
    var_deque: Deque = deque([1, 2, 3])
    var_nametuple: NamedTuple = namedtuple('P', ['x', 'y'])

    # io
    var_io_str: IO[str] = io.StringIO("Hello String")
    var_io_byte: IO[bytes] = io.BytesIO(b"Hello Bytes")
    var_io_file_str: IO[str] = open(__file__)
    var_io_file_byte: IO[bytes] = open(__file__, 'rb')

    # re
    p: Pattern = re.compile("(https?)://([^/\r\n]+)(/[^\r\n]*)?")
    m: Optional[Match] = p.match("https://www.python.org/")

    # Duck types: list-like
    var_seq_list: Sequence[int] = [1, 2, 3]
    var_seq_tuple: Sequence[int] = (1, 2, 3)
    var_iter_list: Iterable[int] = [1, 2, 3]
    var_iter_tuple: Iterable[int] = (1, 2, 3)

    # Duck types: dict-like
    var_map_dict: Mapping[str, str] = {"foo": "Foo"}
    var_mutable_dict: MutableMapping[str, str] = {"bar": "Bar"}
