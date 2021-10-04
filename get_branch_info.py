import streamlit as st


def get_branch_info(branch_name, bId):
    
    st.title(branch_name)
    branch_data = st.session_state['db'].collection('BranchInfo').document(bId).get().to_dict()
    
    
    prefecture = st.text_input('都道府県', value=branch_data['prefecture'])
    manicipality = st.text_input('市町村', value=branch_data['manicipality'])
    user_name = st.text_input('user name', value=branch_data['user_name'])
    password = st.text_input('password', value=branch_data['password'])
    home_page_url = st.text_input('ホームページ URL', value=branch_data['sns'][0])
    facebook_url = st.text_input('Facebook URL', value=branch_data['sns'][1])
    line_url = st.text_input('LINE URL', value=branch_data['sns'][2])
    twitter_url = st.text_input('Twitter URL', value=branch_data['sns'][3])
    instagram_url = st.text_input('Instagram URL', value=branch_data['sns'][4])
    type0 = st.text_input('店舗タイプ1', value=branch_data['type'][0])
    type1 = st.text_input('店舗タイプ2', value=branch_data['type'][1])
    type2 = st.text_input('店舗タイプ3', value=branch_data['type'][2])
    type3 = st.text_input('店舗タイプ4', value=branch_data['type'][3])
    type4 = st.text_input('店舗タイプ5', value=branch_data['type'][4])
    
    save_button = st.button('保存')
    if save_button:
        branch_data['prefecture'] = prefecture
        branch_data['manicipality'] = manicipality
        branch_data['user_name'] = user_name
        branch_data['password'] = password
        branch_data['sns'][0] = home_page_url
        branch_data['sns'][1] = facebook_url
        branch_data['sns'][2] = line_url
        branch_data['sns'][3] = twitter_url
        branch_data['sns'][4] = instagram_url
        branch_data['type'][0] = type0
        branch_data['type'][0] = type1
        branch_data['type'][0] = type2
        branch_data['type'][0] = type3
        branch_data['type'][0] = type4
        st.session_state['db'].collection('BranchInfo').document(bId).set(branch_data)
        st.write('保存しました！')
        