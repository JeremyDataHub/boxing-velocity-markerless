# Markerless 3D Boxing Punch Velocity Estimation

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pose2Sim](https://img.shields.io/badge/Pose2Sim-markerless-green.svg)](https://github.com/perfanalytics/pose2sim)
[![OpenCV](https://img.shields.io/badge/OpenCV-computer_vision-red.svg)](https://opencv.org/)
[![SciPy](https://img.shields.io/badge/SciPy-signal_processing-orange.svg)](https://scipy.org/)

> Multi-camera markerless motion capture pipeline for estimating 3D boxing punch velocity in ecological conditions. Developed within the REVEA research program (French Boxing Federation × M2S Laboratory, Université Rennes 2).


## Proof-of-Concept Results

| Subject | Wrist | Max Velocity (m/s) | Mean Velocity (m/s) |
|----------|--------|-------------------|---------------------|
| Subject 1 | Right | 11.41 | 6.21 |
| Subject 1 | Left  | 7.08  | 5.32 |
| Subject 2 | Right | 8.48  | 6.39 |
| Subject 2 | Left  | 4.80  | 4.74 |

A velocity threshold of 4 m/s allows automatic discrimination between effective punches and guard repositioning movements.

<p align="center">
  <img src="figures/velocity_profile.png" width="700" alt="Resultant wrist velocity with detected peaks"/>
  <br/>
  <em>Resultant wrist velocity showing automatic punch detection</em>
</p>


## Problem Context

The REVEA research program aims to compare athletic performance between real and virtual environments using immersive VR protocols.

In boxing, punches are executed in fully three-dimensional space. Fighters continuously rotate, translate and change orientation inside the ring. A single planar 2D analysis is therefore insufficient.

Additionally, motion capture had to be markerless because recordings were performed during real sparring sessions under ecological conditions.

The challenge was to design a robust multi-camera video pipeline capable of estimating 3D punch velocity without markers and without disrupting athletes.


## Evaluated Approaches

Several solutions were explored:

**Sports2D** is limited to planar 2D analysis and not suitable for rotating athletes who move freely in space.

**DeepLabCut** requires extensive manual labeling of training data. 3D reconstruction requires additional complex setup and the uniformity of boxing gloves makes keypoint detection challenging.

**Custom OpenCV tracking** would be technically feasible but require implementing a complete multi-view 3D reconstruction framework from scratch.

Because boxers move freely in space and continuously rotate relative to cameras, a full 3D reconstruction framework was necessary. This led to the selection of Pose2Sim.


## Pose2Sim

[Pose2Sim](https://github.com/perfanalytics/pose2sim) is an open-source markerless motion capture pipeline developed by David Pagnon. The system performs 2D pose estimation on each camera view independently, then uses multi-view triangulation to reconstruct 3D joint trajectories.

The pipeline involves synchronized multi-camera videos, intrinsic and extrinsic calibration, 2D pose estimation per camera, triangulation to obtain 3D coordinates, and export to .trc format (industry-standard biomechanics file).

When cameras are properly calibrated and synchronized, Pose2Sim generates temporally consistent 3D coordinates of body joints, enabling biomechanical analysis.

In this project, the .trc file contains 3D positions (x, y, z) of each joint at each timestamp. This file can be visualized directly in OpenSim for quality control. Python scripts then process the same .trc file to compute punch velocities from wrist trajectories.

<p align="center">
  <img src="media/pose_estimation_visualization.gif" width="600" alt="3D pose estimation tracking"/>
  <br/>
  <em>3D joint tracking from multi-camera triangulation</em>
</p>


## System Pipeline

### Proof-of-Concept Setup

Initial trials with GoPro cameras in the boxing ring environment faced calibration challenges due to wide-angle fish-eye distortion on the overhead camera, large inter-camera distances (approximately 5m), and uncontrolled lighting with background activity.

A controlled proof-of-concept was therefore conducted using two synchronized smartphones at optimal distance (approximately 2m), demonstrating protocol feasibility before scaling to ecological conditions.

```
Camera 1 (Smartphone 1080p 60fps)  ──┐
                                     ├──▶ Synchronization
Camera 2 (Smartphone 1080p 60fps)  ──┘            │
                                                  ▼
                                 Intrinsic Calibration (Pose2Sim)
                                                  │
                                                  ▼
                                 Extrinsic Calibration (Pose2Sim)
                                                  │
                                                  ▼
                              2D Pose Estimation per Camera (Pose2Sim)
                                                  │
                                                  ▼
                                  3D Triangulation (Pose2Sim)
                                                  │
                                                  ▼
                                3D Joint Positions (.trc Output)
                                                  │
                                                  ▼
                                         Velocity Computation
                                                  │
                                                  ▼
                                   Peak Detection (4m/s Threshold)
```

This validated protocol can now be adapted to the original ring setup with improved calibration procedures (larger checkerboard format, optimized camera placement).


## Velocity Computation Strategy

The analysis is performed on .trc files generated by Pose2Sim after 3D reconstruction and filtering.

The wrist joint is used as a proxy for fist velocity. From the 3D position over time, velocity components are computed using numerical time differentiation. Resultant velocity is computed as the square root of the sum of squared velocity components (vx² + vy² + vz²). Peaks above 4 m/s are detected as effective punches.

The full implementation is available in `vitesses_poings.py`.


## Key Engineering Challenges

### Fish-Eye Overhead Camera

The overhead GoPro required fish-eye mode to capture the entire ring area. This significantly complicated extrinsic calibration.

An A3 checkerboard with 7 cm squares was selected and tested at optimized distances to ensure stable detection across all camera views.


### Multi-Person Pose Instability

Multi-person detection produced unstable reconstructions due to occlusions and overlapping limbs during sparring sequences.

Single-subject segmented processing was adopted to improve reconstruction robustness and reduce computational overhead.


### Camera Synchronization

Initial synchronization attempts produced low correlation scores because captured footage lacked sufficiently distinctive movement features.

Introducing a vertical jump at the start of each recording created a strong temporal alignment event that significantly improved synchronization quality.


## Tech Stack

| Category | Tools |
|----------|-------|
| 3D Markerless Capture | Pose2Sim |
| Programming | Python |
| Numerical Processing | NumPy, SciPy |
| Computer Vision | OpenCV |
| Visualization | Matplotlib |
| Hardware | GoPro ×3, Smartphones ×2 |

## Academic Reference

This project was conducted as part of:

> Birba, J., Giot, B., Le Gall, M. (2025). Markerless 3D estimation of boxing punch velocity in ecological conditions. Master 2 DIGISPORT Graduate School, Rennes 2 University. REVEA Research Program, M2S Laboratory × French Boxing Federation.

*Jérémy Birba | [LinkedIn](https://linkedin.com/in/birba-jeremy)*
