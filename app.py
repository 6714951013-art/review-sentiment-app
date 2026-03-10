import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="AI วิเคราะห์รีวิว", page_icon="📊")
st.title("📊 แอปวิเคราะห์อารมณ์จากรีวิวลูกค้า")
st.write("ใส่ข้อความรีวิวของลูกค้าด้านล่าง แล้วให้ AI ช่วยวิเคราะห์ความรู้สึกและสรุปปัญหาให้ครับ")

# ==========================================
# ใส่ API Key ของคุณตรงนี้ (เอามาจากรูปภาพ)
MY_API_KEY = "AIzaSyBXYQ_InvphYvwWziWGigvGnOqe05D-cUg"
# ==========================================

# 2. ช่องให้ผู้ใช้พิมพ์/วางรีวิว
review_text = st.text_area("✍️ วางข้อความรีวิวตรงนี้:", height=150)

# 3. ปุ่มกดเริ่มวิเคราะห์
if st.button("🚀 วิเคราะห์รีวิว", type="primary"):
    if not review_text:
        st.warning("⚠️ กรุณาใส่ข้อความรีวิวก่อนครับ")
    else:
        try:
            # ตั้งค่า Gemini API ด้วย Key ที่ฝังไว้
            genai.configure(api_key=MY_API_KEY)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # คำสั่ง (Prompt)
            prompt = f"""
            จงวิเคราะห์ข้อความรีวิวของลูกค้าต่อไปนี้:
            "{review_text}"
            
            กรุณาตอบกลับในรูปแบบดังนี้:
            1. อารมณ์ของรีวิว: (ระบุว่าเป็น บวก / ลบ / หรือ เฉยๆ)
            2. สรุปใจความสำคัญ: (สรุปสั้นๆ 1-2 ประโยค)
            3. ปัญหาที่พบ (ถ้ามี): (ถ้ารีวิวพูดถึงปัญหา ให้ลิสต์ออกมา ถ้าไม่มีให้บอกว่า "ไม่พบปัญหา")
            """
            
            with st.spinner("กำลังวิเคราะห์ข้อมูล..."):
                # สั่งให้ AI สร้างคำตอบ
                response = model.generate_content(prompt)
                
                # แสดงผลลัพธ์
                st.success("วิเคราะห์เสร็จสิ้น!")
                st.markdown("### 📋 ผลการวิเคราะห์:")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")