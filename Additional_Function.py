import io
def returnByte(filename):
    with open(filename, "rb") as f:
        return f.read()

def returnFile(ByteObject):
    return io.BytesIO(ByteObject)


def saveByte(ByteObject, filename):
    with open(filename, "wb") as f:
        f.write(ByteObject)
        f.close()

def fileSizeinBytes(filename):
    with open(filename, "rb") as f:
        return len(f.read())


def splitByte(ByteObject, n):
    return [ByteObject[i:i+n] for i in range(0, len(ByteObject), n)]

def combineByte(ByteObjectArray):
    return b''.join(ByteObjectArray)