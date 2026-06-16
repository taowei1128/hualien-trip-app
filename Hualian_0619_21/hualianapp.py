import streamlit as st
import streamlit.components.v1 as components
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="星巴巴花蓮之旅", page_icon="🌊", layout="centered")

st.title("🎉 楠梓星巴克退役/現役小隊：三天兩夜吵翻花蓮")
st.markdown("把期末和做不完的飲料拋到腦後，來上山下海啦幹！")
st.markdown("---")

tab_schedule, tab_accommodation, tab_rafting, tab_members = st.tabs([
    "🗺️ 行程總表",
    "🏠 住宿資訊",
    "🚣 泛舟資訊",
    "😎 出勤人員名單"
])

# ================= 行程表頁面 =================
with tab_schedule:
    day1, day2, day3 = st.tabs(["Day 1 (6/19)", "Day 2 (6/20)", "Day 3 (6/21)"])

    with day1:
        st.header("🌅 Day 1: 爆肝列車與太平洋狂歡")
        st.info("🚆 **05:23-09:50｜新自強 3000 (411次) 爆肝列車**\n\n凌晨 5:00 新左營集合！上車後不用懷疑，全部人直接睡死到花蓮。\n\n**座位：** 4車 29, 31, 41, 43, 45, 47號")
        st.success("🚗 **10:00-12:00｜熱血取車與早午餐**\n\n抵達花蓮火車站，辦理 7 人座租車手續 (Ryan 擔當大司機！)。\n\n📍導航：[點我開啟 Google Map](https://maps.app.goo.gl/ZCmmj2pddWNP8hgMA)")
        with st.expander("🍳 點我看早午餐推薦清單 (請大司機導航)"):
            st.markdown("**1. COUNTRY MOTHER'S**\n**2. 職饗雞湯小卷米粉**\n**3. 花蓮廟口紅茶有限公司**\n**4. 周家蒸餃小籠包**")
        st.warning("🛍️ **13:00-16:00｜舊鐵道文化商圈逛逛！**\n\n沿著舊鐵道的文創小街，有小吃、飾品、文創品，伴手禮也可以看看！")
        st.success("☕ **16:00-18:00｜海景咖啡廳愜意看夕陽**\n\n有幾間咖啡廳可以做選擇，可隨時調整：\n* 海碉堡 x 穎！咖啡\n* 浪。慢咖啡")
        st.info("🔑 **18:00-20:00｜Airbnb 休息時刻！**\n\n看有沒有人要小睡、滑個手機為自己充電一下！")
        st.error("🥩 **20:00-22:00｜石屋吃燒烤**\n\n📍地址：花蓮縣花蓮市民生里中正路644之2號")
        st.warning("🍻 **22:00 - ｜買酒回民宿聊天睡搞搞**\n\n買好酒水零食，回民宿繼續聊天買醉！")

    with day2:
        st.header("🚣‍♂️ Day 2: 秀姑巒溪泛舟大作戰")
        st.info("🚐 **09:00-11:00｜花蓮市區接駁車至向上泛舟**\n\n提早起床喔！花蓮市區集合上接駁車，大家可以在車上繼續補眠。")
        st.success("🚣 **11:00-16:00｜賣力泛舟中**\n\n賣力泛舟中！**想看郭詩婷落水 😂** 這是一場體力與意志力的考驗，記得不要帶手機下水！")
        st.warning("🚿 **16:00-19:00｜回程與回民宿整理**\n\n搭乘接駁車回到市區，收拾濕掉的衣服！在民宿/飯店休息一下洗個澡。")
        st.error("🍗 **19:00-20:00｜東大門夜市逛起來！**\n\n直接開逛東大門超爽，可以帶回 Airbnb 吃！\n\n**必吃推薦：** 蔣家官財板、法式官財板、強蛋餅、吉香炸蛋蔥油餅、妙不可言果汁...等。")
        st.success("🍻 **20:00 - ｜看要怎樣就怎樣啦！**\n\n玩桌遊！玩畫畫遊戲！聊心事！去深夜景觀咖啡廳！吃花蓮宵夜！主打一個有夠 Chill 😎")

    with day3:
        st.header("🚗 Day 3: 海岸線兜風")
        st.info("🎶 上午：台 11 線兜風 (車上輪播 icyball) -> 石梯坪踏水拍美照")
        st.success("🛍️ 下午：採買花蓮名產 (麻糬、剝皮辣椒等)")
        st.warning("🏠 傍晚：帶著充飽電的身心，搭車返回高雄")

    st.markdown("---")

