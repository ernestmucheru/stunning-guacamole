import pyperclip 

from contact import Contact
def test_copy_email(self):
    '''
    Test to confirm that we are copying the email address from a found contact
    '''
    self.new_contact.save_contact()
    Contact.copy_email("0712345678")

    self.assertEqual(self.new_contact.email,pyperclip.paste())                                                                                                                                                                                                                                                                              


      