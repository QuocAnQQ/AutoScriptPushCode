from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Giao diện web đơn giản với một form input
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Ping Test Tool</title>
    <style>
        body { font-family: sans-serif; background-color: #282c34; color: #abb2bf; text-align: center; margin-top: 50px; }
        h1 { color: #61afef; }
        form { margin-top: 20px; }
        input[type=text] { padding: 10px; width: 300px; border-radius: 5px; border: 1px solid #61afef; background-color: #21252b; color: #abb2bf;}
        input[type=submit] { padding: 10px 20px; border-radius: 5px; border: none; background-color: #98c379; color: #282c34; cursor: pointer; }
        pre { background-color: #21252b; text-align: left; padding: 15px; border-radius: 5px; white-space: pre-wrap; word-wrap: break-word; max-width: 600px; margin: 20px auto; }
    </style>
</head>
<body>
    <h1>Ping Test Tool 핑</h1>
    <p>Enter an IP address to ping:</p>
    <form method="post">
        <input type="text" name="ip" placeholder="e.g., 8.8.8.8">
        <input type="submit" value="Ping">
    </form>
    
    {% if result %}
        <h2>Result:</h2>
        <pre>{{ result }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        ip_address = request.form.get('ip', '')
        
        # !!! LỖ HỔNG BẢO MẬT NẰM Ở ĐÂY !!!
        # Ứng dụng nối trực tiếp chuỗi đầu vào của người dùng vào một câu lệnh shell.
        # Điều này cho phép kẻ tấn công chèn thêm các lệnh khác bằng dấu ";"
        cmd = "ping -c 3 " + ip_address
        
        # Thực thi lệnh và lấy kết quả
        result = os.popen(cmd).read()

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
