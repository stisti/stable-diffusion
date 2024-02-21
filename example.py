from optimum.onnxruntime import ORTStableDiffusionPipeline

model_id = "sd_v15_onnx"
pipeline = ORTStableDiffusionPipeline.from_pretrained(model_id)
prompt = "astronaut riding a horse"
image = pipeline(prompt).images[0]
image.save("example.png")