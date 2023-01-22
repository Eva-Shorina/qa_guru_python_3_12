import pytest
from allure_commons.types import Severity
from selene.support.shared import browser
import allure

@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'eva.shorina')
@allure.feature('Авторизация')
@allure.link('https://github.com', name='Testing')
def test_passed_1():
    pass

def test_passed_1():
    browser.open('https://demoqa.com/automation-practice-form')
    pass

def test_passed_2():
    browser.open('https://demoqa.com/automation-practice-form')
    pass

def test_passed_3():
    browser.open('https://demoqa.com/automation-practice-form')
    pass

def test_passed_4():
    browser.open('https://demoqa.com/automation-practice-form')
    pass

def test_passed_5():
    browser.open('https://demoqa.com/automation-practice-form')
    pass

@pytest.mark.skip(reason='Изменились требования к задаче')
def test_skipped_1():
    browser.open('https://demoqa.com/automation-practice-form')
    pass

@pytest.mark.skip(reason='Требуется доработка')
def test_skipped_2():
    browser.open('https://demoqa.com/automation-practice-form')
    pass

@pytest.mark.skip(reason='Не найдена документация')
def test_skipped_3():
    browser.open('https://demoqa.com/automation-practice-form')
    pass

def test_failed_1():
    browser.open('https://demoqa.com/automation-practice-form')
    assert 1==0