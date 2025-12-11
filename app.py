from pathlib import Path
import pickle
import streamlit as st
import streamlit_authenticator as sa

### USER AUTHENTICATION ###

# User information
names = ['Peter Parker', 'Rebecca Miller']
usernames = ['pparker', 'rmiller']
passwords = ['abc123', 'def456']

# Load hashed passwords (you already created this file earlier)
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

# New credentials dictionary format
credentials = {
    "usernames": {
        usernames[0]: {
            "name": names[0],
            "password": hashed_passwords[0],
        },
        usernames[1]: {
            "name": names[1],
            "password": hashed_passwords[1],
        },
    }
}

# Authenticator (new signature)
authenticator = sa.Authenticate(
    credentials,
    "sales_dashboard",
    "abcdef",
    cookie_expiry_days=30
)

# NEW login format (fields replaces form_name)
fields = {"Form name": "Login"}

name, authentication_status, username = authenticator.login(fields=fields)

# Login status messages
if authentication_status is False:
    st.error("Username/password is incorrect")

elif authentication_status is None:
    st.warning("Please enter your username and password")

# Successful login
else:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    st.write("You are logged in!")




# pip install streamlit-authenticator==0.1.5
# bcrypt as hashing method
# cd login_form
# streamlit run app_2.py

    

