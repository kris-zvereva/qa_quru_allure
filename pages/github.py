from selene import browser, have

class GithubPage:

    def open(self):
        browser.open('/')

    def search_for_repo(self, repo):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type(repo).press_enter()

    def open_repo(self, repo):
        browser.element(f'[href="/{repo}"]').click()

    def open_issues(self):
        browser.element('#issues-tab').click()

    def issues_should_have_text(self, value):
        browser.element('html').should(have.text(value))