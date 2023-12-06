# Anti-Spoofing Detector

The **AntiSpoofingDetector** is an advanced anti-spoofing/liveness detection system that leverages facial recognition technology. This project is implemented using **Python** and **OpenCV**, providing a robust solution to distinguish between real faces and spoof attempts.

## Features

- **Facial Recognition:** The detector utilizes state-of-the-art facial recognition techniques to identify and authenticate real faces.
  
- **Liveness Detection:** With the help of a trained model, the system assesses the liveness of detected faces to prevent spoofing attempts.

- **Python and OpenCV:** The project is implemented in Python, a versatile and widely-used programming language, and employs the OpenCV library for computer vision tasks.

- **Trained Model:** The AntiSpoofingDetector incorporates a pre-trained model, ensuring accurate and reliable performance in different scenarios.

## Installation

To use the AntiSpoofingDetector, you need to install the following dependencies:

### OpenCV

```bash
pip install opencv-python
```

### Ultralytics

```bash
pip install ultralytics
```
### Mediapipe

```bash
pip install mediapipe
```

### PyTorch (Optional, for GPU acceleration)

If you have a compatible GPU and want to accelerate the system using CUDA, follow these steps:

1. Install the CUDA Toolkit: [CUDA Toolkit Installation Guide](link-to-cuda-installation-guide).

2. Install PyTorch with GPU support: https://pytorch.org/get-started/locally/

## Unzip Dataset, Runs, and Models

The AntiSpoofingDetector relies on various archives for its functionality. Follow these steps to set up the necessary components:

### 1. Download the Dataset
Obtain the dataset file named `Dataset.zip` from the provided source.

### 2. Extract the Dataset
Locate the downloaded `Dataset.zip` file in your file system.

#### On Windows:
- Right-click on the `Dataset.zip` file.
- Select "Extract All..." and choose the destination folder.

#### On Linux or macOS:
- Open a terminal.
- Navigate to the directory containing the `Dataset.zip` file.
- Run the following command:
    ```bash
    unzip Dataset.zip
    ```

### 3. Download the Runs
Obtain the runs archive file named `runs.zip` from the provided source.

### 4. Extract the Runs
Locate the downloaded `runs.zip` file in your file system.

#### On Windows:
- Right-click on the `runs.zip` file.
- Select "Extract All..." and choose the destination folder.

#### On Linux or macOS:
- Open a terminal.
- Navigate to the directory containing the `runs.zip` file.
- Run the following command:
    ```bash
    unzip runs.zip
    ```

### 5. Download the Models
Obtain the models archive file named `models.zip` from the provided source.

### 6. Extract the Models
Locate the downloaded `models.zip` file in your file system.

#### On Windows:
- Right-click on the `models.zip` file.
- Select "Extract All..." and choose the destination folder.

#### On Linux or macOS:
- Open a terminal.
- Navigate to the directory containing the `models.zip` file.
- Run the following command:
    ```bash
    unzip models.zip
    ```

By following these steps, you'll have successfully extracted the necessary components for the AntiSpoofingDetector, including the dataset, runs, and models. Adjust the instructions as needed for your specific project structure and user requirements.



## Running the Application

To run the AntiSpoofingDetector, follow these steps:

1. Open a terminal.
2. Navigate to the directory containing `main.py`:
    ```bash
    cd /path/to/AntiSpoofingDetector
    ```
3. Run the main script:
    ```bash
    python main.py
    ```

### Training a New Model

To train a new model, follow these steps:

1. Navigate to the directory containing `train.py`:
    ```bash
    cd /path/to/AntiSpoofingDetector
    ```
2. Run the training script:
    ```bash
    python train.py
    ```
3. After training, use the best model (`best.pt`) from `run/detect/train/weights` and place it in the `models` folder.
4. Use the trained model in `main.py` for liveness detection.


