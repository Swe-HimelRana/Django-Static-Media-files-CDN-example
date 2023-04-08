**Welcome** 
This repo is an example of how to use cdn for static files in django or restframework
what you need is just put your configuration info in `project/cdn/*/config.py`
and use it on `settings.py` file like below


      

    # Internationalization
    # https://docs.djangoproject.com/en/4.2/topics/i18n/
 
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_TZ = True
    
    # Static files (CSS, JavaScript, Images)
    
    # https://docs.djangoproject.com/en/4.2/howto/static-files/

    STATIC_URL = 'static/'

    # Default primary key field type
    
    # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    
    # Using cdn for static and media files
    # you can follow https://django-storages.readthedocs.io/en/latest/ documentation 
    # but if you need code example you can choose this repo. also in this repo i have shown an code example of how to use cloudflare but official documentation do not have any cloudflare instruction.

    from .cdn.cloudflare.config  import *
    
      
    
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


Note: I did not remove any configuration keys for batter understanding. but those keys has been removed from cdn account. 