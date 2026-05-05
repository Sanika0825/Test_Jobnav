import pytest
import time
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.excel_utils import ExcelUtils

# Load test data from Excel
excel_file = "test_data.xlsx"
excel_utils = ExcelUtils(excel_file)
test_data = excel_utils.get_data()

class TestSignup:
    @pytest.mark.parametrize("data", test_data, ids=[f"Row_{d.get('row_index')}" for d in test_data])
    def test_signup_flow(self, driver, data):
        # Extract data from the dictionary, handling None values gracefully
        first_name = data.get("First_Name") if data.get("First_Name") is not None else ""
        last_name = data.get("Last_Name") if data.get("Last_Name") is not None else ""
        phone = data.get("Phone") if data.get("Phone") is not None else ""
        email = data.get("Email") if data.get("Email") is not None else ""
        password = data.get("Password") if data.get("Password") is not None else ""
        row_index = data.get("row_index")

        expected_result = data.get("Expected_Result")
        
        # Initialize Page Objects
        home_page = HomePage(driver)
        signup_page = SignupPage(driver) 

        try:
            # Execute Test Steps
            home_page.navigate_to_home()
            home_page.click_join_now()

            # Fill Signup form
            signup_page.select_job_seeker()
            signup_page.fill_first_name(first_name)
            signup_page.fill_last_name(last_name)
            signup_page.fill_phone(phone)
            signup_page.fill_email(email)
            signup_page.fill_password(password)
            
            signup_page.submit_form()
            
            # If the expected result is not "Pass", we assume it's the exact text of an error message we expect to see
            if expected_result and expected_result.lower() != "pass":
                # Check if the specific error message appeared on the screen
                error_displayed = signup_page.is_text_displayed(expected_result)
                assert error_displayed, f"Expected error message '{expected_result}' was not displayed on the page."
            else:
                # Optional sleep to wait for page transition if it's a valid signup
                time.sleep(3) 
            
            # Write "Pass" to the Excel sheet
            excel_utils.update_status(row_index, "Status", "Pass")
            
        except Exception as e:
            # Write "Fail" to the Excel sheet
            excel_utils.update_status(row_index, "Status", "Fail")
            raise e  # Re-raise to fail the test in pytest output
