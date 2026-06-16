# Satellite Image Change Detection System

A computer vision project that detects and quantifies changes between satellite images captured at different points in time using Python and OpenCV.

## Features

* Difference Map Generation
* Binary Change Detection
* Noise Reduction
* Contour-Based Region Detection
* Bounding Box Visualization
* Change Area Estimation
* Configurable Detection Parameters

Version 2.0 Updates
ORB Feature-Based Image Alignment
The project now includes an experimental image registration module using ORB (Oriented FAST and Rotated BRIEF) feature detection and homography estimation.
Updated pipeline
Satellite Images
↓
ORB Feature Detection
↓
Feature Matching
↓
Homography Estimation
↓
Image Alignment
↓
Change Detection

This helps reduce false positives caused by image shifts and viewpoint differences before performing change detection.Note: Alignment performance depends on image quality, scene similarity, and the amount of structural change between acquisition dates.

## Sample Output

### Vizhinjam Port Development Analysis

![Vizhinjam Results](assets/vizhinjam_results.png)

The system successfully identified infrastructure expansion and construction activity from multi-temporal satellite imagery.

## Technologies Used

* Python
* OpenCV
* NumPy
* Matplotlib

## Pipeline

```text
Input Images
      ↓
Preprocessing
      ↓
Difference Calculation
      ↓
Thresholding
      ↓
Noise Removal
      ↓
Contour Detection
      ↓
Change Statistics
```

## Project Structure

```text
satellite-change-detection/
│
├── src/
│   ├── image_loader.py
│   ├── preprocessing.py
│   ├── change_detector.py
│   └── config.py
│
├── requirements.txt
├── README.md
└── main.py
```

## Usage

```bash
python main.py
```

Configure detection parameters in:

```python
src/config.py
```

## Case Study

### Vizhinjam Port, Kerala

Observed changes:

* Port infrastructure expansion
* Increased storage areas
* Road network development
* Coastal construction activity

## Current Limitations

* Sensitive to image misalignment
* Affected by lighting and contrast differences
* Requires images of the same dimensions

## Future Improvements

* Image Registration
* NDVI Vegetation Analysis
* FastAPI Dashboard
* Automated Report Generation
* Multi-temporal Change Analysis

## Learning Outcomes

* Computer Vision
* Image Processing
* Change Detection
* Data Visualization
* Earth Observation Concepts

## Author

Developed as part of a personal Earth Observation and Aerospace Software Engineering portfolio.
