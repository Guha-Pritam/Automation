import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.EU084 import EU084_const as EU
from Projects.Common_function import common
import Projects.constants as CS

pdf = FPDF()
CF = common()


def header_function():
    CF.old_login_connect(EU.board_name)
    CF.wait_until_progress("START EVALUATING")
    connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
    if "Ready" in connectText.text:
        CF.write_header(pdf, 'EU084')
        CF.wait_until_old_progress("START EVALUATING")
        CF.write_result(pdf, 'Connection : ', 'SYSTEM READY')
        CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, EU.iframe))
        time.sleep(5)
        CF.wait_until_clickable(EU.continue_button)
        print('Click CONTINUE button')

        CF.driver.switch_to.parent_frame()
        time.sleep(10)
        CF.old_update_progress_log(pdf)
        time.sleep(5)
        CF.take_image(pdf, EU.iframe,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\live_image.png',
                      'live_image.png')
        time.sleep(5)


class EU084:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def auto_mode(self):
        pdf.add_page()
        header_function()
        CF.click_button(EU.LCD_backlight_button)
        time.sleep(5)
        CF.take_image(pdf, EU.iframe,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\live_video.png',
                      'live_video.png')
        time.sleep(3)
        CF.click_button(EU.temp_limit_path)
        CF.click_button(EU.set_temp_limit)
        time.sleep(3)
        CF.click_button(EU.auto_mode_path)
        CF.old_write_result(pdf, 'Auto_Mode_testing : ', 'SYSTEM READY')
        CF.click_button(EU.set_auto_mode)
        time.sleep(3)
        CF.click_button(EU.start_temp_mode_path)
        CF.click_button(EU.set_start_temp)
        time.sleep(3)
        CF.click_button(EU.end_temp_mode_path)
        CF.click_button(EU.set_end_temp)
        time.sleep(3)
        CF.click_button(EU.start_button)
        CF.wait_until_old_connection_path()
        CF.take_image(pdf, EU.iframe,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\auto_video.png',
                      'auto_video.png')
        time.sleep(15)
        CF.click_button(EU.maximize_graph)
        time.sleep(5)
        CF.take_image(pdf, EU.graph_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\auto_graph.png',
                      'auto_graph.png')
        time.sleep(5)
        CF.click_button(EU.maximize_graph)
        time.sleep(5)
        CF.old_update_progress_log(pdf)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('EU084_result.pdf')
        CF.click_button(CS.off_old_connect_button)
        CF.driver.close()

    def manual_mode(self):
        pdf.add_page()
        header_function()
        CF.click_button(EU.LCD_backlight_button)
        time.sleep(5)
        CF.take_image(pdf, EU.iframe,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\manual_live_video.png',
                      'manual_live_video.png')
        time.sleep(3)
        CF.click_button(EU.temp_limit_path)
        CF.click_button(EU.set_temp_limit)
        time.sleep(3)
        CF.click_button(EU.auto_mode_path)
        CF.old_write_result(pdf, 'Manual_Mode_testing : ', 'SYSTEM READY')
        CF.click_button(EU.set_manual_mode)
        slider = CF.driver.find_element(By.XPATH, EU.slider_button_path)
        CF.actions.move_to_element(slider).pause(1).click_and_hold(slider).move_by_offset(170, 0). \
            release().perform()
        time.sleep(3)
        CF.click_button(EU.set_button)
        CF.wait_until_old_connection_path()
        CF.take_image(pdf, EU.iframe,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\manual_video.png',
                      'manual_video.png')
        time.sleep(15)
        CF.click_button(EU.maximize_graph)
        time.sleep(5)
        CF.take_image(pdf, EU.graph_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\manual_graph.png',
                      'manual_graph.png')
        CF.click_button(EU.maximize_graph)
        time.sleep(5)
        CF.old_update_progress_log(pdf)
        time.sleep(5)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('EU084_result.pdf')
        CF.click_button(CS.off_old_connect_button)
        CF.driver.close()


if __name__ == "__main__":
    stu = EU084()
    stu.auto_mode()
    stu.manual_mode()
