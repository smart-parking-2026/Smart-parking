from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html dir="rtl">
    <head>
        <title>نظام المواقف الذكي</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; padding: 50px; }
            .container { display: flex; justify-content: center; gap: 20px; margin-top: 30px; }
            .parking-spot {
                width: 120px; height: 180px;
                border: 3px solid #333; border-radius: 10px;
                display: flex; align-items: center; justify-content: center;
                font-weight: bold; color: white; transition: 0.3s;
            }
            .occupied { background-color: #e74c3c; } /* أحمر للمحجوز */
            .vacant { background-color: #2ecc71; }   /* أخضر للفارغ */
            h1 { color: #2c3e50; }
        </style>
    </head>
    <body>
        <h1>نظام مراقبة مواقف السيارات الذكي 2026</h1>
        <p>الحالة المباشرة للمواقف من السحابة:</p>
        <div class="container">
            <div class="parking-spot occupied">موقف 1<br>(محجوز)</div>
            <div class="parking-spot vacant">موقف 2<br>(فارغ)</div>
            <div class="parking-spot occupied">موقف 3<br>(محجوز)</div>
            <div class="parking-spot vacant">موقف 4<br>(فارغ)</div>
        </div>
        <br>
        <p style="color: #7f8c8d;">تحديث تلقائي عبر Render & GitHub</p>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run()
