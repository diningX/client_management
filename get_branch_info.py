import streamlit as st

def get_branch_info(branch_name):
    back = st.sidebar.button('<Back')
    logout = st.sidebar.button('Logout')
    if back:
        st.session_state['login'] = 1
    if logout:
        st.session_state['login'] = 0
    if st.session_state['login'] == 2:
        st.title(branch_name)
        bId = [k for k, v in st.session_state['branch_dic'].items() if v == branch_name][0]
        st.session_state['db'].collection('BranchInfo').where('')
        
