import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.CN299 import CN299_const as CN
from Projects.Common_function import common
import Projects.constants as CS

pdf = FPDF()
CF = common()


def header_function():
    CF.old_login_connect(CN.board_name)
    CF.wait_until_progress("START EVALUATING")
    connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
    if "Ready" in connectText.text:
        CF.write_header(pdf, 'CN299-1')
        CF.wait_until_progress("START EVALUATING")
        CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
        time.sleep(5)
        CF.old_update_progress_log(pdf)
        # GOING LIVE VIDEO
        hover = CF.driver.find_element(By.XPATH, CS.old_live_video_xpath)
        CF.actions.move_to_element(hover).perform()

        CF.driver.implicitly_wait(0.5)
        CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, CS.old_switch_to_frame))
        CF.wait_until_clickable(CS.old_refresh_button)
        time.sleep(5)
        print('vvvvv')

        CF.driver.switch_to.parent_frame()
        CF.take_image(pdf, CS.old_live_video_xpath,
                      'D:\\Automation\\Projects\\screenshot\\live_image.png',
                      'live_image.png')


class CN299:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def maximize_voltage(self):
        pdf.add_page()
        header_function()
        time.sleep(5)
        hover = CF.driver.find_element(By.XPATH, CS.old_connection_path)
        CF.actions.move_to_element(hover).perform()
        print('hover')
        CF.click_button(CN.old_output_voltage)
        CF.click_button(CN.old_5V_voltage)
        time.sleep(5)
        CF.click_button(CN.old_set_button)
        CF.wait_until_progress('Input Voltage, Output Voltage and VLDO read from board is successful')
        time.sleep(5)
        CF.click_button(CN.maximize_graph_path)
        time.sleep(5)
        CF.write_result(pdf, '5V value coming : ', 'Input Voltage, Output Voltage and VLDO read from board is '
                                                   'successful')
        CF.take_image(pdf, CN.graph_path, 'D:\\Automation\\Projects\\screenshot\\graph.png',
                      'graph.png')
        CF.click_button(CN.maximize_graph_path)
        CF.old_update_progress_log(pdf)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('CN299_result.pdf')
        CF.click_button(CS.off_old_connect_button)
        CF.driver.close()


if __name__ == "__main__":
    stu = CN299()
    stu.maximize_voltage()
