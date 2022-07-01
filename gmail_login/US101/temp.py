# import org.openqa.selenium.chrome.ChromeDriver;
# import  org.openqa.selenium.chrome.ChromeOptions;
#
# public class Geolocation_Popup
# {
# 	public static void main(String[] args)  {
#
# 		System.setProperty("webdriver.chrome.driver","C:\\Automation\\chromedriver_win32\\chromedriver.exe");
# 		ChromeOptions options = new ChromeOptions();
# 		options.addArguments("start-maximized");
# 		options.addArguments("disable-geolocation");
# 		ChromeDriver driver = new ChromeDriver(options);
# 		driver.get("https://www.google.com");
# 	}
#
# }



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.chrome.options import Options
# import time
#
# desired_cap = {
#     'browser_version': '75.0',
#     'os': 'Windows',
#     'os_version': '10',
#     'chromeOptions': {
#         'args': ["--use-fake-device-for-media-stream", "--use-fake-ui-for-media-stream"]
#     }
# }
# driver = webdriver.Remote(command_executor='http://YOUR_USERNAME:YOUR_ACCESS_KEY@hub.browserstack.com/wd/hub',
#                           desired_capabilities=desired_cap)
#
# # WebCam Test
# driver.get("https://webcamtests.com/check")
# time.sleep(5)
# driver.find_element_by_id("webcam-launcher").click()
# time.sleep(5)
#
