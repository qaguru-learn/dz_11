from demoqa_tests.models.pages.registration_page import RegistrationPage
from demoqa_tests.models.pages.simple_registration_page import SimpleRegistrationPage


class LeftPanel:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.simple_registration_page = SimpleRegistrationPage()

    def open(self, first_button, second_button):
        if first_button == 'Elements' and second_button == 'Text Box':
            return self.simple_registration_page.open()
        elif first_button == 'Forms' and second_button == 'Practice Form':
            return self.registration_page.open()

    def open_simple_registration_form(self):
        return self.open('Elements', 'Text Box')

    def open_registration_form(self):
        return self.open('Forms', 'Practice Form')
