import streamlit as st
from datetime import datetime, timedelta

# Judul aplikasi
st.title("Countdown Waktu Deadline")

# Input tanggal dan waktu deadline
deadline = st.date_input("Pilih tanggal deadline:")
deadline_time = st.time_input("Pilih waktu deadline:")

# Menggabungkan tanggal dan waktu deadline
if deadline and deadline_time:
    deadline_datetime = datetime.combine(deadline, deadline_time)
    now = datetime.now()
    if deadline_datetime > now:
        # Hitung sisa waktu
        countdown = deadline_datetime - now
        days = countdown.days
        seconds = countdown.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        # Tampilkan countdown
        st.subheader("Waktu yang tersisa:")
        st.write(f"{days} hari, {hours} jam, {minutes} menit, {seconds} detik")
    else:
        st.warning("Deadline sudah terlewati!")
