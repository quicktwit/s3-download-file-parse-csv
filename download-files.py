import csv
from boto3.session import Session

ACCESS_KEY = ''
SECRET_KEY = ''
BUCKET_NAME = ''
csv_file = 'test.csv' # your csv path
subdirectory = 'some_directory_name/' # if subdirectory is available

session = Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3 = session.resource('s3')
bucket = s3.Bucket(BUCKET_NAME)

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        full_path = subdirectory + row[0]
        try:
            bucket.download_file(full_path, row[0])
            print('File Downloaded: ', row[0])
        except:
            print('No file found')
