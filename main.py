import streamlit as st
import os
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from secret.secret import keys as KEYS
from secret.secret import PASSWORD_MANAGE



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
    st.session_state['PASSWORD_MANAGE'] = os.environ.get('PASSWORD_MANAGE')
    st.session_state['PASSWORD_MANAGE'] = PASSWORD_MANAGE
if st.session_state['login'] == 0:

    st.session_state['db'] = firestore.client()
    st.title('クライアント情報管理画面')
    PASS = st.text_input('PASSWORD')
    LOGIN_BUTTON = st.button('LogIn')
    if LOGIN_BUTTON:
        if PASS == st.session_state['PASSWORD_MANAGE']:
            st.session_state['login'] = 1
        else:
            st.write('passwordがちげえぞ')
            

if st.session_state['login'] == 1:
    st.write('ログイン完了')
    query = st.session_state['db'].collection('ClientInfo')
    docs = query.get()
    client_list = []
    for doc in docs:
        client_data_dic = {}
        client_data = doc.to_dict()
        client_data_dic['client_name'] = client_data['client_name']
        client_data_dic['branch_list'] = {}
        for bId in client_data['bId']:
            branch_data = db.collection('BranchInfo').document(bId)
            branch_data = branch_data.to_dict()
            branch_name = branch_data['branchName']
            client_data_dic['branch_list']['branchName'] = bId
        client_list.append(client_data_dic)
    st.write(client_list)