import datetime
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
# import pyaudio
import wave
import constants as CS

url = CS.evm_url
screenshot_path = r"./screenshot"
if not os.path.isdir(screenshot_path):
    os.makedirs(screenshot_path)

PROGRESS_LOG = []
OLD_PROGRESS_LOG = []
VR_LOG = []
SLAVE_LOG = []
INFORMATION = []


class Common:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument(r'--user-data-dir=C:\Users\THIS PC\Desktop\gmail login\session')
        self.options.add_argument('--profile-directory=session')
        self.options.add_argument("--incognito")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=self.options)
        self.actions = ActionChains(self.driver)

        # self.options.add_argument("--enable-infobars")
        # self.options.add_argument("--enable-extensions")

        self.wait = WebDriverWait(self.driver, 280)
        self.e = datetime.datetime.now()
        self.driver.maximize_window()

    def click_button(self, UI_button):
        live = self.wait.until(EC.element_to_be_clickable((By.XPATH, UI_button)))
        live.click()

    def login_and_connect(self, board_name):
        self.driver.get(CS.evm_url)
        self.click_button(CS.login)
        time.sleep(3)

        self.click_button(CS.login_url_1)
        time.sleep(5)

        email = self.driver.find_element(By.XPATH, CS.email_1)
        email.send_keys(CS.username)
        time.sleep(5)

        password = self.driver.find_element(By.XPATH, CS.passwrd_1)
        password.send_keys(CS.passwrd)
        self.click_button(CS.submit)
        time.sleep(15)

        search_element = '//*[@id="formSerachBar"]'
        inputElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, search_element)))
        inputElement.send_keys(board_name)
        self.wait_until_clickable(CS.connect_jp128)
        self.wait_until_clickable(CS.Connect_Button)

    def old_login_connect(self, board_name):
        self.driver.get(CS.evm_url)
        self.click_button(CS.login)
        time.sleep(3)

        self.click_button(CS.login_url_1)
        time.sleep(5)

        email = self.driver.find_element(By.XPATH, CS.email_1)
        email.send_keys(CS.username)
        time.sleep(5)

        password = self.driver.find_element(By.XPATH, CS.passwrd_1)
        password.send_keys(CS.passwrd)
        self.click_button(CS.submit)
        time.sleep(15)

        search_element = '//*[@id="formSerachBar"]'
        inputElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, search_element)))
        inputElement.send_keys(board_name)
        time.sleep(10)

        self.wait_until_clickable(CS.connect_jp128)
        time.sleep(10)

        self.driver.find_element(By.XPATH, CS.old_close_user_guide).click()

        self.wait_until_clickable(CS.old_connect_button)

    def video_testing(self, pdf, switch_to_frame):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, switch_to_frame))
        print('Click for refresh')
        self.click_button(CS.Video_refresh)
        time.sleep(10)

        # PASS IF THERE IS KBps MORE THAN 200 and Fail if 0 KBps
        kbps = self.driver.find_element(By.XPATH, CS.kbps_path).text
        time.sleep(10)
        slice_txt = kbps[0:3]
        convert_int = int(slice_txt)
        print(convert_int)
        if convert_int > 0:
            self.driver.switch_to.parent_frame()
            self.write_result(pdf, 'Video :', 'SYSTEM READY')
            print('PASS')
        else:
            self.driver.switch_to.parent_frame()
            self.write_result(pdf, 'No data has come...', 'SYSTEM READY')
            print('FAIL')
        time.sleep(5)

    def write_header(self, pdf1, Board_name):
        pdf1.set_font("Arial", size=15)
        pdf1.cell(0, 7, txt="BOARD NAME", ln=1, align='C')
        pdf1.cell(0, 7, txt=str(Board_name), ln=2, align='C')

    def write_result(self, pdf1, test_case, right_txt):
        pdf1.set_font("Arial", 'B', size=12)
        progress_log = self.driver.find_element(By.XPATH, '//*[@id="console_status"]').text
        pdf1.set_text_color(0, 0, 0)
        pdf1.cell(0, 30, txt=str(test_case), ln=0, align='L')
        if right_txt in progress_log:
            pdf1.set_text_color(0, 128, 0)
            pdf1.cell(0, 30, txt="PASS", ln=1, align='R')
        else:
            pdf1.set_text_color(255, 0, 0)
            pdf1.cell(0, 25, txt="FAIL", ln=1, align='R')

    def old_write_result(self, pdf1, test_case, right_txt):
        pdf1.set_font("Arial", 'B', size=12)
        progress_log = self.driver.find_element(By.XPATH,
                                                '//*[@id="console_status"]/div/tx-elements/div[2]/div/ul').text
        pdf1.set_text_color(0, 0, 0)
        pdf1.cell(0, 30, txt=str(test_case), ln=0, align='L')
        if right_txt in progress_log:
            pdf1.set_text_color(0, 128, 0)
            pdf1.cell(0, 30, txt="PASS", ln=1, align='R')
        else:
            pdf1.set_text_color(255, 0, 0)
            pdf1.cell(0, 25, txt="FAIL", ln=1, align='R')

    # def old_write_result(pdf1, test_case, right_txt):
    #     pdf1.set_font("Arial", 'B', size=12)
    #     progress_log = driver.find_element(By.XPATH, '//*[@id="console_status"]').text
    #     pdf1.set_text_color(0, 0, 0)
    #     pdf1.cell(0, 30, txt=str(test_case), ln=0, align='L')
    #     if right_txt in progress_log:
    #         pdf1.set_text_color(0, 128, 0)
    #         pdf1.cell(0, 30, txt="PASS", ln=1, align='R')
    #     else:
    #         pdf1.set_text_color(255, 0, 0)
    #         pdf1.cell(0, 25, txt="FAIL", ln=1, align='R')

    def update_progress_log(self, pdf1):
        global PROGRESS_LOG
        pdf1.set_font("Arial", size=12)
        path = '//*[@id="default-dashboard"]/div[1]/nav/div[2]/form'
        connectText = self.driver.find_element(By.XPATH, path)
        progress_log = self.driver.find_element(By.XPATH, '//*[@id="console_status"]').text.split("\n")
        latest_progres_data = progress_log[len(PROGRESS_LOG):]
        PROGRESS_LOG = progress_log
        if "Ready" in connectText.text:
            for line in latest_progres_data:
                pdf1.set_text_color(0, 0, 0)
                pdf1.cell(0, 10, txt=line, ln=1, align='L')

    def slave_log_path(self, pdf1):
        global SLAVE_LOG
        pdf1.set_font("Arial", size=12)
        path = '//*[@id="default-dashboard"]/div[1]/nav/div[2]/form'
        connectText = self.driver.find_element(By.XPATH, path)
        progress_log = self.driver.find_element(By.XPATH, '//*[@id="85e79079-07e7-7719-6bda-59d3bf7dd5a6"]').text.split(
            "\n")
        latest_slave_data = progress_log[len(SLAVE_LOG):]
        SLAVE_LOG = progress_log
        if "Ready" in connectText.text:
            for line in latest_slave_data:
                pdf1.set_text_color(0, 0, 0)
                pdf1.cell(0, 10, txt=line, ln=1, align='L')

    def update_VR_log(self, pdf1):
        global VR_LOG
        pdf1.set_font("Arial", size=12)
        path = '//*[@id="default-dashboard"]/div[1]/nav/div[2]/form'
        connectText = self.driver.find_element(By.XPATH, path)
        progress_log = self.driver.find_element(By.XPATH, '//*[@id="11f1e3dc-7e13-2931-ab0c-e3893cab89d3"]').text.split(
            "\n")
        latest_progres_data = progress_log[len(VR_LOG):]
        VR_LOG = progress_log
        if "Ready" in connectText.text:
            for line in latest_progres_data:
                pdf1.set_text_color(0, 0, 0)
                pdf1.cell(0, 10, txt=line, ln=1, align='L')

    def old_take_information(self, pdf1):
        global INFORMATION
        pdf1.set_font("Arial", size=12)
        path = '//*[@id="navbar6"]/ul[3]/li[2]/div'
        connectText = self.driver.find_element(By.XPATH, path)
        print(connectText.text)
        information_log = self.driver.find_element(By.XPATH, CS.old_information).text.split("   ")
        latest_information_data = information_log[len(INFORMATION):]
        INFORMATION = information_log
        if "Ready" in connectText.text:
            for line in latest_information_data:
                pdf1.set_text_color(0, 0, 0)
                pdf1.cell(0, 10, txt=line, ln=1, align='L')
                print("[|| INFORMATION ||] ", line)

    def old_update_progress_log(self, pdf1):
        global OLD_PROGRESS_LOG
        pdf1.set_font("Arial", size=12)
        path = '//*[@id="navbar6"]/ul[3]/li[2]/div'
        connectText = self.driver.find_element(By.XPATH, path)
        print(connectText.text)
        progress_log = self.driver.find_element(By.XPATH, CS.old_progress_log_path).text.split("\n")
        latest_progres_data = progress_log[len(OLD_PROGRESS_LOG):]
        OLD_PROGRESS_LOG = progress_log
        if "Ready" in connectText.text:
            for line in latest_progres_data:
                # print('progress log cm')
                pdf1.set_text_color(0, 0, 0)
                pdf1.cell(0, 10, txt=line, ln=1, align='L')
                print("[|| OLD_PROGRESS__LOG ||] ", line)
        else:
            print("[|| Pritam ||] ", connectText.text)

    def take_image(self, pdf1, Image_Path, img, image):
        Image1 = self.driver.find_element(By.XPATH, Image_Path)
        Image1.screenshot(screenshot_path + "/" + image)
        pdf1.cell(40)
        pdf1.image(img, x=50, w=100, h=50)
        pdf1.ln(5)

    # def record_audio(self, wav):
    #     CHUNK = 1024
    #     FORMAT = pyaudio.paInt16
    #     CHANNELS = 1
    #     RATE = 44100
    #     RECORD_SECONDS = 20
    #     WAVE_OUTPUT_FILENAME = screenshot_path + "/" + wav
    #
    #     p = pyaudio.PyAudio()
    #
    #     stream = p.open(format=FORMAT,
    #                     channels=CHANNELS,
    #                     rate=RATE,
    #                     input=True,
    #                     frames_per_buffer=CHUNK)
    #
    #     print("* recording")
    #     frames = []
    #     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #         data = stream.read(CHUNK)
    #         frames.append(data)
    #
    #     print("* done recording")
    #
    #     stream.stop_stream()
    #     stream.close()
    #     p.terminate()
    #
    #     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    #     wf.setnchannels(CHANNELS)
    #     wf.setsampwidth(p.get_sample_size(FORMAT))
    #     wf.setframerate(RATE)
    #     wf.writeframes(b''.join(frames))
    #     wf.close()

    def add_audio_link_pdf(self, pdf1, test_name, LINK):
        pdf1.set_font("Arial", 'B', size=12)
        pdf1.set_text_color(0, 0, 0)
        pdf1.cell(0, 30, txt=str(test_name), ln=0, align='L')
        pdf1.set_font("Arial", size=12)
        pdf1.set_text_color(0, -5, 255)
        pdf1.cell(0, 30, txt=str(LINK), ln=1, align='R', link=LINK)

    def wait_until_old_progress(self, string):
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, CS.old_progress_log_path), string))

    def wait_until_progress(self, string):
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, CS.progress_log_path), string))

    def wait_until_clickable(self, xpath):
        secondButton = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        secondButton.click()

    def wait_until_old_connection_path(self):
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, CS.old_connection_path), 'Ready'))

    def wait_until_connection_path(self):
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))

    # def Text_To_Pdf(txt_File, Pdf_file):
    #     pdf = FPDF())
    #     pdf.add_page()
    #     pdf.set_font("Arial", size=12)
    #     file = open(screenshot_path + "/" + txt_File, "r")
    #
    #     for xy in file:
    #         pdf.cell(200, 10, txt=xy, ln=1, align='l')
    #
    #     pdf.output(Pdf_file)
    #     pdf.close()
    #     file.close()

    # def Merger_Pdf(First_pdf, Second_pdf, Result_pdf):
    #     File_path = "D:\\TenXer\\gmail_login\\"
    #     merger = PdfFileMerger()
    #     merger.append(File_path + First_pdf)
    #     merger.append(File_path + Second_pdf)
    #     merger.write(File_path + Result_pdf)
    #     merger.close()
    #
    #
    # def Merger_txt(First_txt, Second_txt, Result_txt):
    #     File_path = "D:\\TenXer\\gmail_login\\JP128\\screenshot"
    #     filenames = [File_path + First_txt, File_path + Second_txt]
    #     with open(File_path + Result_txt, 'w') as outfile:
    #         for names in filenames:
    #             with open(names) as infile:
    #                 outfile.write(infile.read())
    #             outfile.write("\n")
    #
    #
    # def Remove_File(First_file):
#     os.remove(First_file)
