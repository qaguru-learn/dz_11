from selene import browser, have, be, by
from demoqa_tests.data.users import User, Genders, Hobbies
from demoqa_tests.models import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_firstname(self, current_user: User):
        browser.element('#firstName').should(be.blank).type(current_user.fullname.split(' ')[0])
        return self

    def fill_lastname(self, current_user: User):
        browser.element('#lastName').should(be.blank).type(current_user.fullname.split(' ')[-1])
        return self

    def fill_email(self, current_user: User):
        browser.element('#userEmail').should(be.blank).type(current_user.email)
        return self

    def gender_make_choice(self, current_user: User):
        choice = {Genders.MALE.value: 1, Genders.FEMALE.value: 2}
        browser.element(f"#gender-radio-{choice[current_user.gender]}").double_click()
        return self

    def fill_phone_number(self, current_user: User):
        browser.element('#userNumber').should(be.blank).type(current_user.phone_number)
        return self

    def fill_birthday(self, current_user: User):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__year-select").click().\
            element(by.text(f'{current_user.birthday.year}')).click()
        browser.element(".react-datepicker__month-select").click().\
            element(by.text(f'{current_user.birthday.strftime("%B")}')).click()
        browser.element(f".react-datepicker__week .react-datepicker__day--0{current_user.birthday.day}").click()
        return self

    def fill_subjects(self, current_user: User):
        browser.element('#subjectsInput').type(current_user.subject).press_enter()
        return self

    def hobbies_make_choice(self, current_user: User):
        choice = {Hobbies.SPORTS.value: 1,
                  Hobbies.READING.value: 2, Hobbies.MUSIC.value: 3}
        browser.element(f'[for=hobbies-checkbox-{choice[current_user.hobby]}]').click()
        return self

    def upload_picture(self, current_user: User):
        browser.element('#uploadPicture').type(resource.path(current_user.photo))
        return self

    def fill_address(self, current_user: User):
        browser.element('#currentAddress').should(be.blank).type(current_user.address)
        return self

    def fill_state_city(self, current_user: User):
        browser.element('#react-select-3-input').should(be.blank).type(current_user.state_city.split(' ')[0]).press_enter()
        browser.element('#react-select-4-input').should(be.blank).type(current_user.state_city.split(' ')[-1]).press_enter()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def form_should_be_completed(self):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
        return self

    def register(self, current_user: User):
        (self
            .fill_firstname(current_user)
            .fill_lastname(current_user)
            .fill_email(current_user)
            .gender_make_choice(current_user)
            .fill_phone_number(current_user)
            .fill_birthday(current_user)
            .fill_subjects(current_user)
            .hobbies_make_choice(current_user)
            .upload_picture(current_user)
            .fill_address(current_user)
            .fill_state_city(current_user)
            .submit())
        return self

    def should_registered_with(self, current_user: User):
        self.form_should_be_completed()
        browser.element('.table').all('td').even.should(have.exact_texts(
            current_user.fullname,
            current_user.email,
            current_user.gender,
            current_user.phone_number,
            current_user.birthday.strftime('%d %B,%Y'),
            current_user.subject,
            current_user.hobby,
            current_user.photo,
            current_user.address,
            current_user.state_city
        ))
        return self
