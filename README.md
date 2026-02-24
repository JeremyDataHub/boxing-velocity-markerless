# Markerless 3D Boxing Punch Velocity Estimation

> Multi-camera markerless motion capture pipeline for estimating 3D boxing punch velocity in ecological conditions. Developed within the REVEA research program (French Boxing Federation × M2S Laboratory, Université Rennes 2).


<p align="center">
  <img src="media/ring_setup.jpg" alt="Boxing ring multi-camera setup"/>
</p>


## Results

| Subject | Wrist | Max Velocity (m/s) | Mean Velocity (m/s) |
|----------|--------|-------------------|---------------------|
| Subject 1 | Right | 11.41 | 6.21 |
| Subject 1 | Left  | 7.08  | 5.32 |
| Subject 2 | Right | 8.48  | 6.39 |
| Subject 2 | Left  | 4.80  | 4.74 |

A velocity threshold of **4 m/s** allows automatic discrimination between effective punches and guard repositioning movements.

<p align="center">
  <img src="figures/jeremy_resultant_velocity.png" width="600" alt="Resultant wrist velocity"/>
  <br/>
  <em>Example of resultant wrist velocity with detected peaks</em>
</p>


## Problem Context

The REVEA research program aims to compare athletic performance between real and virtual environments using immersive VR protocols.

In boxing, punches are executed in fully three-dimensional space. Fighters continuously rotate, translate and change orientation inside the ring. A single planar 2D analysis is therefore insufficient.

Additionally, motion capture had to be markerless because recordings were performed during real sparring sessions under ecological conditions.

The challenge was to design a robust multi-camera video pipeline capable of estimating 3D punch velocity without markers and without disrupting athletes.


## Evaluated Approaches

Several solutions were explored:

- **Sports2D**  
  Limited to planar 2D analysis. Not suitable for rotating athletes.

- **DeepLabCut**  
  Requires extensive manual labeling. 3D reconstruction requires additional complex setup.

- **Custom OpenCV tracking**  
  Technically feasible but would require full multi-view 3D reconstruction implementation.

Because boxers move freely in space and continuously rotate relative to cameras, a full 3D reconstruction framework was necessary.

This led to the selection of **Pose2Sim**.


## Pose2Sim

**[Pose2Sim GitHub Repository](https://github.com/perfanalytics/pose2sim)**

Pose2Sim is an open-source markerless motion capture pipeline that:

- Uses synchronized multi-camera videos  
- Performs intrinsic and extrinsic calibration  
- Reconstructs 3D joint trajectories via triangulation  
- Exports joint coordinates in `.trc` format  

When cameras are properly calibrated and synchronized, Pose2Sim generates temporally consistent 3D coordinates of body joints, enabling biomechanical analysis.

In this project, the exported `.trc` files were used to compute punch velocities directly from reconstructed wrist trajectories.


## System Pipeline
