# Bottrainer
BotTrainer is an LLM-based NLU system for intent classification and entity extraction from text and voice inputs. Built with Streamlit, it integrates OpenAI API and Ollama (e.g., Llama 3) to deliver real-time predictions, making chatbot development faster and easier.

##BotTrainer – LLM-Based NLU System

BotTrainer is an intelligent Natural Language Understanding (NLU) system that uses modern Large Language Models (LLMs) to classify user intents and extract structured information from text or speech input.

It is designed to simplify chatbot training by eliminating the need for complex rule-based systems or large labeled datasets.

##Key Features

Intent Classification
Accurately predicts user intent (e.g., order_food, greeting, etc.)

Entity Extraction
Identifies important information from user input

LLM Integration
Supports both:

OpenAI API

Ollama (local models like Llama 3)

Voice Input Support
Uses speech recognition to process spoken commands

Evaluation Module
Measures model performance using accuracy and other metrics

Interactive UI
Built with Streamlit for easy testing and visualization

## How It Works

User enters text or voice input

Input is processed through an NLU pipeline

A prompt is generated and sent to an LLM

The LLM returns structured JSON output

The system extracts:

Intent

Confidence score

Entities

## Tech Stack

Python

Streamlit

OpenAI API / Ollama

SpeechRecognition

Pandas, Matplotlib, Seaborn

## Use Cases

Chatbot development

Voice assistants

Customer support automation

AI-based intent classification systems

## Highlights

Works with both cloud-based and local LLMs

Beginner-friendly and extensible architecture

Real-time prediction and evaluation

No heavy ML training required
