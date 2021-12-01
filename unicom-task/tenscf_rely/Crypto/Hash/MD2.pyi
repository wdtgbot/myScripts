from typing import Union

Buffer = Union[bytes, bytearray, memoryview]

class MD4Hash(object):
    digest_size: int
    block_size: int
    oid: str

    def __init__(self, data: Buffer = ...) -> None: ...
    def update(self, data: Buffer) -> None: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def copy(self) -> MD4Hash: ...
    def new(self, data: Buffer = ...) -> MD4Hash: ...

def new(data: Buffer = ...) -> MD4Hash: ...
digest_size: int
block_size: int