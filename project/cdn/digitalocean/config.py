DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = 'DO00XVBR48ZWLHNAUCJT'
AWS_SECRET_ACCESS_KEY = 'JuvqUEXybe0at0BCjHP/6Q4u9HfygQrjwzGX9lCtlr0'
AWS_STORAGE_BUCKET_NAME = 'djangocdn'
AWS_DEFAULT_ACL = 'public-read' 
AWS_S3_ENDPOINT_URL = 'https://sgp1.digitaloceanspaces.com' # Make sure nyc3 is correct
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}

AWS_STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/{AWS_STATIC_LOCATION}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'