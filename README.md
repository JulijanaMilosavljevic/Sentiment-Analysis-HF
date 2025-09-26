# Sentiment Analysis with Hugging Face

This project demonstrates how to use Hugging Face Transformers to perform sentiment analysis on text data.  
We fine-tuned a pretrained model (`distilbert-base-uncased`) on the IMDb dataset and deployed a Gradio app.

## 🚀 Features
- Fine-tuning with Hugging Face `transformers` and `datasets`
- Evaluation with accuracy, F1-score
- Interactive Gradio demo

## 📦 Installation
```bash
git clone https://github.com/JulijanaMilosavljevic/Sentiment-Analysis-HF.git
cd sentiment-analysis-hf
pip install -r requirements.txt
```
## Downloading the Large Model

> **IMPORTANT:** This project uses a large model file `model.safetensors` (~256 MB) which is **not stored directly in the GitHub repository** due to GitHub's 100 MB file limit.

### Option 1: Using Git LFS (Recommended)
If you want the model to be automatically downloaded when cloning:

```bash
# Install Git LFS (if not already installed)
git lfs install

# Clone the repository
git clone https://github.com/JulijanaMilosavljevic/Sentiment-Analysis-HF.git

# Enter the project directory
cd Sentiment-Analysis-HF

# Pull the LFS files
git lfs pull
