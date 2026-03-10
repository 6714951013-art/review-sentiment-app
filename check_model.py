import google.generativeai as genai

# เอา API Key ของคุณมาใส่ตรงนี้นะครับ
genai.configure(api_key="AIzaSyBXYQ_InvphYvwWziWGigvGnOqe05D-cUg") 

print("กำลังค้นหาโมเดลที่ใช้งานได้...")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)