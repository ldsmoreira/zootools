BLOCK_SEPARATOR = b'\n\n'

def getfmt(key: str, group: str = "default", **meta) -> bytes:

  mainheader = b'get'+b' '+key.encode()+b' '+b'0'+ BLOCK_SEPARATOR

  metaheader = f"group::{group}\n"

  for key in meta.keys():
    metaheader+=f"{key}::{meta[key]}\n"

  request = mainheader + metaheader.encode() + b'\n'

  return request

def setfmt(key: str, data: bytes, group: str = "default", **meta) -> bytes:

  mainheader = b'set'+b' '+key.encode()+b' '+str(len(data)).encode()+ BLOCK_SEPARATOR

  metaheader = f"group::{group}\n"

  for key in meta.keys():
    metaheader+=f"{key}::{meta[key]}\n"

  request = mainheader + metaheader.encode() + b'\n' + data

  return request
