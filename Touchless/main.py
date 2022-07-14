import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.Touchless import touchless_const as TC
from selenium.webdriver.support import expected_conditions as EC
from Projects.Common_function import common
import Projects.constants as CS


pdf = FPDF()
CF = common()


class TouchLess:
    def __int__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def header_function(self):
        CF.driver.get('https://renesas.evmlabs.com/user/form624fdb5bc555b02c8c23cc7d?APP=5f12f3d2c555b026c55ae500')
        time.sleep(5)
        pdf.add_page()
        CF.click_button(CS.Connect_Button)
        CF.wait_until_connection_path()
        connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
        if "Ready" in connectText.text:
            CF.click_button(CS.live_button)
            CF.write_header(pdf, 'CN118')
            CF.wait_until_progress("SYSTEM READY")
            time.sleep(15)
            CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
            CF.update_progress_log(pdf)

            buttons = CF.driver.find_element(By.XPATH, '//*[@id="e070dc25-3c08-1b76-d911-e40a39f1b1b9"]/div/tx-elements/div[2]/table/tbody/tr[1]').find_element(By.TAG_NAME, 'td')
            for i in range(15):
                buttons.click()

            pdf.set_font("Arial", 'B', size=12)
            pdf.output('Touchless_result.pdf')


if __name__ == "__main__":
    stu = TouchLess()
    stu.header_function()
