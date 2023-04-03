import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

classUrl = "https://app.tophat.com/e/849492/lecture/"


def handleUnansweredQuestion(questionElement):
    questionElement.click()

    multipleChoiceHolder = driver.find_element(
        By.XPATH,
        "//div[@role='radiogroup']",
    )

    # this will answer 'A' every time, it might be better to randomize this
    answerA = multipleChoiceHolder.find_element(By.XPATH, "//label")
    answerA.click()

    print("attempted click A")

    try:
        print("attempted submit")
        submitAnswerButton = driver.find_element(
            By.XPATH, "//button[@data-click-id='submit answer']"
        )
        submitAnswerButton.click()
        print("submitted")
    except selenium.common.exceptions.NoSuchElementException:
        pass  # if the submission is closed, will not find the submit button, this is fine no need to print error


def answerAllQuestions():
    try:
        # this could be made more efficient by navigating the tree directly, though efficiency is not a high concern

        contentTree = driver.find_element(By.XPATH, "//div[@aria-label='Content Tree']")
        li = contentTree.find_element(By.XPATH, "//li")

        questions = li.find_elements(By.XPATH, "./*")

        for question in questions:
            try:
                print("quest found")
                # question.find_element(
                #     By.XPATH, "//div[@class='list-row list-row--unanswered']"
                # )
                handleUnansweredQuestion(question)
            except selenium.common.exceptions.NoSuchElementException:
                pass

            time.sleep(2)

    # this may happen if the elements change on the webpage while in the process of manipulating, this is unlikely but won't crash the program
    except Exception as e1:
        print(e1)


driver = webdriver.Chrome()
driver.get(classUrl)
time.sleep(25)  # it takes about this long to get through the authenticator

while True:
    answerAllQuestions()
    time.sleep(15)
