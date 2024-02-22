from optimum.onnxruntime import ORTStableDiffusionXLPipeline

model_id = "stabilityai/stable-diffusion-xl-base-1.0"
pipeline = ORTStableDiffusionXLPipeline.from_pretrained(model_id, export=True)
prompt = "astronaut riding a horse"
image = pipeline(prompt).images[0]
image.save("example-xl.png")
pipeline.save_pretrained("./onnx-stable-diffusion-xl")
