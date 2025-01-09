class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        return ' | '.join(f'{str_field}={self.__dict__[str_field]}' for str_field in self.str_fields)
