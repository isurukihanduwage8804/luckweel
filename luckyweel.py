import streamlit as st
import random
import time

st.title("🎡 BusinessBook Luck Wheel")

# තෑගි ලැයිස්තුව
options = ["Rs.100", "Free Card", "No Prize", "Rs.500", "Discount", "Big Win!"]

if st.button("රෝදය කැරකවන්න (Spin)"):
    # කැරකෙන animation එක පෙන්වන තැන
    placeholder = st.empty()
    
    # රෝදය වේගයෙන් කැරකෙන බව පෙන්වීමට
    spins = random.randint(20, 40) # වට කීයක් කැරකෙනවාද යන්න අහඹු ලෙස තීරණය වේ
    
    for i in range(spins):
        current = options[i % len(options)]
        # රෝදයේ වේගය ක්‍රමයෙන් අඩු වන පෙනුම (Ease out effect)
        sleep_time = 0.05 + (i / spins) * 0.2 
        
        placeholder.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; 
                        height: 200px; width: 200px; border-radius: 50%; 
                        border: 10px solid #1877F2; background-color: #f0f2f5;
                        margin: auto; transition: all {sleep_time}s;">
                <h2 style="color: #1877F2; text-align: center;">{current}</h2>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(sleep_time)

    # අවසාන තීරණය
    result = random.choice(options)
    placeholder.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; 
                        height: 200px; width: 200px; border-radius: 50%; 
                        border: 10px solid #28a745; background-color: #d4edda;
                        margin: auto;">
                <h1 style="color: #155724; text-align: center;">{result}</h1>
            </div>
        """, unsafe_allow_html=True)
    
    st.balloons()
    st.success(f"සුභ පැතුම්! ඔබ {result} දිනාගත්තා.")
