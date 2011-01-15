'''
Only one form would be enough, with an argument given in the __init__
to delete the correct field.
'''

# from django
from django import forms

# from app
from models import Contact


class ContactForm(forms.ModelForm):
    """ModelForm for the Contact model"""

    class Meta:
        model = Contact


class ContactFormWithBirthday(ContactForm):
    """ContactForm with a birthday field"""

    class Meta(ContactForm.Meta):
        exclude = ('image', )


class ContactFormWithImage(ContactForm):
    """ContactForm with an upload image field"""

    class Meta(ContactForm.Meta):
        exclude = ('birthday', )
