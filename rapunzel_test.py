import streamlit as st

st.set_page_config(page_title="Ne kadar Rapunzel'sin?", page_icon="👸", layout="centered")

st.title("👸 Ne kadar Rapunzel'sin? Testi")
st.write("Sevgilim, bu testi çöz ve bakalım içindeki Rapunzel ne kadar güçlü 💜")

# İlk 5 soru (göstermelik, sonucu etkilemez)
questions = [
    {
        "q": "Saçlarını nasıl tanımlarsın?",
        "opts": ["Çok uzun ve bakımlı 🌟", "Orta boy, normal 🙂", "Kısa ve pratik ✂️"]
    },
    {
        "q": "Kulede tek başına yaşasan ne yapardın?",
        "opts": ["Kitap okurum, şarkı söylerim 🎶", "Telefonla arkadaşlarla konuşurum ☎️", "Uyurum 😴"]
    },
    {
        "q": "Bir prenses olarak maceraya bakışın?",
        "opts": ["Tam benlik, dünyayı keşfetmek isterim 🌍", "Arada sırada fena olmaz 😌", "Yok ben evde mutluyum 🏡"]
    },
    {
        "q": "Sevdiğin renk nedir?",
        "opts": ["Mor/Lila 💜", "Pembe/Altın 🌸", "Siyah ⚫️"]
    },
    {
        "q": "Bir masal karakteri seçsen hangisi olurdun?",
        "opts": ["Rapunzel 👸", "Elsa ❄️", "Külkedisi 👠"]
    }
]

# Gösterim için soruları çiz (cevaplar sonucu etkilemeyecek)
for i, item in enumerate(questions, start=1):
    st.radio(item["q"], item["opts"], key=f"q_{i}")

# Asıl sonucu belirleyen gizli sorular
partner_q1 = st.radio("Sevgilin var mı?", ["Evet", "Hayır"], key="partner_exists")
partner_q2 = st.radio("Sevgilinin adı S harfi ile mi başlıyor?", ["Evet", "Hayır"], key="partner_name_s")

# Sonuç
if st.button("Sonucu Gör ✨"):
    if partner_q1 == "Evet" and partner_q2 == "Evet":
        st.success("💜 Sen %100 Sevgilinin minik tatli prensesi ve Rapunzelisin 👸✨")
        st.balloons()
    else:
        st.info("Rapunzel olmak için bazı koşullar eksik gibi 😉")
