import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

pipeline.start(config)


while True:
    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    if not color_frame:
        continue

    color_frame = np.asanyarray(color_frame.get_data())

    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break

    cv2.imshow("Color Frame", color_frame)

pipeline.stop()
cv2.destroyAllWindows()