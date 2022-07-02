import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.EU065 import EU065_const as EU
from Projects.Common_function import common
import Projects.constants as CS

pdf = FPDF()
CF = common()


def header_function():
    CF.old_login_connect(EU.board_name)
    CF.wait_until_progress("START EVALUATING")
    connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
    if "Ready" in connectText.text:
        CF.write_header(pdf, 'EU065')
        CF.wait_until_old_progress("START EVALUATING")
        CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, EU.iframe))
        time.sleep(5)
        CF.wait_until_clickable(EU.continue_button)
        print('Click CONTINUE button')

        CF.driver.switch_to.parent_frame()
        time.sleep(10)
        CF.write_result(pdf, 'Connection : ', 'SYSTEM READY')
        CF.old_update_progress_log(pdf)
        CF.take_image(pdf, EU.iframe,
                      'D:\\Automation\\Projects\\screenshot\\live_image.png',
                      'live_image.png')
        time.sleep(5)


class EU065:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def light_control_function(self):
        pdf.add_page()
        header_function()
        CF.write_result(pdf, 'Light-Control-Function : ', 'SYSTEM READY')
        time.sleep(5)
        CF.take_image(pdf, EU.iframe,
                      'D:\\Automation\\Projects\\screenshot\\pre_forward_live.png',
                      'pre_forward_live.png')
        time.sleep(5)
        slider = CF.driver.find_element(By.XPATH, EU.slider_button)
        CF.actions.move_to_element(slider).pause(1).click_and_hold(slider).move_by_offset(100, 0). \
            release().perform()
        time.sleep(5)
        CF.click_button(EU.time_flight_on_button)
        time.sleep(3)
        CF.click_button(EU.forward_button)
        CF.click_button(EU.apply_button)
        CF.wait_until_old_progress('Moved forward')
        CF.take_image(pdf, EU.iframe,
                      'D:\\Automation\\Projects\\screenshot\\after_forward_live.png',
                      'after_forward_live.png')
        time.sleep(3)
        CF.old_update_progress_log(pdf)
        time.sleep(3)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')
        pdf.output('EU065_result.pdf')
        CF.click_button(CS.off_old_connect_button)
        CF.driver.close()

    def RGB_control_function(self):
        pdf.add_page()
        header_function()
        CF.write_result(pdf, 'RGB-Control-Function : ', 'SYSTEM READY')
        time.sleep(5)
        CF.take_image(pdf, EU.iframe,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\pre_RGB_live.png',
                      'pre_RGB_live.png')
        time.sleep(5)
        CF.click_button(EU.control_path)
        CF.click_button(EU.RGB_path)
        R_slider = CF.driver.find_element(By.XPATH, EU.R_path)
        CF.actions.move_to_element(R_slider).pause(1).click_and_hold(R_slider). \
            move_by_offset(150, 0).release().perform()

        G_slider = CF.driver.find_element(By.XPATH, EU.G_path)
        CF.actions.move_to_element(G_slider).pause(1).click_and_hold(G_slider). \
            move_by_offset(150, 0).release().perform()

        B_slider = CF.driver.find_element(By.XPATH, EU.B_path)
        CF.actions.move_to_element(B_slider).pause(1).click_and_hold(B_slider). \
            move_by_offset(150, 0).release().perform()
        time.sleep(3)
        CF.click_button(EU.time_flight_on_button)
        CF.click_button(EU.reverse_button)
        time.sleep(3)
        CF.click_button(EU.apply_button)
        CF.wait_until_old_progress('Moved reverse')
        CF.take_image(pdf, EU.iframe,
                      'D:\\Automation\\Projects\\screenshot\\after_RGB_live.png',
                      'after_RGB_live.png')
        time.sleep(3)
        CF.old_update_progress_log(pdf)
        time.sleep(3)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('EU065_result.pdf')
        CF.click_button(CS.off_old_connect_button)
        CF.driver.close()


if __name__ == "__main__":
    stu = EU065()
    stu.light_control_function()
    stu.RGB_control_function()
