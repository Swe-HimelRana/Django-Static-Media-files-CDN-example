DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = 'fa54d16fc265483111ce9ab44d77b1bf'
AWS_SECRET_ACCESS_KEY = '809472911673d96299c703b79c82b7fd2e4ba9c127acbbee4fc1355ce25a7bd2'
AWS_STORAGE_BUCKET_NAME = 'djangostatic'
# AWS_DEFAULT_ACL = 'public-read' 
AWS_S3_ENDPOINT_URL = 'https://29481058ae147e1bb8d402b81e75855f.r2.cloudflarestorage.com' # Make sure nyc3 is correct
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}

AWS_STATIC_LOCATION = 'static'
AWS_S3_CUSTOM_DOMAIN = f'pub-eac55273159c43088c0370234413c245.r2.dev'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'