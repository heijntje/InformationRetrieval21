from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import tkinter
from tkinter import messagebox
import time


# Just to be sure we want the files that need to be downloaded when training
# (party programmes as pdfs etc.) are downloaded to a separate folder for each profile
# Paths need to be added for each profile for this.
options1 = Options()
options1.add_experimental_option("prefs", {
    "download.default_directory": r"ADD A SPECIFIC FOLDER FOR YOUR DOWNLOADS PROFILE 1 HERE",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
options2 = Options()
options2.add_experimental_option("prefs", {
    "download.default_directory": r"ADD A SPECIFIC FOLDER FOR YOUR DOWNLOADS PROFILE 2 HERE",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
options3 = Options()
options3.add_experimental_option("prefs", {
    "download.default_directory": r"ADD A SPECIFIC FOLDER FOR YOUR DOWNLOADS PROFILE 3 HERE",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
options4 = Options()
options4.add_experimental_option("prefs", {
    "download.default_directory": r"ADD A SPECIFIC FOLDER FOR YOUR DOWNLOADS PROFILE 4 HERE",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
options5 = Options()
options5.add_experimental_option("prefs", {
    "download.default_directory": r"ADD A SPECIFIC FOLDER FOR YOUR DOWNLOADS PROFILE 5 HERE",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
options6 = Options()
options6.add_experimental_option("prefs", {
    "download.default_directory": r"ADD A SPECIFIC FOLDER FOR YOUR DOWNLOADS PROFILE 6 HERE",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

options8 = Options()
options8.add_experimental_option("prefs", {
    "download.default_directory": r"ADD A SPECIFIC FOLDER FOR YOUR DOWNLOADS PROFILE 6c HERE",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# # =============================== SETUP ===============================
# Setting up the drivers
driver1 = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options1)
driver2 = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options2)
driver3 = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options3)
driver4 = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options4)
driver5 = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options5)
driver6 = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options6)
driver7 = webdriver.Chrome(ChromeDriverManager().install())
driver6c = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options8)
driver7c = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(1)

# =============================== Logging into social media accounts ===============================
# Before the experiment starts we manually log in to facebook and instagram
# as specifically instagram will ask to login to show profiles.
# This time is also used to accept the cookies of google, instagram, facebook and twitter manually.
driver1.get("https://www.google.com")
driver2.get("https://www.google.com")
driver3.get("https://www.google.com")
driver4.get("https://www.google.com")
driver5.get("https://www.google.com")
driver6.get("https://www.google.com")
driver7.get("https://www.google.com")
driver6c.get("https://www.google.com")
driver7c.get("https://www.google.com")
time.sleep(5)
messagebox.showinfo("Logged in")

# =============================== TRAINING PART ===============================
# Retrieving the urls used for training
profilesdict = {}

for i in range(1,7):
    file = open("Trainingprofiles/profile" + str(i) + ".txt", "r")
    trainingurls = file.read().splitlines()
    file.close()
    profilesdict['profile' + str(i)] = trainingurls

urlsdict = {}
profile1done = False
profile2done = False
profile3done = False
profile4done = False
profile5done = False

# Actual training, each url is visited by its corresponding driver.
# The driver then stays on that page 5 seconds to give it loading time,
# a screenshot is taken for later control and then moves on.
for urlid in range(len(profilesdict['profile6'])): # Profile 6 is the longest list of urls.
    # a dictionary is created that holds the urls that are loaded in this loop for each driver
    for profid in range(1,7):
        if(urlid < len(profilesdict['profile' + str(profid)])):
            urlsdict['url' + str(profid)] = profilesdict['profile' + str(profid)][urlid]
        else:
            urlsdict['url' + str(profid)] = "https://www.google.com"

    # profile1
    words = urlsdict['url1'].split()
    # We hardcoded the cooky handling in the url txt files, each time we switch to a new website (that has a cookie banner)
    # the xpath with a value of the cookiebutton to click is provided
    # these lines always contain the word "cookies" and therefore always have a length over 1,
    # while the urls always are length 1.
    if(len(words) > 1):
        try:
            driver1.find_element_by_xpath(words[1].replace("_", " ")).click() # the replace is because we change whitespaces in underscores (_) as otherwise the split function will split the xpath element
        except:
            print("1 Cookie button not found for url: " + str(urlid))
    else:
        if(not profile1done):
            try:
                driver1.get(words[0])
            except Exception as e:
                print("Failed to retrieve page: " + str(urlid) + " on driver 1")
                print(e)
            if(words[0] == "https://www.google.com"):
                profile1done = True

    # profile2
    words = urlsdict['url2'].split()
    if(len(words) > 1):
        try:
            driver2.find_element_by_xpath(words[1].replace("_", " ")).click()
        except:
            print("2 Cookie button not found for url: " + str(urlid))
    else:
        if(not profile2done):
            try:
                driver2.get(words[0])
            except Exception as e:
                print("Failed to retrieve page: " + str(urlid) + " on driver 2")
                print(e)
            if(words[0] == "https://www.google.com"):
                profile2done = True

    # profile3
    words = urlsdict['url3'].split()
    if(len(words) > 1):
        try:
            driver3.find_element_by_xpath(words[1].replace("_", " ")).click()
        except:
            print("3 Cookie button not found for url: " + str(urlid))
    else:
        if(not profile3done):
            try:
                driver3.get(words[0])
            except Exception as e:
                print("Failed to retrieve page: " + str(urlid) + " on driver 3")
                print(e)
            if(words[0] == "https://www.google.com"):
                profile3done = True

    # profile4
    words = urlsdict['url4'].split()
    if(len(words) > 1):
        try:
            driver4.find_element_by_xpath(words[1].replace("_", " ")).click()
        except:
            print("4 Cookie button not found for url: " + str(urlid))
    else:
        if(not profile4done):
            try:
                driver4.get(words[0])
            except Exception as e:
                print("Failed to retrieve page: " + str(urlid) + " on driver 4")
                print(e)
            if(words[0] == "https://www.google.com"):
                profile4done = True

    # profile5
    words = urlsdict['url5'].split()
    if(len(words) > 1):
        try:
            driver5.find_element_by_xpath(words[1].replace("_", " ")).click()
        except:
            print("5 Cookie button not found for url: " + str(urlid))
    else:
        if(not profile5done):
            try:
                driver5.get(words[0])
            except Exception as e:
                print("Failed to retrieve page: " + str(urlid) + " on driver 5")
                print(e)
            if(words[0] == "https://www.google.com"):
                profile5done = True

    # profile6
    words = urlsdict['url6'].split()
    if(len(words) > 1):
        try:
            driver6.find_element_by_xpath(words[1].replace("_", " ")).click()
        except:
            print("6 Cookie button not found for url: " + str(urlid))
    else:
        try:
            driver6.get(words[0])
        except Exception as e:
            print("Failed to retrieve page: " + str(urlid) + " on driver 6")
            print(e)

    # profile6control, of course this uses the same url as profile 6
    words = urlsdict['url6'].split()
    if(len(words) > 1):
        try:
            driver6c.find_element_by_xpath(words[1].replace("_", " ")).click()
        except:
            print("6c Cookie button not found for url: " + str(urlid))
    else:
        try:
            driver6c.get(words[0])
        except Exception as e:
            print("Failed to retrieve page: " + str(urlid) + " on driver 6c")
            print(e)


    time.sleep(5)
    if(not profile1done):
        driver1.save_screenshot("screenshotstrain/screen" + str(urlid) + "-1.png")
    if(not profile2done):
        driver2.save_screenshot("screenshotstrain/screen" + str(urlid) + "-2.png")
    if(not profile3done):
        driver3.save_screenshot("screenshotstrain/screen" + str(urlid) + "-3.png")
    if(not profile4done):
        driver4.save_screenshot("screenshotstrain/screen" + str(urlid) + "-4.png")
    if(not profile5done):
        driver5.save_screenshot("screenshotstrain/screen" + str(urlid) + "-5.png")
    driver6.save_screenshot("screenshotstrain/screen" + str(urlid) + "-6.png")
    driver6c.save_screenshot("screenshotstrain/screen" + str(urlid) + "-6c.png")


# =============================== QUERY PART ===============================
# Retrieving the queries from the file
file = open("queries.txt", "r")
queries = file.read().splitlines()
file.close()

base_url = "https://www.google.com/search?q="

# Actual querying, each query is appended to the base url, the page is retrieved and given some time to fully load
# the html of the page is then written to a txt file such that it can later be used for comparison
# a screenshot is saved just for checking for errors and then the script goes back to google.com and waits 16 minutes to go on with the next query
for qid, q in enumerate(queries):
    driver1.get(base_url+q)
    driver2.get(base_url+q)
    driver3.get(base_url+q)
    driver4.get(base_url+q)
    driver5.get(base_url+q)
    driver6.get(base_url+q)
    driver7.get(base_url+q)
    driver6c.get(base_url+q)
    driver7c.get(base_url+q)
    time.sleep(2)

    htmlSource1 = driver1.page_source
    htmlSource2 = driver2.page_source
    htmlSource3 = driver3.page_source
    htmlSource4 = driver4.page_source
    htmlSource5 = driver5.page_source
    htmlSource6 = driver6.page_source
    htmlSource7 = driver7.page_source
    htmlSource6c = driver6c.page_source
    htmlSource7c = driver7c.page_source

    with open("queryhtmls/" + str(qid) + "-1.txt", 'w', encoding="utf-8") as f:
        f.write(htmlSource1)
    with open("queryhtmls/" + str(qid) + "-2.txt", 'w', encoding="utf-8") as f:
        f.write(htmlSource2)
    with open("queryhtmls/" + str(qid) + "-3.txt", 'w', encoding="utf-8") as f:
        f.write(htmlSource3)
    with open("queryhtmls/" + str(qid) + "-4.txt", 'w', encoding="utf-8") as f:
        f.write(htmlSource4)
    with open("queryhtmls/" + str(qid) + "-5.txt", 'w', encoding="utf-8") as f:
        f.write(htmlSource5)
    with open("queryhtmls/" + str(qid) + "-6.txt", 'w', encoding="utf-8") as f:
        f.write(htmlSource6)
    with open("queryhtmls/" + str(qid) + "-7.txt", 'w', encoding="utf-8") as f:
        f.write(htmlSource7)
    with open("queryhtmls/" + str(qid) + "-6c.txt", 'w', encoding="utf-8") as f:
        f.write(htmlSource6c)
    with open("queryhtmls/" + str(qid) + "-7c.txt", 'w', encoding="utf-8") as f:
        f.write(htmlSource7c)

    driver1.save_screenshot("screenshotsquery/screen" + str(qid) + "-1.png")
    driver2.save_screenshot("screenshotsquery/screen" + str(qid) + "-2.png")
    driver3.save_screenshot("screenshotsquery/screen" + str(qid) + "-3.png")
    driver4.save_screenshot("screenshotsquery/screen" + str(qid) + "-4.png")
    driver5.save_screenshot("screenshotsquery/screen" + str(qid) + "-5.png")
    driver6.save_screenshot("screenshotsquery/screen" + str(qid) + "-6.png")
    driver7.save_screenshot("screenshotsquery/screen" + str(qid) + "-7.png")
    driver6c.save_screenshot("screenshotsquery/screen" + str(qid) + "-6c.png")
    driver7c.save_screenshot("screenshotsquery/screen" + str(qid) + "-7c.png")

    driver1.get("https://www.google.com")
    driver2.get("https://www.google.com")
    driver3.get("https://www.google.com")
    driver4.get("https://www.google.com")
    driver5.get("https://www.google.com")
    driver6.get("https://www.google.com")
    driver7.get("https://www.google.com")
    driver6c.get("https://www.google.com")
    driver7c.get("https://www.google.com")
    time.sleep(960) # set to a minimum of 16 minutes

driver.quit()
