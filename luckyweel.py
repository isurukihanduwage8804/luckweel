import streamlit as st
import sqlite3
import random
import time

# පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="BusinessBook Mega Wheel", layout="wide")

# Database සම්බන්ධතාවය
conn = sqlite3.connect('businessbook_v3.db', check_same_thread=False)
c = conn.cursor()

# Tables සෑදීම (Balance එකත් සමඟ)
c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, balance INTEGER DEFAULT 0)')
conn.commit()

# --- Session State ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("BusinessBook Login")
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab2:
        new_un = st.text_input("New Username")
        new_pw = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            c.execute('INSERT INTO users (username, password, balance) VALUES (?,?,?)', (new_un, new_pw, 0))
            conn.commit()
            st.success("Registered! Go to Login.")
            
    with tab1:
        un = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.button("Login"):
            c.execute('SELECT * FROM users WHERE username =? AND password =?', (un, pw))
            user_data = c.fetchone()
            if user_data:
                st.session_state['logged_in'] = True
                st.session_state['user'] = un
                st.rerun()
            else:
                st.error("Invalid Login")

else:
    # --- LOGGED IN AREA ---
    # දකුණු පසින් Balance එක පෙන්වීම
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
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.rerun()

    with col1:
        st.title(f"Welcome, {st.session_state['user']}! 🎡")
        
        prizes = [1000, 2000, 3000, 4000, 5000, 6000]
        colors = ["#FF4B4B", "#FFA500", "#FFD700", "#00C851", "#33b5e5", "#aa66cc"]

        if st.button("SPIN MEGA WHEEL! 🔥"):
            rotation = random.randint(3000, 6000)
            
            wheel_style = f"""
            <div style="display: flex; flex-direction: column; align-items: center;">
                <div style="width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-top: 40px solid #333; z-index: 10; margin-bottom: -15px;"></div>
                <div style="width: 350px; height: 350px; border-radius: 50%; border: 10px solid #333;
                    background: conic-gradient({colors[0]} 0deg 60deg, {colors[1]} 60deg 120deg, {colors[2]} 120deg 180deg, {colors[3]} 180deg 240deg, {colors[4]} 240deg 300deg, {colors[5]} 300deg 360deg);
                    position: relative; transition: transform 5s cubic-bezier(0.15, 0, 0.15, 1); transform: rotate({rotation}deg);">
                    <div style="position: absolute; width: 100%; height: 100%; color: white; font-weight: bold; font-size: 20px;">
                        <div style="position: absolute; top: 12%; left: 62%; transform: rotate(30deg);">1000</div>
                        <div style="position: absolute; top: 48%; left: 78%; transform: rotate(90deg);">2000</div>
                        <div style="position: absolute; bottom: 12%; left: 62%; transform: rotate(150deg);">3000</div>
                        <div style="position: absolute; bottom: 12%; right: 62%; transform: rotate(210deg);">4000</div>
                        <div style="position: absolute; top: 48%; right: 78%; transform: rotate(270deg);">5000</div>
                        <div style="position: absolute; top: 12%; right: 62%; transform: rotate(330deg);">6000</div>
                    </div>
                </div>
            </div>
            """
            placeholder = st.empty()
            placeholder.markdown(wheel_style, unsafe_allow_html=True)
            
            time.sleep(5)
            
            # දිනුම ගණනය කර Balance එකට එකතු කිරීම
            final_angle = rotation % 360
            winning_index = int(((360 - (final_angle + 30)) % 360) / 60)
            won_amount = prizes[winning_index]
            
            new_total = current_balance + won_amount
            c.execute('UPDATE users SET balance=? WHERE username=?', (new_total, st.session_state['user']))
            conn.commit()
            
            st.balloons()
            st.success(f"You won Rs. {won_amount}!")
            st.rerun() # Balance එක Update වී පෙනෙන්නට Page එක Refresh කරයි
