# mini-copilot

by [Satvik](https://www.linkedin.com/in/satvik-paramkusham/)

Mini-Copilot is a local copilot that you can run on your machine without the internet.

### What can it do?
It can teach you a history lesson, debate with you, and even play word games. You can configure it to do a lot more.

### Specifications
- Framework: FastAPI
- Provider: Ollama Local API

### Salient features of Mini-copilot
- Runs without internet
- No GPU required
- Doesn't use Langchain or LlamaIndex
- Fully expandable
- Fully Open Source

## Getting Started

Follow these instructions to get the Mini-Copilot app running on your local machine:

### 1. Install Ollama and run the model using CLI.
I am using the 'dolphin-phi' model. You can choose other models from [Ollama library](https://ollama.ai/library)
```bash
ollama run dolphin-phi
```

### 2. Clone the repository
```bash
git clone https://github.com/satvik314/mini-copilot.git
```

### 3. Navigate to the cloned repository
```bash
cd mini-copilot
```

### 4. Install the required libraries
```bash
pip install -r requirements.txt
```

### 5. Run the FastAPI App
```bash
uvicorn main:app --reload
```

In the app, you can choose among the many actions already configured. 

⭐️ Leave us a star on GitHub.
