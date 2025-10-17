# Depth-Camera-D435i

## Project Overview

In this project, I use the **Intel RealSense D435i** depth camera to explore how to capture and process depth and color data on different platforms.

The main goals of the project are to:

- **Stream depth and color data** from the D435i camera  
- **Use the alignment feature** to align depth frames with color frames  
- **Test and compare performance** on both **Windows** and **NVIDIA Jetson Nano (Ubuntu)** environments  

---

## About the Intel RealSense D435i

The **Intel RealSense D435i** is a depth-sensing camera that integrates:
- A pair of **stereo infrared sensors** for depth estimation  
- A **color (RGB) camera**  
- An **inertial measurement unit (IMU)** for motion tracking  

This combination allows it to capture synchronized RGB, depth, and motion data — making it ideal for robotics, computer vision, and 3D perception tasks.

---

## What This Repository Includes

| Section | Description |
|----------|--------------|
| `windows_setup/` | Installation steps and test scripts for Windows 10 |
| `jetson_nano_setup/` | Setup instructions and install script for Jetson Nano (Ubuntu) |
| `examples/` | Python scripts for streaming, alignment, and visualization |
| `docs/` | Notes, screenshots, and troubleshooting information |

---

## Key Features

- Capture and visualize RGB-D frames in real time  
- Align depth to color using the **`rs.align()`** function from the RealSense SDK  
- Run the same code on both desktop and embedded platforms  
- Validate camera performance and frame synchronization  

---

## Installation

## Prerequisites (both platforms)
- Intel RealSense D435i connected via USB 3.0 (use a good cable and USB 3 port)  
- Recommended Python: **3.7–3.11** (prebuilt `pyrealsense2` wheels). Newer Python versions may require building from source.

---

## Windows 10 / 11 — Step-by-step

1. **Install Intel RealSense SDK / Viewer** (optional but recommended)  
   - Download the latest releases from the [Intel RealSense GitHub](https://github.com/IntelRealSense/librealsense/releases)  
   - Install the SDK and drivers (includes `realsense-viewer`)  
   - Use the viewer to check camera streams and firmware.

2. **Verify device in Device Manager**  
   - Open *Device Manager* → look for Intel RealSense devices (RGB, Depth, etc.)  
   - Update firmware if prompted.

3. **Install Python dependencies**  
   - Open CMD / PowerShell (using the same Python environment you’ll run scripts from)  
   - Run:
     ```bash
     pip install numpy opencv-python
     pip install pyrealsense2
     ```
   - If `pip install pyrealsense2` fails, check your Python version. Prebuilt wheels exist for Python 3.7–3.11. Otherwise, you may need to build from source.

4. **Quick test**  
   - Run the RealSense Viewer:  
     ```bash
     realsense-viewer
     ```  
   - Run a simple Python script:

     ```python
     # simple_test.py
     import pyrealsense2 as rs
     p = rs.pipeline()
     p.start()
     frames = p.wait_for_frames()
     print("Frames type:", [f.profile for f in frames])
     p.stop()
     ```

     ```bash
     python simple_test.py
     ```

5. **Troubleshooting**  
   - Ensure USB 3.0 connection  
   - Update camera firmware  
   - Use 64-bit Python  
   - Check GitHub issues / RealSense support for pip wheel problems

---

## NVIDIA Jetson Nano (Ubuntu) — Step-by-step Installation

> ⚠️ Jetson versions (JetPack) and L4T kernel versions matter.  
> Always refer to the official Intel RealSense Jetson guide and helper scripts for your specific setup.

**Reference:** [Intel RealSense Jetson Guide](https://github.com/IntelRealSense/librealsense/blob/master/doc/Jetson.md)

---

### 1. Update system & install prerequisites

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y git cmake build-essential libssl-dev libusb-1.0-0-dev
```

### 2. Follow the official Jetson installation guide

Intel provides a Jetson-specific guide with scripts to patch kernel modules and install `librealsense` for Jetson devices.  

- Works for many JetPack / L4T versions  
- Always use the official scripts corresponding to your JetPack/L4T version  

**Reference:** [Intel RealSense Developer Documentation](https://github.com/IntelRealSense/librealsense/blob/master/doc/Jetson.md)

### 3. Use JetsonHacks / install script (convenience)

The [JetsonHacksNano/installLibrealsense](https://github.com/JetsonHacksNano/installLibrealsense) repository provides a tested script to build and install `librealsense` on Jetson Nano.

```bash
git clone https://github.com/JetsonHacksNano/installLibrealsense.git
cd installLibrealsense
./scripts/patchUbuntu.sh   # or follow instructions in the repo
```
🔹 Adjust the steps according to your JetPack / L4T version.

### 4. Build / install pyrealsense2 on Jetson

On Jetson, prebuilt Python wheels are rare, so building from source is recommended:
```bash
cd ~
git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense/wrappers/python
sudo apt install python3-dev python3-pip
pip3 install -r requirements.txt || true
python3 setup.py build
sudo python3 setup.py install
```
> ⚠️ Exact commands may vary depending on your JetPack / L4T version. Always check the official guide and JetsonHacks repo for updates.

### 5. Verify installation 
1. Plug in the camera and run the RealSense Viewer:
```bash
realsense-viewer
```
2. Or test with a quick Python snippet:
```bash
python3 -c "import pyrealsense2 as rs; p=rs.pipeline(); p.start(); frames=p.wait_for_frames(); print('OK'); p.stop()"

```

## Alignment / Example verification
Once **`pyrealsense2`** works, run your alignment demo to verify depth-to-color alignment: 
``` bash

```


## Useful references
Intel RealSense (librealsense) GitHub — build & releases. [github](https://github.com/IntelRealSense/librealsense?utm_source=chatgpt.com)   
pyrealsense2 (PyPI) — Python wrapper and supported versions. [pypi](https://pypi.org/project/pyrealsense2/2.54.2.5684/?utm_source=chatgpt.com)   
RealSense Jetson installation guide — Jetson-specific steps and kernel patches. [RealSense Documentation](https://dev.realsenseai.com/docs/nvidia-jetson-tx2-installation?utm_source=chatgpt.com)   
JetsonHacks **`installLibrealsense`** — convenience scripts for Jetson Nano. [github](https://github.com/JetsonHacksNano/installLibrealsense?utm_source=chatgpt.com)   
