import os
from flask import Flask, request, jsonify, render_template_string
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# الربط بقاعدة البيانات (سيستخدم MONGO_URI من إعدادات Render)
MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['smarTparking']
logs_collection = db['parking_logs']

# واجهة لوحة التحكم الاحترافية
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>نظام إدارة الموقف الذكي</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, sans-serif; background-color: #f0f2f5; margin: 0; padding: 20px; text-align: center; }
        .container { max-width: 1000px; margin: auto; background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { color: #1a73e8; margin-bottom: 30px; border-bottom: 2px solid #eee; padding-bottom: 15px; }
        
        .control-panel { background: #f8f9fa; padding: 20px; border-radius: 12px; margin-bottom: 30px; border: 1px solid #dee2e6; }
        .group { margin-bottom: 15px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; }
        .group-label { width: 100%; font-weight: bold; margin-bottom: 10px; color: #555; }
        
        button { padding: 10px 20px; font-size: 14px; cursor: pointer; border: none; border-radius: 6px; color: white; transition: 0.2s; font-weight: bold; }
        .btn-entry { background-color: #28a745; } /* أخضر للدخول */
        .btn-exit { background-color: #dc3545; }  /* أحمر للخروج */
        button:hover { opacity: 0.8; transform: translateY(-2px); }
        
        table { width: 100%; border-collapse: collapse; margin-top: 20px; background: white; }
        th, td { padding: 12px; border: 1px solid #eee; text-align: center; }
        th { background-color: #1a73e8; color: white; }
        .badge { padding: 4px 10px; border-radius: 12px; font-size: 12px; color: white; }
        .bg-prof { background-color: #6f42c1; }   /* أرجواني للأستاذ */
        .bg-student { background-color: #17a2b8; } /* أزرق للطالب */
        .bg-worker { background-color: #fd7e14; }  /* برتقالي للعامل */
        .status-entry { color: #28a745; font-weight: bold; }
        .status-exit { color: #dc3545; font-weight: bold; }
    </style>
    <script>
        function logAction(plate, type, action) {
            fetch('/log_car', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({plate: plate, type: type, action: action})
            }).then(() => {
                alert("تم تسجيل عملية " + (action === 'Entry' ? 'دخول' : 'خروج') + " للوحة: " + plate);
                location.reload();
            });
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>🚗 لوحة التحكم في مواقف جامعة سطيف</h1>
        
        <div class="control-panel">
            <div class="group">
                <div class="group-label">محاكاة دخول سيارات (Entry)</div>
                <button class="btn-entry" onclick="logAction('00123-122-19', 'أستاذ', 'Entry')">+ دخول أستاذ</button>
                <button class="btn-entry" onclick="logAction('05544-118-19', 'طالب', 'Entry')">+ دخول طالب</button>
                <button class="btn-entry" onclick="logAction('09988-121-19', 'عامل', 'Entry')">+ دخول عامل</button>
            </div>
            
            <div class="group">
                <div class="group-label">محاكاة خروج سيارات (Exit)</div>
                <button class="btn-exit" onclick="logAction('00123-122-19', 'أستاذ', 'Exit')">- خروج أستاذ</button>
                <button class="btn-exit" onclick="logAction('05544-118-19', 'طالب', 'Exit')">- خروج طالب</button>
                <button class="btn-exit" onclick="logAction('09988-121-19', 'عامل', 'Exit')">- خروج عامل</button>
            </div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>الماطريكول</th>
                    <th>الفئة</th>
                    <th>الحالة</th>
                    <th>التاريخ والوقت</th>
                </tr>
            </thead>
            <tbody>
                {% for log in logs %}
                <tr>
                    <td><strong>{{ log.plate_number }}</strong></td>
                    <td>
                        <span class="badge {% if log.user_type == 'أستاذ' %}bg-prof{% elif log.user_type == 'طالب' %}bg-student{% else %}bg-worker{% endif %}">
                            {{ log.user_type }}
                        </span>
                    </td>
                    <td>
                        <span class="{{ 'status-entry' if log.action == 'Entry' else 'status-exit' }}">
                            {{ 'دخول ↑' if log.action == 'Entry' else 'خروج ↓' }}
                        </span>
                    </td>
                    <td>{{ log.timestamp }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # جلب السجلات من الأحدث للأقدم
    all_logs = list(logs_collection.find().sort("sort_time", -1).limit(20))
    return render_template_string(HTML_TEMPLATE, logs=all_logs)

@app.route('/log_car', methods=['POST'])
def log_car():
    data = request.json
    now = datetime.now()
    
    new_log = {
        "plate_number": data.get("plate"),
        "user_type": data.get("type"),
        "action": data.get("action"), # 'Entry' أو 'Exit'
        "timestamp": now.strftime("%Y-%m-%d | %H:%M:%S"), # صيغة الوقت والتاريخ
        "sort_time": now # حقل مخفي للترتيب فقط
    }
    
    logs_collection.insert_one(new_log)
    return jsonify({"status": "success"}), 201

if __name__ == "__main__":
    app.run()
