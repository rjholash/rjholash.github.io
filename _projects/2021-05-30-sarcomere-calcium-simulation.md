---
layout: page
title: "Calcium Diffusion Simulation in a 3D Sarcomere Model"
description: Computational modeling of the muscle activation process
img: sarcomere_model.jpg
importance: 3
category: computational-biology
---

Graduate students worked with a spatially realistic 3D model of a half-sarcomere to simulate calcium diffusion, buffering, and reuptake during activation and fatigue. The model supports broader understanding of excitation–contraction coupling under different loading conditions.

## Computational Approach

Our model uses a stochastic agent-based approach to simulate:
- Calcium ion release from the sarcoplasmic reticulum
- Diffusion through the sarcomeric space
- Binding to troponin C and other calcium buffers
- Reuptake by SERCA pumps

## Technical Implementation

The simulation is built using MCell, a Monte Carlo simulator for cellular microphysiology, and analyzed with custom Python scripts. The 3D geometry of the sarcomere is reconstructed from electron microscopy data.

## Research Impact

This computational model helps bridge the gap between molecular mechanisms and whole-muscle function, offering insights into how structural changes affect calcium handling during muscle activation and fatigue. The findings have implications for understanding muscle disorders and developing targeted interventions.

## Publication

The methods and findings of this research were published in PLOS Computational Biology:

[Holash RJ, MacIntosh BR (2019) A stochastic simulation of skeletal muscle calcium transients in a structurally realistic sarcomere model using MCell. PLOS Computational Biology 15(3): e1006712.](https://doi.org/10.1371/journal.pcbi.1006712)
