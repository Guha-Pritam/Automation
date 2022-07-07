import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from Projects.JP167 import JP167_const as JP
from Projects.Common_function import common
import Projects.constants as CS

pdf = FPDF()
CF = common()


class JP167:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def header_function(self):
        CF.login_and_connect(JP.BOARD_NAME)
        time.sleep(5)
        connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
        if "Ready" in connectText.text:
            CF.click_button(CS.live_button)
            CF.write_header(pdf, 'JP167')
            CF.wait_until_progress("SYSTEM READY")
            time.sleep(15)
            CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
            time.sleep(15)
            CF.update_progress_log(pdf)
            CF.take_image(pdf, JP.LIVE_VIDEO_PATH,
                          'D:\\Automation\\Projects\\screenshot\\LIVE_video.png',
                          'LIVE_video.png')
            CF.take_image(pdf, JP.OSCILLOSCOPE_VIDEO_PATH,
                          'D:\\Automation\\Projects\\screenshot\\OSCI_video.png',
                          'OSCI_video.png')

    def power_line_communication(self):
        pdf.add_page()
        JP167.header_function(self)

        # ON THE TARGET BUTTON
        CF.click_button(JP.TARGET_2_BUTTON)
        CF.wait_until_progress('$> Node 2 selected')
        time.sleep(3)
        CF.write_result(pdf, 'Clicking-Target2-function : ', '$> Node 2 selected')
        CF.wait_until_connection_path()
        CF.take_image(pdf, JP.OSCILLOSCOPE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\click_OSCI_video.png',
                      'click_OSCI_video.png')
        CF.take_image(pdf, JP.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\click_LIVE_video.png',
                      'click_LIVE_video.png')
        CF.update_progress_log(pdf)

        # LED COLOUR CONTROL ( ORANGE )
        CF.click_button(JP.ORANGE_RGB_PATH)
        CF.wait_until_progress('$Orange color selected')
        time.sleep(3)
        CF.write_result(pdf, 'Orange-slider : ', '$Orange color selected')
        CF.take_image(pdf, JP.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\Orange_LIVE_video.png',
                      'Orange_LIVE_video.png')
        CF.update_progress_log(pdf)

        # LED COLOUR CONTROL ( RED )
        CF.click_button(JP.RED_RGB_PATH)
        CF.wait_until_progress('$Red color selected')
        time.sleep(3)
        CF.write_result(pdf, 'Red-slider : ', '$Red color selected')
        CF.take_image(pdf, JP.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\Red_LIVE_video.png',
                      'Red_LIVE_video.png')
        CF.update_progress_log(pdf)

        # LED COLOUR CONTROL ( BLUE )
        CF.click_button(JP.BLUE_RGB_PATH)
        CF.wait_until_progress('$Blue color selected')
        time.sleep(3)
        CF.write_result(pdf, 'Blue-slider : ', '$Blue color selected')
        CF.take_image(pdf, JP.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\Blue_LIVE_video.png',
                      'Blue_LIVE_video.png')
        CF.update_progress_log(pdf)

        # LED COLOUR CONTROL ( YELLOW )
        CF.click_button(JP.YELLOW_RGB_PATH)
        CF.wait_until_progress('$Yellow color selected')
        time.sleep(3)
        CF.write_result(pdf, 'Yellow-slider : ', '$Yellow color selected')
        CF.take_image(pdf, JP.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\Yellow_LIVE_video.png',
                      'Yellow_LIVE_video.png')
        CF.update_progress_log(pdf)

        # LED COLOUR CONTROL ( WHITE )
        CF.click_button(JP.WHITE_RGB_PATH)
        CF.wait_until_progress('$White color selected')
        time.sleep(3)
        CF.write_result(pdf, 'White-slider : ', '$White color selected')
        CF.take_image(pdf, JP.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\White_LIVE_video.png',
                      'White_LIVE_video.png')
        CF.update_progress_log(pdf)

        # LED COLOUR CONTROL ( PINK )
        CF.click_button(JP.PINK_RGB_PATH)
        CF.wait_until_progress('$Pink color selected')
        time.sleep(3)
        CF.write_result(pdf, 'Pink-slider : ', '$Pink color selected')
        CF.take_image(pdf, JP.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\Pink_LIVE_video.png',
                      'Pink_LIVE_video.png')
        CF.update_progress_log(pdf)

        # SET INTENSITY RGB
        Scroll = CF.driver.find_element(By.XPATH, JP.INTENSITY_SLIDER)
        CF.actions.drag_and_drop_by_offset(Scroll, 0, 20).perform()

        CF.wait_until_progress('$intensity control set to :50%')
        CF.write_result(pdf, 'Slider-connection : ', '$intensity control set to :50%')
        time.sleep(5)
        CF.take_image(pdf, JP.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\Intensity_LIVE_video.png',
                      'Intensity_LIVE_video.png')
        CF.update_progress_log(pdf)
        time.sleep(10)

        Scroll = CF.driver.find_element(By.XPATH, JP.INTENSITY_SLIDER)
        CF.actions.drag_and_drop_by_offset(Scroll, -70, 20).perform()
        CF.wait_until_progress('$intensity control set to :0%')
        CF.write_result(pdf, 'Slider-connection : ', '$intensity control set to :0%')
        time.sleep(5)
        CF.take_image(pdf, JP.LIVE_VIDEO_PATH,
                      'D:\\Automation\\Projects\\screenshot\\Intensity-2_LIVE_video.png',
                      'Intensity-2_LIVE_video.png')
        CF.update_progress_log(pdf)
        Scroll = CF.driver.find_element(By.XPATH, JP.INTENSITY_SLIDER)
        CF.actions.drag_and_drop_by_offset(Scroll, 0, 20).perform()
        CF.wait_until_connection_path()

        # CLICK THE START BUTTON
        CF.click_button(JP.START_BUTTON)
        CF.wait_until_connection_path()
        CF.write_result(pdf, 'Light-Demo : ', '$> Auto illumination started')
        CF.wait_until_connection_path()
        for i in range(5):
            time.sleep(2)
            CF.take_image(pdf, JP.OSCILLOSCOPE_VIDEO_PATH,
                          f'D:\\Automation\\Projects\\screenshot\\{i}_OSCI.png',
                          f'{i}_OSCI.png')
            CF.take_image(pdf, JP.LIVE_VIDEO_PATH,
                          f'D:\\Automation\\Projects\\screenshot\\{i}_Auto.png',
                          f'{i}_Auto.png')
        CF.update_progress_log(pdf)
        time.sleep(5)

        CF.click_button(JP.TARGET_2_BUTTON)
        CF.wait_until_connection_path()
        CF.click_button(JP.TARGET_1_BUTTON)
        CF.update_progress_log(pdf)

        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('JP167_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()


if __name__ == "__main__":
    stu = JP167()
    stu.power_line_communication()
