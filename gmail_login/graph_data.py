# import json
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
#
# def click_button(UI_button):
#     live = wait.until(EC.element_to_be_clickable((By.XPATH, UI_button)))
#     live.click()
#
#
# options = webdriver.ChromeOptions()
# # options.add_argument(r'--user-data-dir=C:\Users\THIS PC\Desktop\gmail login\session')
# # options.add_argument('--profile-directory=session')
# options.add_argument("--incognito")
# chrm_caps = webdriver.DesiredCapabilities.CHROME.copy()
# chrm_caps['goog:loggingPrefs'] = {'performance': 'ALL'}
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options,
#                           desired_capabilities=chrm_caps)
# wait = WebDriverWait(driver, 60)
# driver.maximize_window()
# driver.get(JP.url)
# click_button(JP.Connect_Button)
# time.sleep(5)
# while 1:
#     for wsData in driver.get_log('performance'):
#         # print(wsData)
#         wsJson = json.loads((wsData['message']))
#         if wsJson["message"]["method"] == "Network.webSocketFrameReceived":
#             print("[ data ]", wsJson["message"]["params"]["response"]['payloadData'])
#             print("line")
#
#         # if wsJson["message"]["method"] == "Network.webSocketFrameSent":
#         #     print("Tx :" + wsJson["message"]["params"]["response"]["payloadData"])
#         # print(wsData['data'])
#     time.sleep(3)
#
#

