# LangChain Parallel Quiz & Notes Generator:
This project demonstrates how to use LangChain parallel chains to generate study notes and quiz questions simultaneously from a single input text using one large language model.
The application uses Groq-hosted LLaMA 3.3 and LangChain’s RunnableParallel to execute multiple tasks in parallel while sharing the same model instance.

# Key Features
Parallel task execution using LangChain
Single LLM shared across multiple tasks
Automatic generation of:
Concise study notes
Five quiz questions
Clean LCEL (LangChain Expression Language) pipeline
Secure API key handling via environment variables

# Project Structure
langchain-parallel-quiz-notes/
│
├── main.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore

# Requirements
Python 3.9+
Groq API key

# Install dependencies

pip install -r requirements.txt
# The program will:
Process the input text
Generate notes and quiz questions in parallel
Merge the results into a single structured output

# Architecture Overview
Input Text
   │
   ├── Notes Generation Chain
   ├── Quiz Generation Chain
   │        (Parallel Execution)
   ↓
Merged Output

# Technologies Used
LangChain
Groq API
LLaMA 3.3 (70B)
Python

# Use Cases
Educational content generation
Study material preparation
AI-assisted learning tools
Demonstration of multi-task LLM pipelines

# License
This project is open-source and available for educational and research purposes.
