def test_search_issue(browser_setup, github_page):
    github_page.open()
    github_page.search_for_repo("kris-zvereva/qa_quru_allure")
    github_page.open_repo("kris-zvereva/qa_quru_allure")
    github_page.open_issues()
    github_page.issues_should_have_text("test_issue")