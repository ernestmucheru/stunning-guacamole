import unittest
from contact import Contact

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviors.
    Args:
        unittest.TestCase: TestCase that helps in creating test cases
    '''

# Items up here...
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("James", "Muriuki", "0700279345","james@ms.com")

    def test_init(self):
        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number,"0700279345")
        self.assertEqual(self.new_contact.email,"james@ms.com")

    #Second Test
    def test_save_contact(self):
        '''
        test_save_contact test case to tes if the object is saved into the contact list
        '''

        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),1)
    if __name__ == '__main__':
        unittest.main()
 
