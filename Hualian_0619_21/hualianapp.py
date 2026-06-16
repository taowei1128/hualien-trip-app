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
        st.info("🚆 **05:23-09:50｜新自強 3000 (411次) 爆肝列車**\n\n凌晨 5:00 新左營集合！上車後不用懷疑，全部人準備好直接睡死到花蓮。\n\n**座位：** 4車 29, 31, 41, 43, 45, 47號")
        st.success("🚗 **10:00-12:00｜熱血取車與早午餐**\n\n抵達花蓮火車站，辦理 7 人座租車手續 (宏越租車花蓮店，Ryan 擔當大司機！)。\n\n📍導航：[點我開啟 Google Map](https://maps.app.goo.gl/ZCmmj2pddWNP8hgMA)")
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
        st.success("🚣 **11:00-16:00｜賣力泛舟中**\n\n賣力泛舟中！**想看郭詩婷落水噎！** 這是一場體力的考驗，記得不要帶手機下水！")
        st.warning("🚿 **16:00-19:00｜回程與回民宿整理**\n\n搭乘接駁車回到市區，收拾濕掉的衣服！在民宿/飯店休息一下洗個澡。")
        st.error("🍗 **19:00-20:00｜東大門夜市逛起來！**\n\n直接開逛東大門超爽，可以帶回 Airbnb 吃！\n\n**必吃推薦：** 蔣家官財板、法式官財板、強蛋餅、吉香炸蛋蔥油餅、妙不可言果汁...等。")
        st.success("🍻 **20:00 - ｜看要怎樣就怎樣啦！**\n\n玩桌遊！玩畫畫遊戲！聊心事！去深夜景觀咖啡廳！吃花蓮宵夜！主打一個有夠 Chill 😎")

    with day3:
        st.header("🎒 Day 3: 歐咪呀給買爆與平安返家")
        st.info("⏰ **09:00-11:00｜起床準備 Check out**\n\n一堆人一定都來不及收！")
        st.success("🍳 **11:00-12:00｜錢記早餐**\n\n📍地址：花蓮縣花蓮市主權里德安一街213號")
        st.warning("🛍️ **12:00-15:30｜歐咪呀給 Time！**\n\n趕快去買！")
        st.error("🚗 **15:30-16:30｜還車與金額結算**\n\n分帳、還車！辛苦大司機 Ryan 了 <3")
        st.info("🚆 **17:29-21:54｜新自強 3000 (432次)，平安抵達高雄啦！**\n\n**座位：** 1車 26, 28, 29, 30, 31, 32號")

    st.markdown("---")


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

# ================= 泛舟攻略頁面 =================
with tab_rafting:
    st.header("🚣 向上泛舟：行前指南")

    st.markdown("### 📍 基本資訊")
    st.markdown("**地址：** 花蓮縣瑞穗鄉瑞良村中山路三段216-1號")
    st.markdown("**網址：** [向上泛舟官方網站](https://hsiangsun.com.tw/)")
    st.markdown("🚌 **接送時間：** 預計上午 09:00")
    st.markdown("⚠️ *(時間變動以司機訊息為主，阿丹負責聯繫)*")
    st.markdown("🗺️ **上車地點：** [點我開啟 Google Map](https://maps.app.goo.gl/mHFimqwgXfm6d1sZ9)")

    st.markdown("---")
    st.markdown("### 🚨 泛舟活動注意事項 🚨")

    st.warning("⚠️ **健康與年齡限制：**\n* 孕婦、氣喘、心臟病、高血壓、癲癇、骨質疏鬆等禁止參加，請主動告知。\n* 0-5歲嬰孩童及65歲以上長者不適合參與。")
    st.info("👕 **服裝與裝備：**\n* 請穿著**長袖、長褲** (預防曬傷及擦傷) 及**包腳鞋** (布鞋或防水鞋)。\n* 現場可租借鞋子 (150~200元/雙)。\n* **必帶：** 換洗衣物及毛巾 (泛舟一定會全濕，終點有盥洗間及投幣吹風機)。")
    st.error("🚫 **嚴禁攜帶：**\n* 過程中請勿攜帶貴重物品 (手機、手錶等)！若損壞遺失皆不負責。")
    st.success("🍱 **其他：**\n* 請勿空腹參加！活動結束後終點有提供點心 (憑識別帶兌換)。\n* 乘船人數：一艘船 8~10 位 (可能需與他人併船)。\n* 寵物不可同行，現場無人看管。")

# ================= 出勤人員頁面 =================
with tab_members:
    st.header("🔥 狂暴出勤名單")
    st.write("錢賺了就是要花啊！活著不就是要出去玩嗎？")

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
            st.markdown("**炮友：** 目前「應該」從缺")
            st.markdown("**角色：** 不要再給我半夜洗衣服了你他媽的！未來可能被調店的雞掰人！")
            st.caption("#香港定居者")

    with col2:
        with st.expander("🍻 Zoe"):
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
