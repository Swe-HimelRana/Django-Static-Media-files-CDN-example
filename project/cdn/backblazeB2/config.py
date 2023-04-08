DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = '005dbb2c2bb90d50000000002'
AWS_SECRET_ACCESS_KEY = 'K005CwyyDVALSao8Ndmr0/rG25vim3o'
AWS_STORAGE_BUCKET_NAME = 'codingexpert'
AWS_DEFAULT_ACL = 'public-read' 
AWS_S3_ENDPOINT_URL = 'https://s3.us-east-005.backblazeb2.com' # Make sure nyc3 is correct
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}

AWS_STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/{AWS_STATIC_LOCATION}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'