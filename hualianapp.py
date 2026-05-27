import streamlit as st
import pandas as pd

# 設定頁面標題與圖示，這會在 iOS 加入主畫面時顯示
st.set_page_config(page_title="花蓮慶功之旅", page_icon="🌊", layout="centered")

st.title("🎉 花蓮三天兩夜慶功之旅")
st.markdown("口試大魔王退散！把 DEA 複雜度分析拋到腦後，準備上山下海囉！")

# 使用 tabs 來切換每天行程，在手機上滑動點擊非常直覺
tab1, tab2, tab3 = st.tabs(["Day 1 (6/19)", "Day 2 (6/20)", "Day 3 (6/21)"])

with tab1:
    st.header("🌊 Day 1: 太平洋 Chill 體驗")
    st.info("🚆 上午：搭乘台鐵直達花蓮，車上好好補眠")
    st.success("🛶 下午：崇德海灘 SUP 立槳 / 獨木舟 (看清水斷崖！)")
    st.warning("🥩 晚上：老時光燒肉酒肴大口吃肉 + 東大門夜市")

with tab2:
    st.header("🧗‍♂️ Day 2: 溪谷沁涼大作戰")
    st.info("💦 白天：三棧溪半/全日溯溪，深潭跳水跳起來！")
    st.success("🍔 傍晚：速食炸雞快速補血，或找冷氣咖啡廳耍廢")
    st.warning("🍻 晚上：原住民風味餐與熱炒，海鮮山產點滿桌")

with tab3:
    st.header("🚗 Day 3: 海岸線兜風")
    st.info("🎶 上午：台 11 線兜風 (車上輪播 icyball) -> 石梯坪踏水拍美照")
    st.success("🛍️ 下午：採買花蓮名產 (麻糬、剝皮辣椒等)")
    st.warning("🏠 傍晚：帶著充飽電的身心，搭車返回高雄")

st.markdown("---")

# 加入簡單的景點分佈地圖，方便手機上直接查看相對位置
st.subheader("🗺️ 重點行程地圖")
# 花蓮幾個主要景點的概略經緯度
map_data = pd.DataFrame({
    'lat': [23.993, 24.195, 23.978, 24.103, 23.483],
    'lon': [121.601, 121.652, 121.603, 121.602, 121.516],
    'name': ['花蓮火車站', '崇德海灘', '老時光燒肉', '三棧溪', '石梯坪']
})
# 顯示地圖
st.map(map_data, zoom=9)