import pyautogui
import time
import pyperclip


#CUSTOMIZE ACCORDINGLY
MSG_BOX = (893,946)
SELECT_MSG = (910,868)
COPY_BUTTON = (747,84)
BARD_TEXT_BOX = (1407,946)
COPY_BUTTON_REGION = (1700, 650, 150, 300)
WA_TEXT_BOX = (542,1013)
TIME_TO_RESPOND = 15

def get_msg_txt():
    #right click on cordinates latest msg
    pyautogui.click(MSG_BOX, button='right')
    time.sleep(1)
    #left click on cordinates select msg
    pyautogui.moveTo(SELECT_MSG, duration=0.2)
    #double click on current mouse position
    pyautogui.doubleClick()
    time.sleep(1)

    pyautogui.click(COPY_BUTTON) #click on copy button

    clipboard_text = pyperclip.paste()

    return clipboard_text

def get_response(query_text):
    #click on cordinates bard text box
    pyautogui.click(BARD_TEXT_BOX)

    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')

    #interval for bing to respond
    time.sleep(TIME_TO_RESPOND)

    #mov mouse 100px up
    # pyautogui.moveRel(0,-150,duration=0.2)

    time.sleep(1)

    # x = pyautogui.locateCenterOnScreen('images/copybut.png',confidence=0.7)
    # pyautogui.click(x)

    #for bard
    selected_region = COPY_BUTTON_REGION
    #scolll down
    pyautogui.moveRel(0,-300,duration=0.7)
    pyautogui.scroll(-1700)

    time.sleep(1)

    x = pyautogui.locateCenterOnScreen('images/dots.png',confidence=0.7,region=selected_region)
    pyautogui.click(x)

    time.sleep(1)
    x = pyautogui.locateCenterOnScreen('images/bardcopy.png',confidence=0.7)
    pyautogui.click(x)

    time.sleep(1)

    bing_response = pyperclip.paste()

    return bing_response

def send_response(response_text):
    pyautogui.click(WA_TEXT_BOX)
    time.sleep(0.5)
    #paste msg using ctrl + v
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.press('enter')

def cycle():
    query_text = get_msg_txt()
    response_text = get_response(query_text)
    time.sleep(1)
    send_response(response_text)
    time.sleep(5)
    return response_text


last_msg = ""
print("Most Recent Msg : ", last_msg)

count = 1
while True:
    msg_text = get_msg_txt()
    if msg_text != last_msg:
        print("Last Msg : ", last_msg)
        print("New Msg : ", msg_text)
        print("Different Message Detected, Now responding")
        cycle()
        last_msg = get_msg_txt()
        time.sleep(2)
    else:
        print("No new messages, Checking Again. Try No:", count)
        count = count + 1
        time.sleep(3)
    
