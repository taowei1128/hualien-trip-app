import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="花蓮吵啥 旅遊手冊", page_icon="🌊", layout="centered")

st.title("🌊 花蓮吵啥 - 楠梓星巴克夥伴出遊企劃")
st.markdown("**日期：2026 06/19 - 06/21**")

# 建立三個頁籤
tab1, tab2, tab3 = st.tabs(["👥 出勤夥伴", "📅 行程總覽", "🏠 住宿與重要須知"])

with tab1:
    st.header("出勤人員名單")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Taowei**\n\n這零號還强迫大家跟他一起出遊，只能說被提姆討厭不是沒有原因的！ #狂暴梔子花")
        st.success("**Samael**\n\n老婆：Anny。未來可能被調店的雞掰人！ #香港定居者")
        st.warning("**Tammy**\n\n高知識分子未來要去台北念研究所的慾女。 #性生活要有啊")
    with col2:
        st.info("**Dennis**\n\n定位：神明之子。據說上次哭是看媽祖繞境，陽光大男孩，也是這次旅遊的水上活動教練。 #我沒有隱形")
        st.success("**Zoe**\n\n被情緒勒索導致很晚才從星巴克離職的值班妹，真的很欠罵！ #P值也有人權")
        st.warning("**Ryan (Pyan)**\n\n未來將扛下楠梓晚班S的梁柱，但他其實超爛... #智商趨近於0")

with tab2:
    st.header("爆肝行程表")
    
    with st.expander("Day 1: 爆肝列車與太平洋狂歡 (06/19)"):
        st.write("""
        - **05:23 - 09:50** | 新自强 3000-411號車之爆肝列車 (凌晨5:00新左營集合！準備好直接睡死到花蓮)
        - **10:00 - 12:00** | 熱血取車 (宏越租車，大司機 Ryan 負責) 與早午餐
        - **18:00 - 20:00** | 東大門夜市逛起乃！
        """)
        
    with st.expander("Day 2: 賣力泛舟中 (06/20)"):
        st.write("""
        - **09:00 - 11:00** | 花蓮市區集合上接駁車，前往向上泛舟
        - **11:00 - 15:00** | 賣力泛舟中
        """)
        
    with st.expander("Day 3: 平安返家 (06/21)"):
        st.write("""
        - **17:29 - 21:54** | 搭車平安抵達高雄啦！
        """)

with tab3:
    st.header("住宿與重要須知")
    
    st.subheader("🏠 住宿：花蓮包棟民宿 - 煦家 HSU+")
    st.write("""
    - **地址**：花蓮縣花蓮市國富里國富十三街51號
    - **Check in**：16:00 | **Check out**：11:00
    - ⚠️ **特別警告**：整棟禁菸，請 Dennis 特別注意!!!
    """)
    
    st.subheader("🚣 向上泛舟 注意事項")
    st.write("""
    - 務必穿著長袖、長褲及包腳鞋，現場可租鞋 (150~200元/雙)。
    - **一定會全濕**，請務必攜帶換洗衣物及毛巾。
    - 請勿攜帶貴重物品 (手機、手錶等)，遺失損壞不負責。
    - 不能空腹參加，終點有提供點心！
    """)

st.divider()
st.caption("Made with ❤️ by 花蓮吵啥團隊")
