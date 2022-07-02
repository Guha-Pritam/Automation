import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.AS104 import AS104_const as AS
from Projects.Common_function import common
import Projects.constants as CS

pdf = FPDF()
CF = common()


def header_function():
    CF.old_login_connect(AS.board_name)
    CF.wait_until_progress("START EVALUATING")
    connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
    if "Ready" in connectText.text:
        CF.write_header(pdf, 'AS104')
        CF.wait_until_old_progress("START EVALUATING")
        CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
        time.sleep(5)
        CF.old_update_progress_log(pdf)
        time.sleep(5)
        # GOING LIVE VIDEO
        hover = CF.driver.find_element(By.XPATH, CS.old_live_video_xpath)
        CF.actions.move_to_element(hover).perform()

        CF.driver.implicitly_wait(0.5)
        CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, CS.old_switch_to_frame))
        CF.wait_until_clickable(CS.old_refresh_button)
        time.sleep(8)
        print('[|| CLICKED ||]-- REFRESH button')

        CF.driver.switch_to.parent_frame()
        CF.take_image(pdf, CS.old_live_video_xpath,
                      'D:\\Automation\\Projects\\gmail_login\\screenshot\\live_image.png',
                      'live_image.png')
        time.sleep(3)


class AS104:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def config_function(self):
        pdf.add_page()
        header_function()
        time.sleep(5)

        hover = CF.driver.find_element(By.XPATH, CS.old_connection_path)
        CF.actions.move_to_element(hover).perform()
        print('[ || HOVER OUTSIDE ||]')

        CF.click_button(AS.config_start_button)
        CF.wait_until_old_progress('Board Reset - Kindly restart the evaluation')
        CF.write_result(pdf, 'Config-Function : ', 'Board Reset - Kindly restart the evaluation')
        time.sleep(5)

        CF.take_image(pdf, AS.graph_path,
                      'D:\\Automation\\Projects\\gmail_login\\screenshot\\graph_config_AS104.png',
                      'graph_config_AS104.png')

        CF.take_image(pdf, AS.system_status_path,
                      'D:\\Automation\\Projects\\gmail_login\\screenshot\\system_config_AS104.png',
                      'system_config_AS104.png')
        time.sleep(5)
        CF.old_update_progress_log(pdf)
        time.sleep(5)

        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('AS104_result.pdf')
        CF.click_button(CS.off_old_connect_button)
        CF.driver.close()

    def in_rush(self):
        pdf.add_page()
        header_function()
        time.sleep(5)

        hover = CF.driver.find_element(By.XPATH, CS.old_connection_path)
        CF.actions.move_to_element(hover).perform()
        print('[ || HOVER OUTSIDE ||]')

        CF.write_result(pdf, 'IN--Rush : ', 'SYSTEM READY')

        CF.click_button(AS.in_rush_path)
        time.sleep(3)
        CF.click_button(AS.three_W_path)
        time.sleep(3)
        CF.click_button(AS.load_power_path)
        CF.click_button(AS.set_load_power)
        time.sleep(2)
        CF.click_button(AS.duration_sec_path)
        CF.click_button(AS.set_duration_sec)
        CF.click_button(AS.start_button)
        time.sleep(5)
        CF.wait_until_old_progress('Battery Disconnected')
        CF.take_image(pdf, AS.graph_path,
                      'D:\\Automation\\Projects\\gmail_login\\screenshot\\graph_rush_AS104.png',
                      'graph_rush_AS104.png')

        CF.take_image(pdf, AS.system_status_path,
                      'D:\\Automation\\Projects\\gmail_login\\screenshot\\system_rush_AS104.png',
                      'system_rush_AS104.png')
        time.sleep(5)
        CF.old_update_progress_log(pdf)

        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('AS104_result.pdf')
        CF.click_button(CS.off_old_connect_button)
        CF.driver.close()


if __name__ == "__main__":
    stu = AS104()
    stu.config_function()
    # stu.in_rush()
