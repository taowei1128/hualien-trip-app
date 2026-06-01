import streamlit as st
import pandas as pd
import os

# 設定頁面標題與圖示
st.set_page_config(page_title="花蓮慶功之旅", page_icon="🌊", layout="centered")

st.title("🎉 楠梓星巴克退役/現役小隊：花蓮三天兩夜之旅")
st.markdown("把論文跟做不完的飲料拋到腦後，準備上山下海囉！")
st.markdown("---")

# 在最上方加入頁籤切換：新增「住宿資訊」
tab_schedule, tab_accommodation, tab_members = st.tabs(["🗺️ 行程總表", "🏠 住宿資訊", "😎 出勤人員名單"])

# ================= 行程表頁面 =================
with tab_schedule:
    day1, day2, day3 = st.tabs(["Day 1 (6/19)", "Day 2 (6/20)", "Day 3 (6/21)"])

    with day1:
        st.header("🌅 Day 1: 爆肝紅眼列車與海線狂歡")
        st.info("🚆 05:23-09:50：新自強3000 (第4車)。凌晨出發，請在車上睡死補充體力！")
        st.success("🚗 10:00-11:30：花蓮車站合體！領七人座，直奔在地早午餐。")
        st.warning("🏠 11:30-12:00：前往民宿「煦家 HSU+」寄放行李。")
        st.success("🛶 13:30-16:00：(下午大解放) 崇德海灘 SUP 立槳 或 網美咖啡廳看海耍廢。")
        st.info("🔑 16:30-17:30：回民宿正式 Check-in，洗掉一身海水與疲憊。")
        st.error("🥩 18:00-21:00：慶功大餐 ＋ 東大門夜市買醉續攤。")

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
    st.subheader("🎨 專屬手繪行程地圖")
# ================= 住宿資訊頁面 =================
with tab_accommodation:
    st.header("🏠 溫馨狂暴小窩")
    st.subheader("煦家 HSU+ (花蓮包棟民宿)")
    
    st.markdown("**📍 地址：** 花蓮縣花蓮市國富里國富十三街 51 號")
    st.markdown("🗺️ **導航連結：** [點我開啟 Google Map](https://maps.app.goo.gl/ifo8Mmhrmv6K4SEL7)")
    st.markdown("**🔗 IG 網頁：** [airbnb.hsu.ig](https://www.instagram.com/airbnb.hsu/)")
    st.markdown("**📞 房東電話：** 0972-258-558")
    
    st.markdown("---")
    st.markdown("### ⏰ 入住與退房時間")
    st.info("✅ **Check-in：** 6 / 19 - 16:00 (抵達花蓮後可先去寄放行李)")
    st.warning("✅ **Check-out：** 6 / 21 - 11:00 (退房後行李可寄放至 15:00)")
    
    st.markdown("---")
    st.markdown("### 🚨 住宿公約 🚨")
    st.error("🚭 **整棟禁菸！！請 Dennis 特別注意，不要在室內抽菸！！**")

# ================= 出勤人員頁面 =================
with tab_members:
    st.header("🔥 狂暴出勤名單")
    st.write("錢賺了就是要花啊！活著不就是要出去玩嗎？")
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("👑 Taowei"):
            try:
                st.image(os.path.join(BASE_DIR, "taowei.jpg"), use_column_width=True)
            except:
                pass
            st.markdown("**性向：** 謎團")
            st.markdown("**角色：** 這零號還強迫大家跟他一起出遊，只能說被提姆討厭不是沒有原因的！")
            st.caption("#站上的狂暴者")
            
        with st.expander("🌊 Dennis"):
            try:
                st.image(os.path.join(BASE_DIR, "dennis.jpg"), use_column_width=True)
            except:
                pass
            st.markdown("**定位：** 神明之子")
            st.markdown("**角色：** 據說上次哭是看媽祖繞境，陽光大男孩，也是這次旅遊的水上活動教練。")
            st.caption("#我沒有隱形")
            
        with st.expander("👕 Samael"):
            try:
                st.image(os.path.join(BASE_DIR, "samael.jpg"), use_column_width=True)
            except:
                pass
            st.markdown("**老婆：** Anny (女同)")
            st.markdown("**角色：** 不要再給我半夜洗衣服了你他媽的！未來可能被調店的雞掰人！")
            st.caption("#香港定居者")

    with col2:
        with st.expander("☕ Zoe"):
            try:
                st.image(os.path.join(BASE_DIR, "zoe.jpg"), use_column_width=True)
            except:
                pass
            st.markdown("**性生活：** 久遠")
            st.markdown("**角色：** 被情緒勒索導致很晚才從星巴克離職的值班妹，真的很欠罵！")
            st.caption("#P值也有人權")
            
        with st.expander("📚 Tammy"):
            try:
                st.image(os.path.join(BASE_DIR, "tammy.jpg"), use_column_width=True)
            except:
                pass
            st.markdown("**體重：** 天文數字")
            st.markdown("**角色：** 做飲料會讓人很難通過走道，高知識分子未來要去台北念研究所的慾女。")
            st.caption("#性生活要有啊")
            
        with st.expander("👶 Ryan"):
            try:
                st.image(os.path.join(BASE_DIR, "ryan.jpg"), use_column_width=True)
            except:
                pass
            st.markdown("**前女友：** 黃姿穎")
            st.markdown("**角色：** 溫蒂的寶貝啊！未來將扛下楠梓晚班 S 的梁柱，但他其實超爛……")
            st.caption("#智商趨近於0")
