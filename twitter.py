from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username="" #Your Username
password="" #Your Password
tweet=""    #The Tweet You want to post 
username2=""#The Person you want to follow

class Twitter:
    def __init__(self, username, password,tweet,username2):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.browser.maximize_window()
        self.username = username
        self.password = password
        self.tweet = tweet

    def login(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        self.browser.find_element_by_xpath("//input[@name='text']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div").click()
        time.sleep(3)
        self.browser.find_element_by_xpath("//input[@name='password']").send_keys(self.password)
        self.browser.find_element_by_xpath("//div[@data-testid='LoginForm_Login_Button']//div[@dir='auto']").click()

    def post_tweet(self):
        self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div").send_keys(self.tweet)
        time.sleep(2)
        self.browser.find_element_by_xpath("//div[@role='button']//div[@dir='auto']//span//span[contains(text(),'Tweet')]").click()

    def post_tweets(self):
        x=15
        while True:
            x+=1
            time.sleep(1)
            if x>1000 :
                break
            self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div").send_keys(x)
            time.sleep(1)
            self.browser.find_element_by_xpath("//div[@role='button']//div[@dir='auto']//span//span[contains(text(),'Tweet')]").click()

    def follow(self):
        self.browser.get("https://twitter.com/"+username2)
        time.sleep(5)
        self.browser.find_element_by_css_selector("span[class='css-901oao css-16my406 css-bfa6kz r-poiln3 r-a023e6 r-rjixqe r-bcqeeo r-qvutc0'] span[class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0']").click()
        
    def Unfollow(self):
        self.browser.get("https://twitter.com/"+username2)
        time.sleep(5)
        self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div[3]/div/div/div/span/span").click()
        time.sleep(5)
        self.browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span").click()




Twt=Twitter(username,password,tweet,username2)
Twt.login()
time.sleep(5)
#Twt.post_tweet()
#Twt.post_tweets()
Twt.follow()
#Twt.Unfollow()

