class FileIOBase:
    '''
    Base class for all classes that operate on a file
    '''
    def __init__(self, file_name):
        self.file_name = file_name
