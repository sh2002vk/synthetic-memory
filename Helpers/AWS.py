import boto3
from botocore.exceptions import NoCredentialsError
import os


class AWS:
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )
        return

    def downloadS3(self, dataPath):
        """ Downloads an asset from s3

        :param dataPath:
        :return:
        """

        s3 = self.session.client('s3')
        try:
            asset = s3.download_file(dataPath)
            print(f"Downloaded {dataPath} from s3")
            return asset
        except NoCredentialsError:
            print("ERROR: No AWS credentials found")
        except Exception as e:
            print(f"ERROR: downloading {dataPath} from s3")
            print(e)


