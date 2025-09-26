import gradio as gr
from transformers import pipeline

# Loading model from local folder
model_pipeline = pipeline("sentiment-analysis", model="./sentiment-model")

def analyze(text):
    result = model_pipeline(text)[0]
    label_map = {"LABEL_0": "NEGATIVE", "LABEL_1": "POSITIVE"}
    label = label_map.get(result['label'], result['label'])
    return f"{label} ({round(result['score'], 2)})"

demo = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(lines=2, placeholder="Enter a sentence..."),
    outputs="text",
    title="Sentiment Analysis",
    description="DistilBERT fine-tuned on IMDb dataset"
)

if __name__ == "__main__":
    demo.launch()
