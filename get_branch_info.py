import streamlit as st

def get_branch_info(branch_name, bId):
    back = st.sidebar.button('<Back')
    logout = st.sidebar.button('Logout')
    if back:
        st.session_state['login'] = 1
    if logout:
        st.session_state['login'] = 0
    if st.session_state['login'] == 2:
        st.title(branch_name)
        branch_data = st.write(st.session_state['db'].collection('BranchInfo').document(bId).get().to_dict())
        
        prefecture = st.text_input('都道府県', value=branch_data['prefecture'])
        manicipality = st.text_input('市町村', value=branch_data['manicipality'])
        user_name = st.text_input('ユーザーネーム', value=branch_data['user_name'])
        password = st.text_input('password', value=branch_data['password'])
        home_page_url = st.text_input('ホームページ URL', value=branch_data['sns'][0])
        facebook_url = st.text_input('Facebook URL', value=branch_data['sns'][1])
        line_url = st.text_input('LINE URL', value=branch_data['sns'][2])
        twitter_url = st.text_input('Twitter URL', value=branch_data['sns'][3])
        instagram_url = st.text_input('Instagram URL', value=branch_data['sns'][4])
        type0 = st.text_input('店舗タイプ１', value=branch_data['type'][0])
        type1 = st.text_input('店舗タイプ１', value=branch_data['type'][1])
        type2 = st.text_input('店舗タイプ１', value=branch_data['type'][2])
        type3 = st.text_input('店舗タイプ１', value=branch_data['type'][3])
        type4 = st.text_input('店舗タイプ１', value=branch_data['type'][4])
        
        
        save_button = st.button('保存')
            

        
