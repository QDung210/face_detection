# Face Detection Setup Guide

## Trường hợp 1: Có IP Camera

Nếu bạn đã có IP Camera, hãy thực hiện bước sau:

- Sửa đường link trong code tại dòng:
  ```python
  cap = connect_rtsp_stream("rtsp://localhost:8554/test")
  ```
- Thay thế bằng đường link RTSP của IP Camera của bạn

---

## Trường hợp 2: Không có IP Camera (Chỉ có Webcam)

Để tạo giả lập IP camera bằng webcam, bạn cần tải các phần mềm sau:

### 📥 Download Required Software

1. **OBS Studio**: [https://obsproject.com/](https://obsproject.com/)
2. **OBS RTSP Server Plugin**: [obs-rtspserver-v3.1.0-macos-universal.zip](https://github.com/iamscottxu/obs-rtspserver/releases/tag/v3.1.0)
   > 💡 *Kéo xuống cuối trang releases để tải file zip*

### 🔧 Hướng dẫn cài đặt

#### **Bước 1:** Cài đặt Plugin
- Giải nén file `obs-rtspserver-v3.1.0-macos-universal.zip`
- Copy thư mục `obs-plugins` vào thư mục cài đặt OBS
  ```
  Ví dụ: C:\Program Files\obs-studio
  ```

#### **Bước 2:** Thiết lập Video Source
- Mở phần mềm **OBS Studio**
- Trong phần **Sources**, bấm dấu **`+`**
- Chọn **"Video Capture Device"**
- Bấm **OK** hai lần

#### **Bước 3:** Copy RTSP Link
- Bấm **Tools** → Chọn **RtspServer**
- Bấm **"RtspServer.Properties.Target.Address.Copy"** để copy link localhost

#### **Bước 4:** Start RTSP Server
- Bấm **"RtspServer.Properties.StartOutput"** để bắt đầu streaming

#### **Bước 5:** Cập nhật Code
- Mở file `rtsp.py`
- Tìm dòng:
  ```python
  cap = connect_rtsp_stream("rtsp://localhost:8554/test")
  ```
- Thay thế bằng đường link vừa copy từ bước 3

#### **Bước 6:** Run Code
```bash
python rtsp.py
```

---
