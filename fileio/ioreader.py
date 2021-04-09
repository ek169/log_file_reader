from iobase import FileIOBase

class FileIOReader(FileIOBase):
        '''
        Class for operating on a file which contains key, value pairs 
        '''

        def __init__(self, file_name=""):
            """initialize class and passes file name to base class"""
            FileIOBase.__init__(self, file_name)


        def read_line_as_kv_pair(self, line, delimiter="="):
            """parses a line based on it containing key value pairs with delimeter

            :param line: string containing line from a text file
            :param delimiter: character on which key, value pairs are split

            :return: dictionary of key, value pairs in log file
            """
            import shlex
            import re

            split_line = []

            # go through each entry and split upon spaces that aren't within quotes "" or ''
            for entry in shlex.split(line):

                # go through these splits and split upon "="
                split = entry.split(delimiter)
                if len(split) == 2:
                    split_line.append(tuple(split))
                else:
                    split_line.append((split[0], ""))

            # create dictionary from key value pairs
            line_dict = dict(split_line)

            return line_dict


        def update_line_using_kv_pair(self, line="", line_as_kv_pair={}, processing_dict={}):
            """Updates a text line using a dictionary of keys and processing functions, where the processing
            functions will be applied to some key, value pair

            :param line: string to process
            :param line_as_kv_pair: dictionary of key, value pairs in line
            :param processing_dict: dictionary where the keys are the keys found in the line, and the associated
                                    value is a function which performs processing on the key, value pair in the line
            :return: modified line
            """
            for k, v in line_as_kv_pair.items():

                if k in processing_dict:

                    try:

                        line = processing_dict[k](line, k, v)

                    except TypeError:

                        print("Function does not follow convention for arguments function(line, key, value)")
                        continue

            return line
