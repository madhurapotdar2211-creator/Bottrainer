🤖 BotTrainer – LLM-Based NLU System
BotTrainer is a modern Natural Language Understanding (NLU) system that uses Large Language Models to perform intent classification and entity extraction from both text and voice inputs. It simplifies chatbot development by removing the need for complex training pipelines.


🚀 Features
🔍 Intent Classification – Detects user intent accurately
🧠 Entity Extraction – Extracts structured data from input
🎙️ Voice Input Support – Uses speech recognition for voice commands
⚡ LLM Powered – Works with:
OpenAI API
Ollama (local models like Llama 3)
📊 Model Evaluation – Evaluate predictions using metrics
💻 Interactive UI – Built with Streamlit

project structure :
bottrainer/
bottrainer/
│── app.py
│── src/
│   ├── __init__.py
│   ├── nlu/
│   │   ├── nlu_pipeline.py
│   │   ├── llm_handler.py
│   ├── evaluation/
│       ├── evaluator.py
│── prompts/
│   └── intent_prompt.txt
│── data/               
│── assets/      
│── requirements.txt
│── README.md
│── .gitignore


How It Works
User enters text or voice input
Input is passed to the NLU pipeline
Prompt is generated using a template
LLM processes the input
Output is returned in structured JSON:
JSON
ex:
{
  "intent": "order_food",
  "confidence": 0.95,
  "entities": {}
}

Tech Stack0:
Python
Streamlit
Ollama / OpenAI API
SpeechRecognition
Pandas, Matplotlib, Seaborn


Use Cases:
Chatbot development
Voice assistants
Customer support automation
AI-based intent classification systems
      

