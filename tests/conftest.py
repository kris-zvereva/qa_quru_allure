import pytest
from selene import browser

from pages.github import GithubPage


@pytest.fixture
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = "https://github.com"
    yield
    browser.quit()


@pytest.fixture
def github_page():
    page = GithubPage()
    yield page