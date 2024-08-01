import time
from pageObjects.item_page import Selection
from utilities.readProperties import Read_config


class Test001:
    Base_URL = Read_config.getApplication_Url()

    def test_item(self, setup):
        self.driver = setup
        self.driver.get(self.Base_URL)
        time.sleep(20)
        self.lp = Selection(self.driver)
        self.lp.selecting_items()
        self.lp.switching_window()
        self.lp.item_added_to_cart()
        self.lp.proceed_to_payment()

        self.driver.close()
