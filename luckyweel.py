import streamlit as st
import random
import time

# පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="Mega Wheel", page_icon="🎡")

def mega_wheel():
    st.title("🎡 BusinessBook Mega Wheel")
    st.write("1000 සිට 6000 දක්වා දිනාගන්න! ඉතා වේගයෙන් කැරකේ.")

    # තෑගි සහ වර්ණ
    prizes = ["1000", "2000", "3000", "4000", "5000", "6000"]
    colors = ["#FF4B4B", "#FFA500", "#FFD700", "#00C851", "#33b5e5", "#aa66cc"]

    if st.button("SPIN MEGA WHEEL! 🔥"):
        # වට ගණන වැඩි කිරීමට (අංශක 2000 සිට 5000 දක්වා)
        rotation = random.randint(2000, 5000)
        
        # රෝදය ඇතුළේ පාට (Conic Gradient පාවිච්චි කරලා ලේසියෙන්ම හදමු)
        # මෙය පින්තූරයේ තිබූ විදිහටම පාට 6 ලස්සනට පෙන්වයි
        gradient = f"""
            conic-gradient(
                {colors[0]} 0deg 60deg, 
                {colors[1]} 60deg 120deg, 
                {colors[2]} 120deg 180deg, 
                {colors[3]} 180deg 240deg, 
                {colors[4]} 240deg 300deg, 
                {colors[5]} 300deg 360deg
            )
        """

        # ඉලක්කම් පෙන්වන කොටස (Text labels)
        # රෝදය කැරකෙන වේගය (Transition) තත්පර 4ක් ලෙස සකසා ඇත
        wheel_html = f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px;">
            <div style="width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 40px solid #333; z-index: 10; margin-bottom: -10px;"></div>
            <div style="
                width: 300px; 
                height: 300px; 
                border-radius: 50%; 
                border: 10px solid #333;
                background: {gradient};
                position: relative;
                transition: transform 4s cubic-bezier(0.15, 0, 0.15, 1);
                transform: rotate({rotation}deg);
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                <div style="position: absolute; width: 100%; height: 100%; font-size: 18px; font-weight: bold; color: white;">
                    <div style="position: absolute; top: 10%; left: 40%; transform: rotate(0deg);">1000</div>
                    <div style="position: absolute; top: 30%; right: 5%; transform: rotate(60deg);">2000</div>
                    <div style="position: absolute; bottom: 30%; right: 5%; transform: rotate(120deg);">3000</div>
                    <div style="position: absolute; bottom: 10%; left: 40%; transform: rotate(180deg);">4000</div>
                    <div style="position: absolute; bottom: 30%; left: 5%; transform: rotate(240deg);">5000</div>
                    <div style="position: absolute; top: 30%; left: 5%; transform: rotate(300deg);">6000</div>
                </div>
                <div style="width: 50px; height: 50px; background: white; border-radius: 50%; border: 4px solid #333; z-index: 5; display: flex; align-items: center; justify-content: center;">
                    <b>GO</b>
                </div>
            </div>
        </div>
        """
        
        # HTML එක පෙන්වීම
        placeholder = st.empty()
        placeholder.markdown(wheel_html, unsafe_allow_html=True)
        
        # කැරකෙනකම් තත්පර 4ක් රැඳී සිටීම
        time.sleep(4)
        
        # ප්‍රතිඵලය ගණනය කිරීම
        final_angle = rotation % 360
        winning_index = int(((360 - final_angle) % 360) / 60)
        winner = prizes[winning_index]

        st.balloons()
        st.success(f"සුභ පැතුම්! ඔබ Rs. {winner} දිනාගත්තා! 🤑")

# App එක පෙන්වීමට
mega_wheel()
