import streamlit as st
import random
import time

def luck_wheel():
    st.title("🎡 BusinessBook Fortune Wheel")
    st.write("පින්තූරයේ පරිදිම වර්ණවත් රෝදය කැරකවන්න!")

    # රෝදයේ අයිතම සහ ඒවායේ වර්ණ
    items = [
        {"label": "Item 1", "color": "#FF0000"}, # රතු
        {"label": "Item 2", "color": "#FF8C00"}, # තැඹිලි
        {"label": "Item 3", "color": "#FFFF00"}, # කහ
        {"label": "Item 4", "color": "#00FF00"}, # කොළ
        {"label": "Item 5", "color": "#00BFFF"}, # නිල්
        {"label": "Item 6", "color": "#8A2BE2"}  # දම්
    ]

    if st.button("SPIN NOW! 🌀"):
        # අහඹු ලෙස ජයග්‍රාහකයෙක් තෝරා ගැනීම
        winner = random.choice(items)
        rotation = random.randint(720, 1440) # වට කිහිපයක් කැරකීමට (Degree)

        # CSS මගින් රෝදය කැරකෙන පෙනුම ලබා දීම
        wheel_html = f"""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <div id="wheel" style="
                width: 300px; height: 300px; border-radius: 50%;
                border: 5px solid #333; position: relative;
                background: conic-gradient(
                    {items[0]['color']} 0deg 60deg, 
                    {items[1]['color']} 60deg 120deg, 
                    {items[2]['color']} 120deg 180deg, 
                    {items[3]['color']} 180deg 240deg, 
                    {items[4]['color']} 240deg 300deg, 
                    {items[5]['color']} 300deg 360deg
                );
                transition: transform 4s cubic-bezier(0.1, 0, 0.1, 1);
                transform: rotate({rotation}deg);
            ">
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                            background: white; border-radius: 50%; padding: 10px; font-weight: bold; border: 2px solid #333;">
                    SPIN
                </div>
            </div>
            <div style="width: 0; height: 0; 
                border-left: 15px solid transparent; border-right: 15px solid transparent;
                border-top: 30px solid black; margin-top: -10px; z-index: 10;">
            </div>
        </div>
        """
        
        placeholder = st.empty()
        placeholder.markdown(wheel_html, unsafe_allow_html=True)
        
        # රෝදය නැවතී ප්‍රතිඵලය පෙන්වීමට තත්පර 4ක් රැඳී සිටීම
        time.sleep(4)
        st.balloons()
        st.success(f"දිනුම: {winner['label']} 🎉")

# ඇප් එකේ පෙන්වීමට
luck_wheel()
