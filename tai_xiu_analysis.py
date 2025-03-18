
import streamlit as st
import pandas as pd

# Tiêu đề trang
st.title("Phân Tích Tài Xỉu")

# Khởi tạo hoặc tải dữ liệu
if "history" not in st.session_state:
    st.session_state.history = []

# Nhập kết quả mới
st.subheader("Nhập Kết Quả")
result = st.radio("Chọn kết quả:", ["Tài", "Xỉu"])
if st.button("Thêm vào lịch sử"):
    st.session_state.history.append(result)

# Hiển thị lịch sử
st.subheader("Lịch Sử Kết Quả")
df = pd.DataFrame(st.session_state.history, columns=["Kết Quả"])
st.write(df)

# Tính toán tỷ lệ
if not df.empty:
    tai_count = df[df["Kết Quả"] == "Tài"].count()[0]
    xiu_count = df[df["Kết Quả"] == "Xỉu"].count()[0]
    total = tai_count + xiu_count
    st.subheader("Thống Kê")
    st.write(f"✅ **Tài**: {tai_count} lần ({tai_count/total:.2%})")
    st.write(f"❌ **Xỉu**: {xiu_count} lần ({xiu_count/total:.2%})")

# Biểu đồ
st.subheader("Biểu Đồ Kết Quả")
st.bar_chart(df["Kết Quả"].value_counts())
