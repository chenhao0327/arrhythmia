from __future__ import annotations
import streamlit as st

import pandas as pd
import datetime
import csv
import plotly.graph_objs as go
from PIL import Image


def main():
    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("")
    app_mode = st.sidebar.selectbox("请选择手术类型",
        ["Introduction", "PM","RFCA_AF","RFCA_others"])
    if app_mode == "Introduction":
        st.sidebar.success('欢迎访问陈浩医生的个人网站')
        Introduction()
    elif app_mode == "PM":
        st.sidebar.success('起搏器随访数据')
        PM()
    elif app_mode=="RFCA_AF":
        st.sidebar.success('房颤消融随访数据')
        RFCA_AF()
    elif app_mode=="RFCA_others":
        st.sidebar.success('其他射频消融随访数据')
        RFCA_others()


## 改变网页题目和图标
st.set_page_config(
    page_title="Welcome to Chenhao's Website",
    page_icon="😊",)

## 隐藏footer
hide_streamlit_style = """
            <style>
            # MainMenu {visibility: ;}
            footer {visibility: hidden;}
            footer:after {
                content:'build by Chenhao';
                visibility: visible;
                display: block;
                position: relative;
                # background-color: red;
                padding: 5px;
                top: 2px;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def Introduction():
    st.write("# 欢迎来到陈浩手术的随访数据! 👏🏻")
    st.markdown(
        """
        本网站是陈浩医生私人搭建的随访数据收集网站，为了更好的管理手术患者。

    """
    )

def PM():
    name = st.text_input('姓名（很重要请务必写对）')
    ip=st.text_input('住院号')
    birth = st.date_input('生日（很重要请务必写对）')
    birthage = datetime.date.today().year - birth.year
    age = st.number_input('年龄（岁）',birthage)
    sexual = st.selectbox('性别',options=['男性','女性'])
    pm_date = st.date_input('手术或随访日期')
    pm=st.text_area('手术或随访经过')
    diagnosis = st.selectbox('诊断',options=['S_PM','D_PM','LBBP','ICD','CRT'])

    def inr():
        with open("PM.csv","a+", encoding='utf8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            with open("PM.csv","r", encoding='utf8', newline='') as f:# 以读的方式打开csv，判断是否存在标题
                reader = csv.reader(f)
                if not [row for row in reader]:
                    writer.writerow(["姓名",'住院号',"生日","年龄","性别","手术或随访日期","手术或随访经过",'诊断'])
                    writer.writerow([name,ip,birth,age,sexual,pm_date,pm,diagnosis])
                else:
                    writer.writerow([name,ip,birth,age,sexual,pm_date,pm,diagnosis])

    if __name__ == '__main__':
        if st.button("提交"):
            inr()
    data = pd.read_csv('PM.csv')
    data2 = data.loc[(data['姓名'] == name)]
    data3 = data[['姓名','住院号','手术或随访日期']]
    if st.button("你的既往手术历史"):
        st.table(data2)
    if st.button('所有患者信息'):
        st.table(data3)
    jibing = st.selectbox('你想查什么疾病病人的信息',options=['S_PM','D_PM','LBBP','ICD','CRT'])
    data5 = data.loc[(data['诊断']== jibing)]
    data4 = data5[['姓名','住院号','手术或随访日期']]
    if st.button('你是想查%s病人吗' % jibing):
        st.table(data4)



def RFCA_AF():
    name = st.text_input('姓名（很重要请务必写对）')
    ip=st.text_input('住院号')
    birth = st.date_input('生日（很重要请务必写对）')
    birthage = datetime.date.today().year - birth.year
    age = st.number_input('年龄（岁）',birthage)
    sexual = st.selectbox('性别',options=['男性','女性'])
    pm_date = st.date_input('手术或随访日期')
    pm=st.text_area('手术或随访经过')
    LA=st.number_input('左房前后径（mm）')
    def inr():
        with open("AF.csv","a+", encoding='utf8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            with open("AF.csv","r", encoding='utf8', newline='') as f:# 以读的方式打开csv，判断是否存在标题
                reader = csv.reader(f)
                if not [row for row in reader]:
                    writer.writerow(["姓名",'住院号',"生日","年龄","性别","手术或随访日期","手术或随访经过",'左房前后径'])
                    writer.writerow([name,ip,birth,age,sexual,pm_date,pm,LA])
                else:
                    writer.writerow([name,ip,birth,age,sexual,pm_date,pm,LA])

    if __name__ == '__main__':
        if st.button("提交"):
            inr()
    data = pd.read_csv('AF.csv')
    data2 = data.loc[(data['姓名'] == name)]
    data3 = data[['姓名','住院号','手术或随访日期']]
    if st.button("你的既往手术历史"):
        st.table(data2)
    chart_data = pd.DataFrame(
                data2,
                columns = ['左房前后径','手术或随访日期']
            )
    chart_data = chart_data.sort_values(by='手术或随访日期') # 按检查日期排序
    fig = go.Figure(
                data=[go.Scatter(
                    x=chart_data['手术或随访日期'],
                    y=chart_data['左房前后径'],
                    mode='lines+markers',
                    marker=dict(color='rgb(100, 100, 100)'),
                    line=dict(color='rgb(200, 200, 200)'))],
            )

    fig.update_layout(
                title='%s你的左房前后径变化趋势' % name,
                xaxis_title='检查日期',
                xaxis_showgrid=False,
                xaxis_ticks='outside',
                xaxis_linecolor='rgb(204, 204, 204)',
                xaxis_linewidth=5,

                yaxis_title='左房前后径（mm）',
                yaxis_showgrid=False,
                yaxis_linecolor='rgb(204, 204, 204)',
                yaxis_linewidth=5,

                plot_bgcolor='rgb(240, 240, 240)',
                )
    if st.button('你的左房前后径变化'):
        st.plotly_chart(fig)
    if st.button('所有患者信息'):
        st.table(data3)

def RFCA_others():
    name = st.text_input('姓名（很重要请务必写对）')
    ip=st.text_input('住院号')
    birth = st.date_input('生日（很重要请务必写对）')
    birthage = datetime.date.today().year - birth.year
    age = st.number_input('年龄（岁）',birthage)
    sexual = st.selectbox('性别',options=['男性','女性'])
    pm_date = st.date_input('手术或随访日期')
    pm=st.text_area('手术或随访经过')
    diagnosis=st.selectbox('诊断',options=['AVNRT','AVRT|AP','PVC|VT','PAC|AT','AFL'])
    image0=st.text_input('你的图片')
    def inr():
        with open("others.csv","a+", encoding='utf8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            with open("others.csv","r", encoding='utf8', newline='') as f:# 以读的方式打开csv，判断是否存在标题
                reader = csv.reader(f)
                if not [row for row in reader]:
                    writer.writerow(["姓名",'住院号',"生日","年龄","性别","手术或随访日期","手术或随访经过",'诊断','图片'])
                    writer.writerow([name,ip,birth,age,sexual,pm_date,pm,diagnosis,image0])
                else:
                    writer.writerow([name,ip,birth,age,sexual,pm_date,pm,diagnosis,image0])

    if __name__ == '__main__':
        if st.button("提交"):
            inr()
    data = pd.read_csv('others.csv')
    data2 = data.loc[(data['姓名'] == name)]
    data3 = data[['姓名','住院号','手术或随访日期']]
    ima=data2.iloc[[0],[8]].values[0][0]
    #image = Image.open('%s' % ima)
    if st.button("你的既往手术历史"):
        st.table(data2)
        #st.image(image, caption='%s的图' % name,use_column_width=True)
        st.markdown("%s" % ima)
        #st.markdown("<div ><img src=%s width=60% /></div>"% ima)
    if st.button('所有患者信息'):
        st.table(data3)
    jibing = st.selectbox('你想查什么疾病病人的信息',options=['AVNRT','AVRT|AP','PVC|VT','PAC|AT','AFL'])
    data5 = data.loc[(data['诊断']== jibing)]
    data4 = data5[['姓名','住院号','手术或随访日期']]
    if st.button('你是想查%s病人吗' % jibing):
        st.table(data4)

if __name__ == "__main__":
    main()