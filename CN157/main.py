import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
import CN157_const as CN
from Common_function import common
import constants as CS

pdf = FPDF()
CF = common()


def header_function():
    CF.old_login_connect(CN.board_name)
    CF.wait_until_progress("START EVALUATING")
    connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
    if "Ready" in connectText.text:
        CF.write_header(pdf, 'CN157')
        CF.wait_until_old_progress("START EVALUATING")
        CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, CN.iframe))
        time.sleep(5)
        CF.wait_until_clickable(CN.continue_button)
        print('vvvvv')

        CF.driver.switch_to.parent_frame()
        time.sleep(10)
        CF.write_result(pdf, 'Connection : ', 'SYSTEM READY')
        time.sleep(5)
        CF.old_update_progress_log(pdf)
        time.sleep(5)
        CF.take_image(pdf, CN.iframe,
                      'D:\\Automation\\Projects\\CN157\\screenshot\\live_image.png',
                      'live_image.png')
        time.sleep(5)


class CN157:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def manual_testing(self):
        pdf.add_page()
        header_function()
        time.sleep(5)
        CF.old_write_result(pdf, 'Manual_testing : ', 'SYSTEM READY')
        CF.click_button(CN.manual_apply_button)
        CF.wait_until_old_progress('Light Intensity set to 0%')
        time.sleep(3)
        CF.take_image(pdf, CN.iframe,
                      'D:\\Automation\\Projects\\CN157\\screenshot\\manual_0%.png',
                      'manual_0%.png')
        time.sleep(5)
        slider = CF.driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div/div['
                                        '2]/div/div/div/div/div/ul/li[1]/div/div/tx-elements/div['
                                        '2]/div/div/form/tx-elements[1]/div[2]/div/div/div[3]/span[5]')
        CF.actions.move_to_element(slider).pause(1).click_and_hold(slider).move_by_offset(100, 0). \
            release().perform()
        time.sleep(5)
        CF.click_button(CN.manual_apply_button)
        CF.wait_until_old_progress('Light Intensity set to 56%')
        time.sleep(3)
        CF.take_image(pdf, CN.iframe,
                      'D:\\Automation\\Projects\\CN157\\screenshot\\manual_56%.png',
                      'manual_56%.png')
        time.sleep(5)
        CF.actions.move_to_element(slider).pause(1).click_and_hold(slider).move_by_offset(180, 0). \
            release().perform()
        time.sleep(5)
        CF.click_button(CN.manual_apply_button)
        CF.wait_until_old_progress('Light Intensity set to 100%')
        time.sleep(3)
        CF.take_image(pdf, CN.iframe,
                      'D:\\Automation\\Projects\\CN157\\screenshot\\manual_95%.png',
                      'manual_95%.png')
        time.sleep(5)
        CF.old_update_progress_log(pdf)
        time.sleep(3)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')
        pdf.output('CN157_result.pdf')
        CF.click_button(CS.old_connect_button)
        CF.driver.close()

    def auto_testing(self):
        pdf.add_page()
        header_function()
        time.sleep(5)
        CF.old_write_result(pdf, 'Auto_testing : ', 'SYSTEM READY')
        time.sleep(5)
        CF.click_button(CN.auto_apply_button)
        CF.wait_until_old_progress('Light Intensity set to 10%')
        CF.take_image(pdf, CN.iframe,
                      'D:\\Automation\\Projects\\CN157\\screenshot\\auto_10%.png',
                      'auto_10%.png')
        CF.wait_until_old_progress('Light Intensity set to 20%')
        # CF.old_write_result(pdf, 'Image : ', 'Auto Mode')
        CF.take_image(pdf, CN.iframe,
                      'D:\\Automation\\Projects\\CN157\\screenshot\\auto_20%.png',
                      'auto_20%.png')
        CF.wait_until_old_progress('Light Intensity set to 30%')
        CF.take_image(pdf, CN.iframe,
                      'D:\\Automation\\Projects\\CN157\\screenshot\\auto_30%.png',
                      'auto_30%.png')
        CF.wait_until_old_progress('Light Intensity set to 40%')
        CF.take_image(pdf, CN.iframe,
                      'D:\\Automation\\Projects\\CN157\\screenshot\\auto_40%.png',
                      'auto_40%.png')
        CF.wait_until_old_progress('Light Intensity set to 50%')
        CF.take_image(pdf, CN.iframe,
                      'D:\\Automation\\Projects\\CN157\\screenshot\\auto_50%.png',
                      'auto_50%.png')
        time.sleep(5)
        CF.old_update_progress_log(pdf)
        time.sleep(3)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')
        pdf.output('CN157_result.pdf')
        CF.click_button(CS.old_connect_button)
        CF.driver.close()


if __name__ == "__main__":
    stu = CN157()
    stu.manual_testing()
    stu.auto_testing()
