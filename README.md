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
