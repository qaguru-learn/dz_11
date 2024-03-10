import datetime
import allure
from demoqa_tests.models.appmanager import app
from demoqa_tests.data.users import User, Genders, Hobbies, SimpleUser


@allure.story('Registration form')
def test_registration_page():
    yuriy = User(
        fullname='Yuriy Choba',
        email='yuriy.choba@ex.com',
        gender=Genders.MALE.value,
        phone_number='8987654321',
        birthday=datetime.date(1990, 3, 15),
        subject='Maths',
        hobby=Hobbies.READING.value,
        photo='rick.jpeg',
        address='Lenin street, 28',
        state_city='NCR Delhi',
    )

    with allure.step('Open simple registration form'):
        app.left_panel.open_registration_form()

    with allure.step('Fill registration form'):
        registered_page = app.left_panel.registration_page.register(yuriy)

    with allure.step('Check registration form'):
        registered_page.should_registered_with(yuriy)


@allure.story('Simple registration form')
def test_simple_registration_page():
    yuriy = SimpleUser(
        fullname='Yuriy Choba',
        email='yuriy.choba@ex.com',
        current_address='NCR, Delhi, Lenin street, 28',
        permanent_address='NCR, Delhi, Lenin street, 28',
    )

    with allure.step('Open simple registration form'):
        app.left_panel.open_simple_registration_form()

    with allure.step('Fill registration form'):
        registered_page = app.left_panel.simple_registration_page.register(yuriy)

    with allure.step('Check registration form'):
        registered_page.should_registered_with(yuriy)
