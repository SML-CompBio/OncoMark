## Installation

OncoMark is built on the deep learning framework [TensorFlow](https://www.tensorflow.org/). It is important to install a suitable version of TensorFlow depending on your compute platform (CPU/GPU) and Python environment. The [official TensorFlow installation guide](https://www.tensorflow.org/install) provides detailed instructions.

### Step 1: Install TensorFlow
Visit the [TensorFlow installation guide](https://www.tensorflow.org/install) to choose the appropriate version for your system.

#### Example: Install TensorFlow with GPU Support
For systems with NVIDIA GPUs and CUDA support:

```bash
# Install TensorFlow with GPU support
pip install tensorflow[and-cuda]
```

#### Example: Install TensorFlow for CPU-Only
For systems without GPUs:

```bash
# Install TensorFlow for CPU-only
pip install tensorflow
```

### Step 2: Install OncoMark
After successfully installing TensorFlow, you can install OncoMark directly from PyPI:

```bash
# Install OncoMark from PyPI
pip install OncoMark
```

Alternatively, to install the latest version directly from the GitHub repository:

```bash
# Install OncoMark from GitHub
pip install git+https://github.com/SML-CompBio/OncoMark.git
```

### Step 3: Verify Installation
To verify that OncoMark is installed correctly, run the following commands in Python:

```python
import OncoMark
print(OncoMark.__version__)
```

If the command outputs the version number of OncoMark, the installation was successful.

### Additional Requirements
Ensure that any dependencies, such as `joblib` or `pandas`, are also installed. These will typically be installed automatically with OncoMark, but you can manually install them if needed:

```bash
pip install joblib==1.4.2 pandas==2.2.3 scipy==1.14.1 numpy==2.0.2
```

You’re ready to start using OncoMark! Explore its features to analyze hallmark activity from transcriptomics data.

---
