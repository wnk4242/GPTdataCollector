## Automatically Collect ChatGPT Responses Using the OpenAI API

## Overview

This project demonstrates how to **automatically collect ChatGPT responses** using the **OpenAI API**. Instead of manually entering prompts on the ChatGPT website and copying the results, this Python-based workflow allows users to programmatically send prompts to ChatGPT, retrieve structured outputs, and save them directly into organized datasets (e.g., CSV files).

This technique is particularly useful for:
- **Large-scale data collection**
- **Automation of repetitive ChatGPT tasks**

---

## Features

- Automatically submit prompts to ChatGPT using the OpenAI API.
- Retrieve structured responses including scores and rationales.
- Store results in a CSV file for easy analysis.
- Customize prompts and rubrics for different research or evaluation purposes.
- Includes progress bars and rate-limiting controls to manage API requests.

---

## Requirements

- Python 3.8+
- OpenAI Python SDK (`openai`)
- pandas
- tqdm

Install the required packages:

```bash
pip install openai pandas tqdm
```

---

## How It Works

1. **Connect to the OpenAI API**: Securely load your API key.
2. **Send prompts programmatically**: Use Python to send each prompt to ChatGPT.
3. **Parse the responses**: Extract the scores and explanations.
4. **Save the results**: Organize everything into a structured CSV file.

---

## Example: Grading ESL Student Grammar

Prepare your prompts: Define a list of sentences or questions you want ChatGPT to evaluate.

Write a grading rubric: Craft a clear instruction set for ChatGPT, specifying how it should assign scores.

This repository provides an example where:
- Sentences written by ESL students are evaluated.
- ChatGPT scores each sentence from 1 (poor grammar) to 5 (excellent grammar) based on a rubric.
- Rationales are collected explaining each assigned score.

Run the script:

```bash
main.py
```

You will get a `chatgpt_esl_grammar_scores.csv` file containing:
- Student sentences
- Assigned scores
- Explanations
- Metadata (iteration number, original order, etc.)

---

## Project Structure

```
.
├── main.py
├── API.txt             # Your OpenAI API key
├── chatgpt_esl_grammar_scores.csv
├── README.md
```

**Note:** For security, **never** share or commit your API key to GitHub.

---

## Customization

You can easily adapt this project to:
- Grade essays, short answers, or discussion posts.
- Score creativity, critical thinking, or language use.
- Simulate peer feedback or automated teaching assistants.

---

## Disclaimer

This project relies on the consistency of ChatGPT outputs. In real-world grading applications, human validation is recommended to ensure fairness and accuracy.

