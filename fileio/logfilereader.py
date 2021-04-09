from ioreader import FileIOReader

class LogFileReader(FileIOReader):

    def __init__(self, file_name=""):
        FileIOReader.__init__(self, file_name)

    def parse_timestamp():
        pass
        # there would be some timestamp regular expression processing here, and this would be a separate
        # function that would perform this processing

        #timestamp_regex = "\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})(\.\d+)\]"
        #timestamp_match = re.search(timestamp_regex, line)
        #print(timestamp_match.group(1))
        #re.sub(timestamp_regex, "", line)


    def write_modified_file(self, new_file_name="new_file.log", processing_dict={}):
        """Modifies a particular value in a log file on a per line basis

        :param new_file_name: new file to create
        :param key: key who's value to modify
        :param processing_func: a function which processing the value for a given key
        :return: True if processing was successful, false if otherwise
        """
        with open(new_file_name,'w') as new_file:

            with open(self.file_name) as old_file:

                for line in old_file:

                    line_dict = self.read_line_as_kv_pair(line)

                    new_line = self.update_line_using_kv_pair(line, line_dict, processing_dict)

                    new_file.write(new_line)

        return True



    '''
    Currently these functions exist inside of the LogFileReader, but if they were general enough
    and used often they could exist as standalone functions inside a different utility file, or
    within a GeneralReader class.
    '''

    def process_dob(self, line, dob_key, dob_value):
        """Updates the value for the 'DOB' key in the line to be formatted as follows 'DOB'=X/X/YYYY

        :param line: string to modify
        :param dob_key: key for the DOB
        :param dob_value: value for the associated DOB key
        :return: Modified line
        """
        return line.replace(dob_value, "X/X/" + str(dob_value.split("/")[-1]))

    def process_first_name(self, line, first_name_key, first_name_value):
        """Updates the value for the 'DOB' key in the line to be formatted as follows 'DOB'=X/X/YYYY

        :param line: string to modify
        :param dob_key: key for the DOB
        :param dob_value: value for the associated DOB key
        :return: Modified line
        """
        return line.replace(first_name_value, "REDACTED")
