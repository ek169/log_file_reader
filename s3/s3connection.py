import boto3

class S3BucketConnection:
    def __init__(self, aws_bucket="", aws_access_id="", aws_secret_key="", aws_service="", aws_region_name=""):
        self.aws_bucket = aws_bucket
        self.aws_access_id = aws_access_id
        self.aws_secret_key = aws_secret_key
        self.aws_service = aws_service
        self.aws_region_name = aws_region_name

    def download_file(self, remote_name, local_name):
        s3.Bucket(self.aws_bucket).download_file(Key=remote_name, Filename=local_name)

    def upload_file(self, file_name, s3_obj_name):
        try:
            r = s3.Bucket(self.aws_bucket).upload_file(file_name, s3_obj_name)
        except:
            return False
        return True
