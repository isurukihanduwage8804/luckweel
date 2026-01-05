import streamlit as st
import random
import time

def high_speed_wheel():
    st.title("🎡 BusinessBook Mega Wheel")
    st.write("1000 සිට 6000 දක්වා දිනාගන්න! ඉතා වේගයෙන් කැරකේ.")

    # ඉලක්කම් සහ වර්ණ (1000, 2000, 3000, 4000, 5000, 6000)
    prizes = [
        {"val": "1000", "color": "#FF0000"}, # Red
        {"val": "2000", "color": "#FF8C00"}, # Orange
        {"val": "3000", "color": "#FFFF00"}, # Yellow
        {"val": "4000", "color": "#00FF00"}, # Green
        {"val": "5000", "color": "#00BFFF"}, # Blue
        {"val": "6000", "color": "#8A2BE2"}  # Purple
    ]

    if st.button("SPIN MEGA WHEEL! 🔥"):
        # වට ගණන ගොඩක් වැඩි කළා (3600 සිට 7200 දක්වා - ඒ කියන්නේ වට 10ක් 20ක් විතර)
        rotation = random.randint(3600, 7200) 
        
        # ඉලක්කම් රෝදය ඇතුළේ පෙන්වන HTML කොටස
        # රෝදය කැරකෙන වේගය තත්පර 5ක් ලෙස දී ඇත (Transition: 5s)
        wheel_segments = ""
        for i, p in enumerate(prizes):
            angle = i * 60
            wheel_segments += f"""
            <div style="position: absolute; width: 50%; height: 50%; background: {p['color']};
                        transform-origin: 100% 100%; transform: rotate({angle}deg) skewY(-30deg);
                        border: 1px solid #333;">
            </div>
            <div style="position: absolute; width: 100%; height: 100%; text-align: center;
                        transform: rotate({angle + 30}deg); color: black; font-weight: bold;
                        padding-top: 20px; font-size: 20px;">
                {p['val']}
            </div>
            """

        wheel_html = f"""
        <div style="display: flex; flex-direction: column; align-items: center; padding: 50px;">
            <div id="pointer" style="width: 0; height: 0; 
                border-left: 20px solid transparent; border-right: 20px solid transparent;
                border-top: 40px solid #333; margin-bottom: -10px; z-index: 10;">
            </div>
            <div id="wheel_container" style="
                width: 350px; height: 350px; border-radius: 50%;
                border: 8px solid #333; position: relative;
                overflow: hidden; background: white;
                transition: transform 5s cubic-bezier(0.15, 0, 0.15, 1);
                transform: rotate({rotation}deg);
            ">
                {wheel_segments}
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                            width: 60px; height: 60px; background: white; border-radius: 50%;
                            border: 4px solid #333; z-index: 5; display: flex; align-items: center; justify-content: center;">
                    <b>SPIN</b>
                </div>
            </div>
        </div>
        """
        
        placeholder = st.empty()
        placeholder.markdown(wheel_html, unsafe_allow_html=True)
        
        # කැරකෙනකම් තත්පර 5ක් ඉන්න
        time.sleep(5)
        
        # ජයග්‍රාහකයා ගණනය කිරීම (අංශක ගණන අනුව)
        final_angle = rotation % 360
        # Pointer එක තියෙන්නේ උඩ (0 deg). රෝදය කැරකෙන දිශාව අනුව index එක බලමු
        # රෝදය clockwise කැරකෙන නිසා index එක ගණනය කරන්නේ මෙහෙමයි:
        winning_index = int(((360 - final_angle) % 360) / 60)
        winner = prizes[winning_index]['val']

        st.balloons()
        st.markdown(f"<h1 style='text-align: center; color: green;'>දිනුම: Rs. {winner} !!! 🤑</h1>", unsafe_allow_html=True)

# Run function
high_speed_wheel()
