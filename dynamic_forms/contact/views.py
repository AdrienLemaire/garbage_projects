# from django
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

# from app
from forms import ContactFormWithBirthday
from forms import ContactFormWithImage
from models import Contact


def list_contacts(request):
    """Return the list of registered users"""

    contacts = Contact.objects.all()
    return render_to_response(
        "contact/list_contacts.html",
        locals(),
        context_instance=RequestContext(request),
    )


def add_contact(request, type_form=None):
    """
    If type_form not specified, ask to choose the type of form.
    Else, display the form.
    """

    if type_form == "birthday":
        contactform = ContactFormWithBirthday()
    elif type_form == "image":
        contactform = ContactFormWithImage()

    if request.method == "POST":
        """We try to save the new contact"""
        if "birthday" in request.POST:
            contactform = ContactFormWithBirthday(request.POST)
        elif "image" in request.POST:
            contactform = ContactFormWithImage(request.POST, request.FILES)
        if contactform.is_valid():
            contactform.save()
            return HttpResponseRedirect(reverse("contact:list_contacts"))
        else:
            warnings = "There was a problem with the submitted form. "\
                "Please see the error messages next to the affected"\
                " fields."

    # Variable to avoid the extends "base.html" in the template if ajax
    base_template = "base_ajax.html" if request.is_ajax() else "base.html"

    return render_to_response(
        "contact/add_contact.html",
        locals(),
        context_instance=RequestContext(request),
    )


def show_contact(request, pk):
    """Give details for one contact"""

    contact = Contact.objects.get(id=pk)
    base_template = "base_ajax.html" if request.is_ajax() else "base.html"

    return render_to_response(
        "contact/show_contact.html",
        locals(),
        context_instance=RequestContext(request),
    )

