from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # الحصول على الوقت الحالي
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html_content = f"""
    <!DOCTYPE html>
    <html dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="5"> <title>نظام المواقف الذكي</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; background-color: #ecf0f1; padding: 30px; }}
            .header {{ background-color: #2c3e50; color: white; padding: 20px; border-radius: 10px; margin-bottom: 30px; }}
            .status-bar {{ margin-bottom: 20px; font-weight: bold; color: #34495e; }}
            .container {{ display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; }}
            .parking-spot {{
                width: 140px; height: 200px;
                border: 4px solid #34495e; border-radius: 15px;
                display: flex; flex-direction: column; align-items: center; justify-content: center;
                font-weight: bold; color: white; transition: 0.3s;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }}
            .occupied {{ background-color: #e74c3c; border-color: #c0392b; }} /* محجوز */
            .vacant {{ background-color: #2ecc71; border-color: #27ae60; }}   /* فارغ */
            .car-icon {{ font-size: 40px; margin-bottom: 10px; }}
            .footer {{ margin-top: 40px; font-size: 0.9em; color: #7f8c8d; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>نظام مراقبة مواقف السيارات الذكي 2026</h1>
        </div>
        
        <div class="status-bar">
            آخر تحديث للسحابة: <span style="color: #2980b9;">{now}</span>
        </div>

        <div class="container">
            <div class="parking-spot occupied">
                <div class="car-icon">🚗</div>
                موقف 1<br>(محجوز)
            </div>
            <div class="parking-spot vacant">
                <div class="car-icon">🅿️</div>
                موقف 2<br>(فارغ)
            </div>
            <div class="parking-spot occupied">
                <div class="car-icon">🚗</div>
                موقف 3<br>(محجوز)
            </div>
            <div class="parking-spot vacant">
                <div class="car-icon">🅿️</div>
                موقف 4<br>(فارغ)
            </div>
        </div>

        <div class="footer">
            <p>يتم تحديث البيانات تلقائياً كل 5 ثوانٍ من سيرفر Render</p>
            <p>الموقع الآن متصل بنجاح 🟢</p>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run()
         
