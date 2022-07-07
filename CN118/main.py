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
            CF.update_progress_log(pdf)
            CF.click_button(CN.MAXIMIZE_LIVE_VIDEO)
            time.sleep(5)
            CF.take_image(pdf, CN.LIVE_VIDEO_PATH,
                          'D:\\Automation\\Projects\\screenshot\\LIVE_video.png',
                          'LIVE_video.png')
            time.sleep(3)
            CF.click_button(CN.MAXIMIZE_LIVE_VIDEO)
            CF.take_image(pdf, CN.GRAPH_PATH,
                          'D:\\Automation\\Projects\\screenshot\\GRAPH_video.png',
                          'GRAPH_video.png')

    def mini_power_monitor_function(self):
        pdf.add_page()
        CN118.header_function(self)

        CF.click_button(CN.INDUCTIVE_LOAD_BUTTON)
        time.sleep(5)
        CF.write_result(pdf, 'INDUCTIVE_LOAD_BUTTON : ', '$> Load one is ON')
        CF.wait_until_progress('$> Load one is ON')
        CF.click_button(CN.MAXIMIZE_LIVE_VIDEO)
        time.sleep(5)
        CF.take_image(pdf, CN.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\Induc_LIVE_video.png',
                      'Induc_LIVE_video.png')
        time.sleep(3)
        CF.click_button(CN.MAXIMIZE_LIVE_VIDEO)
        CF.update_progress_log(pdf)

        CF.click_button(CN.RESISTIVE_LOAD_BUTTON)
        time.sleep(5)
        CF.write_result(pdf, 'RESISTIVE_LOAD_BUTTON : ', '$> Load two is ON')
        CF.wait_until_progress('$> Load two is ON')
        CF.click_button(CN.MAXIMIZE_LIVE_VIDEO)
        time.sleep(5)
        CF.take_image(pdf, CN.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\RESISTIVE_LIVE_video.png',
                      'RESISTIVE_LIVE_video.png')
        time.sleep(3)
        CF.click_button(CN.MAXIMIZE_LIVE_VIDEO)
        CF.take_image(pdf, CN.GRAPH_PATH,
                      'D:\\Automation\\Projects\\screenshot\\RESISTIVE_GRAPH_video.png',
                      'RESISTIVE_GRAPH_video.png')
        CF.take_image(pdf, CN.PARAMETER_PATH,
                      'D:\\Automation\\Projects\\screenshot\\RESISTIVE_PARA_video.png',
                      'RESISTIVE_PARA_video.png')
        CF.update_progress_log(pdf)

        CF.click_button(CN.CAPACITIVE_LOAD_BUTTON)
        time.sleep(5)
        CF.write_result(pdf, 'CAPACITIVE_LOAD_BUTTON : ', '$> Load Three is ON')
        CF.wait_until_progress('$> Load Three is ON')
        CF.click_button(CN.MAXIMIZE_LIVE_VIDEO)
        time.sleep(5)
        CF.take_image(pdf, CN.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\CAPA_LIVE_video.png',
                      'CAPA_LIVE_video.png')
        time.sleep(3)
        CF.click_button(CN.MAXIMIZE_LIVE_VIDEO)
        time.sleep(5)
        CF.take_image(pdf, CN.GRAPH_PATH,
                      'D:\\Automation\\Projects\\screenshot\\CAPA_GRAPH_video.png',
                      'CAPA_GRAPH_video.png')
        CF.take_image(pdf, CN.PARAMETER_PATH,
                      'D:\\Automation\\Projects\\screenshot\\CAPA_PARA_video.png',
                      'CAPA_PARA_video.png')
        CF.update_progress_log(pdf)

        CF.click_button(CN.MOVE_UP_BUTTON)
        time.sleep(5)
        CF.write_result(pdf, 'MOVE_UP_BUTTON : ', '$> Pressed KEY1 switch in CN118 Board')
        CF.wait_until_progress('$> Pressed KEY1 switch in CN118 Board')
        CF.take_image(pdf, CN.GRAPH_PATH,
                      'D:\\Automation\\Projects\\screenshot\\MOVEUP_GRAPH_video.png',
                      'MOVEUP_GRAPH_video.png')
        CF.take_image(pdf, CN.PARAMETER_PATH,
                      'D:\\Automation\\Projects\\screenshot\\MOVEUP_PARA_video.png',
                      'MOVEUP_PARA_video.png')
        CF.update_progress_log(pdf)

        CF.click_button(CN.MOVE_DOWN_BUTTON)
        time.sleep(5)
        CF.write_result(pdf, 'MOVE_DOWN_BUTTON : ', '$> Pressed KEY2 switch in CN118 Board')
        CF.wait_until_progress('$> Pressed KEY2 switch in CN118 Board')
        time.sleep(5)
        CF.take_image(pdf, CN.GRAPH_PATH,
                      'D:\\Automation\\Projects\\screenshot\\MOVEDO_GRAPH_video.png',
                      'MOVEDO_GRAPH_video.png')
        CF.take_image(pdf, CN.PARAMETER_PATH,
                      'D:\\Automation\\Projects\\screenshot\\MOVEDO_PARA_video.png',
                      'MOVEDO_PARA_video.png')
        CF.update_progress_log(pdf)

        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('CN118_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()


if __name__ == "__main__":
    stu = CN118()
    stu.mini_power_monitor_function()






