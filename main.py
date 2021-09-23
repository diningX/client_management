import streamlit as st
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from secret import keys as KEYS



if not firebase_admin._apps:

    
    # 初期済みでない場合は初期化処理を行う
    keys = {
    "type": os.environ.get('type'),
    "project_id": os.environ.get('project_id'),
    "private_key_id": os.environ.get('private_key_id'),
    "private_key": os.environ.get('private_key'),
    "client_email": os.environ.get('client_email'),
    "client_id": os.environ.get('client_id'),
    "auth_uri": os.environ.get('auth_uri'),
    "token_uri": os.environ.get('token_uri'),
    "auth_provider_x509_cert_url": os.environ.get('auth_provider_x509_cert_url'),
    "client_x509_cert_url": os.environ.get('client_x509_cert_url')
    }
    
    keys = KEYS
    
    #print(type(keys))

    #json_open = open('keys.json', 'w')
    #json.dump(keys, json_open, indent=2)
    #json_open.close()
    #json_open = open('keys.json', 'r')
    #json_file = json.load(json_open)
    #print('=========================')
    #print(json_file)
    #print('=========================')

    cred = credentials.Certificate(keys)
    firebase_admin.initialize_app(cred)

if 'login' not in st.session_state:
    st.session_state['login'] = 0
if 'password_manage' not in st.session_state:
    st.session_state['password_manage'] = os.environ.get('PASSWORD_MANAGE')
if st.session_state['login'] == 0:

    st.session_state['db'] = firestore.client()
    st.title('クライアント情報管理画面')
    PASS = st.text_input('PASSWORD')
    if PASS == st.session_state['PASSWORD_MANAGE']:
        st.session_state['login'] = 1
    else:

    