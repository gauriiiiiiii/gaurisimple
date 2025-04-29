# streamlit_ledger_app.py

import streamlit as st

# Initialize session state
if "ledger" not in st.session_state:
    st.session_state.ledger = []

st.title("💰 Simple Ledger App")

# Input form
with st.form("transaction_form"):
    transaction_type = st.selectbox("Transaction Type", ["income", "expense"])
    amount = st.number_input("Amount (₹)", min_value=0.0, step=0.5)
    description = st.text_input("Description")
    submitted = st.form_submit_button("Add Transaction")

    if submitted:
        st.session_state.ledger.append({
            "type": transaction_type,
            "amount": amount,
            "description": description
        })
        st.success("Transaction added!")

# Display ledger
st.subheader("📒 Ledger")
if st.session_state.ledger:
    for i, transaction in enumerate(st.session_state.ledger, 1):
        st.write(f"{i}. **{transaction['type'].capitalize()}** - ₹{transaction['amount']} : _{transaction['description']}_")
else:
    st.info("No transactions added yet.")

# Calculate and show balance
income = sum(t['amount'] for t in st.session_state.ledger if t['type'] == 'income')
expense = sum(t['amount'] for t in st.session_state.ledger if t['type'] == 'expense')
balance = income - expense

st.subheader("📊 Summary")
st.metric("Total Income", f"₹{income}")
st.metric("Total Expense", f"₹{expense}")
st.metric("Balance", f"₹{balance}")
