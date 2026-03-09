# Hệ Thống Quản Lý Sinh Viên (Student Management System)

## Thông Tin Cá Nhân

* **Họ tên:** Trần Quốc Sang
* **Mã số sinh viên:** 23715111

---

# Giới Thiệu Dự Án

Đây là dự án **Hệ Thống Quản Lý Sinh Viên** được xây dựng nhằm hỗ trợ việc quản lý thông tin sinh viên thông qua giao diện web.

Người dùng có thể thực hiện các chức năng:

* Thêm sinh viên
* Chỉnh sửa thông tin sinh viên
* Xóa sinh viên
* Tìm kiếm sinh viên theo tên
* Xem thống kê dữ liệu sinh viên
* Xuất dữ liệu sinh viên ra file CSV

Hệ thống được xây dựng với **backend FastAPI** và **frontend ReactJS**, sử dụng **SQLite** làm cơ sở dữ liệu.

---

# Công Nghệ Sử Dụng (Tech Stack)

### Backend

* **FastAPI** – Framework xây dựng REST API
* **SQLAlchemy** – ORM để làm việc với cơ sở dữ liệu
* **SQLite** – Cơ sở dữ liệu nhẹ

### Frontend

* **React JS** – Xây dựng giao diện người dùng
* **Fetch API** – Gửi request đến backend

### Database

* **SQLite**

---

# Công Cụ Hỗ Trợ (Tools)

Trong quá trình phát triển dự án, các công cụ sau đã được sử dụng để hỗ trợ lập trình:

* **Lovable**
* **Angrivity**
* **Cursor**
* **Windsurf**
* **Git & GitHub** – Quản lý phiên bản mã nguồn

---

# Chức Năng Chính

## 1. Quản Lý Sinh Viên

* Thêm sinh viên mới
* Cập nhật thông tin sinh viên
* Xóa sinh viên
* Hiển thị danh sách sinh viên

## 2. Tìm Kiếm

* Tìm kiếm sinh viên theo **tên**
* Kết quả hiển thị **real-time**

## 3. Thống Kê

Hệ thống cung cấp một số thống kê cơ bản:

* Tổng số sinh viên
* GPA trung bình
* Số sinh viên theo ngành học

## 4. Xuất Dữ Liệu

* Xuất danh sách sinh viên ra **file CSV**

---

# Cấu Trúc Thư Mục Dự Án

```
project-root
│
├── backend
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│
├── frontend
│   ├── src
│   │   ├── App.js
│   │   ├── App.css
│
└── README.md
```

---

# Cách Chạy Dự Án

## 1. Chạy Backend

Cài đặt thư viện cần thiết:

```bash
pip install fastapi uvicorn sqlalchemy
```

Chạy server:

```bash
uvicorn main:app --reload
```

Backend sẽ chạy tại:

```
http://127.0.0.1:8000
```

---

## 2. Chạy Frontend

Di chuyển vào thư mục frontend:

```bash
cd frontend
```

Cài đặt dependencies:

```bash
npm install
```

Chạy ứng dụng React:

```bash
npm start
```

Frontend sẽ chạy tại:

```
http://localhost:3000
```

---

# Nhật Ký Thực Hiện (Development Log)

### Bước 1 – Xây dựng Backend

* Thiết kế database bằng **SQLAlchemy**
* Tạo API CRUD cho sinh viên
* Xây dựng API thống kê:

  * tổng số sinh viên
  * GPA trung bình
  * số sinh viên theo ngành

### Bước 2 – Xây dựng Frontend

* Thiết kế giao diện quản lý sinh viên bằng **React**
* Hiển thị bảng danh sách sinh viên
* Xây dựng form thêm và chỉnh sửa sinh viên

### Bước 3 – Bổ sung chức năng

* Tìm kiếm sinh viên theo tên
* Hiển thị thống kê
* Xuất dữ liệu sinh viên ra file CSV

### Bước 4 – Kiểm thử

* Kiểm tra API backend
* Kiểm tra các chức năng CRUD
* Kiểm tra kết nối frontend và backend

---

# Hướng Phát Triển Trong Tương Lai

Một số cải tiến có thể thực hiện trong tương lai:

* Thêm **biểu đồ thống kê (charts)**
* Thêm **hệ thống đăng nhập (authentication)**
* Thêm **phân trang dữ liệu**
* Cải thiện UI với các thư viện như **Material UI hoặc Ant Design**

---

# Tác Giả

**Trần Quốc Sang**
Mã số sinh viên: **23715111**
