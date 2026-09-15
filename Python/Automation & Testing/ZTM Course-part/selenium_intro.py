from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.chrome.options import Options




def run_automation():
    # shuts down the abilitie to send telemetry info except for letting them know a little bit to the site. 
    os.environ['SELENIUM_MANAGER_OPTOUT'] = 'true'


    #specifying the browser type
    options = Options()
    options.binary_location = '/usr/bin/brave-browser'



    # instantiating the browser object. 
    brave_browser = webdriver.Chrome(options=options)

    try:
        
        # brave_browser.maximize_window()
        
        # executing the object.
        brave_browser.get('https://qaplayground.com/practice/input-fields')
        # print(brave_browser.title)

        # making sure and verify hard wetheter correct title and site. if not it will go in error. 
        assert 'Input Field Automation Practice' in brave_browser.title


        # 1# clear input and submission input
        movieName_Input = brave_browser.find_element(By.ID, "movieNameInput")
        movieName_Input.clear()
        
        some_input1 = "Inception"
        some_input2 = "Matrix"
        movieName_Input.send_keys(some_input2)
        
        # 1# submission button
        time.sleep(1)
        submitMovieBtn = brave_browser.find_element(By.ID, "submitMovieBtn")
        submitMovieBtn.click()

        # 1# verifying hard method that the execution was successful
        output_message = brave_browser.find_element(By.ID, "result-s01")
        assert some_input2 in output_message.text
        print(output_message.text)

        # priority in selectig the selecting method: by id, by name, by css.selector(for complex structure where you need ot find an element in a element), last resort byxpath. 

        # time delay for ethics
        time.sleep(1)

    finally:
        # # because brave is very security you have to explicitly close it
        brave_browser.close()
        # # make sure to exit the operation. 
        # print("terminating browser...")
        brave_browser.quit()


def main():
    run_automation()


if __name__ == "__main__":
    main()


