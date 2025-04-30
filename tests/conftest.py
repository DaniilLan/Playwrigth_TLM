import pytest
from Methods.methods_page import *
from Methods.db_method import QueryDB

@pytest.fixture()
def main_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        yield page

@pytest.fixture()
def page_general(main_page):
    page = main_page
    page.goto(url_auth_test)
    yield MethodsPageUsers(page)


@pytest.fixture()
def page_auth(main_page):
    page = main_page
    page.goto(url_auth_test)
    yield MethodsPageUsers(page)


@pytest.fixture()
def page_users(main_page):
    page = main_page
    page.goto(url_users_test)
    yield MethodsPageUsers(page)


@pytest.fixture()
def page_help(main_page):
    page = main_page
    page.goto(url_help_test)
    yield MethodsPageUsers(page)


@pytest.fixture()
def page_support(main_page):
    page = main_page
    page.goto(url_support_test)
    yield MethodsPageUsers(page)


@pytest.fixture
def test_user():
    db = QueryDB()
    user_data = db.query_create_user()
    yield user_data
    db.query_delete_user(user_data['id'])
