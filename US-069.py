# import time
# import datetime
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import constants as JP
# from fpdf import FPDF
# from PyPDF2 import PdfFileMerger
# import os
# import image
#
# screenshot_path = r"./screenshot"
# if not os.path.isdir(screenshot_path):
#     os.makedirs(screenshot_path)
#
#
# def click_button(UI_button):
#     live = wait.until(EC.element_to_be_clickable((By.XPATH, UI_button)))
#     live.click()
#
#
# def Convert_ProgressLog_text(ProgressLog_txt):
#     handler = open(screenshot_path + "/" + ProgressLog_txt, "+a")
#     handler.write(e.strftime("Time %I:%M %p\n"))
#     handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
#     handler.close()
#
#
# def Take_Image(Image_Path, Image_pdf):
#     Image = driver.find_element(By.XPATH, Image_Path)
#     Image.screenshot(screenshot_path + '/image.png')
#     image.image_to_pdf(screenshot_path + '/image.png', Image_pdf)
#
#
# def Text_To_Pdf(txt_File, Pdf_file):
#     pdf = FPDF()
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
#
#
# def Merger_Pdf(First_pdf, Second_pdf, Result_pdf):
#     File_path = "D:\\TenXer\\gmail_login\\"
#     merger = PdfFileMerger()
#     merger.append(File_path + First_pdf)
#     merger.append(File_path + Second_pdf)
#     merger.write(File_path + Result_pdf)
#     merger.close()
#
#
# def Remove_File(First_file):
#     os.remove(First_file)
#
#
# options = webdriver.ChromeOptions()
# options.add_argument(r'--user-data-dir=C:\Users\THIS PC\Desktop\gmail login\session')
# options.add_argument('--profile-directory=session')
# options.add_argument("--incognito")
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
# actions = ActionChains(driver)
# wait = WebDriverWait(driver, 60)
# url = JP.US069_url
# e = datetime.datetime.now()
#
# driver.maximize_window()
#
# # -------------------------------------------- STAGE-1 START---------------------------------------------------------
#
# # Clicks the radio button for start the live program
# driver.get(url)
# click_button(JP.Connect_Button)
# time.sleep(5)
# # ready_path = '//*[@id="default-dashboard"]/div[1]/nav/div[2]/form/span'
# # connectText = wait.until(EC.presence_of_element_located((By.XPATH, ready_path)))
#
# path = '//*[@id="default-dashboard"]/div[1]/nav/div[2]/form'
# connectText = driver.find_element(By.XPATH, path)
#
# if "Ready" in connectText.text:
#     # Scroll the window step by step
#     SCROLL_PAUSE_TIME = 1
#     for i in range(1, 20):
#         x_path = f'//*[@id="helpCarousel"]/div[{i}]'
#         actions.move_to_element(driver.find_element(By.XPATH, x_path)).perform()
#         time.sleep(SCROLL_PAUSE_TIME)
#     time.sleep(5)
#     print('Successfully scrolled')
#
#     # clicks the live button for saw the live part
#     click_button(JP.Live_Button)
#     time.sleep(10)
#
#     # click for refresh video
#     driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div['
#                                                          '1]/div[2]/div[2]/div/div/div/div/ul/li['
#                                                          '1]/div/div/tx-elements/div[2]/div/div/div[3]/iframe'))
#     print('Click for refresh')
#     click_button(JP.Video_refresh_US069)
#     driver.switch_to.parent_frame()
#     time.sleep(8)
#
#     # Take screen shoot of live video
#     click_button(JP.Maximize_live_video_US069)
#     time.sleep(5)
#
#     Take_Image(JP.Live_video_path_US069, 'video_uso69.pdf')
#
#     Convert_ProgressLog_text('progress_log.txt')
#     Text_To_Pdf('progress_log.txt', 'progress_log.pdf')
#
#     click_button(JP.Maximize_live_video_US069)
#     time.sleep(5)
#
#     Merger_Pdf('./progress_log.pdf', './video_uso69.pdf', './us069_0.pdf')
#
#     Remove_File('./video_uso69.pdf')
#     Remove_File('./progress_log.pdf')
#
#     # -------------------------------- RUNTIME MOTOR CONTROL---------------------------------------------------------
#
#     click_button(JP.On_US069)
#     time.sleep(10)
#
#     # Scroll slider
#     Scroll = driver.find_element(By.XPATH, '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div[1]/div[2]/div['
#                                            '2]/div/div/div/div/ul/li[5]/div/div/tx-elements/div[2]/div[1]/div['
#                                            '2]/ng-content[1]/ng-content/tx-elements/div[2]/div/div/form/tx-elements['
#                                            '3]/div[2]/div/div/div[2]/span[3]')
#     ActionChains(driver).drag_and_drop_by_offset(Scroll, 10, 0).perform()
#     time.sleep(10)
#
#     # Open graph and click picture
#     click_button(JP.Time_graph_US069)
#     time.sleep(3)
#
#     Take_Image(JP.Time_graph_path, 'graph_us069_1.pdf')
#
#     click_button(JP.Time_graph_US069)
#     time.sleep(3)
#
#     # Take screen shoot of live video
#     click_button(JP.Maximize_live_video_US069)
#     time.sleep(5)
#
#     Take_Image(JP.Live_video_path_US069, 'video_uso69_live.pdf')
#
#     click_button(JP.Maximize_live_video_US069)
#     time.sleep(5)
#
#     Convert_ProgressLog_text('runtime_us069.txt')
#     Text_To_Pdf('runtime_us069.txt', 'runtime_us069.pdf')
#
#     Merger_Pdf('./runtime_us069.pdf', './video_uso69_live.pdf', './graph_11.pdf')
#     Merger_Pdf('./graph_11.pdf', './graph_us069_1.pdf', './graph_1.pdf')
#     Merger_Pdf('./us069_0.pdf', './graph_1.pdf', './graph_2.pdf')
#
#     Remove_File('./graph_us069_1.pdf')
#     Remove_File('./runtime_us069.pdf')
#     Remove_File('./us069_0.pdf')
#     Remove_File('./graph_1.pdf')
#     Remove_File('./graph_11.pdf')
#     Remove_File('./video_uso69_live.pdf')
# 
#     # Click RPM and take a screen shoot
#     click_button(JP.Rpm_graph_US069)
#     time.sleep(3)
#
#     click_button(JP.Maximize_ram_US069)
#     time.sleep(3)
#
#     Take_Image(JP.Rpm_graph_path, 'graph_us069_2.pdf')
#
#     Convert_ProgressLog_text('runtime_us069_1.txt')
#     Text_To_Pdf('runtime_us069_1.txt', 'runtime_us069_1.pdf')
#
#     Merger_Pdf('./runtime_us069_1.pdf', './graph_us069_2.pdf', './graph_3.pdf')
#     Merger_Pdf('./graph_2.pdf', './graph_3.pdf', './graph_4.pdf')
#
#     Remove_File('./runtime_us069_1.pdf')
#     Remove_File('./graph_us069_2.pdf')
#     Remove_File('./graph_2.pdf')
#     Remove_File('./graph_3.pdf')
#
#     click_button(JP.Maximize_ram_US069)
#
#     # Clicked Motor Data Graph
#     click_button(JP.Motor_graph_US069)
#     time.sleep(3)
#
#     click_button(JP.Maximize_motor_US069)
#     time.sleep(3)
#     Take_Image(JP.Motor_graph_path, 'graph_us069_3.pdf')
#
#     Convert_ProgressLog_text('runtime_us069_2.txt')
#     Text_To_Pdf('runtime_us069_2.txt', 'runtime_us069_2.pdf')
#
#     Merger_Pdf('./runtime_us069_2.pdf', './graph_us069_3.pdf', './graph_5.pdf')
#     Merger_Pdf('./graph_4.pdf', './graph_5.pdf', './us069_1.pdf')
#
#     Remove_File('./runtime_us069_2.pdf')
#     Remove_File('./graph_us069_3.pdf')
#     Remove_File('./graph_4.pdf')
#     Remove_File('./graph_5.pdf')
#
#     click_button(JP.Maximize_motor_US069)
#     time.sleep(3)
#     click_button(JP.Time_US069)
#     time.sleep(3)
#     click_button(JP.Click_off_US069)
#     time.sleep(7)
#
#     # # ---------------------------- SWITCH TO CHARGING PORT---------------------------------------------------------
#
#     # Switch to charging tab
#     click_button(JP.Switch_charging_US069)
#     time.sleep(3)
#
#     # Set the voltage
#     click_button(JP.Charging_voltage_US069)
#     time.sleep(3)
#     click_button(JP.Set_60V_Us069)
#     time.sleep(3)
#     print('Set 60V charging voltage')
#
#     # Target battery voltage
#     click_button(JP.Battery_voltage_US069)
#     time.sleep(3)
#     click_button(JP.Set_54V_Us069)
#     time.sleep(3)
#     print('Set 54V battery voltage')
#
#     # Battery charging current
#     click_button(JP.Battery_current_US069)
#     time.sleep(3)
#     click_button(JP.Set_4A_US069)
#     time.sleep(3)
#     print('Set 4A charging current')
#
#     click_button(JP.Start_charging_US069)
#     time.sleep(25)
#
#     # Maximize the graph and take screen shoot
#     click_button(JP.Maximize_graph_US069)
#     time.sleep(3)
#
#     Take_Image(JP.Graph_path_US069, 'video_us069.pdf')
#
#     Convert_ProgressLog_text('progress_log.txt')
#     Text_To_Pdf('progress_log.txt', 'progress_log.pdf')
#
#     click_button(JP.Maximize_graph_US069)
#     time.sleep(3)
#
#     Merger_Pdf('./progress_log.pdf', './video_us069.pdf', './us069_2.pdf')
#     Merger_Pdf('./us069_1.pdf', './us069_2.pdf', './us069_3.pdf')
#
#     Remove_File('./video_us069.pdf')
#     Remove_File('./progress_log.pdf')
#     Remove_File('./us069_2.pdf')
#     Remove_File('./us069_1.pdf')
#
#     Take_Image(JP.Live_parameters_US069, 'parameter_us069.pdf')
#
#     driver.save_screenshot(screenshot_path + '/US069.png')
#     image.image_to_pdf(screenshot_path + '/US069.png', "full_screen_us069.pdf")
#
#     Merger_Pdf('./parameter_us069.pdf', './full_screen_us069.pdf', './us069_4.pdf')
#     Merger_Pdf('./us069_3.pdf', './us069_4.pdf', './Result_US069.pdf')
#
#     Remove_File('./parameter_us069.pdf')
#     Remove_File('./full_screen_us069.pdf')
#     Remove_File('./us069_4.pdf')
#     Remove_File('./us069_3.pdf')
#
#     # Stop the charging
#     click_button(JP.Stop_charging_US069)
#     time.sleep(5)
#     # Off the radio button
#     click_button(JP.Connect_Button)
# else:
#     print('Some one use this board')
#     driver.save_screenshot(screenshot_path + '/US069.png')
#     image.image_to_pdf(screenshot_path + '/US069.png', "Result_US069.pdf")
