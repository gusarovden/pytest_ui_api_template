from page.AuthPage import AuthPage
from page.MainPage import MainPage

def test_auth(browser):
    email = "den689608@gmail.com"
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(email, "Q_werty4321")

    main_page = MainPage(browser)
    main_page.open_menu()

    info = main_page.get_account_info()

    assert main_page.get_current_url().endswith("...")
    assert info[0] == "Denis"
    assert info[1] == email


    # auth_page = AuthPage(browser)
    # auth_page.go()
    # auth_page.login_as("den689608@gmail.com","(Q_werty4321)")

    # # Проверяем, что после запуска теста URL заканчивается заданной подстрокой:
    # assert auth_page.get_current_url().endswith("...")   