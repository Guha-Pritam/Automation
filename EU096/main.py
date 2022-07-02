import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.EU096 import EU096_const as EU
from Projects.Common_function import common
import Projects.constants as CS

pdf = FPDF()
CF = common()


def header_function():
    CF.old_login_connect(EU.board_name)
    CF.wait_until_progress("START EVALUATING")
    connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
    if "Ready" in connectText.text:
        CF.write_header(pdf, 'EU096')
        CF.wait_until_old_progress("START EVALUATING")
        # GOING LIVE VIDEO
        hover = CF.driver.find_element(By.XPATH, CS.old_live_video_xpath)
        CF.actions.move_to_element(hover).perform()

        CF.driver.implicitly_wait(0.5)
        CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, CS.old_switch_to_frame))
        CF.wait_until_clickable(CS.old_refresh_button)
        time.sleep(10)
        print('Clicked REFRESH button')

        CF.driver.switch_to.parent_frame()
        CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
        CF.old_update_progress_log(pdf)
        CF.take_image(pdf, CS.old_live_video_xpath,
                      'D:\\Automation\\Projects\\screenshot\\live_image.png',
                      'live_image.png')


class EU096:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def full_function(self):
        pdf.add_page()
        header_function()
        time.sleep(5)
        CF.write_result(pdf, 'ON_Time-function : ', 'SYSTEM READY')
        hover = CF.driver.find_element(By.XPATH, CS.old_connection_path)
        CF.actions.move_to_element(hover).perform()
        print('click outside')

        CF.click_button(EU.t0_path)
        t0_send_keys = CF.driver.find_element(By.XPATH, EU.t0_input_path)
        t0_send_keys.send_keys(EU.t0_keys)
        time.sleep(5)

        CF.click_button(EU.t1_path)
        t1_send_keys = CF.driver.find_element(By.XPATH, EU.t1_input_path)
        t1_send_keys.send_keys(EU.t1_keys)
        time.sleep(5)

        CF.click_button(EU.set_button)
        CF.wait_until_old_progress('Configured board with ON delay timer')
        time.sleep(5)
        CF.take_image(pdf, EU.graph_path,
                      'D:\\Automation\\Projects\\screenshot\\graph_set.png',
                      'graph_set.png')
        time.sleep(3)
        CF.old_update_progress_log(pdf)
        time.sleep(5)

        CF.click_button(EU.power_off_button)
        CF.wait_until_old_progress('Power OFF delay waveforms are captured')
        time.sleep(5)
        CF.take_image(pdf, EU.graph_path,
                      'D:\\Automation\\Projects\\screenshot\\graph_power_off.png',
                      'graph_power_off.png')
        time.sleep(3)
        CF.old_update_progress_log(pdf)
        time.sleep(5)

        CF.click_button(EU.power_on_button)
        CF.wait_until_old_progress('Power ON delay waveforms are captured')
        time.sleep(5)
        CF.take_image(pdf, EU.graph_path,
                      'D:\\Automation\\Projects\\screenshot\\graph_power_on.png',
                      'graph_power_on.png')
        time.sleep(3)
        CF.old_update_progress_log(pdf)
        time.sleep(5)

        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('EU096_result.pdf')
        CF.click_button(CS.off_old_connect_button)
        CF.driver.close()


if __name__ == "__main__":
    stu = EU096()
    stu.full_function()
