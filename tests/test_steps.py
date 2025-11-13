import allure
from selene import browser


@allure.title('Verify the issue exists in repository')
@allure.description('This test verifies that the specific issue is displayed in the GitHub repository')
@allure.feature('GitHub Issues')
@allure.story('Issue Display')
@allure.severity(allure.severity_level.NORMAL)
def test_search_issue(browser_setup, github_page):
    with allure.step('open GitHub page'):
        github_page.open()

    with allure.step('search the repo'):
        github_page.search_for_repo("kris-zvereva/qa_quru_allure")

    with allure.step('open the repo'):
        github_page.open_repo("kris-zvereva/qa_quru_allure")

    with allure.step('switch to Issues tab'):
        github_page.open_issues()

    with allure.step('verify Issue is displayed'):
        github_page.issues_should_have_text("test_issue")
        screenshot = browser.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="issue test result", attachment_type=allure.attachment_type.PNG)