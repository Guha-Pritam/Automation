import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from JP128 import JP128_const as JP
from Common_function import common
import constants as CS

pdf1 = FPDF()
CF = common()


# -------------------------------------------- HEADER FUNCTION---------------------------------------------------------

def header_function():
    CF.login_and_connect(JP.board_name)
    time.sleep(5)
    connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
    if "Ready" in connectText.text:
        # CONNECTION TESTING
        CF.click_button(CS.live_button)
        CF.write_header(pdf1, 'JP128')
        CF.wait_until_progress("SYSTEM READY")
        CF.write_result(pdf1, 'Connection :', 'SYSTEM READY')
        CF.update_progress_log(pdf1)
        print('Connection is Ready')

        # -------------------------------------------- VIDEO TESTING ---------------------------------------------------
        CF.video_testing(pdf1, JP.switch_to_frame)
        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.Maximize_live_video)
        time.sleep(7)

        CF.take_image(pdf1, JP.live_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\image1.png',
                      'image1.png')

        CF.click_button(JP.Maximize_live_video)
        time.sleep(5)
        print(' complete video testing.....')

        # -------------------------------------------- HMI TESTING -----------------------------------------------


class JP128:
    def __init__(self):
        self.date_time = (CF.e.strftime("Time : %b %d %Y %H:%M:%S"))

    def HMI_testing(self):
        # START GIVING COMMANDS
        pdf1.add_page()
        header_function()
        time.sleep(3)
        CF.click_button(JP.turn_on_light_jp128)
        CF.record_audio("voice1.wav")
        time.sleep(5)
        CF.write_result(pdf1, 'HMI Tracking :', 'START EVALUATING')
        CF.add_audio_link_pdf(pdf1, 'Light-On : ', 'file:///D:/TenXer/gmail_login/Run_all_BOARDS/screenshot/voice1.wav')
        time.sleep(5)
        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.maximize_video_jp128)
        time.sleep(7)

        CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\image2.png',
                      'image2.png')

        CF.click_button(JP.maximize_video_jp128)
        CF.update_progress_log(pdf1)

        # TURN OFF LIGHT
        CF.click_button(JP.Turn_off_light_jp128)
        CF.record_audio("voice2.wav")
        time.sleep(5)
        CF.add_audio_link_pdf(pdf1, 'Light-Off : ', 'file:///D:/TenXer/gmail_login/Run_all_BOARDS/screenshot/voice2.wav')
        time.sleep(5)
        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.maximize_video_jp128)
        time.sleep(7)

        CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\image3.png',
                      'image3.png')

        CF.click_button(JP.maximize_video_jp128)
        CF.update_progress_log(pdf1)
        time.sleep(5)

        # TURN ON TV
        CF.click_button(JP.Turn_on_tv_jp128)
        CF.record_audio("voice3.wav")
        time.sleep(5)
        CF.add_audio_link_pdf(pdf1, 'Light-On-TV : ', 'file:///D:/TenXer/gmail_login/Run_all_BOARDS/screenshot/voice3'
                                                      '.wav')
        time.sleep(5)
        # pdf1.set_text_color(0, 0, 0)
        # pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.maximize_video_jp128)
        time.sleep(7)

        CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\image4.png',
                      'image4.png')

        CF.click_button(JP.maximize_video_jp128)
        CF.update_progress_log(pdf1)
        time.sleep(7)

        # CHANNEL UP
        CF.click_button(JP.Channel_up_jp128)
        CF.record_audio("voice4.wav")
        time.sleep(5)
        CF.add_audio_link_pdf(pdf1, 'Channel-UP : ', 'file:///D:/TenXer/gmail_login/Run_all_BOARDS/screenshot/voice4'
                                                     '.wav')
        time.sleep(5)
        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.maximize_video_jp128)
        time.sleep(7)

        CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\image5.png',
                      'image5.png')

        CF.click_button(JP.maximize_video_jp128)
        CF.update_progress_log(pdf1)
        time.sleep(5)

        # CHANNEL DOWN
        CF.click_button(JP.Channel_down_jp128)
        CF.record_audio("voice5.wav")
        time.sleep(5)
        CF.add_audio_link_pdf(pdf1, 'Channel-Down : ', 'file:///D:/TenXer/gmail_login/Run_all_BOARDS/screenshot'
                                                       '/voice5.wav')
        time.sleep(5)
        # pdf1.set_text_color(0, 0, 0)
        # pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.maximize_video_jp128)
        time.sleep(7)

        CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\image6.png',
                      'image6.png')

        CF.click_button(JP.maximize_video_jp128)
        CF.update_progress_log(pdf1)
        time.sleep(7)

        # TURN OFF TV
        CF.click_button(JP.Turn_off_tv_jp128)
        CF.record_audio("voice6.wav")
        time.sleep(5)
        CF.add_audio_link_pdf(pdf1, 'Turn-Off-TV : ', 'file:///D:/TenXer/gmail_login/Run_all_BOARDS/screenshot/voice6'
                                                      '.wav')
        time.sleep(5)
        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.maximize_video_jp128)
        time.sleep(7)

        CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\image7.png',
                      'image7.png')

        CF.click_button(JP.maximize_video_jp128)
        CF.update_progress_log(pdf1)
        pdf1.cell(0, 7, txt=self.date_time, align='L')

        pdf1.output('JP128_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()
        print(' complete HMI testing.....')

        # -------------------------------------------- PERFORMANCE UNDER NOICE ROAD --------------------------------

    def noice_road(self):
        pdf1.add_page()
        header_function()
        CF.wait_until_clickable(JP.i_agree_button)
        time.sleep(5)
        CF.write_result(pdf1, 'HMI-Tracking : (PERFORMANCE UNDER NOICE ROAD)--', 'START EVALUATING')
        CF.driver.find_element(By.XPATH, JP.induce_noice_button).click()
        print('jjjj')
        time.sleep(5)
        CF.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        CF.click_button(JP.river_button)
        time.sleep(3)

        # START GIVING COMMANDS
        CF.click_button(JP.turn_on_light_jp128)
        CF.record_audio("voice7.wav")
        time.sleep(5)
        CF.add_audio_link_pdf(pdf1, 'Light-On : ', 'file:///D:/TenXer/gmail_login/Run_all_BOARDS/screenshot/voice7.wav')
        time.sleep(5)
        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.maximize_video_jp128)
        time.sleep(7)

        CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\image8.png',
                      'image8.png')

        CF.click_button(JP.maximize_video_jp128)
        CF.update_progress_log(pdf1)
        time.sleep(7)

        # TURN OFF LIGHT
        CF.click_button(JP.Turn_off_light_jp128)
        CF.record_audio("voice8.wav")
        time.sleep(5)
        CF.add_audio_link_pdf(pdf1, 'Light-Off : ', 'file:///D:/TenXer/gmail_login/Run_all_BOARDS/screenshot/voice8.wav')
        time.sleep(5)
        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.maximize_video_jp128)
        time.sleep(7)

        CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\image9.png',
                      'image9.png')

        CF.click_button(JP.maximize_video_jp128)
        CF.update_progress_log(pdf1)
        time.sleep(7)

        # TURN ON TV
        CF.click_button(JP.Turn_on_tv_jp128)
        CF.record_audio("voice9.wav")
        time.sleep(5)
        CF.add_audio_link_pdf(pdf1, 'Light-On-TV : ', 'file:///D:/TenXer/gmail_login/Run_all_BOARDS/screenshot/voice9'
                                                      '.wav')
        time.sleep(5)

        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.maximize_video_jp128)
        time.sleep(7)

        CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\image10.png',
                      'image10.png')

        CF.click_button(JP.maximize_video_jp128)
        CF.update_progress_log(pdf1)
        time.sleep(7)

        # CHANNEL UP
        CF.click_button(JP.Channel_up_jp128)
        CF.record_audio("voice10.wav")
        time.sleep(5)
        CF.add_audio_link_pdf(pdf1, 'Channel-UP : ', 'file:///D:/TenXer/gmail_login/Run_all_BOARDS/screenshot/voice10'
                                                     '.wav')
        time.sleep(5)
        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.maximize_video_jp128)
        time.sleep(7)

        CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\image11.png',
                      'image11.png')

        CF.click_button(JP.maximize_video_jp128)
        time.sleep(5)
        CF.update_progress_log(pdf1)
        pdf1.cell(0, 7, txt=self.date_time, align='L')

        pdf1.output('JP128_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()
        print(' complete road testing.....')

    #     # -------------------------------------------- PERFORMANCE UNDER NOICE TRAFFIC ----------------------------
    #
    # def traffic_noice():
    #     CF.click_button(JP.traffic_button)
    #     time.sleep(3)
    #     CF.write_result(pdf1, 'HMI-Tracking : (PERFORMANCE UNDER NOICE TRAFFIC)--')
    #     time.sleep(5)
    #
    #     # START GIVING COMMANDS
    #     CF.click_button(JP.turn_on_light_jp128)
    #     CF.record_audio("voice11.wav")
    #     time.sleep(10)
    #     CF.update_progress_log(pdf1)
    #     CF.add_audio_link_pdf(pdf1, 'Light-On : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice11.wav')
    #     time.sleep(5)
    #     pdf1.ln(11)
    #     pdf1.set_text_color(0, 0, 0)
    #     pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image12.png',
    #                   'image12.png')
    #
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     # TURN OFF LIGHT
    #     CF.click_button(JP.Turn_off_light_jp128)
    #     CF.record_audio("voice12.wav")
    #     time.sleep(10)
    #     CF.update_progress_log(pdf1)
    #     CF.add_audio_link_pdf(pdf1, 'Light-Off : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice12.wav')
    #     time.sleep(5)
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image13.png',
    #                   'image13.png')
    #
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     # TURN ON TV
    #     CF.click_button(JP.Turn_on_tv_jp128)
    #     CF.record_audio("voice13.wav")
    #     time.sleep(10)
    #     CF.update_progress_log(pdf1)
    #     CF.add_audio_link_pdf(pdf1, 'Light-On-TV : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice13.wav')
    #     time.sleep(5)
    #     pdf1.ln(11)
    #     pdf1.set_text_color(0, 0, 0)
    #     pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image14.png',
    #                   'image14.png')
    #
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     # CHANNEL UP
    #     CF.click_button(JP.Channel_up_jp128)
    #     CF.record_audio("voice14.wav")
    #     time.sleep(10)
    #     CF.update_progress_log(pdf1)
    #     CF.add_audio_link_pdf(pdf1, 'Channel-UP : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice14.wav')
    #     time.sleep(5)
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image15.png',
    #                   'image15.png')
    #
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(5)
    #     print(' complete traffic testing.....')
    #
    #     # # -------------------------------------------- PERFORMANCE UNDER NOICE BABBLE ---------------------------
    #
    # def babble_noice():
    #     CF.click_button(JP.babble_button)
    #     time.sleep(3)
    #     CF.write_result(pdf1, 'HMI-Tracking : (PERFORMANCE UNDER NOICE BABBLE Tracking)--')
    #     time.sleep(5)
    #
    #     # START GIVING COMMANDS
    #     CF.click_button(JP.turn_on_light_jp128)
    #     CF.record_audio("voice15.wav")
    #     time.sleep(10)
    #     CF.update_progress_log(pdf1)
    #     CF.add_audio_link_pdf(pdf1, 'Light-On : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice15.wav')
    #     time.sleep(5)
    #     pdf1.ln(11)
    #     pdf1.set_text_color(0, 0, 0)
    #     pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image16.png',
    #                   'image16.png')
    #
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     # TURN OFF LIGHT
    #     CF.click_button(JP.Turn_off_light_jp128)
    #     CF.record_audio("voice16.wav")
    #     time.sleep(10)
    #     CF.update_progress_log(pdf1)
    #     CF.add_audio_link_pdf(pdf1, 'Light-Off : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice16.wav')
    #     time.sleep(5)
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image17.png',
    #                   'image17.png')
    #
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     # TURN ON TV
    #     CF.click_button(JP.Turn_on_tv_jp128)
    #     CF.record_audio("voice17.wav")
    #     time.sleep(10)
    #     CF.update_progress_log(pdf1)
    #     CF.add_audio_link_pdf(pdf1, 'Light-On-TV : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice17.wav')
    #     time.sleep(5)
    #     pdf1.ln(11)
    #     pdf1.set_text_color(0, 0, 0)
    #     pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image18.png',
    #                   'image18.png')
    #
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     # CHANNEL UP
    #     CF.click_button(JP.Channel_up_jp128)
    #     CF.record_audio("voice18.wav")
    #     time.sleep(10)
    #     CF.update_progress_log(pdf1)
    #     CF.add_audio_link_pdf(pdf1, 'Channel-UP : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice18.wav')
    #     time.sleep(5)
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image19.png',
    #                   'image19.png')
    #
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(5)
    #     print(' complete babble testing.....')
    #
    # # -------------------------------------------- 2 D DRAWING ENGINE ----------------------------------------------
    #
    # def drawing_engine():
    #     CF.click_button(JP.display_performance)
    #     time.sleep(5)
    #     CF.click_button(JP.d_drawing_button)
    #     time.sleep(5)
    #     CF.click_button(JP.click_apply_button)
    #     time.sleep(5)
    #     CF.write_result(pdf1, '2 D drawing Engine Tracking : ')
    #     CF.update_progress_log(pdf1)
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     pdf1.cell(0, 30, txt="After on the switch---take screenshots", ln=1, align='L')
    #     time.sleep(3)
    #
    #     CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image20.png',
    #                   'image20.png')
    #     time.sleep(3)
    #
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(5)
    #
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.Maximize_live_video)
    #     time.sleep(7)
    #
    #     pdf1.cell(0, 30, txt="After on the switch---take screenshots", ln=1, align='L')
    #     time.sleep(3)
    #     CF.take_image(pdf1, JP.live_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image21.png',
    #                   'image21.png')
    #     time.sleep(3)
    #
    #     CF.click_button(JP.Maximize_live_video)
    #     time.sleep(5)
    #     CF.click_button(JP.d_drawing_button)
    #     time.sleep(5)
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(7)
    #
    #     pdf1.cell(0, 30, txt="After off the switch---take screenshots", ln=1, align='L')
    #     time.sleep(3)
    #     pdf1.ln(2)
    #
    #     CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image22.png',
    #                   'image22.png')
    #     time.sleep(3)
    #
    #     CF.click_button(JP.maximize_video_jp128)
    #     time.sleep(5)
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.Maximize_live_video)
    #     time.sleep(7)
    #
    #     pdf1.cell(0, 30, txt="After off the switch---take screenshots", ln=1, align='L')
    #     time.sleep(3)
    #
    #     CF.take_image(pdf1, JP.live_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image23.png',
    #                   'image23.png')
    #     time.sleep(3)
    #
    #     CF.click_button(JP.Maximize_live_video)
    #     time.sleep(5)
    #     # TAKE IMAGE AND ADD THE PDF
    #     CF.click_button(JP.maximize_graph_button)
    #     time.sleep(7)
    #
    #     pdf1.cell(0, 30, txt="After off the switch---take screenshots", ln=1, align='L')
    #     time.sleep(3)
    #
    #     CF.take_image(pdf1, JP.graph_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image24.png',
    #                   'image24.png')
    #     time.sleep(3)
    #
    #     CF.click_button(JP.maximize_graph_button)
    #     time.sleep(5)
    #     drawing_engine()


if __name__ == "__main__":
    stu = JP128()
    stu.HMI_testing()
    stu.noice_road()
