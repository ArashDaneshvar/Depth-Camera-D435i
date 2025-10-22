import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

pipeline.start(config)


while True:
    frames = pipeline.wait_for_frames()
    depth = frames.get_depth_frame()
    if not depth:
        continue

    depth_frame = np.asanyarray(depth.get_data())

    # Normalize depth frame for visualization
    depth_normalized = cv2.normalize(depth_frame, None, 0, 255, cv2.NORM_MINMAX)
    depth_gray = depth_normalized.astype(np.uint8)

    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_gray, alpha=0.08), cv2.COLORMAP_INFERNO)

    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break

    cv2.imshow("Depth Frame", depth_colormap)

pipeline.stop()
cv2.destroyAllWindows()
