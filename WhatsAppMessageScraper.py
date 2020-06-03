# https://www.github.com/iamnosa
# Let's import the Selenium package
from selenium import webdriver
import time

# Let's use Firefox as our browser
web = webdriver.Firefox()
web.get('http://web.whatsapp.com')
# input()
time.sleep(6)
contactDict = {}
name = ''
msgText = ''


def getMessage(pContact):
    try:
        #print("Lokation:" + pContact.location)
        #contact = elemContact[x]
        txtName = pContact.text
        pContact.click()
        elemText = web.find_elements_by_xpath(
            '//span[@class="_3FXB1 selectable-text invisible-space copyable-text"]')
        #elemText = web.find_elements_by_class_name("_3_7SH _3DFk6")

        # '//span[@class="_3FXB1 selectable-text invisible-space copyable-text"]')
        # for msg in elemText:
        #    print('Text:' + msg.text)
        #y_relative_coord = elemText.location['y']
        #print("posY:" + y_relative_coord)
    except:
        pass

    try:
        bNewMsg = False
        n = len(elemText)
        msgText = elemText[n-1].text
        #print('Last msg:' + msgText)
        loca = elemText[n-1].location
        print(loca['x'])
        if not msgText.startswith('.'):
            if txtName in contactDict:
                # ist der letzte text von einem bekannten kontakt und neu?
                storedMsg = contactDict[txtName]
                if msgText != storedMsg:
                    if loca['x'] < 600:
                        # dann ersetzen
                        contactDict[txtName] = msgText
                        bNewMsg = True
                        # print('### Neue Message von ' + txtName + ':' + msgText)
                        #chatFile = open("/Users/andyfischer/Desktop/chat.txt", "a")
                        #chatFile.write(txtName + ':' + msgText + "\n\n")
                        # chatFile.close()
                # else:
                    #print('Keine neue MSG von ' + txtName)
            else:
                # dem dictionary hinzufuegen
                #print(txtName + ":" + msgText)
                if loca['x'] < 600:
                    contactDict[txtName] = msgText
                    bNewMsg = True

            if bNewMsg:
                txtInitial = txtName[0:4]

                chatFile = open("/Users/andyfischer/Desktop/chat.txt", "a")
                #chatFile.write(txtName + ':' + msgText + "\n\n")
                chatFile.write(txtInitial + ':' + msgText[0:50] + "\n\n")
                chatFile.close()
                print(txtInitial + ':' + msgText)
    except:
        pass
    # finally:
        # print('------')
    return


while True:
    elemContact = web.find_elements_by_xpath('//span[@class="_3TEwt"]')
    iLen = len(elemContact)
    for x in range(iLen-4, iLen):
        # for contact in elemContact:
        # x.click()
        #print("Name:" + contact.text)
        getMessage(elemContact[x])
    getMessage(elemContact[0])
    #print('warte 2 Sekunden')
    # time.sleep(2)
