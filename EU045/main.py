import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from EU045 import EU045_const as EU
from Common_function import common
import constants as CS

pdf = FPDF()
CF = common()


def header_function():
    CF.login_and_connect(EU.board_name)
    time.sleep(10)
    connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
    if "Ready" in connectText.text:
        CF.click_button(CS.live_button)
        CF.write_header(pdf, 'EU045')
        CF.wait_until_progress("SYSTEM READY")
        CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\appli_video'
                                                      '.png', 'appli_video.png')
        CF.click_button(EU.maximize_live_video)
        time.sleep(5)
        CF.take_image(pdf, EU.live_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\live_video.png',
                      'live_video.png')
        CF.click_button(EU.maximize_live_video)
        time.sleep(8)
        CF.update_progress_log(pdf)
        time.sleep(5)


class EU045:
    def __init__(self):
        self.date_time = (CF.e.strftime("DATE : %b %d %Y TIME : %H:%M:%S"))

    def alcohol_gas_function(self):
        pdf.add_page()
        header_function()
        CF.click_button(EU.alcohol_gas_shot)
        CF.wait_until_progress('Inducing of gas turned OFF')
        CF.write_result(pdf, 'Alcohol_gas_testing : ', 'Inducing of gas turned OFF')
        CF.click_button(EU.maximize_live_video)
        time.sleep(5)
        CF.take_image(pdf, EU.live_video_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\alcohol_live_video.png',
                      'alcohol_live_video.png')
        CF.click_button(EU.maximize_live_video)
        CF.wait_until_progress('Inducing of gas turned OFF')
        CF.take_image(pdf, EU.application_video_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\alcohol_apply'
                      '.png', 'alcohol_apply.png')
        # CLICKING Device GAS SHOT
        CF.click_button(EU.device_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.write_result(pdf, 'Alcohol_gas_testing : DEVICE -- ', 'Inducing of gas turned OFF')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\device_gas'
                                                      '.png', 'device_gas.png')
        time.sleep(5)

        # CLICKING Sensors GAS SHOT
        CF.click_button(EU.sensor_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.write_result(pdf, 'Alcohol_gas_testing : SENSORS -- ', 'Inducing of gas turned OFF')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\sensors_gas'
                                                      '.png', 'sensors_gas.png')
        time.sleep(5)

        # CLICKING Graphs GAS SHOT
        CF.click_button(EU.graph_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.write_result(pdf, 'Alcohol_gas_testing : GRAPHS -- ', 'Inducing of gas turned OFF')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\graph_gas'
                                                      '.png', 'graph_gas.png')
        time.sleep(5)

        # CLICKING Tables GAS SHOT
        CF.click_button(EU.tables_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.write_result(pdf, 'Alcohol_gas_testing : TABLES -- ', 'Inducing of gas turned OFF')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\table_gas'
                                                      '.png', 'table_gas.png')
        time.sleep(5)

        # CLICKING Settings GAS SHOT
        CF.click_button(EU.setting_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.write_result(pdf, 'Alcohol_gas_testing : SETTINGS -- ', 'Inducing of gas turned OFF')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot'
                                                      '\\settings_gas.png', 'settings_gas.png')
        time.sleep(5)
        CF.update_progress_log(pdf)
        time.sleep(3)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('EU045_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()

    def humidity_shot_function(self):
        pdf.add_page()
        header_function()
        CF.click_button(EU.humidity_button)
        CF.wait_until_progress('Humidifier turned OFF')
        CF.write_result(pdf, 'Humidity_shot_function : ', 'Humidifier turned OFF')
        CF.click_button(EU.maximize_live_video)
        time.sleep(5)
        CF.take_image(pdf, EU.live_video_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\humidity_live_video.png',
                      'humidity_live_video.png')
        CF.click_button(EU.maximize_live_video)
        CF.wait_until_progress('Humidifier turned OFF')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot'
                                                      '\\humidity_apply.png', 'humidity_apply.png')
        # CLICKING Device GAS SHOT
        CF.click_button(EU.device_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.write_result(pdf, 'Humidity_shot_function : DEVICE -- ', 'Humidifier turned OFF')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot'
                                                      '\\device_humidity.png', 'device_humidity.png')
        time.sleep(5)

        # CLICKING Sensors GAS SHOT
        CF.click_button(EU.sensor_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.write_result(pdf, 'Humidity_shot_function : SENSORS -- ', 'Humidifier turned OFF')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot'
                                                      '\\sensors_humidity.png', 'sensors_humidity.png')
        time.sleep(5)

        # CLICKING Graphs GAS SHOT
        CF.click_button(EU.graph_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.write_result(pdf, 'Humidity_shot_function : GRAPHS -- ', 'Humidifier turned OFF')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot'
                                                      '\\graph_humidity.png', 'graph_humidity.png')
        time.sleep(5)

        # CLICKING Tables GAS SHOT
        CF.click_button(EU.tables_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.write_result(pdf, 'Humidity_shot_function : TABLES -- ', 'Humidifier turned OFF')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot'
                                                      '\\table_humidity.png', 'table_humidity.png')
        time.sleep(5)

        # CLICKING Settings GAS SHOT
        CF.click_button(EU.setting_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.write_result(pdf, 'Humidity_shot_function : SETTINGS -- ', 'Humidifier turned OFF')
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot'
                                                      '\\settings_humidity.png', 'settings_humidity.png')
        time.sleep(5)
        CF.update_progress_log(pdf)
        time.sleep(3)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')

        pdf.output('EU045_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()

    def temperature_function(self):
        pdf.add_page()
        header_function()
        CF.click_button(EU.temperature_button)
        CF.wait_until_progress('Temperature Increased')
        CF.write_result(pdf, 'Temperature_function : ', 'Temperature Increased')
        CF.click_button(EU.maximize_live_video)
        time.sleep(5)
        CF.take_image(pdf, EU.live_video_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\temperature_live_video.png',
                      'temperature_live_video.png')
        CF.click_button(EU.maximize_live_video)
        CF.wait_until_progress('Temperature Increased')
        CF.take_image(pdf, EU.application_video_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\temperature_apply'
                      '.png', 'temperature_apply.png')
        # CLICKING Device GAS SHOT
        CF.click_button(EU.device_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\device_temp'
                                                      '.png', 'device_temp.png')
        time.sleep(5)

        # CLICKING Sensors GAS SHOT
        CF.click_button(EU.sensor_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\sensors_temp'
                                                      '.png', 'sensors_temp.png')
        time.sleep(5)

        # CLICKING Graphs GAS SHOT
        CF.click_button(EU.graph_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\graph_temp'
                                                      '.png', 'graph_temp.png')
        time.sleep(5)

        # CLICKING Tables GAS SHOT
        CF.click_button(EU.tables_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\table_temp'
                                                      '.png', 'table_temp.png')
        time.sleep(5)

        # CLICKING Settings GAS SHOT
        CF.click_button(EU.setting_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot'
                                                      '\\settings_temp.png', 'settings_temp.png')
        time.sleep(5)
        CF.update_progress_log(pdf)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')
        pdf.output('EU045_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()

    def clear_air_function(self):
        pdf.add_page()
        header_function()
        CF.click_button(EU.clear_air_button)
        CF.wait_until_progress('Blower turned ON...Clearing Air')
        CF.write_result(pdf, 'Clear_air_function : ', 'Blower turned ON...Clearing Air')
        CF.click_button(EU.maximize_live_video)
        time.sleep(5)
        CF.take_image(pdf, EU.live_video_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\air_live_video.png',
                      'air_live_video.png')
        CF.click_button(EU.maximize_live_video)
        CF.wait_until_progress('Blower turned ON...Clearing Air')
        CF.take_image(pdf, EU.application_video_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\air_apply'
                      '.png', 'air_apply.png')
        # CLICKING Device GAS SHOT
        CF.click_button(EU.device_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\air_temp'
                                                      '.png', 'air_temp.png')
        time.sleep(5)

        # CLICKING Sensors GAS SHOT
        CF.click_button(EU.sensor_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\air_temp'
                                                      '.png', 'air_temp.png')
        time.sleep(5)

        # CLICKING Graphs GAS SHOT
        CF.click_button(EU.graph_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\air_temp'
                                                      '.png', 'air_temp.png')
        time.sleep(5)

        # CLICKING Tables GAS SHOT
        CF.click_button(EU.tables_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\air_temp'
                                                      '.png', 'air_temp.png')
        time.sleep(5)

        # CLICKING Settings GAS SHOT
        CF.click_button(EU.setting_button)
        time.sleep(5)
        CF.wait_until_connection_path()
        CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot'
                                                      '\\air_temp.png', 'air_temp.png')
        time.sleep(5)
        CF.update_progress_log(pdf)
        time.sleep(3)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 7, txt='Current date and time : ', align='L')
        pdf.cell(0, 7, txt=self.date_time, align='R')
        pdf.output('Euo45_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()


if __name__ == "__main__":
    stu = EU045()
    stu.alcohol_gas_function()
    stu.humidity_shot_function()
    stu.temperature_function()
    stu.clear_air_function()
