import cv2
from ultralytics import YOLO

# Load a pre-trained model (YOLOv8 Nano is fast and lightweight)
model = YOLO('best.pt') 

# Open the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

print("Starting FixLens Vision... Press 'q' to quit.")

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # The AI "looks" at the frame
    results = model(frame, stream=True)

    # Draw boxes around what it sees
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Get coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            
            # Get class name (what object is it?)
            cls = int(box.cls[0])
            name = model.names[cls]
            confidence = float(box.conf[0])

            # Draw the box on the screen
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Put the label (FIXED LINE BELOW)
            cv2.putText(frame, f"{name} {confidence:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the video feed
    cv2.imshow('FixLens Vision Prototype', frame)

    # Press 'q' to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()