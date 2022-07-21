import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.CN268 import CN268_const as CN
from Projects.Common_function import common
import Projects.constants as CS

pdf = FPDF()
CF = common()


class CN268:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def header_function(self):
        pdf.add_page()
        CF.login_and_connect(CN.board_name)
        time.sleep(10)
        connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
        if "Ready" in connectText.text:
            CF.click_button(CS.live_button)
            CF.write_header(pdf, 'CN268-1')
            CF.wait_until_progress("SYSTEM READY")
            time.sleep(5)
            CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
            CF.update_progress_log(pdf)
            CF.take_image(pdf, CN.graph_path, 'D:\\Automation\\Projects\\screenshot\\CN268_graph2.png',
                          'CN268_graph2.png')
            time.sleep(3)
            CF.click_button(CN.start_button)
            time.sleep(8)
            CF.click_button(CN.maximize_live_video)
            time.sleep(5)
            CF.take_image(pdf, CN.live_video_path, 'D:\\Automation\\Projects\\screenshot\\CN268_live_video.png',
                          'CN268_live_video.png')
            CF.click_button(CN.maximize_live_video)
            time.sleep(3)
            CF.update_progress_log(pdf)
            time.sleep(3)
            CF.take_image(pdf, CN.graph_path, 'D:\\Automation\\Projects\\screenshot\\CN268_graph.png',
                          'CN268_graph.png')
            CF.write_result(pdf, 'Slave--Log : ', 'START EVALUATING')
            CF.take_image(pdf, CN.graph_path, 'D:\\Automation\\Projects\\screenshot\\CN268_graph1.png',
                          'CN268_graph1.png')
            time.sleep(5)

            CF.slave_log_path(pdf)
            pdf.set_font("Arial", 'B', size=12)
            pdf.cell(0, 7, txt='Current date and time : ', align='L')
            pdf.cell(0, 7, txt=self.date_time, align='R')

            pdf.output('CN268_result.pdf')
            CF.click_button(CS.Connect_Button)
            CF.driver.close()


if __name__ == "__main__":
    stu = CN268()
    stu.header_function()
