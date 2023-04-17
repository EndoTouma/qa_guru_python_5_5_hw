import os
from selene import have, command
from selene.support.shared import browser


def test_successful_input_registration_form():
	browser.open('/automation-practice-form')

	browser.element('[id = firstName]').type('Evgenii')

	browser.element('[id = lastName]').type('Vervai')

	browser.element('[id = userEmail]').type('esttest@demoqa.ru')

	browser.element('[name = gender][value=Male]').double_click()

	browser.element('[id = userNumber]').type('8005553535')

	browser.element('#dateOfBirthInput').press()
	browser.element('.react-datepicker__month-select').click()
	browser.element('.react-datepicker__month-select').element('[value="6"]').click()
	browser.element('.react-datepicker__year-select').click()
	browser.element('.react-datepicker__year-select').element('[value="1994"]').click()
	browser.element('.react-datepicker__day--026').click()

	browser.element('#subjectsInput').type("Chemistry").press_enter()

	browser.element('label[for="hobbies-checkbox-2"]').click()

	browser.element('#uploadPicture').type(os.getcwd() + "/test.png")

	browser.element('[id = currentAddress]').type('No 1/46 kellagolla Road Nuwara Eliya, 22200 Nuwara Eliya, Sri Lanka')

	browser.element('#state').click()
	browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
	browser.element('#react-select-4-input').type('Delhi').press_enter()

	browser.element('#submit').press_enter()

	browser.all('tbody tr').should(have.exact_texts(
		'Student Name Evgenii Vervai', 'Student Email esttest@demoqa.ru', 'Gender Male', 'Mobile 8005553535',
		'Date of Birth 26 June,1994', 'Subjects Chemistry', 'Hobbies Reading',
		'Picture test.png', 'Address No 1/46 kellagolla Road Nuwara Eliya, 22200 Nuwara Eliya, Sri Lanka',
		'State and City NCR Delhi'))
