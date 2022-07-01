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
# options = webdriver.ChromeOptions()
# options.add_argument(r'--user-data-dir=C:\Users\THIS PC\Desktop\gmail login\session')
# options.add_argument('--profile-directory=session')
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
# actions = ActionChains(driver)
# wait = WebDriverWait(driver, 60)
# url = JP.url
# e = datetime.datetime.now()
#
# driver.maximize_window()
#
# # -------------------------------------------- STAGE-1 START---------------------------------------------------------
#
# # Start creating text file for progress msg
# handler = open(screenshot_path + "/JP158_Stage-1.text", "+a")
#
# # Clicks the radio button for start the live program
# driver.get(url)
# button = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Connect_Button)))
# button.click()
# time.sleep(10)
#
# # Scroll the window step by step
# SCROLL_PAUSE_TIME = 1
# for i in range(1, 9):
#     x_path = f'//*[@id="helpCarousel"]/div[{i}]'
#     actions.move_to_element(driver.find_element(By.XPATH, x_path)).perform()
#     time.sleep(SCROLL_PAUSE_TIME)
# time.sleep(5)
#
#
# def click_button(button):
#     live = wait.until(EC.element_to_be_clickable((By.XPATH, button)))
#     live.click()
#
#
# click_button(JP.Live_Button)
# # clicks the live button for saw the live part
# live = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Live_Button)))
# live.click()
#
# handler.write(e.strftime("Date %d-%m-%Y Time %I:%M %p\n").center(150))
# handler.write('Automatic click of the live button\n')
# time.sleep(5)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
#
# time.sleep(5)
#
# # Clicks 3w radio button
# oneButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Three_Watt_Button)))
# oneButton.click()
#
# handler.write(e.strftime("Time %I:%M %p\n").center(135))
# handler.write('Automatic click of the 3w button\n')
# time.sleep(5)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
# time.sleep(5)
#
# handler.close()
#
# Battery_Image = driver.find_element(By.XPATH, JP.Three_watt_Battery)
# Battery_Image.screenshot(screenshot_path + '/ThreeWatt_battery.png')
# image.image_to_pdf(screenshot_path + '/ThreeWatt_battery.png', "ThreeWatt_battery.pdf")
#
# handler.close()
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "/JP158_Stage-1.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='l')
#
# pdf.output("Stage-1.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Stage-1.pdf")
# merger.append("ThreeWatt_battery.pdf")
# merger.write("Result_Stage-1.pdf")
# merger.close()
#
# # -------------------------------------------- STAGE-2 START---------------------------------------------------------
#
# handler = open(screenshot_path + "/JP158_Stage-2.text", "+a")
#
# # Clicks 8w radio button
# twoButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Eight_Watt_Button)))
# twoButton.click()
#
# handler.write(e.strftime("Time %I:%M %p\n").center(135))
# handler.write('Automatic click of the 8w button\n')
# time.sleep(5)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
# time.sleep(5)
#
# Battery_Image = driver.find_element(By.XPATH, JP.Three_watt_Battery)
# Battery_Image.screenshot(screenshot_path + '/EightWatt_battery.png')
# image.image_to_pdf(screenshot_path + '/EightWatt_battery.png', "EightWatt_battery.pdf")
# time.sleep(5)
#
# handler.close()
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "/JP158_Stage-2.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='L')
#
# pdf.output("Stage-2.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Stage-2.pdf")
# merger.append("EightWatt_battery.pdf")
# merger.write("Result_Stage-2.pdf")
# merger.close()
#
# # # -------------------------------------------- STAGE-3 START---------------------------------------------------------
#
# handler = open(screenshot_path + "/JP158_Stage-3.text", "+a")
#
# # Clicks 11w radio button
# threeButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Eleven_Watt_Button)))
# threeButton.click()
# time.sleep(10)
#
# handler.write(e.strftime("Time %I:%M %p\n").center(135))
# handler.write('Automatic click of the 11w button\n')
# time.sleep(5)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
# time.sleep(5)
#
# Battery_Image = driver.find_element(By.XPATH, JP.Three_watt_Battery)
# Battery_Image.screenshot(screenshot_path + '/ElevenWatt_battery.png')
# image.image_to_pdf(screenshot_path + '/ElevenWatt_battery.png', "ElevenWatt_battery.pdf")
# time.sleep(5)
#
# handler.close()
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "/JP158_Stage-3.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='L')
#
# pdf.output("Stage-3.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Stage-3.pdf")
# merger.append("ElevenWatt_battery.pdf")
# merger.write("Result_Stage-3.pdf")
# merger.close()
#
# merger = PdfFileMerger()
# merger.append("Result_Stage-1.pdf")
# merger.append("Result_Stage-2.pdf")
# merger.append("Result_Stage-3.pdf")
#
# merger.write("Main.pdf")
# merger.close()
#
# os.remove("Stage-1.pdf")
# os.remove("ThreeWatt_battery.pdf")
# os.remove("Stage-2.pdf")
# os.remove("EightWatt_battery.pdf")
# os.remove("Stage-3.pdf")
# os.remove("ElevenWatt_battery.pdf")
# os.remove("Result_Stage-1.pdf")
# os.remove("Result_Stage-2.pdf")
# os.remove("Result_Stage-3.pdf")
#
# # # -------------------------------------------- STAGE-4 START---------------------------------------------------------
#
# handler = open(screenshot_path + "/JP158_Stage-4.text", "+a")
#
# # clicks next button
# nextButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Next_Button)))
# nextButton.click()
# time.sleep(1)
#
# handler.write(e.strftime("Time %I:%M %p\n").center(135))
# handler.write('Automatic click of the Next button\n')
# time.sleep(1)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
# time.sleep(1)
#
# Battery_Image = driver.find_element(By.XPATH, JP.Three_watt_Battery)
# Battery_Image.screenshot(screenshot_path + '/Next_Button.png')
# image.image_to_pdf(screenshot_path + '/Next_Button.png', "Next_Button.pdf")
# time.sleep(5)
#
# handler.close()
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "/JP158_Stage-4.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='L')
#
# pdf.output("Stage-4.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Main.pdf")
# merger.append("Stage-4.pdf")
# merger.append("Next_Button.pdf")
# merger.write("Main_Next_button.pdf")
# merger.close()
#
# os.remove("Stage-4.pdf")
# os.remove("Main.pdf")
# os.remove("Next_Button.pdf")
# time.sleep(5)
#
# # # -------------------------------------------- STAGE-5 SsTART---------------------------------------------------------
#
# handler = open(screenshot_path + "/Previous_Button_Stage-5.text", "+a")
#
# # clicks previous button
# preButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Previous_Button)))
# preButton.click()
# time.sleep(1)
#
# handler.write(e.strftime("Time %I:%M %p\n").center(135))
# handler.write('Automatic click of the Previous button\n')
# time.sleep(1)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
# time.sleep(1)
#
# Battery_Image = driver.find_element(By.XPATH, JP.Three_watt_Battery)
# Battery_Image.screenshot(screenshot_path + '/Previous_Button.png')
# image.image_to_pdf(screenshot_path + '/Previous_Button.png', "Previous_Button.pdf")
# time.sleep(1)
#
# handler.close()
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "/Previous_Button_Stage-5.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='L')
#
# pdf.output("Stage-5.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Main_Next_button.pdf")
# merger.append("Stage-5.pdf")
# merger.append("Previous_Button.pdf")
#
# merger.write("Main_Previous_button.pdf")
# merger.close()
#
# os.remove("Main_Next_button.pdf")
# os.remove("Stage-5.pdf")
# os.remove("Previous_Button.pdf")
#
# time.sleep(5)
#
# # # -------------------------------------------- STAGE-6 START---------------------------------------------------------
#
#
# handler = open(screenshot_path + "/LCD_Button_Stage-6.text", "+a")
#
# # clicks LCD button
# lcdButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Led_Button)))
# lcdButton.click()
# time.sleep(1)
#
# handler.write(e.strftime("Time %I:%M %p\n").center(135))
# handler.write('Automatic click of the LCD button\n')
# time.sleep(1)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
# time.sleep(1)
#
# Battery_Image = driver.find_element(By.XPATH, JP.Three_watt_Battery)
# Battery_Image.screenshot(screenshot_path + '/LCD_Button.png')
# image.image_to_pdf(screenshot_path + '/LCD_Button.png', "LCD_Button.pdf")
# time.sleep(1)
#
# handler.close()
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "/LCD_Button_Stage-6.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='L')
#
# pdf.output("Stage-6.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Main_Previous_button.pdf")
# merger.append("Stage-6.pdf")
# merger.append("LCD_Button.pdf")
#
# merger.write("Main_LCD_button.pdf")
# merger.close()
#
# os.remove("Main_Previous_button.pdf")
# os.remove("Stage-6.pdf")
# os.remove("LCD_Button.pdf")
#
# time.sleep(5)
#
# # # -------------------------------------------- STAGE-7 START---------------------------------------------------------
#
#
# handler = open(screenshot_path + "/Temperature_Button_Stage-7.text", "+a")
#
# # clicks temperature button
# tempButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Temp_Button)))
# tempButton.click()
# time.sleep(1)
#
# handler.write(e.strftime("Time %I:%M %p\n").center(135))
# handler.write('Automatic click of the Temperature button\n')
# time.sleep(1)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
# time.sleep(1)
#
# Battery_Image = driver.find_element(By.XPATH, JP.Three_watt_Battery)
# Battery_Image.screenshot(screenshot_path + '/Temperature_Button.png')
# image.image_to_pdf(screenshot_path + '/Temperature_Button.png', "Temperature_Button.pdf")
# time.sleep(1)
#
# handler.close()
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "/Temperature_Button_Stage-7.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='L')
#
# pdf.output("Stage-7.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Main_LCD_button.pdf")
# merger.append("Stage-7.pdf")
# merger.append("Temperature_Button.pdf")
#
# merger.write("Main_Temperature_button.pdf")
# merger.close()
#
# os.remove("Main_LCD_button.pdf")
# os.remove("Stage-7.pdf")
# os.remove("Temperature_Button.pdf")
#
# time.sleep(5)
#
# # # -------------------------------------------- STAGE-8 START---------------------------------------------------------
#
#
# handler = open(screenshot_path + "/Humidity_Button_Stage-8.text", "+a")
#
# # clicks humidity button
# humidityButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Humidity_Button)))
# humidityButton.click()
# time.sleep(1)
#
# handler.write(e.strftime("Time %I:%M %p\n").center(135))
# handler.write('Automatic click of the Humidity button\n')
# time.sleep(1)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
# time.sleep(1)
#
# Battery_Image = driver.find_element(By.XPATH, JP.Three_watt_Battery)
# Battery_Image.screenshot(screenshot_path + '/Humidity_Button.png')
# image.image_to_pdf(screenshot_path + '/Humidity_Button.png', "Humidity_Button.pdf")
# time.sleep(1)
#
# handler.close()
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "/Humidity_Button_Stage-8.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='L')
#
# pdf.output("Stage-8.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Main_Temperature_button.pdf")
# merger.append("Stage-8.pdf")
# merger.append("Humidity_Button.pdf")
#
# merger.write("Main_Humidity_button.pdf")
# merger.close()
#
# os.remove("Main_Temperature_button.pdf")
# os.remove("Stage-8.pdf")
# os.remove("Humidity_Button.pdf")
#
# time.sleep(5)
#
# # # -------------------------------------------- STAGE-9 START---------------------------------------------------------
#
#
# handler = open(screenshot_path + "/Graph_Open_Stage-9.text", "+a")
#
# # Maximize the graph button
# graphOpenButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Graph_Open_Button)))
# graphOpenButton.click()
# time.sleep(5)
#
# handler.write(e.strftime("Time %I:%M %p\n").center(135))
# handler.write('Automatic click of the Graph button\n')
# time.sleep(5)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
# time.sleep(10)
#
# handler.close()
#
# # Take picture of that graph
# graphImage = driver.find_element(By.XPATH, JP.Graph_Image)
# graphImage.screenshot(screenshot_path + '/JP158graph.png')
# image.image_to_pdf(screenshot_path + '/JP158graph.png', "Graph_image.pdf")
# time.sleep(10)
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "/Graph_Open_Stage-9.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='L')
#
# pdf.output("Stage-9.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Main_Humidity_button.pdf")
# merger.append("Stage-9.pdf")
# merger.append("Graph_image.pdf")
#
# merger.write("Main_Graph_button.pdf")
# merger.close()
#
# os.remove("Main_Humidity_button.pdf")
# os.remove("Stage-9.pdf")
# os.remove("Graph_image.pdf")
#
# time.sleep(5)
#
# # Minimize the graph button
# graphCloseButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Graph_Close_Button)))
# graphCloseButton.click()
# time.sleep(5)
#
# # # -------------------------------------------- STAGE-10 START---------------------------------------------------------
#
#
# handler = open(screenshot_path + "/Video_Open_Stage-10.text", "+a")
#
# # Maximize the video button
# videoOpenButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Video_Open_button)))
# videoOpenButton.click()
# time.sleep(10)
#
# handler.write(e.strftime("Time %I:%M %p\n").center(135))
# handler.write('Automatic click of the Video button\n')
# time.sleep(5)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
# time.sleep(5)
#
# handler.close()
#
# # Take picture of the video page
# videoImage = driver.find_element(By.XPATH, JP.Video_Image)
# videoImage.screenshot(screenshot_path + '/JP158video.png')
# image.image_to_pdf(screenshot_path + '/JP158video.png', "Video_image.pdf")
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "/Video_Open_Stage-10.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='L')
#
# pdf.output("Stage-10.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Main_Graph_button.pdf")
# merger.append("Stage-10.pdf")
# merger.append("Video_image.pdf")
#
# merger.write("Main_Video_button.pdf")
# merger.close()
#
# os.remove("Main_Graph_button.pdf")
# os.remove("Stage-10.pdf")
# os.remove("Video_image.pdf")
#
# time.sleep(5)
#
# # Minimize the graph button
# videoCloseButton = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Video_Close_Button)))
# videoCloseButton.click()
# time.sleep(5)
#
# # # -------------------------------------------- STAGE-11 START---------------------------------------------------------
#
# # Pic image and save
# driver.save_screenshot(screenshot_path + '/JP158.png')
# image.image_to_pdf(screenshot_path + '/JP158.png', "Full_Page.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Main_Video_button.pdf")
# merger.append("Full_Page.pdf")
#
# merger.write("Main_Page.pdf")
# merger.close()
#
# os.remove("Main_Video_button.pdf")
# os.remove("Full_Page.pdf")
#
# # -------------------------------------------- STAGE-11 START---------------------------------------------------------
#
# handler = open(screenshot_path + "/Automation_Output.text", "+a")
#
# # Off the radio button
# button = wait.until(EC.element_to_be_clickable((By.XPATH, JP.Disconnect_Button)))
# button.click()
# time.sleep(5)
#
# handler.write(e.strftime("Time %I:%M %p\n").center(135))
# handler.write('Automatic click of the Connect button for close the program \n')
# time.sleep(5)
#
# handler.write(e.strftime("Time %I:%M %p\n"))
# handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
# time.sleep(5)
#
# handler.close()
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "/Automation_Output.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='L')
#
# pdf.output("Stage-12.pdf")
# pdf.close()
#
# merger = PdfFileMerger()
# merger.append("Main_Page.pdf")
# merger.append("Stage-12.pdf")
#
# merger.write("Automation_Output_Final.pdf")
# merger.close()
#
# os.remove("Main_Page.pdf")
# os.remove("Stage-12.pdf")
