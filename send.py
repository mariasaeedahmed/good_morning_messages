from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
chromepath = r"C:\\web driver\\chromedriver.exe"

# Set Chrome driver options
options = webdriver.ChromeOptions()
options.binary_location = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'  # Change this to the path of your Chrome installation

# Pass the options to the Chrome driver
driver = webdriver.Chrome( options=options)
driver.get("https://www.instagram.com/")
# driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
# driver.find_element()
wait = WebDriverWait(driver, 10)
input_element_username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))

# Now you can interact with the input element
input_element_username.send_keys("")#enter your own username here
wait = WebDriverWait(driver, 10)
input_element_password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))

# Now you can interact with the input element

input_element_password.send_keys("")#enter your password here
wait = WebDriverWait(driver, 5)
login_button= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')))
login_button.click()
sleep(1)
# message_button= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_1p"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[5]/div/div/div/span/div/a/div/div/div/div[1]/svg')))
# message_button.click()
try:
    # Set a longer maximum wait time (e.g., 30 seconds)
    wait = WebDriverWait(driver, 10)

    # If the element is inside an iFrame, switch to the frame first
    # driver.switch_to.frame("frame_name_or_id")

    # Wait until the message button element is present on the page
    message_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_m1"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[5]/div/div/div/span/div/a/div/div/div/div[2]/div')))

    # Click the message button
    message_button.click()

    # Do other interactions with the page as needed...

except TimeoutException as e:
    print("TimeoutException: The element was not found within the specified wait time.")
driver.get("https://www.instagram.com/direct/inbox/?next=%2F")

array_of_recievers=['https://www.instagram.com/direct/t/111875043531777/','https://www.instagram.com/direct/t/100507234687985/','https://www.instagram.com/direct/t/116855713040136/','https://www.instagram.com/direct/t/102668114466877/','https://www.instagram.com/direct/t/113777496682688/','https://www.instagram.com/direct/t/17842542524511050/','https://www.instagram.com/direct/t/116855713040136/','https://www.instagram.com/direct/t/17842160417772257/']
gmorning="Good morning"
joke_part=['Why did the scarecrow win an award? Because he was outstanding in his field!',"Why don't skeletons fight each other? They don't have the guts!","Why couldn't the bicycle stand up by itself? It was two-tired!","Why don't oysters donate to charity?Because they are shellfish!  ","What did one ocean say to the other ocean? Nothing, they just waved!","How do you organize a space party? You planet"]
cute_part=["I BELIEVE IN YOU! GO GET EM AND DONT LET THE MUGGLES GET YOU DOWN","YOU ARE A ROCK STAR AND BOY I AM SO EXCITED THAT THE WORLD WILL GET TO SEE HOW AMAZING YOU ARE TODAY","OKAY BUT LOOK HOW PRETTY YOU ARE! SO GO OUT THERE AND MAKE THEIR JAWS DROP","I MEAN WITH THOSE BRAINS DO YOU REALLY WANNA WASTE ALL THAT POTENTIAL ON SOMETHING BLEH! I THOUGHT NOT SO GO OUT THERE AND TAKE ON THE WORLD","OKAY BUT DAYUMMMMM WITH THAT BRAIN AND FACE COMBINATION IT IS A CRIME TO FEEL BLEH ABOUT YOURSELF SO I BETTER NOT HAVE TO GET YOU UNDER ARREST TODAY"]
reminder=["No matter what happens today REMEMBER GOD IS ON YOUR SIDE<3"]
for i in array_of_recievers:
    driver.get(i)
    time.sleep(5)
    try:
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_a9-- _a9_0')))

        element = driver.find_element(By.XPATH, '//*[@id="mount_0_0_CJ"]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]')
        button.click()
    except:
        print("no not now")


    time.sleep(3)
    #input_message= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_WG"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')))
    #message_button.send_keys("fff")
    #element = driver.find_element_by_css_selector("div.xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.x1iyjqo2.x1gh3ibb.xisnujt.xeuugli.x1odjw0f")
    #driver.find_element_by_css_selector("textarea[placeholder='Message...']").send_keys("message_text")
# Write the message in the text box
    #message_button = wait.until(EC.presence_of_element_located((By.XPATH,("//a[@role = 'textbox']"))))
    #issay pehlay please cut CUT now now
    try:
        element = driver.find_element(By.CSS_SELECTOR, "div.xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.x1iyjqo2.x1gh3ibb.xisnujt.xeuugli.x1odjw0f")
    except:
        print("Element not found. Please check the CSS selector.")
    message = "Hello, this is a test message written using Selenium!"
    #element.send_keys(message)
    time.sleep(5)

# Find the element representing the text box
    #text_box = driver.find_element_by_tag_name('textarea')

# Type the desired message in the text box
    message = f"{gmorning} YOU!! to bring a smile on your face here is a joke: {random.choice(joke_part)}, now i would like to say: {random.choice(cute_part)} and {reminder[0]}"
    #text_box.send_keys(message)
    element.send_keys(message)
    try:
        send_button = driver.find_element(By.CSS_SELECTOR, ".x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1i0vuye.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37.xfs2ol5")
        send_button.click()
        #send_button = driver.find_element_by_css_selector(".x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1i0vuye.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37.xfs2ol5")

    except:
        wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
        try:
            button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_a9--')))
            button.click()
            send_button = driver.find_element(By.CSS_SELECTOR, ".x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1i0vuye.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37.xfs2ol5")
            send_button.click()
        except:
            print("kuch nhi huaa")
        



       
        print("Button not found. Please check the CSS selector.")
   
#//*[@id="mount_0_0_Sd"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]
# Close the browser
#//*[@id="mount_0_0_wX"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]


# Now you can interact with the input element

    
