# 🚀 Hướng Dẫn Chạy Dự Án Oriagent Device

Hướng dẫn từng bước để chạy dự án trên máy tính cá nhân sau khi clone từ GitHub.

---

## 📋 Yêu Cầu Hệ Thống

| Thành phần | Phiên bản tối thiểu |
|---|---|
| **Hệ điều hành** | Ubuntu 20.04+ / macOS / Windows (WSL2) |
| **Docker** | 24.0+ |
| **Docker Compose** | 2.0+ |
| **Python** | 3.10 - 3.12 |
| **Node.js** | 16+ (chỉ cần nếu muốn chạy giao diện Web dev) |
| **RAM** | Tối thiểu 4GB |
| **FFmpeg** | Cần cài đặt (xử lý audio) |

---

## 🔧 Bước 1: Clone Dự Án

```bash
git clone https://github.com/khanhkhmt/fix_agent.git
cd fix_agent
```

---

## 🐳 Bước 2: Khởi Động Hạ Tầng (Docker)

Lệnh này sẽ tự động tải và chạy 3 container: **MySQL**, **Redis**, và **Java Manager API**.

```bash
docker compose -f docker-compose.dev.yml up -d
```

Chờ khoảng 30-60 giây để MySQL khởi tạo xong database. Kiểm tra:

```bash
docker ps
```

Bạn phải thấy 3 container đều ở trạng thái `Up`:
```
xiaozhi-dev-mysql   Up
xiaozhi-dev-redis   Up
xiaozhi-dev-api     Up
```

> **⚠️ Lưu ý quan trọng:** Nếu `xiaozhi-dev-api` bị restart liên tục, hãy chờ thêm 30 giây để MySQL hoàn tất khởi tạo rồi chạy lại: `docker compose -f docker-compose.dev.yml restart manager-api`

---

## 🐍 Bước 3: Cài Đặt Python Server

### 3.1. Tạo môi trường ảo (Virtual Environment)

```bash
cd main/xiaozhi-server
python3 -m venv venv
source venv/bin/activate
```

### 3.2. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

> **💡 Mẹo:** Nếu bị lỗi khi cài `torch`, thêm flag:
> ```bash
> pip install torch==2.2.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cpu
> pip install -r requirements.txt
> ```

### 3.3. Cài đặt FFmpeg (nếu chưa có)

```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg -y

# macOS
brew install ffmpeg
```

---

## ⚙️ Bước 4: Cấu Hình

File cấu hình nằm tại `main/xiaozhi-server/data/.config.yaml`. Mặc định đã sẵn sàng nếu bạn dùng Docker Compose:

```yaml
server:
  ip: 0.0.0.0
  port: 8000
  http_port: 8003
manager-api:
  url: "http://127.0.0.1:8002/xiaozhi"
  secret: "20647e59-3109-418d-9465-d89fa35cfeaa"
```

> **Không cần sửa gì** nếu chạy trên cùng một máy.

---

## ▶️ Bước 5: Chạy Python Server

```bash
# Đảm bảo đang ở trong venv
cd main/xiaozhi-server
source venv/bin/activate

# Chạy server
python3 app.py
```

Khi thấy dòng log sau nghĩa là đã thành công:
```
Websocket地址是  ws://x.x.x.x:8000/xiaozhi/v1/
如想测试websocket请用谷歌浏览器打开test目录下的test_page.html
```

---

## 🌐 Bước 6: Mở Giao Diện Web

### 6.1. Trang Web Test (Chat với AI)

Mở terminal mới, chạy:

```bash
cd main/xiaozhi-server/test
python3 -m http.server 8006
```

Sau đó mở trình duyệt: **http://localhost:8006/test_page.html**

### 6.2. Trang Quản Trị (Cấu hình Agent)

Mở terminal mới, chạy:

```bash
cd main/manager-web
npm install
npm run serve -- --port 8001
```

Sau đó mở trình duyệt: **http://localhost:8001**

- **Tài khoản mặc định:** `admin`
- **Mật khẩu mặc định:** `admin`

---

## 🤖 Bước 7: Cấu Hình AI Agent (Oriagent)

1. Vào trang quản trị `http://localhost:8001`
2. Nhấn menu **"Tác nhân AI"** bên trái
3. Chọn một Agent hoặc tạo mới
4. Điền thông tin Oriagent:
   - **Oriagent App ID:** Lấy từ trang [oriagent.com](https://oriagent.com)
   - **Oriagent Base URL:** `https://api.oriagent.com`
   - **Oriagent Auth Token:** API Key lấy từ Oriagent
5. Nhấn **"Lưu cấu hình"**

> **💡 Chưa có tài khoản Oriagent?**
> 1. Vào [oriagent.com](https://oriagent.com) → Đăng ký
> 2. Tạo App mới → Viết System Prompt cho nhân vật
> 3. Vào phần API Keys → Copy `App ID` và `Auth Token`

---

## 🎙️ Bắt Đầu Trò Chuyện

1. Mở **http://localhost:8006/test_page.html**
2. Nhấn nút **"Kết nối"**
3. Gõ tin nhắn hoặc nhấn micro để nói chuyện với AI!

---

## 📊 Tổng Quan Các Cổng (Ports)

| Cổng | Dịch vụ | Mô tả |
|---|---|---|
| `3306` | MySQL | Database |
| `6379` | Redis | Cache |
| `8000` | WebSocket Server | Kết nối thiết bị / Web Test |
| `8001` | Vue.js Dev Server | Giao diện quản trị |
| `8002` | Java Manager API | Backend REST API |
| `8003` | HTTP Server | Vision API |
| `8006` | Static File Server | Trang Web Test |

---

## ❓ Xử Lý Lỗi Thường Gặp

### Lỗi `ModuleNotFoundError: No module named 'aioconsole'`
→ Bạn chưa kích hoạt môi trường ảo. Chạy `source venv/bin/activate` trước khi chạy `python3 app.py`.

### Lỗi `401 Unauthorized` khi gọi Oriagent
→ Kiểm tra `Oriagent Auth Token` đã đúng chưa. Vào trang quản trị nhập lại token.

### Lỗi `address already in use` (port 8000 hoặc 8003)
→ Có một tiến trình cũ đang chạy. Tắt nó đi:
```bash
kill $(lsof -t -i:8000) 2>/dev/null
kill $(lsof -t -i:8003) 2>/dev/null
```

### Container `xiaozhi-dev-api` bị restart liên tục
→ MySQL chưa sẵn sàng. Chờ 30 giây rồi:
```bash
docker compose -f docker-compose.dev.yml restart manager-api
```

---

## 🏗️ Kiến Trúc Hệ Thống

```
┌──────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Web Admin   │────▶│  Java Manager    │────▶│     MySQL       │
│  (Vue.js)    │     │  API (:8002)     │     │    (:3306)      │
│  :8001       │     └──────────────────┘     └─────────────────┘
└──────────────┘              │
                              │ Cấp cấu hình
                              ▼
┌──────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Web Test /  │────▶│  Python Server   │────▶│  Oriagent Cloud │
│  Thiết bị    │ WS  │  (app.py :8000)  │HTTP │  (Dify LLM)     │
│  :8006       │     └──────────────────┘     └─────────────────┘
└──────────────┘
```

---

**Chúc bạn triển khai thành công! 🎉**
