



import streamlit as st
st.title("🎓 MT Business School")
st.set_page_config(page_title="Accounting Quiz", layout="centered")

st.title("🧾 Accounting Multiple Choice Quiz")

questions = [
    {
        "question": "1. Which of the following is an asset?",
        "options": ["Accounts Payable", "Rent Expense", "Cash", "Owner’s Equity"],
        "answer": "Cash"
    },
    {
        "question": "2. What does the accounting equation state?",
        "options": ["Assets = Revenue + Expenses", "Assets = Liabilities + Owner’s Equity",
                    "Assets = Liabilities - Owner’s Equity", "Assets = Owner’s Equity – Liabilities"],
        "answer": "Assets = Liabilities + Owner’s Equity"
    },
    {
        "question": "3. Which financial statement shows a company's financial position at a specific point in time?",
        "options": ["Income Statement", "Statement of Cash Flows", "Balance Sheet", "Retained Earnings Statement"],
        "answer": "Balance Sheet"
    },
    {
        "question": "4. Which of the following is a liability account?",
        "options": ["Equipment", "Notes Payable", "Capital", "Supplies"],
        "answer": "Notes Payable"
    },
    {
        "question": "5. Which account is increased with a debit?",
        "options": ["Revenue", "Liability", "Asset", "Capital"],
        "answer": "Asset"
    },
    {
        "question": "6. Which principle requires that revenue is recognized when earned?",
        "options": ["Matching Principle", "Revenue Recognition Principle", "Historical Cost Principle", "Full Disclosure Principle"],
        "answer": "Revenue Recognition Principle"
    },
    {
        "question": "7. What is the purpose of depreciation?",
        "options": ["To value an asset at market price", "To spread the cost of an asset over its useful life",
                    "To increase the net income", "To avoid paying taxes"],
        "answer": "To spread the cost of an asset over its useful life"
    },
    {
        "question": "8. Which of the following is a contra-asset account?",
        "options": ["Accumulated Depreciation", "Accounts Receivable", "Equipment", "Accounts Payable"],
        "answer": "Accumulated Depreciation"
    },
    {
        "question": "9. What type of account is “Service Revenue”?",
        "options": ["Asset", "Liability", "Equity", "Revenue"],
        "answer": "Revenue"
    },
    {
        "question": "10. What does the term “accrued expenses” mean?",
        "options": ["Expenses paid in advance", "Expenses incurred but not yet paid", "Expenses that are never recorded",
                    "Expenses for the next period"],
        "answer": "Expenses incurred but not yet paid"
    },
]

user_answers = []
score = 0

with st.form("quiz_form"):
    for i, q in enumerate(questions):
        user_answer = st.radio(q["question"], q["options"], key=f"q{i}")
        user_answers.append(user_answer)

    submitted = st.form_submit_button("Submit")

if submitted:
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    st.success(f"🎉 Your Score: {score} / {len(questions)}")

    if score == len(questions):
        st.balloons()
    elif score >= 7:
        st.info("Well done! You passed.")
    else:
        st.warning("Keep practicing! Try again.")
