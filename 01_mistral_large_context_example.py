import os

from dotenv import load_dotenv
from langchain_core.tracers.context import tracing_v2_enabled
from langsmith import traceable
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

load_dotenv()
api_key = os.environ.get("MISTRAL_API_KEY")
model = "mistral-large-latest"
mistral_client = MistralClient(api_key=api_key)

context = """
# Comprehensive Guide to Opening a Bank Account

## 1. Research and Choose a Bank
   - **Sub-steps:**
     - Compare national, regional, and online banks.
     - Review customer service ratings and user reviews.
     - Assess the bank's physical presence and ATM network.
   - **Scenarios:**
     - **High Fees:** Choose a bank with lower fees if cost is a primary concern.
     - **Specific Services Needed:** If you need specific services like wealth management, choose a bank that offers these.

## 2. Decide on the Type of Account
   - **Sub-steps:**
     - Evaluate your need for a savings account vs. checking account.
     - Consider specialized accounts like student, senior, or business accounts.
   - **Scenarios:**
     - **Student Account:** Opt for an account with no minimum balance and lower fees.
     - **High Transaction Volume:** Choose an account that offers unlimited transactions.

## 3. Gather Required Documents
   - **Sub-steps:**
     - Government-issued ID (passport, driver’s license).
     - Social Security number or Individual Taxpayer Identification Number (ITIN).
     - Proof of address (utility bill, lease agreement).
   - **Scenarios:**
     - **Missing Documents:** If missing a document, contact the bank for alternatives.
     - **Name Discrepancies:** Ensure all documents have consistent name information.

## 4. Check Eligibility Requirements
   - **Sub-steps:**
     - Verify age requirements (usually 18+ for standard accounts).
     - Check residency requirements for non-citizens.
   - **Scenarios:**
     - **Minor Applicants:** Consider joint accounts or custodial accounts.
     - **Non-Residents:** Some banks may offer accounts specifically for non-residents.

## 5. Visit the Bank or Access Online Portal
   - **Sub-steps:**
     - Locate a nearby branch or access the bank’s official website.
     - Ensure the website is secure (look for HTTPS and padlock symbol).
   - **Scenarios:**
     - **Limited Branch Access:** If branches are sparse, prioritize banks with strong online services.
     - **High COVID-19 Restrictions:** Prefer online account opening to avoid physical interactions.

## 6. Schedule an Appointment (if needed)
   - **Sub-steps:**
     - Call or use the bank’s online scheduler to book an appointment.
     - Prepare questions or concerns to discuss during the visit.
   - **Scenarios:**
     - **Busy Schedule:** Early or late appointments may be available to fit your schedule.
     - **Need for Translator:** Request language assistance if needed.

## 7. Complete the Application Form
   - **Sub-steps:**
     - Provide personal information: full name, date of birth, contact details.
     - Fill in employment and income information if required.
   - **Scenarios:**
     - **Incomplete Information:** Contact the bank if unsure about certain information.
     - **Business Accounts:** Additional details like business name and registration may be needed.

## 8. Choose Account Features
   - **Sub-steps:**
     - Decide on overdraft protection and account linking.
     - Select additional services like paperless statements or automatic bill pay.
   - **Scenarios:**
     - **Travel Frequently:** Choose accounts with minimal foreign transaction fees.
     - **High Spending Limits Needed:** Select an account with higher spending and withdrawal limits.

## 9. Provide Identification and Documentation
   - **Sub-steps:**
     - Submit identification documents for verification.
     - For online accounts, upload scans or photos of required documents.
   - **Scenarios:**
     - **Incorrect Documents:** If incorrect documents are submitted, contact the bank to resolve the issue.
     - **Lost Documents:** In case of lost documents, explore alternative forms of identification the bank may accept.

## 10. Agree to Terms and Conditions
   - **Sub-steps:**
     - Review the account’s terms, conditions, and fee schedule.
     - Ensure understanding of account maintenance requirements and penalties.
   - **Scenarios:**
     - **Unclear Terms:** Ask for clarification on any confusing terms or conditions.
     - **Fee Concerns:** If fees are high, inquire about ways to avoid them or consider another bank.

## 11. Sign the Application Form
   - **Sub-steps:**
     - Provide a signature electronically or in-person.
     - Keep a copy of the signed agreement for your records.
   - **Scenarios:**
     - **Remote Opening:** E-signature may be required if opening an account online.
     - **Physical Disability:** If unable to sign, discuss alternative methods with the bank.

## 12. Initial Deposit
   - **Sub-steps:**
     - Deposit the required minimum to activate the account.
     - Use cash, check, or electronic transfer for the initial deposit.
   - **Scenarios:**
     - **No Access to Funds:** Contact the bank to discuss options if you cannot make the initial deposit.
     - **Large Initial Deposit:** Confirm the bank’s procedure and any benefits for large deposits.

## 13. Receive Account Details
   - **Sub-steps:**
     - Note down your new account and routing numbers.
     - Keep this information secure and accessible.
   - **Scenarios:**
     - **Lost Details:** Contact the bank immediately if you lose account information.
     - **Multiple Accounts:** Keep records organized to avoid confusion between accounts.

## 14. Set Up Online Banking
   - **Sub-steps:**
     - Create a username and password for online access.
     - Set up security questions and multi-factor authentication if available.
   - **Scenarios:**
     - **Security Concerns:** Use strong passwords and avoid public Wi-Fi when accessing accounts.
     - **Limited Tech Skills:** Request help from the bank’s customer service if needed.

## 15. Activate Debit Card
   - **Sub-steps:**
     - Follow instructions to activate the card via phone or online.
     - Set up a secure PIN for ATM and purchase transactions.
   - **Scenarios:**
     - **Card Not Received:** Report to the bank if the card does not arrive within the expected time.
     - **Forgot PIN:** Follow the bank’s procedures to reset the PIN securely.

## 16. Order Checks (if necessary)
   - **Sub-steps:**
     - Choose a design and quantity of checks.
     - Include necessary information like your name and address.
   - **Scenarios:**
     - **Check Fraud Concern:** Use secure methods to order checks and store them safely.
     - **Name Changes:** Ensure the name on checks matches your legal identification.

## 17. Set Up Mobile Banking
   - **Sub-steps:**
     - Download the bank’s app from a trusted app store.
     - Log in with your online banking credentials.
   - **Scenarios:**
     - **App Compatibility Issues:** Contact customer support if experiencing issues with the app.
     - **Security Features:** Utilize features like fingerprint or facial recognition if available.

## 18. Enable Account Alerts
   - **Sub-steps:**
     - Choose to receive alerts via email, SMS, or app notifications.
     - Set thresholds for alerts, such as low balance or large transactions.
   - **Scenarios:**
     - **Overwhelmed by Alerts:** Customize settings to receive only essential alerts.
     - **Traveling Abroad:** Ensure alerts are set to accommodate international travel.

## 19. Link External Accounts
   - **Sub-steps:**
     - Use online banking to link accounts at other institutions.
     - Verify linked accounts with trial deposits if required.
   - **Scenarios:**
     - **Verification Delays:** Follow up with the bank if trial deposits do not appear.
     - **Multiple Banks:** Maintain a record of all linked accounts and their purposes.

## 20. Enroll in Direct Deposit
   - **Sub-steps:**
     - Provide your employer with your new account and routing numbers.
     - Complete any required direct deposit forms.
   - **Scenarios:**
     - **Employer Restrictions:** Check with your employer about any specific requirements for direct deposit.
     - **Self-Employment:** Set up direct deposits from clients or payment platforms.

## 21. Transfer Existing Funds
   - **Sub-steps:**
     - Arrange for electronic transfers from your old bank.
     - Ensure all outstanding checks from the old account have cleared.
   - **Scenarios:**
     - **Old Bank Delays:** Contact your old bank if funds are not transferred promptly.
     - **Cross-Border Transfers:** Consider exchange rates and fees if transferring internationally.

## 22. Close Old Accounts
   - **Sub-steps:**
     - Confirm that all transactions and transfers are complete.
     - Follow your old bank’s procedure to formally close the account.
   - **Scenarios:**
     - **Remaining Funds:** Ensure all funds are transferred before closing the old account.
     - **Account Closure Fees:** Be aware of any fees associated with closing the account.
"""

prompt = """Please answer based on the provided context only. 
Please do not miss any part of the provided context. 
My question is how do I open a bank account and the context is
context: {context}
answer:
"""

review_prompt = """
Please do not miss any part of the provided context. You earlier answered the question as below
{answer}
and the context for this was
{context}
Please regenerate your answer so that all parts of the provided context is included.
"""


# with tracing_v2_enabled(project_name="mistral_project"):
@traceable(project_name="generate_response_with_review_02")
def generate_response(prompt=prompt,context=context,review=True):
    chat_response = mistral_client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=prompt.format(context=context))]
    )
    # print(chat_response.choices[0].message.content)
    initial_answer = chat_response.choices[0].message.content
    if review:
        reviewed_answer = review_and_regenerate_response(initial_answer=initial_answer,context=context)
        return reviewed_answer
    else:
        return initial_answer


@traceable(project_name="generate_response_with_review_02")
def review_and_regenerate_response(initial_answer,context):
    chat_response = mistral_client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=review_prompt.format(context=context, answer=initial_answer))]
    )
    # print(chat_response.choices[0].message.content)
    return chat_response.choices[0].message.content


if __name__ == "__main__":
    response = generate_response(review=True)
    print("***************RESPONSE****************")
    print(response)
