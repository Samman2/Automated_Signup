import pytest
import re
import time
import requests
from playwright.sync_api import Page, expect

MAIL_DOMAIN = "gmail.com"
EMAIL = f"{test}@{MAIL_DOMAIN}"

def test_full_signup_flow(page: Page):
#Navigation 
    page.goto("https://authorized-partner.vercel.app/")
    page.get_by_role("button", name="Join Us Now").first.click()
    
# Case : Continue without I agree checkbox
    page.get_by_role("button", name="Continue").click()

    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Continue").click()

# Filling data 
    page.get_by_placeholder("Enter Your First Name").fill("Automation")
    page.get_by_placeholder("Enter Your Last Name").fill("Tester")
    page.get_by_placeholder("Enter Your Email Address").fill(EMAIL)
    page.get_by_placeholder("00-00000000").fill("9711111111")
    
# Case : Checking password mismatched
    password_fields = page.locator('input[type="password"]')
    password_fields.nth(0).fill("S123456789!")
    password_fields.nth(1).fill("S987654321!")
    page.get_by_role("button", name="Next").click()
  
    # Correction 
    password_fields.nth(1).fill("S123456789!")
    page.get_by_role("button", name="Next").click()
    
    #Note 
    # Otp verification cannot be automated as the otp was sent to the user's phone no and its a manual process
    # (Correction : otp was not sent in user's email as the website says Email verification code ) 
    
    print("\n>>> PAUSE: Check your phone for the OTP.")
    otp_code = input("Enter the 6-digit OTP from your phone: ")
    
    page.wait_for_selector("text=Email Verification code", timeout=10000)
    
    otp_inputs = page.locator("input[maxlength='1'], .otp-input-container input, input[type='text']")
    otp_inputs.first.wait_for(state="visible")
    
    for i in range(6):
        otp_inputs.nth(i).fill(otp_code[i])
    page.get_by_role("button", name="Verify Code").click()

    
    