import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.CN300 import CN300_const as CN
from Projects.Common_function import common
import Projects.constants as CS

pdf = FPDF()
CF = common()


def header_function():
    CF.old_login_connect(CN.board_name)
    CF.wait_until_progress("START EVALUATING")
    connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
    if "Ready" in connectText.text:
        CF.write_header(pdf, 'CN300')
        CF.wait_until_progress("START EVALUATING")
        # GOING LIVE VIDEO
        hover = CF.driver.find_element(By.XPATH, CS.old_live_video_xpath)
        CF.actions.move_to_element(hover).perform()

        CF.driver.implicitly_wait(0.5)
        CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, CS.old_switch_to_frame))
        CF.wait_until_clickable(CS.old_refresh_button)
        time.sleep(6)
        print('Clicked REFRESH button')

        CF.driver.switch_to.parent_frame()
        CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
        CF.old_update_progress_log(pdf)
        time.sleep(5)
        CF.take_image(pdf, CS.old_live_video_xpath,
                      'D:\\Automation\\Projects\\screenshot\\live_image.png',
                      'live_image.png')


class CN300:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def full_function(self):
        pdf.add_page()
        header_function()
        time.sleep(5)
        CF.write_result(pdf, 'Full-function : ', 'SYSTEM READY')
        hover = CF.driver.find_element(By.XPATH, CS.old_connection_path)
        CF.actions.move_to_element(hover).perform()
        print('click outside')
        CF.click_button(CN.load_current_path)
        CF.click_button(CN.set_load_current)
        time.sleep(3)
        CF.click_button(CN.start_button)
        CF.wait_until_old_connection_path()
        hover = CF.driver.find_element(By.XPATH, CS.old_live_video_xpath)
        CF.actions.move_to_element(hover).perform()
        CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, CS.old_switch_to_frame))

        CF.driver.switch_to.parent_frame()

        CF.take_image(pdf, CS.old_live_video_xpath,
                      'D:\\Automation\\Projects\\screenshot\\Full_live_image.png',
                      'Full_live_image.png')
        time.sleep(5)
        CF.click_button(CN.maximize_graph)
        time.sleep(5)
        CF.take_image(pdf, CN.graph_path, 'D:\\Automation\\Projects\\screenshot\\graph.png',
                      'graph.png')
        CF.click_button(CN.maximize_graph)
        CF.old_update_progress_log(pdf)
        CF.wait_until_old_progress('Discharge is Complete')

        CF.write_result(pdf, 'Information--Data : ', 'Discharge is Complete')
        time.sleep(5)
        CF.click_button(CN.maximize_graph)
        time.sleep(5)
        CF.take_image(pdf, CN.graph_path, 'D:\\Automation\\Projects\\screenshot\\graph1.png',
                      'graph1.png')
        CF.click_button(CN.maximize_graph)

        CF.take_image(pdf, CN.capacitor_path, 'D:\\Automation\\Projects\\screenshot\\voltage.png',
                      'voltage.png')
        time.sleep(5)

        CF.old_take_information(pdf)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('CN300_result.pdf')
        CF.click_button(CS.off_old_connect_button)
        CF.driver.close()


if __name__ == "__main__":
    stu = CN300()
    stu.full_function()
