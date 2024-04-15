import onnx

#Load trained model
onnx_model = onnx.load("myonnx.onnx")

onnx.checker.check_model(onnx_model)

print(onnx.helper.printable_graph(onnx_model.graph))

import onnxruntime
import numpy as np
from PIL import Image, ImageOps, ImageDraw
import torch
from torchvision import transforms
import gradio as gr

def running(image):
    
    image = image.resize((512, 384))
    
    x = transforms.ToTensor()(image).unsqueeze(0).cpu()
    
    x.resize(1, 3, 384, 512)
    x = x.numpy()
    
    print(x.shape)
    
    focalx = torch.tensor([518]).numpy()
    
    ort_session = onnxruntime.InferenceSession('myonnx.onnx')
    
    ort_output = ort_session.run(['output'], {'input': x, 'onnx::Unsqueeze_1': focalx})[0]
    
    print(ort_output)

    print(ort_output.shape)
    
    #Draw reference boxes
    middle=ort_output[0][0][192][256]
    upperleft=ort_output[0][0][5][5]
    lowerright=ort_output[0][0][379][507]
    
    colored =  (ort_output - ort_output.min()) / (ort_output.max() - ort_output.min()) * 255
    colored = colored.squeeze()
    
    print(colored.shape)
    
    colored = np.array(colored, dtype=np.uint8)
    i=Image.fromarray(colored)
    g=ImageOps.colorize(i.convert("L"), black="gold", white="black", mid="purple")
    draw = ImageDraw.Draw(g)
    draw.rectangle((5, 5, 35, 35), fill=None, outline=(255, 0,0))
    draw.rectangle((241, 177, 271, 207), fill=None, outline=(255, 0,0))
    draw.rectangle((477, 349, 507, 379), fill=None, outline=(255, 0,0))
    
    return (g, str(middle), str(upperleft), str(lowerright))


demo=gr.Interface(fn=running,
             inputs=gr.Image(type="pil"),
             outputs=[gr.Image(type="pil", label="Depth Map"),gr.Textbox(label="Distance to the middle pixel"), gr.Textbox(label="Distance to the upper left"), gr.Textbox(label="Distance to the lower right")], title="Image Depth Estimation Demo", theme='JohnSmith9982/small_and_pretty', description="Upload / Take a Picture and our model will estimate the depth of the image!")
demo.launch(server_port=7860)
