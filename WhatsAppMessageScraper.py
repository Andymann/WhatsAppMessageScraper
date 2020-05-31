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


while True:
    elemContact = web.find_elements_by_xpath('//span[@class="_3TEwt"]')

    for contact in elemContact:
        # x.click()
        #print("Name:" + contact.text)
        try:
            txtName = contact.text
            contact.click()
            elemText = web.find_elements_by_xpath(
                '//span[@class="_3FXB1 selectable-text invisible-space copyable-text"]')
        # for msg in elemText:
        #    print('Text:' + msg.text)
        except:
            pass

        try:
            bNewMsg = False
            n = len(elemText)
            msgText = elemText[n-1].text
            #print('Last msg:' + msgText)
            if msgText.startswith('.'):
                if txtName in contactDict:
                    # ist der letzte text von einem bekannten kontakt und neu?
                    storedMsg = contactDict[txtName]
                    if msgText != storedMsg:
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
    print('warte 5 Sekunden')
    time.sleep(5)
