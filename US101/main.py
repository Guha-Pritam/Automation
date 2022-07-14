import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.US101 import US101_const as US
from Projects.Common_function import common
import Projects.constants as CS
# import pyautogui

pdf = FPDF()
CF = common()


def header_function():
    CF.old_login_connect(US.board_name)
    CF.wait_until_old_progress("Initializing Completed")
    connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
    if "Ready" in connectText.text:
        CF.write_header(pdf, 'US101')
        time.sleep(5)
        # GOING LIVE VIDEO
        hover = CF.driver.find_element(By.XPATH, CS.old_live_video_xpath)
        CF.actions.move_to_element(hover).perform()

        CF.driver.implicitly_wait(0.5)
        CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, CS.old_switch_to_frame))
        CF.wait_until_clickable(CS.old_refresh_button)
        print('Clicked REFRESH button')

        CF.driver.switch_to.parent_frame()
        time.sleep(8)
        CF.write_result(pdf, 'Connection : ', 'Initializing Completed')
        time.sleep(5)
        CF.old_update_progress_log(pdf)
        time.sleep(3)
        CF.take_image(pdf, CS.old_live_video_xpath,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\US101_hover_image.png',
                      'US101_hover_image.png')
        hover = CF.driver.find_element(By.XPATH, CS.old_connection_path)
        CF.actions.move_to_element(hover).perform()

        CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, US.iframe))
        time.sleep(5)
        CF.wait_until_clickable(US.continue_button)
        time.sleep(10)
        print('Click CONTINUE button')

        CF.driver.switch_to.parent_frame()
        CF.take_image(pdf, US.iframe,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\US101_live_image.png',
                      'US101_live_image.png')
        time.sleep(5)


class US101:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def object_detection_function(self):
        pdf.add_page()
        header_function()
        time.sleep(5)
        CF.write_result(pdf, 'Object-Detection-Function : ', 'Initializing Completed')
        CF.click_button(US.object_detection_button)
        time.sleep(5)
        CF.take_image(pdf, US.iframe,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\object_detection_cam.png',
                      'object_detection_cam.png')
        time.sleep(3)
        CF.old_update_progress_log(pdf)
        time.sleep(3)

        CF.click_button(US.option_selection_button)
        CF.click_button(US.web_cam_path)
        CF.click_button(US.start_button)
        time.sleep(25)

        # pyautogui.click('Allow button.png')

        CF.wait_until_old_progress('slowly, for the object to get recongnized by the SMARC')
        time.sleep(45)
        CF.write_result(pdf, 'Web-Camera-Function : ', 'slowly, for the object to get recongnized by the SMARC')
        CF.take_image(pdf, US.iframe,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\object_web_cam.png',
                      'object_web_cam.png')
        time.sleep(3)
        CF.old_update_progress_log(pdf)
        time.sleep(3)

        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('US101_result.pdf')
        CF.click_button(CS.off_old_connect_button)
        CF.driver.close()

    def four_K_playback_function(self):
        pdf.add_page()
        header_function()
        time.sleep(5)
        CF.write_result(pdf, 'Four-K-Playback-Function : ', 'Initializing Completed')

        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('US101_result.pdf')
        CF.click_button(CS.off_old_connect_button)
        CF.driver.close()


if __name__ == "__main__":
    stu = US101()
    stu.object_detection_function()
    stu.four_K_playback_function()
