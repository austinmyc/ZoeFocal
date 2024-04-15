<h1 align="center">
  <br>
  <img src="https://github.com/austinmyc/ZoeFocal/assets/59735570/4edcdb24-384f-41cb-acb2-39fa0c184b4f" width="250">
  <br>
  
</h1>
<h4 align="center">An Improvement study based on <a href="https://github.com/isl-org/ZoeDepth">ZoeDepth</a> for Zero-shot Depth Estimation</h4>
<p align="center">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white">
</p>

<p align="center">
  <a href="#background">Background</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#sample-results">Sample Results</a> •
  <a href="#credits">Credits</a> •
  
</p>


![5e94ba99-9218-4941-8ce2-d420461243e9](https://github.com/austinmyc/ZoeFocal/assets/59735570/9ca0fa96-a712-42d0-bddb-b76d24376d45)



## Background

This study aims to develop a new model to improve the generalization ability of metric depth estimation (MDE) of the ZoeDepth model. Based on
it we designed a new module to introduce focal length information, aiming to capture the relevant information in indoor and outdoor images and achieve better performance.

The trained model would output a matrix of size 384 x 512, where each value in the matrix is the MDE corresponds to the relevant pixel of the input image.

## How To Use

To run this model, simply clone the repo and ensure you have the following packages installed (other than PyTorch):

- [onnx](https://github.com/onnx/onnx)
- [onnxruntime](https://github.com/microsoft/onnxruntime)
- [gradio](https://github.com/gradio-app/gradio)

Run `main.py` , after the gradio interface has been launched, go to `http://127.0.0.1:7860` on your browser.

*Voila!*


## Sample Results

<h2 align="center">
<img src="https://github.com/austinmyc/ZoeFocal/assets/59735570/8eb12171-a2eb-4bd1-a684-c30a4b8b8b19" width="750">
<br>
<img src="https://github.com/austinmyc/ZoeFocal/assets/59735570/b360bf72-2f74-43d3-b2aa-d39cd825d3ba" width="750">
<br>
<img src="https://github.com/austinmyc/ZoeFocal/assets/59735570/ad3fb4d6-daab-4c10-884e-c9879261e23e" width="750">
<br>

<img src="https://github.com/austinmyc/ZoeFocal/assets/59735570/44ec4e59-8b89-4b1f-b6c6-1aea36b11bd8" width="750">
</h2>

## Credits
