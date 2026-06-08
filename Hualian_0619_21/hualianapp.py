import streamlit as st
import streamlit.components.v1 as components
import os

# 自動取得目前 hualianapp.py 所在的資料夾絕對路徑
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 設定頁面標題與圖示
st.set_page_config(page_title="花蓮吵啥之旅", page_icon="🌊", layout="centered")

st.title("🎉 楠梓星巴克退役/現役小隊：花蓮吵啥之旅")
st.markdown("幹人生活著不就是要出去玩嗎？錢賺了就是要花啊你各位啊！")
st.markdown("---")

tab_schedule, tab_accommodation, tab_rafting, tab_members = st.tabs([
    "🗺️ 行程總表", 
    "🏠 住宿資訊", 
    "🚣 泛舟攻略", 
    "😎 出勤人員名單"
])

# ================= 行程表頁面 =================
with tab_schedule:
    day1, day2, day3 = st.tabs(["Day 1 (6/19)", "Day 2 (6/20)", "Day 3 (6/21)"])

    with day1:
        st.header("🌅 Day 1: 爆肝列車與太平洋狂歡")
        st.info("🚆 **05:23-09:50｜新自强 3000-411號車之爆肝列車**\n\n凌晨5:00新左營集合！上車後不用懷疑，全部人準備好直接睡死到花蓮。\n\n**座位：** 4車29號、4車31號、4車41號、4車43號、4車45號、4車47號")
        st.success("🚗 **10:00-12:00｜熱血取車與早午餐**\n\n抵達花蓮火車站，辦理7人座租車手續 (Ryan擔任大司機)。\n\n**租車：** 宏越租車花蓮店")
        
        with st.expander("🍳 點我看早午餐推薦清單"):
            st.markdown("- COUNTRY MOTHER'S\n- 職饗雞湯小卷米粉\n- 花蓮廟口紅茶有限公司\n- 周家蒸餃小籠包")
            
        st.warning("🛶 **13:00-15:00｜下午活動時間**\n\n(依照大家體力決定要不要去海邊或找地方耍廢)")
        st.info("🏠 **17:00-18:00｜Airbnb 休息時刻！**\n\n前往民宿「煦家 HSU+」Check-in 洗澡休息。")
        st.error("🥩 **18:00-20:00｜東大門夜市逛起乃！**\n\n吃爆花蓮小吃，享受慶功最高潮。")

    with day2:
        st.header("🚣‍♂️ Day 2: 秀姑巒溪泛舟大作戰")
        st.info("🚐 **09:00-11:00｜花蓮市區接駁車至向上泛舟**\n\n提早起床喔！花蓮市區集合上接駁車。 (阿丹負責聯繫司機)")
        st.success("🚣 **11:00-15:00｜賣力泛舟中**\n\n體力與意志力的考驗，請記得不要帶手機下水！泛舟一定會全濕，請務必攜帶換洗衣物。")

    with day3:
        st.header("🚂 Day 3: 滿載而歸")
        st.success("🛍️ **白天｜採買花蓮名產自由行**")
        st.info("🚆 **17:29-21:54｜平安抵達高雄啦！**\n\n**座位：** 1車26號、1車28號、1車29號、1車30號、1車31號、1車32號")

    st.markdown("---")
    st.subheader("🗺️ 手繪行程地圖")

    MAP_SVG = """
    <div style="width:100%; max-width:680px; margin: 0 auto;">
    <svg width="100%" viewBox="0 0 680 540" role="img" xmlns="http://www.w3.org/2000/svg">
    <title>花蓮三天兩夜手繪行程地圖</title>
    <defs>
      <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </marker>
    </defs>
    <rect x="380" y="0" width="300" height="540" fill="#daeef8" opacity="0.6"/>
    <rect x="0" y="0" width="400" height="540" fill="#e8f0d8" opacity="0.5"/>
    <path d="M385 20 C388 60, 382 110, 390 160 C396 210, 384 260, 392 310 C398 360, 385 400, 390 450 C394 490, 383 520, 385 540" fill="none" stroke="#6aabca" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="6,2" opacity="0.8"/>
    <rect x="135" y="14" width="210" height="40" rx="10" fill="white" opacity="0.88" stroke="#ddd" stroke-width="1"/>
    <text x="240" y="32" text-anchor="middle" font-size="13" font-family="sans-serif" fill="#333" font-weight="700">🌊 花蓮三天兩夜行程</text>
    <text x="240" y="48" text-anchor="middle" font-size="10" font-family="sans-serif" fill="#888">6/19–6/21</text>
    <text x="490" y="490" text-anchor="middle" font-size="12" font-family="sans-serif" fill="#4a8aaa" font-weight="600" opacity="0.75">太平洋</text>
    </svg>
    </div>
    """
    components.html(MAP_SVG, height=560)

