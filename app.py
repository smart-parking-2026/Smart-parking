from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Get current time
    now = datetime.now().strftime("%H:%M:%S")
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="5"> <title>Smart Parking System</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; background-color: #f0f2f5; padding: 20px; color: #1c1e21; }}
            .header {{ background: linear-gradient(135deg, #1a73e8, #0d47a1); color: white; padding: 25px; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
            .status-info {{ margin-bottom: 25px; font-size: 1.1em; color: #5f6368; }}
            .live-dot {{ height: 10px; width: 10px; background-color: #2ecc71; border-radius: 50%; display: inline-block; margin-right: 5px; animation: blink 1s infinite; }}
            @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} 100% {{ opacity: 1; }} }}
            
            .container {{ display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 20px; }}
            .parking-spot {{
                width: 150px; height: 220px;
                border-radius: 15px;
                display: flex; flex-direction: column; align-items: center; justify-content: center;
                font-weight: bold; color: white; transition: transform 0.2s;
                box-shadow: 0 6px 15px rgba(0,0,0,0.1);
                border: 2px solid rgba(255,255,255,0.2);
            }}
            .parking-spot:hover {{ transform: translateY(-5px); }}
            
            .occupied {{ background-color: #d93025; }} /* Red - Occupied */
            .vacant {{ background-color: #1e8e3e; }}   /* Green - Vacant */
            
            .car-icon {{ font-size: 50px; margin-bottom: 15px; }}
            .footer {{ margin-top: 50px; font-size: 0.85em; color: #70757a; border-top: 1px solid #dadce0; padding-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>SMART PARKING DASHBOARD</h1>
            <p>Cloud-Based Real-Time Monitoring</p>
        </div>
        
        <div class="status-info">
            <span class="live-dot"></span> System Status: <strong>LIVE</strong> | Last Update: <span style="color: #1a73e8;">{now}</span>
        </div>

        <div class="container">
            <div class="parking-spot occupied">
                <div class="car-icon">🚗</div>
                SPOT 01<br>[ OCCUPIED ]
            </div>
            
            <div class="parking-spot vacant">
                <div class="car-icon">🅿️</div>
                SPOT 02<br>[ VACANT ]
            </div>
            
            <div class="parking-spot occupied">
                <div class="car-icon">🚗</div>
                SPOT 03<br>[ OCCUPIED ]
            </div>
            
            <div class="parking-spot vacant">
                <div class="car-icon">🅿️</div>
                SPOT 04<br>[ VACANT ]
            </div>
        </div>

        <div class="footer">
            <p>Smart City Project 2026 - Powered by Render Cloud & Flask</p>
            <p>Auto-refreshing every 5 seconds...</p>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run()
           
        
         
