import cv2

def connect_rtsp_stream(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
    if not cap.isOpened():
        raise Exception("Cannot connect to RTSP stream")
    return cap
def extract_frame(cap, resize_shape=(640, 360)):
    ret, frame = cap.read()
    if not ret:
        return None
    frame = cv2.resize(frame, resize_shape)
    return frame
def face_detection(frame):
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)
    text = "No face detected"  # mặc định
    for (x, y, w, h) in face:
        text = "Face Detected"
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    image = cv2.putText(frame, text, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    return image

if __name__ == "__main__":
    cap = connect_rtsp_stream("rtsp://localhost:8554/test")
    alg = "haarcascade_frontalface_default.xml"
    haar_cascade = cv2.CascadeClassifier(alg)
    while True:
        frame = extract_frame(cap)
        if frame is None:
            break
        cv2.imshow("Live", face_detection(frame))
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
