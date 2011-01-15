from django.db import models


class Contact(models.Model):
    """
    Model for Base form
    NB: Would be better to use the Django User model
    """

    GENDER_CHOICE = (
        (True, "Male"),
        (False, "Female"),
    )

    name = models.CharField("full name", max_length=30, unique=True,
        help_text="Required. 30 characters or fewer. Letters, numbers "
            "and @/./+/-/_ characters",
    )
    email = models.EmailField('e-mail address', blank=True)
    phone = models.CharField('phone number', max_length=12 ,blank=True)
    sex = models.BooleanField(
        'are you a man ?',
        default=True,
        choices=GENDER_CHOICE
    )

    # Special fields
    birthday = models.CharField(blank=True, max_length=10)
    image = models.FileField(
        'Upload an Image',
        upload_to='img/contact',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.name
