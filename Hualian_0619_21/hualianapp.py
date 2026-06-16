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
    st.subheader("🗺️ 手繪行程地圖")

    MAP_SVG = """
    <div style="width:100%; max-width:680px; margin: 0 auto;">
    <svg width="100%" viewBox="0 0 680 540" role="img" xmlns="http://www.w3.org/2000/svg">
    <title>花蓮三天兩夜手繪行程地圖</title>
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
      fill="none" stroke="#6aabca" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="6,2" opacity="0.8" filter="url(#sketch)"/>
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
    <rect x="182" y
    """
