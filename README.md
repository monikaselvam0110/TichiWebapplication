# TichiWebapplication
QA testing project for the Tichi Web Application featuring Login and Signup test cases, defect reporting, and Login automation using Selenium WebDriver.
# Assignment Deliverables

This repository contains all deliverables required for the QA Intern Technical Assignment.

## 1. Test Case Document

A comprehensive manual test case document has been prepared covering both Login and Signup modules.

### Login Test Coverage

The Login module includes test cases for:

- Valid Login
- Invalid Email
- Invalid Password
- Invalid Email & Password
- Empty Email
- Empty Password
- Empty Email and Password
- Invalid Email Format
- Leading and Trailing Spaces
- Maximum Email Length
- Password Visibility Toggle
- Continue Button Validation
- Forgot Password
- Session Validation
- Logout
- UI Validation
- Required Field Validation
- Boundary Value Testing
- Negative Testing
- Positive Testing

---

### Signup Test Coverage

The Signup module includes test cases for:

- Valid Signup
- Mandatory Field Validation
- Empty First Name
- Empty Last Name
- Empty Email
- Empty Mobile Number
- Empty Password
- Empty Confirm Password
- Invalid Email Format
- Duplicate Email
- Duplicate Mobile Number
- Password Mismatch
- Password Complexity Validation
- Mobile Number Validation
- First Name Validation
- Last Name Validation
- Terms & Conditions Validation
- Password Visibility Toggle
- Boundary Value Testing
- Positive Testing
- Negative Testing
- UI Validation

---

Total Manual Test Cases

- Login Test Cases : 75+
- Signup Test Cases : 75+
- Total Test Cases : 150+

---

## 2. Defect Report

A defect report has been created for the issue identified during testing.

### Defect Details

| Field | Value |
|--------|-------|
| Defect ID | BUG-001 |
| Module | Login |
| Title | Invalid Email Format Accepted During Login |
| Severity | High |
| Priority | High |
| Status | Open |
| Reported By | Justish Kanth D |

### Description

The application allows users to proceed with an invalid email format instead of validating the email before authentication.

### Steps to Reproduce

1. Open the Login page.
2. Enter an invalid email.
   Example:
   ```
   abc
   ```
3. Click Continue/Login.
4. Observe the behavior.

### Expected Result

The application should display an error message such as:

> Please enter a valid email address.

The Continue/Login button should not proceed.

### Actual Result

The application accepts the invalid email format and proceeds to the next step.

### Severity

High

### Priority

High

### Status

Open

---

## 3. Automation Testing

Automation has been implemented using Selenium WebDriver with Python.

### Automated Modules

✔ Login

✔ Signup

### Automation Features

- Selenium WebDriver
- Explicit Waits
- Element Synchronization
- JavaScript Click
- Screenshot Capture
- Exception Handling
- Functional Validation

---

## Automation Test Scenarios

### Login

| Test Scenario | Status |
|--------------|--------|
| Valid Login | PASS |
| Invalid Password | PASS |
| Empty Email | PASS |
| Empty Password | PASS |
| Forgot Password Navigation | PASS |
| Invalid Email Format | FAIL |

---

### Signup

| Test Scenario | Status |
|--------------|--------|
| Valid Signup | PASS |
| Mandatory Fields | PASS |
| Password Mismatch | PASS |
| Duplicate Email | PASS |
| Terms & Conditions Validation | PASS |
| Email Validation | PASS |

---

## Execution Summary

| Metric | Result |
|---------|---------|
| Total Automated Tests | 10 |
| Passed | 9 |
| Failed | 1 |
| Pass Percentage | 90% |
| Failed Due To | Login Email Validation Defect |


│   └── Validation Screenshots
```
