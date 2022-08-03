import time
import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class WorkflowyScheduler(object):
    workflowy_url = "https://workflowy.com"
    browser = webdriver.Chrome()

    @classmethod
    def schedule_items_for_today(self):
        todays_date_tag = self.__get_todays_date_tag()

        self.browser.get(self.workflowy_url)

        self.__login()
        self.__search(todays_date_tag)
        self.__mark_results_with_tag("#Focus")
        self.__save_changes()

        self.browser.close()

    @classmethod
    def __login(self):
        self.__click_button("div.header-bar a.button--top-right")
        self.__wait_for_element_to_appear("#id_username")
        self.__fill_text_box("#id_username", settings.workflowy_username)
        self.__fill_text_box("#id_password", settings.workflowy_password)
        self.__click_button("input.button--submit")

    @classmethod
    def __search(self, search_term: str):
        self.__wait_for_element_to_appear("#searchBox")
        self.__fill_text_box("#searchBox", search_term)

    @classmethod
    def __mark_results_with_tag(self, tag: str):
        for element in self.browser.find_elements_by_css_selector("div.name.matches"):
            text = element.text
            if tag not in text:
                text_box = element.find_element_by_css_selector("div.content")
                text_box.click()
                text_box.send_keys(Keys.END)
                text_box.send_keys(" " + tag)

    @classmethod
    def __save_changes(self):
        self.browser.find_element_by_css_selector("div.saveButton").click()
        self.__wait_for_element_to_appear("div.saveButton.saved")

    @classmethod
    def __click_button(self, css_selector: str):
        self.browser.find_element_by_css_selector(css_selector).click()

    @classmethod
    def __wait_for_element_to_appear(self, css_selector):
        WebDriverWait(self.browser, 10).until(lambda driver: driver.find_element_by_css_selector(css_selector))

    @classmethod
    def __fill_text_box(self, css_selector: str, text_to_input: str):
        self.browser.find_element_by_css_selector(css_selector).send_keys(text_to_input)

    @classmethod
    def __get_todays_date_tag(self) -> str:
        return "#%s" % time.strftime("%Y-%m-%d")


if __name__ == "__main__":
    WorkflowyScheduler.schedule_items_for_today()
