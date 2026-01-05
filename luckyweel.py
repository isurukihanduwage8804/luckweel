import streamlit as st
import random
import time

st.set_page_config(page_title="Mega Wheel", page_icon="🎡")

def mega_wheel():
    st.title("🎡 BusinessBook Mega Wheel")
    st.write("1000 සිට 6000 දක්වා නිවැරදිව දිනාගන්න!")

    # තෑගි සහ වර්ණ
    prizes = ["1000", "2000", "3000", "4000", "5000", "6000"]
    colors = ["#FF4B4B", "#FFA500", "#FFD700", "#00C851", "#33b5e5", "#aa66cc"]

    if st.button("SPIN MEGA WHEEL! 🔥"):
        # වට ගණන වැඩි කිරීමට (වේගය වැඩි වේ)
        rotation = random.randint(3000, 6000)
        
        # රෝදය සෑදීම (CSS)
        # මෙහිදී ඉලක්කම් (1000-6000) ඒ ඒ කොටස මැදටම එනසේ අංශක ගණන සකස් කර ඇත
        wheel_html = f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px;">
            <div style="width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 40px solid #333; z-index: 10; margin-bottom: -15px;"></div>
            
            <div style="
                width: 350px; 
                height: 350px; 
                border-radius: 50%; 
                border: 10px solid #333;
                background: conic-gradient(
                    {colors[0]} 0deg 60deg, 
                    {colors[1]} 60deg 120deg, 
                    {colors[2]} 120deg 180deg, 
                    {colors[3]} 180deg 240deg, 
                    {colors[4]} 240deg 300deg, 
                    {colors[5]} 300deg 360deg
                );
                position: relative;
                transition: transform 5s cubic-bezier(0.15, 0, 0.15, 1);
                transform: rotate({rotation}deg);
            ">
                <div style="position: absolute; width: 100%; height: 100%; color: white; font-family: Arial; font-weight: bold; font-size: 22px;">
                    <div style="position: absolute; top: 15%; left: 60%; transform: rotate(30deg);">{prizes[0]}</div>
                    <div style="position: absolute; top: 50%; left: 75%; transform: rotate(90deg);">{prizes[1]}</div>
                    <div style="position: absolute; bottom: 15%; left: 60%; transform: rotate(150deg);">{prizes[2]}</div>
                    <div style="position: absolute; bottom: 15%; right: 60%; transform: rotate(210deg);">{prizes[3]}</div>
                    <div style="position: absolute; top: 50%; right: 75%; transform: rotate(270deg);">{prizes[4]}</div>
                    <div style="position: absolute; top: 15%; right: 60%; transform: rotate(330deg);">{prizes[5]}</div>
                </div>
                
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 70px; height: 70px; background: white; border-radius: 50%; border: 5px solid #333; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 20px; color: black; z-index: 20;">
                    GO
                </div>
            </div>
        </div>
        """
        
        placeholder = st.empty()
        placeholder.markdown(wheel_html, unsafe_allow_html=True)
        
        # තත්පර 5ක් රෝදය කැරකෙන තෙක් සිටීම
        time.sleep(5)
        
        # ජයග්‍රාහකයා තේරීම
        final_angle = rotation % 360
        # Pointer එක උඩ තියෙන නිසා (0/360 deg) ජයග්‍රාහකයා ගණනය කරමු
        winning_index = int(((360 - (final_angle + 30)) % 360) / 60)
        winner = prizes[winning_index]

        st.balloons()
        st.markdown(f"<div style='text-align: center; background-color: #d4edda; padding: 10px; border-radius: 10px;'><h2 style='color: #155724;'>සුභ පැතුම්! ඔබ Rs. {winner} දිනාගත්තා! 🤑</h2></div>", unsafe_allow_html=True)

# Run
mega_wheel()
