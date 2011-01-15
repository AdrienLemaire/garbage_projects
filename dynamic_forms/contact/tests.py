# from django
from django.core.urlresolvers import reverse
from django.test import TestCase


#class ModelsTest(TestCase):


class ViewsTest(TestCase):
    """Tests on the contact application's views"""

    def testListContacts(self):
        """Displays the list of registered users"""
        # First we have no contact
        response = self.client.get(reverse("contact:list_contacts"))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Sorry there is currently no contact")
        # Then we load some fixtures
        # TODO

    def testAddContact(self):
        """The user have to choose the type of form here"""
        response = self.client.get(reverse("contact:add_contact"))
        self.assertEqual(200, response.status_code)
        self.assertContains(response,
            "What kind of contact do you want to create ?")

    def testAddContactWithBirthday(self):
        """Display the form to add a new contact with a birthday field"""
        response = self.client.get(
            reverse("contact:add_contact",
                kwargs={'type_form' : 'birthday'}),
        )
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Birthday")
        # Test to save a contact
        post_data = {
            "name" : "Bob The Sponge",
            "email": "bob@pacific.com",
            "birthday": "01/01/2000",
        }
        response = self.client.post(
            reverse("contact:add_contact",
                kwargs={'type_form' : 'birthday'}),
                post_data, follow=True,
        )
        # if it works, it redirect to the list of users
        self.assertEqual(response.request["PATH_INFO"],
                         reverse("contact:list_contacts"))
        # Test to save a contact without name
        del post_data["name"]
        response = self.client.post(
            reverse("contact:add_contact",
                kwargs={'type_form' : 'birthday'}),
                post_data, follow=True,
        )
        self.assertContains(response,
            "There was a problem with the submitted form")

    def testAddContactWithImage(self):
        """Display the form to add a new contact with an Upload image field"""
        response = self.client.get(
            reverse("contact:add_contact",
                kwargs={'type_form' : 'image'}),
        )
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Upload an Image")

    def testShowContact(self):
        """Show the details for a contact"""
        response = self.client.get(
            reverse("contact:show_contact", kwargs={"pk": 1}),
        )
        self.assertEqual(200, response.status_code)
