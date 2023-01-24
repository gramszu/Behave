Feature: Checking for errors in a text file Report.txt
    As a tester
    I want to be able to check if a text file contains any errors
    So that I can fix them before proceeding

Scenario: Check for errors and OK in file
    Given a text file
    When we check the file for the words "error" and "OK"
    Then the file should contain the word "error"
    And the file should contain the word "OK"