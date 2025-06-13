import cv2
from haar_cascade import face_detection
from eigenfaces import EigenFaceRecognizer

def connect_rtsp_stream(rtsp_url):
    "Hàm này để kết nối tới IP Camera qua giao thức RTSP"
    cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
    if not cap.isOpened():
        raise Exception("Cannot connect to RTSP stream")
    return cap

def extract_frame(cap, resize_shape=(640, 360)):
    "Hàm này để trích xuất frame bằng cv2.CAP_FFMPED ở trên"
    ret, frame = cap.read()
    if not ret:
        return None
    frame = cv2.resize(frame, resize_shape)
    return frame

def detect_and_recognize(frame, haar_cascade, recognizer):
    "Hàm này dùng thuật toán haar_cascade để phát hiện khuôn mặt và vẽ box"
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w]
        try:
            name, dist = recognizer.predict(face_img)
            text = f"{name} ({dist:.0f})"
        except:
            text = "Unknown"
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    return frame

if __name__ == "__main__":
    cap = connect_rtsp_stream("rtsp://localhost:8554/test")
    alg = "haarcascade_frontalface_default.xml"
    haar_cascade = cv2.CascadeClassifier(alg)
    recognizer = EigenFaceRecognizer()

    while True:
        frame = extract_frame(cap)
        if frame is None:
            break
        frame = detect_and_recognize(frame, haar_cascade, recognizer)
        cv2.imshow("Live Face Recognition", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
