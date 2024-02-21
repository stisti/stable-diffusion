# Simple Stable Diffusion

1. Get python 3.9 somehow

    For example, install miniconda and then:
    ```
    conda create -n sd python=3.9
    conda activate sd
    ```

2. Install dependencies

    ```
    pip install -r requirements.txt
    ```

3. Get the model and convert to ONNX format

    ```
    optimum-cli export onnx --model runwayml/stable-diffusion-v1-5 sd_v15_onnx/
    ```

4. Generate an image

    ```
    python example.py
    ```
