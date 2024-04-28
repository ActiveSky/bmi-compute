import streamlit as st
from bmi_calculate import BMICalculator


class Sex:
    Female:str="女"
    Male:str="男"


st.set_page_config(page_title="BMI Calculator App", page_icon=":shark:")

st.title("🌈BMI 计算器")

# sex
md_sex="""
### 1. 请选择性别
"""
st.markdown(md_sex)
sex=st.radio(label="sex",options=[Sex.Female,Sex.Male])

# weight
md_weight="""
### 2. 请输入体重(kg,公斤)
"""
st.markdown(md_weight)
weight=st.number_input(label="weight",min_value=30,max_value=150)


# height
md_height="""
### 3. 请输入身高(m,米)
"""
st.markdown(md_height)
height=st.number_input(label="height",min_value=1.0,max_value=2.5)

# calculate BMI
md_submit="""
### 4. 开始计算
"""
st.markdown(md_submit)
submit_bmi=st.button(label="点击计算")
bmicalculator=BMICalculator()
if submit_bmi:
    bmi,bmi_level=bmicalculator.start(weight,height)
    if bmi is None or bmi_level is None:
        st.error("❎请输入有效的身高和体重数据")
    else:
        st.success("🔥输入成功！")
        st.write("您的BMI指数为:",bmi)
        st.write(f"您的身材为: {bmi_level}.")
    if bmi_level==BMICalculator.OverWeight:
        st.info("⚠️注意: 您的体重已过重，如有需要，请联系我们的健康顾问: xxxxxxxxx")
    elif bmi_level==BMICalculator.UnderWeight:
        st.info("⚠️注意: 您的体重过轻，请加强锻炼!")
    elif bmi_level==BMICalculator.NormalWeight:
        st.info("✅您的体重正常,请继续保持!")
    elif bmi_level==BMICalculator.Obese:
        st.info("❗️❗️❗️您的体重过于肥胖,请联系我们的健康顾问: xxxxxxxxx")

### 4.参考值
md_table="""
### 5. BMI 参考值
"""
st.markdown(md_table)
st.table(bmicalculator.get_bmi_table())


