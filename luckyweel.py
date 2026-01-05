import streamlit as st
import sqlite3
import random
import time

# පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="BusinessBook Mega Wheel", layout="wide")

# Database සම්බන්ධතාවය
conn = sqlite3.connect('businessbook_v4.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, balance INTEGER DEFAULT 0)')
conn.commit()

# ආරම්භයේදී Isuru ගේ ගිණුම පද්ධතියට ඇතුළත් කිරීම (නැතිනම් පමණක්)
c.execute('SELECT * FROM users WHERE username="isuru"')
if not c.fetchone():
    c.execute('INSERT INTO users (username, password, balance) VALUES ("isuru", "123456", 0)')
    conn.commit()

# --- Session State ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'rotation' not in st.session_state:
    st.session_state['rotation'] = 0

# --- LOGIN AREA ---
if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center; color: #1877F2;'>BusinessBook Login</h1>", unsafe_allow_html=True)
    
    col_l, col_r = st.columns([1, 1])
    with col_l:
        un = st.text_input("Username")
    with col_r:
        pw = st.text_input("Password", type="password")
    
    if st.button("Login", use_container_width=True):
        if un == "isuru" and pw == "123456":
            st.session_state['logged_in'] = True
            st.session_state['user'] = un
            st.rerun()
        else:
            st.error("පරිශීලක නාමය හෝ මුරපදය වැරදියි!")

else:
    # --- LOGGED IN AREA ---
    c.execute('SELECT balance FROM users WHERE username=?', (st.session_state['user'],))
    current_balance = c.fetchone()[0]

    col1, col2 = st.columns([3, 1])

    with col2:
        st.markdown(f"""
            <div style="background-color: #f0f2f5; padding: 20px; border-radius: 10px; border: 2px solid #1877F2; text-align: center;">
                <h4 style="margin: 0;">Account Balance</h4>
                <h2 style="color: #1877F2; margin: 0;">Rs. {current_balance}</h2>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        spin_clicked = st.button("SPIN NOW! 🔥", use_container_width=True)
        if st.button("Logout", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()

    with col1:
        st.title(f"ආයුබෝවන් {st.session_state['user']}! 🎡")
        
        prizes = [1000, 2000, 3000, 4000, 5000, 6000]
        colors = ["#FF4B4B", "#FFA500", "#FFD700", "#00C851", "#33b5e5", "#aa66cc"]

        if spin_clicked:
            new_rotation = random.randint(3000, 6000)
            st.session_state['rotation'] += new_rotation
        
        current_rotation = st.session_state['rotation']

        wheel_style = f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 20px;">
            <div style="width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 40px solid #333; z-index: 10; margin-bottom: -15px;"></div>
            <div style="
                width: 350px; height: 350px; border-radius: 50%; border: 10px solid #333;
                background: conic-gradient({colors[0]} 0deg 60deg, {colors[1]} 60deg 120deg, {colors[2]} 120deg 180deg, {colors[3]} 180deg 240deg, {colors[4]} 240deg 300deg, {colors[5]} 300deg 360deg);
                position: relative; transition: transform 5s cubic-bezier(0.15, 0, 0.15, 1); transform: rotate({current_rotation}deg);
            ">
                <div style="position: absolute; width: 100%; height: 100%; color: white; font-weight: bold; font-size: 20px;">
                    <div style="position: absolute; top: 12%; left: 62%; transform: rotate(30deg);">1000</div>
                    <div style="position: absolute; top: 48%; left: 78%; transform: rotate(90deg);">2000</div>
                    <div style="position: absolute; bottom: 12%; left: 62%; transform: rotate(150deg);">3000</div>
                    <div style="position: absolute; bottom: 12%; right: 62%; transform: rotate(210deg);">4000</div>
                    <div style="position: absolute; top: 48%; right: 78%; transform: rotate(270deg);">5000</div>
                    <div style="position: absolute; top: 12%; right: 62%; transform: rotate(330deg);">6000</div>
                </div>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 60px; height: 60px; background: white; border-radius: 50%; border: 4px solid #333; display: flex; align-items: center; justify-content: center; font-weight: bold; color: black; z-index: 20;">GO</div>
            </div>
        </div>
        """
        st.markdown(wheel_style, unsafe_allow_html=True)

        if spin_clicked:
            time.sleep(5)
            final_angle = current_rotation % 360
            winning_index = int(((360 - (final_angle + 30)) % 360) / 60)
            won_amount = prizes[winning_index]
            
            new_total = current_balance + won_amount
            c.execute('UPDATE users SET balance=? WHERE username=?', (new_total, st.session_state['user']))
            conn.commit()
            
            st.balloons()
            st.success(f"ඔබ Rs. {won_amount} ක් දිනාගත්තා!")
            st.rerun()
