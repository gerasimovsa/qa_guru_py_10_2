from selene import browser, be, have


def test_google_search_valid_query():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_invalid_query():
    rand_string = "pdfogkjsbrdt54"
    browser.element('[name="q"]').should(be.blank).type(rand_string).press_enter()
    browser.element('[id="botstuff"]').should(have.text(f'По запросу {rand_string} ничего не найдено.'))
