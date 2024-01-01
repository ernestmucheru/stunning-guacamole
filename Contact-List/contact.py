class Contact:
    """
    Class that generates new instances of contacts
    """
    contact_list = []
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number 
        self.email = email

    def create_contact(fname, lname, phone, email):
        '''
        Function to create a new contact
        '''
        new_contact = Contact(fname, lname, phone, email)
        return new_contact

    # Save contacts
    def save_contacts(contact):
        '''
        Function to save contact
        '''
        contact.save_contact()

    # Delete contact

    def del_contact(contact):
        '''
        Function to delete a contact
        '''
        contact.delete_contact()

    # Finding a contact
    def find_contact(number):
        '''
        Function that finds a contact by number and returns the contact
        '''
        return Contact.find_by_number(number)

    # Check if a contact exists
    def check_existing_contacts(number):
        '''
        Function that check if a contact exists with that number and retunr a Boolean
        '''
        return Contact.contact_exist(number)

    # Displaying all contacts
    def display_contacts():
        '''
        Function that returns all the saved contacts
        '''
        return Contact.display_contacts()




        