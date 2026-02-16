#destructors - when we want to destroy the object
#for proper memory usage, destructors should be used
#when db connection has to be closed
#cleanup operations
#destructor is executed at the last ---after the whole code is executed
#post conditions-closing of the browser, db connection closing, releasing of certain resource
#free memory-(garbage collection) which is automatically called
class Desct:
    def __del__(self):
        print("Closing the DB connection")
        print("--------------------")

    def __init__(self):
        print("Object created")
        print("-------------------------")
a=Desct()
print("End of Program ")
del a

class Filehandler:
    def __init__(self,file):
        self.file=open(file,'w')
        print("File is opening")

    def readfile(self,file):
        print("Reading the file")
    def __del__(self):
        self.file.close()
        print("File Closed")

f=Filehandler("Test.txt")
f.readfile("Test.txt")
del f