import io, os
class Transfer:
    def __init__(self):
        self.name = "Additional_Function"
        self.version = "0.0.1"
        self.author = "Tusher Mondal"
        self.email = "luciefer9062hurley@gmail.com"
        self.usage = "Free for All"

    def returnByte(self, filename, Path):
        with open(Path+"/"+filename, "rb") as f:
            return f.read()

    def returnFile(self, ByteObject):
        return io.BytesIO(ByteObject)


    def saveByte(self, ByteObject, filename, Path):
        with open(Path+"/"+filename, "wb") as f:
            f.write(ByteObject)
            f.close()

    def fileSizeinBytes(self, filename, Path):
        with open(Path+"/"+filename, "rb") as f:
            return len(f.read())


    def splitByte(self, ByteObject, n):
        return [ByteObject[i:i+n] for i in range(0, len(ByteObject), n)]

    def combineByte(self, ByteObjectArray):
        return b''.join(ByteObjectArray)
    
    def listFile(self, Path):
        files = os.listdir(Path)
        files = ",".join(files)
        return files

class Reader:
    def __init__(self):
        self.name = "Additional_Function"
        self.version = "0.0.1"
        self.author = "Tusher Mondal"
        self.email = "luciefer9062hurley@gmail.com"
        self.usage = "Free for All"
        self.Instructions = "\n\nChoose from the following : \n1. Download\n2. Upload\n3. Exit\n\n"
    
    def readFiles(self, Files):
        print("Choose from the following : ")
        i = 1
        for file in Files:
            print(str(i)+')', file)
            i += 1
    
    def readInstruction(self):
        print(self.Instructions)
    
    def readERROR(self, ERROR):
        print("[ERROR] "+ ERROR)