import streamlit as st

def branch_registration():
    logout = st.sidebar.button('Logout')
    if logout:
        st.session_state['login'] = 0
    client = st.selectbox('クライアント', st.session_state['client_list'].keys())
    branch_name = st.text_input('Branch Name')
    user_name = st.text_input('user_name')
    password = st.text_input('password')
    bussinessHours1 = st.text_input('bussiness hours 1 ex(11.00.15.00)')
    bussinessHours2 = st.text_input('bussiness hours 1 ex(18.00.23.00)')
    lotteryDiscountRate = st.number_input('lotteryDiscountRate(抽選割引率)(%)', min_value=0, max_value=100, value=int(50))
    lotteryProbability = st.number_input('lotteryProbability(抽選当選確率)(%)', min_value=0, max_value=100, value=int(50))
    questionnaireDiscountRate = st.number_input('questionnaireDiscountRate(アンケート割引率)(%)', min_value=0, max_value=100, value=int(50))
    prefecture = st.text_input('prefecture(都道県)')
    manicipality = st.text_input('manicipality(市町村)')
    phoneNumber = st.text_input('phoneNumber(電話番号)　ex(012-3456-7890)')

    home_page_url = st.text_input('ホームページ URL')
    facebook_url = st.text_input('Facebook URL')
    line_url = st.text_input('LINE URL')
    twitter_url = st.text_input('Twitter URL')
    instagram_url = st.text_input('Instagram URL')

    type0 = st.text_input('店舗タイプ1')
    type1 = st.text_input('店舗タイプ2')
    type2 = st.text_input('店舗タイプ3')
    type3 = st.text_input('店舗タイプ4')
    type4 = st.text_input('店舗タイプ5')
    
    save_button = st.button('登録')
    if user_name in st.session_state['branch_user_name_list']:
        st.write('同じ店舗のユーザーネームが存在します')
    elif (len(user_name) == 0) or (len(password) == 0) or (len(branch_name) == 0):
        st.write('ユーザーネーム、パスワード、branchNameを入力して下さい')
    elif len(password) < 4:
        st.write('パスワードは５字以上にして下さい')
    elif (len(prefecture) == 0) or (len(manicipality) == 0):
        st.write('都道府県、市町村を入力して下さい')
    elif len(phoneNumber) == 0:
        st.write('電話番号を入力して下さい')
    else:
        st.session_state['branch_user_name_list'].append(user_name)
        branch_data = {'user_name':user_name, 'password':password,
            'branchName':branch_name, 'businessHours':[bussinessHours1, bussinessHours2], 'lotteryDiscountRate':lotteryDiscountRate, 
            'lotteryProbability':lotteryProbability, 'questionnaireDiscountRate':questionnaireDiscountRate, 'prefecture':prefecture, 'manicipality':manicipality,
            'phoneNumber':phoneNumber, 'sns':[home_page_url,facebook_url,line_url,twitter_url,instagram_url], 'type':[type0,type1,type2,type3,type4]}
        st.session_state['db'].collection('BranchInfo').add(branch_data)
        _ = st.session_state['db'].collection('BranchInfo').where('user_name', '==', user_name).get()
        for d in _:
            bId = d.id
        st.session_state['client_list'][client][branch_name] = bId
        _ = st.session_state['db'].collection('ClientInfo').where('clientName', '==', client).get()
        for c in _:
            cId = c.id
        client_data = st.session_state['db'].collection('ClientInfo').document(cId).get().to_dict()
        client_data['bId'].append(bId)
        st.session_state['db'].collection('ClientInfo').document(cId).set(client_data)



def client_registration():
    logout = st.sidebar.button('Logout')
    if logout:
        st.session_state['login'] = 0
    clientName = st.text_input('Clinet Name')
    user_name = st.text_input('user_name')
    password = st.text_input('password')

    save_button = st.button('登録')
    if save_button:
        if user_name in st.session_state['client_user_name_list']:
            st.write('同じユーザーネームのクライアントが存在します。')
        elif len(user_name) == 0:
            st.write('user_nameを入力してください')
        elif len(password) < 5:
            st.write('パスワードはパスワードは５字以上にして下さい')
        else:
            st.write('登録完了')
            client_data = {'clientName':clientName, 'user_name':user_name, 'password':password, 'bId':[]}
            st.session_state['db'].collection('ClientInfo').add(client_data)
            st.session_state['client_user_name_list'].append(user_name)