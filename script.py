from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from creds import login,pwd,hashtag

class TwitterScript:
    def __init__(self):
        
        self.driver = webdriver.Firefox()

    #Login Always must be called first
    def Login(self):
        self.driver.maximize_window()
        self.driver.get('https://twitter.com/login')

        sleep(5)
        logcred = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
        logcred.send_keys(login)
        pwdcred = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
        pwdcred.send_keys(pwd)
        loginbtn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
        loginbtn.click()

        sleep(10)
        #You can acall any of the two available functions here after login in to your account

        # TwitterScript.SearchHashTag(self)
        # TwitterScript.Follow(self)
        # TwitterScript.FollowByHashtag(self)
    
    #Follows the 6 people on the suggestion page , then refreshes it and repeat .
    def Follow(self):
        
        #this link should be altered , put your own id instead of mine 
        self.driver.get('https://twitter.com/i/connect_people?user_id=1248957619387195392')
        sleep(10)
        for X in range(3,9):
            sleep(5)
            followbtn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div['+str(X)+']/div/div/div/div[2]/div[1]/div[2]/div')
            followbtn.click()
            self.driver.refresh()

    #Likes TOP tweets based on #Hashtags
    def SearchHashTag(self):
        search = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input')
        search.send_keys(hashtag)
        search.send_keys(Keys.RETURN)
        sleep(5)
        #loads the tweets 2 time , change the range as you please
        for i in range(1,3):
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(5)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
        sleep(5)
        #likes 5 first posts , change the range for more 
        for X in range(1,5):
           
                like = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div['+str(X)+']/div/div/div/article/div/div[2]/div[2]/div[2]/div[3]/div[3]/div/div')
                like.click()
                sleep(5)

    #Follow people based on #Hashtag 
    def FollowByHashtag(self):
        self.driver.get('https://twitter.com/search?q='+hashtag+'&f=user')
        sleep(5)
        #Follow those you don't already follow and skip those you already do
        #you may wanna adjust this , as a full page loads 37 profiles
        for i in range(1,5):
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(5)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
        sleep(3)
        for X in range(1,9):
            foltext = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div['+str(X)+']/div/div/div/div[2]/div[1]/div[2]/div').text
            if(foltext =='Follow'):
                followbtn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div['+str(X)+']/div/div/div/div[2]/div[1]/div[2]/div')
                followbtn.click()
                sleep(3)
            else:
                X+=1
           
    #Unfollow people
    def Unfollow(self):
        print('Still a WiP')





bot = TwitterScript()
bot.Login()