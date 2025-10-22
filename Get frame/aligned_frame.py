import pyrealsense2 as rs
import numpy as np
import cv2

# Initialize camera pipeline
pipeline = rs.pipeline()
config = rs.config()

# Enable depth and color streams
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Start pipeline
pipeline.start(config)

# Align depth frame to color frame
align_to = rs.stream.color
align = rs.align(align_to)


while True:
    # Wait for a new set of frames
    frames = pipeline.wait_for_frames()
    aligned_frames = align.process(frames)

    # Get aligned frames
    depth_frame = aligned_frames.get_depth_frame()
    color_frame = aligned_frames.get_color_frame()

    if not depth_frame or not color_frame:
        continue

    # Convert frames to numpy arrays
    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())

    # Normalize depth for visualization
    depth_normalized = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX)
    depth_normalized = depth_normalized.astype(np.uint8)
    depth_colormap = cv2.applyColorMap(depth_normalized, cv2.COLORMAP_JET)

    # Stack color + depth images side by side
    combined_image = np.hstack((color_image, depth_colormap))
    cv2.imshow("Both Color and Depth", combined_image)

    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break


pipeline.stop()
cv2.destroyAllWindows()

    