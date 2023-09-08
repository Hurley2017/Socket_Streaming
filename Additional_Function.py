import io
class Download(io):
    def __init__(self):
        self.name = "App"
        self.version = "0.0.1"
        self.author = "Tusher Mondal"
        self.email = "luciefer9062hurley@gmail.com"
        self.usage = "Free for All"

    def returnByte(self, filename):
        with open(filename, "rb") as f:
            return f.read()

    def returnFile(self, ByteObject):
        return io.BytesIO(ByteObject)


    def saveByte(self, ByteObject, filename):
        with open(filename, "wb") as f:
            f.write(ByteObject)
            f.close()

    def fileSizeinBytes(self, filename):
        with open(filename, "rb") as f:
            return len(f.read())


    def splitByte(self, ByteObject, n):
        return [ByteObject[i:i+n] for i in range(0, len(ByteObject), n)]

    def combineByte(self, ByteObjectArray):
        return b''.join(ByteObjectArray)