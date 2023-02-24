import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#UPDATE THIS, ex) classUrl = "https://app.tophat.com/e/3479473/lecture/"
classUrl = "https://app.tophat.com/e/SOME NUMBER/lecture/"


def handleUnansweredQuestion(questionElement):
    questionElement.click()

    multipleChoiceHolder = driver.find_element(
        By.XPATH,
        "//div[@class='MultipleChoiceQuestionAnswerableItemstyles__StyledContainer-sc-6bz3d1-0 bZyhdo']",
    )

    # this will answer 'A' every time, it might be better to randomize this
    answerA = multipleChoiceHolder.find_element(By.XPATH, "//label")
    answerA.click()

    try:
        submitAnswerButton = driver.find_element(
            By.XPATH, "//button[@data-click-id='submit answer']"
        )
        submitAnswerButton.click()
    except selenium.common.exceptions.NoSuchElementException:
        pass  # if the submission is closed, will not find the submit button, this is fine no need to print error


def answerAllQuestions():
    try:
        # this could be made more efficient by navigating the tree directly, though efficiency is not a high concern
        questions = driver.find_elements(
            By.XPATH, "//li[@style='overflow: initial; opacity: 1; height: 52px;']"
        )

        for question in questions:
            try:
                question.find_element(
                    By.XPATH, "//div[@class='list-row list-row--unanswered']"
                )
                handleUnansweredQuestion(question)
            except selenium.common.exceptions.NoSuchElementException:
                pass # if cant find the element, no reason to print exception

            time.sleep(2)

    # this may happen if the elements change on the webpage while in the process of manipulating, this is unlikely but won't crash the program
    except selenium.common.exceptions.StaleElementReferenceException as e1:
        print(e1)


driver = webdriver.Chrome()
driver.get(classUrl)
time.sleep(25)  # it takes about this long to get through the authenticator

while True:
    answerAllQuestions()
    time.sleep(15)
