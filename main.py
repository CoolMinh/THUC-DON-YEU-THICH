import streamlit as  st
appetizer=['Bánh mì nướng phomai','súp hành tây Pháp','Salad Caesar','Gỏi cuốn','Bánh mì bơ tỏi']
main = ['Pizza','Pad Thai','Steak','Moussaka','Paella']
dessert=['Cheesecake','Tiramisu','Crème brulée','Panna cotta','Trifle']
with st.form('Thực đơn yêu thích'):
  option1 = st.multiselect('Món khai vị ưu thích của bạn?',appetizer)
  option2 = st.multiselect('Món chính ưu thích của bạn?',main)
  option3 = st.multiselect('Món tráng miệng ưu thích của bạn?',dessert)
  submitted = st.form_submit_button('Submit')
if submitted:
  st.write('các lựa chọn của bạn là:')
  st.write('**1.món khai vị:**')
  if len(options1)==0:
    st.write('Bạn chưa chọn món khai vị')
  else:
    for i in range(len(option1)):
      st.write(option1[i])

  st.write('**2.món chính:**')
  if len(options2)==0:
    st.write('Bạn chưa chọn món chính')
  else:
    for i in range(len(option2)):
      st.write(option2[i])

  st.write('**3.món tráng miệng:**')
  if len(options3)==0:
    st.write('Bạn chưa chọn món tráng miệng')
  else:
    for i in range(len(option3)):
      st.write(option3[i])
      
      