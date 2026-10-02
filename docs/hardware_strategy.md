# Hardware Strategy

## Overview

This project supports three deployment modes:

- CPU: local validation, smaller test runs, offline review
- GPU: large-scale training, inference acceleration, production-class experimentation
- NPU: compact on-device inference for privacy-sensitive or edge scenarios

## Recommended deployment

### CPU
- Use for dataset preparation and prototype validation.
- Best for small model testing and document indexing.

### GPU
- Default for training and full-scale inference.
- Best for large context windows and interactive pilots assistance.

### NPU
- Use as a companion inference engine for low-latency local workflows.
- Best for privacy-sensitive data processing and edge deployment.

## Notes

NPU implementations vary by vendor and chipset. Use hardware-specific compilers and runtime drivers to convert the fine-tuned model for deployment.
