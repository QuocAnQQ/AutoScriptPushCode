# Sử dụng một base image Python gọn nhẹ
FROM python:3.9-slim

# Thiết lập thư mục làm việc bên trong container
WORKDIR /app

# Sao chép file requirements trước để tận dụng Docker cache
COPY requirements.txt .

# Cài đặt các thư viện Python cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn của ứng dụng vào container
COPY . .

# Mở cổng 5000 để bên ngoài có thể truy cập vào ứng dụng
EXPOSE 5000

# Lệnh để khởi chạy ứng dụng khi container bắt đầu
CMD ["python", "app.py"]
