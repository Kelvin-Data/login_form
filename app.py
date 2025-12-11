from pathlib import Path
import pickle
import streamlit as st
import streamlit_authenticator as sa

### USER AUTHNTICATION ###
names = ['Peter Parker', 'Rebecca Miller']
usernames = ['pparker', 'rmiller']
passwords = ['abc123', 'def456']

hashed_passwords = sa.Hasher(passwords).generate()

# store the password into pickle file
file_path = Path(__file__).parent / 'hashed_pw.pk1'

with file_path.open('rb') as file:
    hashed_passwords = pickle.load(file)

# Build credentials dictionary (NEW format)
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

# Create authenticator (NEW signature)
authenticator = sa.Authenticate(
    credentials,
    "sales_dashboard",  # cookie name
    "abcdef",           # cookie key
    cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")
    
if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    st.write("You are logged in!")



# pip install streamlit-authenticator==0.1.5
# bcrypt as hashing method
# cd login_form
# streamlit run app_2.py

    
