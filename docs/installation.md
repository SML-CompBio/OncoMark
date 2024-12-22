## Installation
ACSCeND is based on the deep learning framework [PyTorch](https://pytorch.org). It is important for users to choose the suitable version of PyTorch based on different compute platforms. The [official instruction](https://pytorch.org/get-started/locally/) may help you install PyTorch correctly.

### Step 1: Install PyTorch
Visit the [PyTorch installation page](https://pytorch.org/get-started/locally/) to select the appropriate version for your platform (CPU/GPU) and Python environment.

For example, to install PyTorch with CUDA support:

```bash
# Install PyTorch with CUDA (adjust the version as needed)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Or for CPU-only:

```bash
# Install PyTorch for CPU-only
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### Step 2: Install ACSCeND
After successfully installing PyTorch, you can install ACSCeND directly from PyPI:

```bash
# pip
pip install ACSCeND
```

Alternatively, if you want the latest version from the GitHub repository, use:

```bash
# Install directly from GitHub
pip install git+https://github.com/SML-CompBio/ACSCEND.git
```

### Step 3: Verify Installation
To confirm that ACSCeND has been installed successfully, run the following command in Python:

```python
import ACSCeND
print(ACSCeND.__version__)
```

You’re all set! Start exploring the features of ACSCeND.

---