import hashlib
from django.conf import settings


def md5_str(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))  # 加盐
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()
