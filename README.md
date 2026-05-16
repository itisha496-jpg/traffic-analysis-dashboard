# 🚦 Traffic Analysis Dashboard

## Overview
AI-powered dashcam video analysis pipeline for Indian roads that detects traffic violations, junctions, and vehicles.

## Tasks Covered
- Task 1: Traffic Violation Detection (Helmet-less, Wrong-side, Signal jumping, Mobile use, Triple riding)
- Task 2: Junction & Road Event Detection
- Task 3: Vehicle Detection & Classification
- Task 4: Analytical Dashboard

## Tech Stack
- YOLOv8 (Ultralytics) — Object Detection
- OpenCV — Video Processing
- Streamlit — Dashboard
- Plotly — Charts
- Python 3.10+

## Setup Instructions

### 1. Install Dependencies
pip install ultralytics streamlit plotly opencv-python-headless

### 2. Run Detection Pipeline
python pipeline.py

### 3. Run Dashboard
streamlit run dashboard.py

## Results on Test Video
- Total Vehicles: 11,767
- Total Violations: 10
- Total Junctions: 5

## Known Limitations
- Helmet detection requires fine-tuned model
- Junction classification is rule-based
- Triple riding detection needs pose estimation
- Works best in daylight conditions

- <img width="1874" height="750" alt="Screenshot 2026-05-15 172549" src="https://github.com/user-attachments/assets/cea0686f-e381-4117-849f-4d203d427ebf" />
<img width="1846" height="826" alt="Screenshot 2026-05-15 172606" src="https://github.com/user-attachments/assets/10744660-0d19-4819-8cbd-482a31ff00f6" />


