
import streamlit as st


if "savings_balance" not in st.session_state:
    st.session_state.savings_balance = 0
if "current_balance" not in st.session_state:
    st.session_state.current_balance = 0
if "notifications" not in st.session_state:
    st.session_state.notifications = []

def savings_account():
    st.subheader("Savings Account")
    amount = st.number_input("Enter amount", min_value=0.0, step=0.01, format="%.2f")

    if st.button("Deposit to Savings"):
        st.session_state.savings_balance += amount
        st.session_state.notifications.append(f"Deposited ₦{amount:.2f} to Savings Account")

    if st.button("Withdraw from Savings"):
        if amount > st.session_state.savings_balance:
            st.error("Insufficient balance")
        else:
            st.session_state.savings_balance -= amount
            st.session_state.notifications.append(f"Withdrew ₦{amount:.2f} from Savings Account")

    st.write(f"Current Savings Balance: ₦{st.session_state.savings_balance:.2f}")

def current_account():
    st.subheader("Current Account")
    amount = st.number_input("Enter amount", min_value=0.0, step=0.01, format="%.2f", key="current_amount")

    if st.button("Deposit to Current"):
        st.session_state.current_balance += amount
        st.session_state.notifications.append(f"Deposited ₦{amount:.2f} to Current Account")

    if st.button("Withdraw from Current"):
        if amount > st.session_state.current_balance:
            st.error("Insufficient balance")
        else:
            st.session_state.current_balance -= amount
            st.session_state.notifications.append(f"Withdrew ₦{amount:.2f} from Current Account")

    st.write(f"Current Current Account Balance: ₦{st.session_state.current_balance:.2f}")

