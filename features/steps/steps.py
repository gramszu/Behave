
from behave import *

@given('a text file')
def step_impl(context):
    context.file = open('report.txt', 'r')

@when('we check the file for the words "error" and "OK"')
def step_impl(context):
    context.contents = context.file.read()

@then('the file should contain the word "error"')
def step_impl(context):
    assert 'error' in context.contents

@then('the file should contain the word "OK"')

def step_impl(context):
    assert 'OK' in context.contents


