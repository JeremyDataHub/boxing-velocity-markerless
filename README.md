# Markerless 3D Boxing Punch Velocity Estimation

> Markerless 3D motion capture pipeline for estimating boxing punch velocity in ecological conditions. Developed as part of the REVEA research program in partnership with the French Boxing Federation and the M2S Laboratory, Rennes 2 University.


![Ring Setup](media/ring_setup.jpg)


## Key Results

Feasibility study conducted in real ring conditions using multi camera markerless capture.

| Subject | Wrist | Max velocity (m/s) | Mean velocity (m/s) |
|----------|--------|-------------------|---------------------|
| Subject 1 | Right | 11.41 | 6.21 |
| Subject 1 | Left  | 7.08  | 5.32 |
| Subject 2 | Right | 8.48  | 6.39 |
| Subject 2 | Left  | 4.80  | 4.74 |

A velocity threshold of approximately 4 m/s was identified to distinguish effective punches from guard movements and repositioning.

![Velocity Example](figures/jeremy_resultant_velocity.png)


## Context

The REVEA research program uses virtual reality to optimize athletic performance. In partnership with the French Boxing Federation, researchers at the M2S Laboratory needed to measure real punch velocities in order to compare boxer performance between real and virtual environments.

The core constraint was that motion capture had to be markerless. Data acquisition takes place in ecological conditions in a real boxing ring without interrupting athletes.

The objective of this project was to develop and validate a video based markerless method capable of measuring punch velocity for future integration into the REVEA real versus virtual comparison protocol.


## Approach

Four solutions were evaluated:

Sports2D  
DeepLabCut  
OpenCV  
Pose2Sim  

Pose2Sim was selected. It is an open source markerless motion capture pipeline developed by David Pagnon. It enables 3D reconstruction from synchronized multi camera videos and exports biomechanical data in OpenSim compatible formats.

Pose2Sim was installed, configured, calibrated and tested across multiple acquisition setups.


## Pipeline Overview

Multi camera video acquisition  
↓  
Pose2Sim processing  

• Intrinsic calibration using checkerboard  
• Extrinsic calibration  
• Pose estimation  
• Camera synchronization  
• 3D triangulation  
• Filtering  

↓  

.trc output file containing 3D joint positions over time  

↓  

Python post processing  

• Wrist position extraction  
• Numerical time derivation using numpy.gradient  
• Resultant velocity computation √(vx² + vy² + vz²)  
• Peak detection using scipy.signal.find_peaks  


![Pose2Sim Reconstruction](media/pose2sim_skeleton.gif)


## Repository Structure
