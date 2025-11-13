import allure
from selene import browser


@allure.title('Verify the issue exists in repository')
@allure.description('This test verifies that the specific issue is displayed in the GitHub repository')
@allure.feature('GitHub Issues')
@allure.story('Issue Display')
@allure.severity(allure.severity_level.NORMAL)
def test_search_issue(browser_setup, github_page):
    repo = "kris-zvereva/qa_quru_allure"
    issue = "test_issue"

    open_browser(github_page)
    search_for_repo(github_page, repo)
    open_repo(github_page, repo)
    open_issues(github_page)
    check_issue(github_page, issue)


@allure.step('open GitHub page')
def open_browser(github_page):
    github_page.open()


@allure.step('search the repo')
def search_for_repo(github_page, repo):
    github_page.search_for_repo(repo)


@allure.step('open the repo')
def open_repo(github_page, repo):
    github_page.open_repo(repo)


@allure.step('switch to Issues tab')
def open_issues(github_page):
    github_page.open_issues()


@allure.step('verify Issue is displayed')
def check_issue(github_page, issue):
    github_page.issues_should_have_text(issue)
    screenshot = browser.driver.get_screenshot_as_png()
    allure.attach(screenshot, name="issue test result", attachment_type=allure.attachment_type.PNG)