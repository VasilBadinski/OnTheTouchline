import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class ArticleValidator:
    message = 'There is an invalid symbol'
    regex = r'^[A-Za-z0-9 .,!?:;\'"()\-\n]+$'

    def __call__(self, value):
        if not re.fullmatch(self.regex, value):
            raise ValidationError(self.message)