import streamlit as st
import streamlit.components.v1 as components
import os

# 自動取得目前 hualianapp.py 所在的資料夾絕對路徑
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 設定頁面標題與圖示
st.set_page_config(page_title="星巴巴花蓮之旅", page_icon="🌊", layout="centered")

st.title("🎉 楠梓星巴克退役/現役小隊：三天兩夜吵翻花蓮")
st.markdown("把期末和做不完的飲料拋到腦後，來上山下海啦幹！")
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
        st.info("🚆 **05:23-09:50｜新自強 3000 (411次) 爆肝列車**\n\n凌晨 5:00 新左營集合！上車後不用懷疑，全部人直接睡死到花蓮。\n\n**座位：** 4車 29, 31, 41, 43, 45, 47號")
        st.success("🚗 **10:00-12:00｜熱血取車與早午餐**\n\n抵達花蓮火車站，辦理 7 人座租車手續 (Ryan 擔當大司機！)。")
        
        with st.expander("🍳 點我看早午餐推薦清單 (請大司機導航)"):
            st.markdown("**1. 單一純賣雞湯小卷米粉：** 11點開門，海味滿滿的花蓮必吃神店。\n**2. 森山舍：** 10點開門，日式老屋超好拍，網美打卡首選。\n**3. Country Mother's：** 大份量美式早午餐，班尼迪克蛋超讚。\n**4. 廟口紅茶：** 經典古早味，紅茶配台式馬卡龍與蛋餅。")
            
        st.warning("🏠 **12:30-13:00｜寄放行李**\n\n前往民宿「煦家 HSU+」寄放行李。")
        st.success("🛶 **13:30-16:00｜下午大解放**\n\n崇德海灘 SUP 立槳，或找間網美咖啡廳看海耍廢。")
        st.info("🔑 **16:30-17:30｜民宿 Check-in**\n\n回民宿洗掉一身海水與疲憊。")
        st.error("🥩 **18:00-21:00｜慶功最高潮**\n\n慶功大餐 (老時光) ＋ 東大門夜市買醉續攤。")

    with day2:
        st.header("🚣‍♂️ Day 2: 秀姑巒溪泛舟大作戰")
        st.info("🚐 **09:00｜專車接送 (阿丹負責聯繫司機)**\n\n請準時於指定地點上車！因為有專車，大家可以在車上繼續補眠，不用自己開車。")
        st.success("🚣 **11:00-15:00｜向上泛舟 (瑞穗起點)**\n\n抵達瑞穗，開始長達約 4 小時的泛舟行程。這是一場體力與意志力的考驗，記得不要帶手機下水！")
        st.warning("🚿 **15:00-16:00｜終點長虹橋洗澡與點心**\n\n泛舟一定會全濕！終點有提供盥洗間（提供沐浴乳、洗髮精），還有點心可以憑識別帶兌換。")
        st.error("🚌 **16:00-18:00｜接駁回市區與大餐**\n\n搭乘接駁車回到市區後，直奔餐廳大口吃原住民風味餐或熱炒，彌補今天消耗的體力！")

    with day3:
        st.header("🚗 Day 3: 海岸線兜風")
        st.info("🎶 上午：台 11 線兜風 (車上輪播 icyball) -> 石梯坪踏水拍美照")
        st.success("🛍️ 下午：採買花蓮名產 (麻糬、剝皮辣椒等)")
        st.warning("🏠 傍晚：帶著充飽電的身心，搭車返回高雄")

    st.markdown("---")
    st.subheader("🗺️ 手繪行程地圖")

    MAP_SVG = """
    <div style="width:100%; max-width:680px; margin: 0 auto;">
    <svg width="100%" viewBox="0 0 680 540" role="img" xmlns="http://www.w3.org/2000/svg">
    <title>花蓮三天兩夜手繪行程地圖</title>
    <desc>手繪風格花蓮地圖，標示六個重要景點：花蓮火車站、煦家民宿、崇德海灘、慶功大餐、向上泛舟、石梯坪</desc>
    <defs>
      <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
        <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      </marker>
      <filter id="sketch" x="-5%" y="-5%" width="110%" height="110%">
        <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="4" result="noise"/>
        <feDisplacementMap in="SourceGraphic" in2="noise" scale="1.5" xChannelSelector="R" yChannelSelector="G"/>
      </filter>
    </defs>

    <rect x="380" y="0" width="300" height="540" fill="#daeef8" opacity="0.6"/>
    <rect x="0" y="0" width="400" height="540" fill="#e8f0d8" opacity="0.5"/>

    <path d="M385 20 C388 60, 382 110, 390 160 C396 210, 384 260, 392 310 C398 360, 385 400, 390 450 C394 490, 383 520, 385 540"
      fill="none" stroke="#6aabca" stroke-width="2.5" stroke-linecap="round"
      stroke-dasharray="6,2" opacity="0.8" filter="url(#sketch)"/>

    <path d="M40 100 L60 70 L80 100" fill="none" stroke="#8aaa70" stroke-width="1.5" stroke-linecap="round" opacity="0.5"/>
    <path d="M70 120 L95 85 L120 120" fill="none" stroke="#8aaa70" stroke-width="1.5" stroke-linecap="round" opacity="0.5"/>
    <path d="M55 155 L75 125 L95 155" fill="none" stroke="#8aaa70" stroke-width="1.5" stroke-linecap="round" opacity="0.4"/>
    <path d="M30 200 L55 165 L80 200" fill="none" stroke="#8aaa70" stroke-width="1.5" stroke-linecap="round" opacity="0.4"/>
    <path d="M80 230 L108 195 L136 230" fill="none" stroke="#8aaa70" stroke-width="1.2" stroke-linecap="round" opacity="0.35"/>
    <path d="M35 260 L62 228 L90 260" fill="none" stroke="#8aaa70" stroke-width="1.2" stroke-linecap="round" opacity="0.3"/>
    <path d="M60 300 L90 265 L120 300" fill="none" stroke="#8aaa70" stroke-width="1.2" stroke-linecap="round" opacity="0.3"/>

    <path d="M410 80 Q430 72 450 80" fill="none" stroke="#6aabca" stroke-width="1" stroke-linecap="round" opacity="0.5"/>
    <path d="M460 120 Q480 112 500 120" fill="none" stroke="#6aabca" stroke-width="1" stroke-linecap="round" opacity="0.4"/>
    <path d="M420 200 Q445 192 468 200" fill="none" stroke="#6aabca" stroke-width="1" stroke-linecap="round" opacity="0.4"/>
    <path d="M500 260 Q520 252 540 260" fill="none" stroke="#6aabca" stroke-width="1" stroke-linecap="round" opacity="0.35"/>
    <path d="M430 350 Q455 342 478 350" fill="none" stroke="#6aabca" stroke-width="1" stroke-linecap="round" opacity="0.4"/>
    <path d="M510 420 Q530 412 550 420" fill="none" stroke="#6aabca" stroke-width="1" stroke-linecap="round" opacity="0.35"/>
    <path d="M440 470 Q465 462 488 470" fill="none" stroke="#6aabca" stroke-width="1" stroke-linecap="round" opacity="0.3"/>

    <path d="M365 195 C370 240, 368 290, 372 340 C374 390, 368 430, 370 470"
      fill="none" stroke="#d4904a" stroke-width="2" stroke-dasharray="8,4" stroke-linecap="round" opacity="0.7"/>
    <path d="M285 80 C282 130, 280 180, 278 240 C276 300, 274 360, 270 420"
      fill="none" stroke="#c77b3a" stroke-width="2.5" stroke-linecap="round" opacity="0.5"/>

    <rect x="390" y="292" width="38" height="18" rx="4" fill="#d4904a" opacity="0.85"/>
    <text x="409" y="305" text-anchor="middle" font-size="10" font-family="sans-serif" fill="white" font-weight="600">台11</text>
    <rect x="248" y="192" width="38" height="18" rx="4" fill="#c77b3a" opacity="0.85"/>
    <text x="267" y="205" text-anchor="middle" font-size="10" font-family="sans-serif" fill="white" font-weight="600">台9</text>

    <g filter="url(#sketch)">
      <ellipse cx="290" cy="120" rx="18" ry="18" fill="#f5d66b" stroke="#c8a420" stroke-width="1.5" opacity="0.95"/>
      <text x="290" y="116" text-anchor="middle" font-size="15" font-family="sans-serif">🚆</text>
      <text x="290" y="128" text-anchor="middle" font-size="8" font-family="sans-serif" fill="#7a5c10" font-weight="700">D1</text>
    </g>
    <rect x="312" y="105" width="88" height="30" rx="6" fill="white" opacity="0.9" stroke="#c8a420" stroke-width="1"/>
    <text x="356" y="120" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#5a3e0a" font-weight="600">花蓮火車站</text>
    <text x="356" y="131" text-anchor="middle" font-size="9" font-family="sans-serif" fill="#9a7c40">10:00 抵達</text>

    <g filter="url(#sketch)">
      <ellipse cx="295" cy="162" rx="16" ry="16" fill="#f5d66b" stroke="#c8a420" stroke-width="1.5" opacity="0.95"/>
      <text x="295" y="158" text-anchor="middle" font-size="13" font-family="sans-serif">🏠</text>
      <text x="295" y="170" text-anchor="middle" font-size="8" font-family="sans-serif" fill="#7a5c10" font-weight="700">D1</text>
    </g>
    <rect x="315" y="148" width="88" height="30" rx="6" fill="white" opacity="0.9" stroke="#c8a420" stroke-width="1"/>
    <text x="359" y="163" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#5a3e0a" font-weight="600">煦家 HSU+</text>
    <text x="359" y="174" text-anchor="middle" font-size="9" font-family="sans-serif" fill="#9a7c40">寄放行李</text>

    <g filter="url(#sketch)">
      <ellipse cx="375" cy="212" rx="18" ry="18" fill="#6aabca" stroke="#2c7ea0" stroke-width="1.5" opacity="0.95"/>
      <text x="375" y="208" text-anchor="middle" font-size="15" font-family="sans-serif">🏄</text>
      <text x="375" y="220" text-anchor="middle" font-size="8" font-family="sans-serif" fill="white" font-weight="700">D1</text>
    </g>
    <rect x="182" y="198" width="88" height="30" rx="6" fill="white" opacity="0.9" stroke="#2c7ea0" stroke-width="1"/>
    <text x="226" y="213" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#1a4e6e" font-weight="600">崇德海灘</text>
    <text x="226" y="224" text-anchor="middle" font-size="9" font-family="sans-serif" fill="#4a8eae">SUP 立槳</text>
    <line x1="270" y1="213" x2="356" y2="213" stroke="#2c7ea0" stroke-width="1" stroke-dasharray="3,2" marker-end="url(#arrow)" opacity="0.6"/>

    <g filter="url(#sketch)">
      <ellipse cx="300" cy="258" rx="16" ry="16" fill="#f5d66b" stroke="#c8a420" stroke-width="1.5" opacity="0.95"/>
      <text x="300" y="254" text-anchor="middle" font-size="13" font-family="sans-serif">🥩</text>
      <text x="300" y="266" text-anchor="middle" font-size="8" font-family="sans-serif" fill="#7a5c10" font-weight="700">D1</text>
    </g>
    <rect x="320" y="244" width="90" height="30" rx="6" fill="white" opacity="0.9" stroke="#c8a420" stroke-width="1"/>
    <text x="365" y="259" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#5a3e0a" font-weight="600">慶功大餐</text>
    <text x="365" y="270" text-anchor="middle" font-size="9" font-family="sans-serif" fill="#9a7c40">東大門夜市</text>

    <g filter="url(#sketch)">
      <ellipse cx="260" cy="380" rx="18" ry="18" fill="#5db89a" stroke="#2a7860" stroke-width="1.5" opacity="0.95"/>
      <text x="260" y="376" text-anchor="middle" font-size="15" font-family="sans-serif">🚣</text>
      <text x="260" y="388" text-anchor="middle" font-size="8" font-family="sans-serif" fill="white" font-weight="700">D2</text>
    </g>
    <rect x="140" y="366" width="90" height="30" rx="6" fill="white" opacity="0.9" stroke="#2a7860" stroke-width="1"/>
    <text x="185" y="381" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#1a4e3e" font-weight="600">向上泛舟</text>
    <text x="185" y="392" text-anchor="middle" font-size="9" font-family="sans-serif" fill="#2a7860">專車接送</text>
    <line x1="230" y1="381" x2="242" y2="381" stroke="#2a7860" stroke-width="1" stroke-dasharray="3,2" marker-end="url(#arrow)" opacity="0.6"/>

    <g filter="url(#sketch)">
      <ellipse cx="372" cy="458" rx="18" ry="18" fill="#e87a5a" stroke="#b04028" stroke-width="1.5" opacity="0.95"/>
      <text x="372" y="454" text-anchor="middle" font-size="15" font-family="sans-serif">📸</text>
      <text x="372" y="466" text-anchor="middle" font-size="8" font-family="sans-serif" fill="white" font-weight="700">D3</text>
    </g>
    <rect x="182" y="444" width="86" height="30" rx="6" fill="white" opacity="0.9" stroke="#b04028" stroke-width="1"/>
    <text x="225" y="459" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#5a1a08" font-weight="600">石梯坪</text>
    <text x="225" y="470" text-anchor="middle" font-size="9" font-family="sans-serif" fill="#b04028">踏水拍美照</text>
    <line x1="268" y1="459" x2="353" y2="459" stroke="#b04028" stroke-width="1" stroke-dasharray="3,2" marker-end="url(#arrow)" opacity="0.6"/>

    <path d="M300 274 C296 296, 280 340, 265 365"
      fill="none" stroke="#aaa" stroke-width="1.2" stroke-dasharray="4,3" opacity="0.5" marker-end="url(#arrow)"/>
    <path d="M275 390 C290 410, 340 440, 355 450"
      fill="none" stroke="#aaa" stroke-width="1.2" stroke-dasharray="4,3" opacity="0.5" marker-end="url(#arrow)"/>

    <rect x="22" y="428" width="148" height="100" rx="8" fill="white" opacity="0.85" stroke="#ccc" stroke-width="1"/>
    <text x="96" y="448" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#333" font-weight="600">行程圖例</text>
    <rect x="36" y="456" width="12" height="12" rx="3" fill="#f5d66b" stroke="#c8a420" stroke-width="1"/>
    <text x="54" y="466" font-size="10" font-family="sans-serif" fill="#555">Day 1 景點</text>
    <rect x="36" y="474" width="12" height="12" rx="3" fill="#5db89a" stroke="#2a7860" stroke-width="1"/>
    <text x="54" y="484" font-size="10" font-family="sans-serif" fill="#555">Day 2 景點</text>
    <rect x="36" y="492" width="12" height="12" rx="3" fill="#e87a5a" stroke="#b04028" stroke-width="1"/>
    <text x="54" y="502" font-size="10" font-family="sans-serif" fill="#555">Day 3 景點</text>
    <line x1="36" y1="516" x2="48" y2="516" stroke="#aaa" stroke-width="1.2" stroke-dasharray="4,3"/>
    <text x="54" y="520" font-size="10" font-family="sans-serif" fill="#555">行程順序</text>

    <rect x="135" y="14" width="210" height="40" rx="10" fill="white" opacity="0.88" stroke="#ddd" stroke-width="1"/>
    <text x="240" y="32" text-anchor="middle" font-size="13" font-family="sans-serif" fill="#333" font-weight="700">🌊 花蓮三天兩夜行程</text>
    <text x="240" y="48" text-anchor="middle" font-size="10" font-family="sans-serif" fill="#888">6/19–6/21</text>

    <text x="490" y="490" text-anchor="middle" font-size="12" font-family="sans-serif" fill="#4a8aaa" font-weight="600" opacity="0.75">太平洋</text>
    <text x="70" y="310" text-anchor="middle" font-size="10" font-family="sans-serif" fill="#6a8a50" opacity="0.7" transform="rotate(-90 70 310)">中央山脈</text>
    </svg>
    </div>
    """

    components.html(MAP_SVG, height=560)

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
    st.header("🚣 向上泛舟：行前終極指南")
    
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
    
    st.success("🍱 **餐飲與其他：**\n* 請勿空腹參加！活動結束後終點有提供點心 (憑識別帶兌換)。\n* 乘船人數：一艘船 8~10 位 (可能需與他人併船)。\n* 寵物不可同行，現場無人看管。")

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
