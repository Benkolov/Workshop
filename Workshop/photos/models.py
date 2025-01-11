from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from Workshop.core.model_mixins import StrFromFieldsMixin
from Workshop.pets.models import Pet
from Workshop.photos.validators import validate_image_less_than_5mb


UserModel = get_user_model()

class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'publication_date', 'location', 'description')
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        null=False,
        blank=True,
        validators=(validate_image_less_than_5mb,),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
