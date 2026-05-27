import streamlit as st
import pandas as pd
import os

# 設定頁面標題與圖示
st.set_page_config(page_title="花蓮慶功之旅", page_icon="🌊", layout="centered")

st.title("🎉 楠梓星巴克退役/現役小隊：花蓮三天兩夜之旅")
st.markdown("把論文跟做不完的飲料拋到腦後，準備上山下海囉！")
st.markdown("---")

# 在最上方加入頁籤切換：分為「行程表」與「出勤人員」
tab_schedule, tab_members = st.tabs(["🗺️ 行程總表", "😎 出勤人員名單"])

# ================= 行程表頁面 =================
with tab_schedule:
    day1, day2, day3 = st.tabs(["Day 1 (6/19)", "Day 2 (6/20)", "Day 3 (6/21)"])

    with day1:
        st.header("🌊 Day 1: 太平洋 Chill 體驗")
        st.info("🚆 上午：搭乘台鐵直達花蓮，車上好好補眠")
        st.success("🛶 下午：崇德海灘 SUP 立槳 / 獨木舟 (看清水斷崖！)")
        st.warning("🥩 晚上：老時光燒肉酒肴大口吃肉 + 東大門夜市")

    with day2:
        st.header("🧗‍♂️ Day 2: 溪谷沁涼大作戰")
        st.info("💦 白天：三棧溪半/全日溯溪，深潭跳水跳起來！")
        st.success("🍔 傍晚：速食炸雞快速補血，或找冷氣咖啡廳耍廢")
        st.warning("🍻 晚上：原住民風味餐與熱炒，海鮮山產點滿桌")

    with day3:
        st.header("🚗 Day 3: 海岸線兜風")
        st.info("🎶 上午：台 11 線兜風 (車上輪播 icyball) -> 石梯坪踏水拍美照")
        st.success("🛍️ 下午：採買花蓮名產 (麻糬、剝皮辣椒等)")
        st.warning("🏠 傍晚：帶著充飽電的身心，搭車返回高雄")

    st.markdown("---")
    st.subheader("🗺️ 重點行程地圖")
    map_data = pd.DataFrame({
        'lat': [23.993, 24.195, 23.978, 24.103, 23.483],
        'lon': [121.601, 121.652, 121.603, 121.602, 121.516],
        'name': ['花蓮火車站', '崇德海灘', '老時光燒肉', '三棧溪', '石梯坪']
    })
    st.map(map_data, zoom=9)

# ================= 出勤人員頁面 =================
with tab_members:
    st.header("🔥 狂暴出勤名單")
    st.write("錢賺了就是要花啊！活著不就是要出去玩嗎？")
    
    # 使用欄位(columns)讓版面看起來像人物卡片
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("👑 Taowei"):
            try:
                st.image("taowei.jpg", use_column_width=True)
            except Exception as e:
                st.warning("照片載入失敗")
            st.markdown("**性向：** 謎團")
            st.markdown("**角色：** 這零號還強迫大家跟他一起出遊，只能說被提姆討厭不是沒有原因的！")
            st.caption("#站上的狂暴者")
            
        with st.expander("🌊 Dennis"):
            try:
                st.image("dennis.jpg", use_column_width=True)
            except Exception as e:
                st.warning("照片載入失敗")
            st.markdown("**定位：** 神明之子")
            st.markdown("**角色：** 據說上次哭是看媽祖繞境，陽光大男孩，也是這次旅遊的水上活動教練。")
            st.caption("#我沒有隱形")
            
        with st.expander("👕 Samael"):
            try:
                st.image("samael.jpg", use_column_width=True)
            except Exception as e:
                st.warning("照片載入失敗")
            st.markdown("**老婆：** Anny (女同)")
            st.markdown("**角色：** 不要再給我半夜洗衣服了你他媽的！未來可能被調店的雞掰人！")
            st.caption("#香港定居者")

    with col2:
        with st.expander("☕ Zoe"):
            try:
                st.image("zoe.jpg", use_column_width=True)
            except Exception as e:
                st.warning("照片載入失敗")
            st.markdown("**性生活：** 久遠")
            st.markdown("**角色：** 被情緒勒索導致很晚才從星巴克離職的值班妹，真的很欠罵！")
            st.caption("#P值也有人權")
            
        with st.expander("📚 Tammy"):
            try:
                st.image("tammy.jpg", use_column_width=True)
            except Exception as e:
                st.warning("照片載入失敗")
            st.markdown("**體重：** 天文數字")
            st.markdown("**角色：** 做飲料會讓人很難通過走道，高知識分子未來要去台北念研究所的慾女。")
            st.caption("#性生活要有啊")
            
        with st.expander("👶 Ryan"):
            try:
                st.image("ryan.jpg", use_column_width=True)
            except Exception as e:
                st.warning("照片載入失敗")
            st.markdown("**前女友：** 黃姿穎")
            st.markdown("**角色：** 溫蒂的寶貝啊！未來將扛下楠梓晚班 S 的梁柱，但他其實超爛……")
            st.caption("#智商趨近於0")

# python -m streamlit run hualianapp.py
