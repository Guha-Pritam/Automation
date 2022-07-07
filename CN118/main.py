import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.CN118 import CN118_const as CN
from Projects.Common_function import common
import Projects.constants as CS

pdf = FPDF()
CF = common()


class CN118:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def header_function(self):
        CF.login_and_connect(CN.BOARD_NAME)
        time.sleep(5)
        connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
        if "Ready" in connectText.text:
            CF.click_button(CS.live_button)
            CF.write_header(pdf, 'CN118')
            CF.wait_until_progress("SYSTEM READY")
            time.sleep(15)
            CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
            time.sleep(15)
            CF.update_progress_log(pdf)
            CF
            CF.take_image(pdf, CN.LIVE_VIDEO_PATH,
                          'D:\\Automation\\Projects\\screenshot\\LIVE_video.png',
                          'LIVE_video.png')
