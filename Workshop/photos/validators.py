from django.core.exceptions import ValidationError

from Workshop.core.utils import megabytes_to_bytes


def validate_image_less_than_5mb(fileobj):
    filesize = fileobj.size
    megabyte_limit = 5.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f'Max file size is {megabyte_limit}MB')
