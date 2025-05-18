# Gamine - Gaming Peripherals E-commerce

## Tổng quan

Gamine là hệ thống thương mại điện tử chuyên về thiết bị ngoại vi gaming (bàn phím, chuột, tai nghe, màn hình...) bao gồm:

- Website bán hàng (gamine-react)
- Trang quản trị (admin-panel)
- Backend API (Django)

## Cấu trúc dự án

- `admin/backend` - Backend Django API
- `admin-panel` - Frontend Admin Panel (React + TypeScript)
- `gamine-react` - Frontend E-commerce (React)
- `nginx` - Cấu hình Nginx
- `docker-compose.yml` - Cấu hình Docker Compose để chạy toàn bộ hệ thống

## Triển khai trên AWS EC2

### Yêu cầu
- AWS EC2 instance
- Docker và Docker Compose

### Các bước triển khai

1. Clone repository:
```bash
git clone https://github.com/TramGiaNguyen/gamine.git
cd gamine
```

2. Cài đặt Docker và Docker Compose:
```bash
# Với Amazon Linux
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo systemctl enable docker
sudo usermod -a -G docker ec2-user
# Đăng xuất và đăng nhập lại

sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

3. Cập nhật cấu hình:
   - Cập nhật `docker-compose.yml` với địa chỉ EC2 public IP
   - Cập nhật `nginx/conf.d/default.conf` với server_name phù hợp

4. Khởi động hệ thống:
```bash
docker-compose up -d
```

5. Truy cập các dịch vụ:
   - Website: http://your-ec2-ip
   - Admin panel: http://your-ec2-ip/admin
   - API: http://your-ec2-ip:8000/api

## Phát triển local

### Yêu cầu
- Docker và Docker Compose
- Node.js và npm

### Các bước cài đặt

1. Clone repository:
```bash
git clone https://github.com/TramGiaNguyen/gamine.git
cd gamine
```

2. Khởi động hệ thống bằng Docker:
```bash
docker-compose up -d
```

3. Truy cập:
   - Website: http://localhost:3001
   - Admin panel: http://localhost:3000
   - API: http://localhost:8000/api 