from s3.s3_connection import S3BucketConnection
from fileio.logfilereader import LogFileReader

if __name__ == '__main__':

    aws_bucket = 's3/bucket/name'
    access_id = "access/id"
    secret_key = "secret/key"
    file_name = "file/name"

    # make connection with s3 bucket
    s3_connection = S3BucketConnection(aws_bucket,access_id,secret_key,'s3','us-east-2')

    # download log file
    s3_connection.download_file(file_name, "log_file.log")

    logFileReader = LogFileReader(file_name)

    '''
    The second argument passed into the write_modified_file function is a map of key, value pairs - where the keys
    are the key the string we look for in a particular line of a log file, and the value is a function which will
    process the key, value pair in the log file if it exists. These maps could be predefined and stored in a class
    for reuse.
    '''

    logFileReader.write_modified_file("updated_log_file.log",
                                      {"DOB": logFileReader.process_dob, "First":logFileReader.process_first_name})

    s3_connection.upload_file("updated_log_file.log", "updated_log_file.log")