# ================= 住宿資訊頁面 =================
with tab_accommodation:
    st.header("🏠 溫馨狂暴小窩")
    st.subheader("花蓮包棟民宿 - 煦家 HSU+")

    st.markdown("**📍 地址：** 花蓮縣花蓮市國富里國富十三街51號")
    st.markdown("**🔗 IG 網頁：** [airbnb.hsu](https://www.instagram.com/airbnb.hsu/)")
    st.markdown("**📞 房東電話：** 0972258558")

    st.markdown("---")
    st.markdown("### ⏰ 入住與退房時間")
    st.info("✅ **Check in 時間：** 16:00 (行李可先寄放)")
    st.warning("✅ **Check out 時間：** 11:00 (退房後行李可寄放至 15:00)")

    st.markdown("---")
    st.markdown("### 🚨 住宿公約 🚨")
    st.error("🚭 **整棟禁菸！！請 Dennis 特別注意！！！**")

# ================= 泛舟攻略頁面 =================
with tab_rafting:
    st.header("🚣 向上泛舟：行前終極指南")
    
    st.markdown("### 📍 基本資訊")
    st.markdown("**向上泛舟公司 Xiuguluan River Hsiangsun Rafting**")
    st.markdown("**地址：** 花蓮縣瑞穗鄉瑞良村中山路三段216-1號")
    st.markdown("**網址：** [https://hsiangsun.com.tw/](https://hsiangsun.com.tw/)")
    st.markdown("🚌 **接送時間：** 預計上午9點00分 (時間變動以司機訊息為主，阿丹負責聯繫)")
    
    st.markdown("---")
    st.markdown("### 🚨 泛舟活動注意事項 🚨")
    
    st.warning("⚠️ **健康與年齡限制：**\n* 孕婦、氣喘、心臟病、高血壓、癲癇、骨質疏鬆等禁止參加，請主動告知。\n* 0-5歲嬰孩童及65歲以上長者不適合參與。")
    
    st.info("👕 **服裝與裝備：**\n* 請穿著**長袖、長褲** (預防曬傷及擦傷) 及**包腳鞋** (布鞋或防水鞋)。\n* 現場有商店租借鞋子 (租鞋150~200元/雙)。\n* **必帶：** 換洗衣物及毛巾 (泛舟一定會全濕，終點有盥洗間及投幣式吹風機)。")
    
    st.error("🚫 **嚴禁攜帶：**\n* 泛舟過程中，請勿攜帶貴重物品 (如：手機、手錶等)！若在途中損壞遺失皆不負責。")
    
    st.success("🍱 **餐飲與其他：**\n* 活動時間較長，請勿空腹參加活動，活動結束後終點有提供點心 (須以識別帶兌換)。\n* 一艘船乘坐8~10位，人數不足須與其他旅客併船。\n* 寵物不能一起參與泛舟，請事先找好寄宿。")

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
            st.markdown("**角色：** 這零號還强迫大家跟他一起出遊，只能說被提姆討厭不是沒有原因的！")
            st.caption("#狂暴梔子花")

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
            st.markdown("**老婆：** Anny(女同)")
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
            st.markdown("**角色：** 溫蒂的寶貝啊！未來將扛下楠梓晚班S的梁柱，但他其實超爛……")
            st.caption("#智商趨近於0")
