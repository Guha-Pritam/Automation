import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.CN243 import CN243_const as CN
from Projects.Common_function import common
import Projects.constants as CS

pdf = FPDF()
CF = common()


class CN243:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def header_function(self):
        CF.login_and_connect(CN.board_name)
        time.sleep(5)
        connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
        if "Ready" in connectText.text:
            CF.click_button(CS.live_button)
            CF.write_header(pdf, 'CN243')
            CF.wait_until_progress("SYSTEM READY")
            time.sleep(15)
            CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
            time.sleep(10)
            CF.update_progress_log(pdf)
            CF.click_button(CN.I_AGREE_BUTTON)
            CF.take_image(pdf, CN.DISPLAY_VIDEO_PATH,
                          'D:\\Automation\\Projects\\screenshot\\display_video.png',
                          'display_video.png')
            CF.take_image(pdf, CN.LIVE_VIDEO_PATH,
                          'D:\\Automation\\Projects\\screenshot\\live_video.png',
                          'live_video.png')

    def rgb_common_function(self):
        CF.slider(CN.RED_LED_PATH)
        CF.wait_until_progress("[ RED: 210 | GREEN: 0 | BLUE: 0 | ] set.")
        CF.write_result(pdf, 'RED-LED : ', '[ RED: 210 | GREEN: 0 | BLUE: 0 | ] set.')
        time.sleep(8)

        CF.take_image(pdf, CN.DISPLAY_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\RED_display_video.png',
                      'RED_display_video.png')
        CF.take_image(pdf, CN.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\RED_live_video.png',
                      'RED_live_video.png')
        CF.take_image(pdf, CN.LIVE_PARAMETER_XPATH,
                      'D:\\Automation\\Projects\\screenshot\\Live_parameter_video.png',
                      'Live_parameter_video.png')
        CF.slider_reverse(CN.RED_LED_PATH)
        time.sleep(5)
        CF.update_progress_log(pdf)

        # STARTING GREEN--LED FUNCTION
        CF.slider(CN.GREEN_LED_PATH)
        CF.wait_until_progress("[ RED: 0 | GREEN: 210 | BLUE: 0 | ] set.")
        CF.write_result(pdf, 'GREEN-LED : ', '[ RED: 0 | GREEN: 210 | BLUE: 0 | ] set.')
        time.sleep(8)

        CF.take_image(pdf, CN.DISPLAY_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\GREEN_display_video.png',
                      'GREEN_display_video.png')
        CF.take_image(pdf, CN.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\GREEN_live_video.png',
                      'GREEN_live_video.png')
        CF.take_image(pdf, CN.LIVE_PARAMETER_XPATH,
                      'D:\\Automation\\Projects\\screenshot\\G-Live_parameter_video.png',
                      'G-Live_parameter_video.png')
        CF.slider_reverse(CN.GREEN_LED_PATH)
        time.sleep(5)
        CF.update_progress_log(pdf)

        # STARTING BLUE--LED FUNCTION
        CF.slider(CN.BLUE_LED_PATH)
        CF.wait_until_progress("[ RED: 0 | GREEN: 0 | BLUE: 210 | ] set.")
        CF.write_result(pdf, 'BLUE-LED : ', '[ RED: 0 | GREEN: 0 | BLUE: 210 | ] set.')
        time.sleep(8)

        CF.take_image(pdf, CN.DISPLAY_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\BLUE_display_video.png',
                      'BLUE_display_video.png')
        CF.take_image(pdf, CN.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\BLUE_live_video.png',
                      'BLUE_live_video.png')
        CF.take_image(pdf, CN.LIVE_PARAMETER_XPATH,
                      'D:\\Automation\\Projects\\screenshot\\B-Live_parameter_video.png',
                      'B-Live_parameter_video.png')
        CF.slider_reverse(CN.BLUE_LED_PATH)
        time.sleep(5)
        CF.update_progress_log(pdf)

    def disconnected_rgb_function(self):
        CN243.header_function(self)

        CF.wait_until_progress("SYSTEM READY")
        CF.write_result(pdf, 'DISCONNECTED-RGB-FUNCTION : ', 'START EVALUATING')
        CN243.rgb_common_function(self)

    def connected_rgb_function(self):
        pdf.add_page()
        CN243.disconnected_rgb_function(self)
        CF.click_button(CN.RGB_CONNECTED_BUTTON)
        time.sleep(5)

        CF.wait_until_progress("Sensor is Connected to RGB Application")
        CF.write_result(pdf, 'CONNECTED-RGB-FUNCTION : ', 'START EVALUATING')

        # STARTING INTENSITY--LED FUNCTION
        CF.slider(CN.RED_LED_PATH)
        time.sleep(5)
        CF.slider(CN.GREEN_LED_PATH)
        time.sleep(5)
        CF.slider(CN.BLUE_LED_PATH)
        time.sleep(5)
        CF.take_image(pdf, CN.DISPLAY_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\Pre_INTENSITY_display_video.png',
                      'Pre_INTENSITY_display_video.png')
        CF.take_image(pdf, CN.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\Pre_INTENSITY_live_video.png',
                      'Pre_INTENSITY_live_video.png')
        CF.take_image(pdf, CN.LIVE_PARAMETER_XPATH,
                      'D:\\Automation\\Projects\\screenshot\\Pre_I-Live_parameter_video.png',
                      'Pre_I-Live_parameter_video.png')
        CF.update_progress_log(pdf)

        Slider = CF.driver.find_element(By.XPATH, CN.INTENSITY_PATH)
        CF.actions.drag_and_drop_by_offset(Slider, 0, 90).perform()

        CF.wait_until_connection_path()
        CF.write_result(pdf, 'INTENSITY : ', 'START EVALUATING')
        time.sleep(8)

        CF.take_image(pdf, CN.DISPLAY_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\INTENSITY_display_video.png',
                      'INTENSITY_display_video.png')
        CF.take_image(pdf, CN.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\INTENSITY_live_video.png',
                      'INTENSITY_live_video.png')
        CF.take_image(pdf, CN.LIVE_PARAMETER_XPATH,
                      'D:\\Automation\\Projects\\screenshot\\I-Live_parameter_video.png',
                      'I-Live_parameter_video.png')
        time.sleep(5)
        CF.update_progress_log(pdf)

        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('CN243_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()


if __name__ == "__main__":
    stu = CN243()
    stu.disconnected_rgb_function()
    stu.connected_rgb_function()
