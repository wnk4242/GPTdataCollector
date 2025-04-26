import random
from tqdm import tqdm
import pandas as pd
import time
from openai import OpenAI

# Load API key and initialize client
API_KEY = open("API.txt", "r").read()
client = OpenAI(api_key=API_KEY)

# Simulated ESL student sentences (some grammatically correct, some incorrect)
Sentences = [
    "I goes to school every day.",
    "She like to play soccer on weekends.",
    "They are studying for their final exams.",
    "He has went to the store yesterday.",
    "We enjoys cooking dinner together.",
    "My brother plays the piano very well.",
    "Yesterday I am walk to the park.",
    "The cat is sleeping on the sofa.",
    "She don't know the answer.",
    "The students has finished their project."
]

# Define a function to get ChatGPT's grammar score

def get_grammar_score(sentence_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an experienced English teacher grading grammar."},
            {"role": "user", "content": f"You will evaluate the grammatical accuracy of the following sentence: '{sentence_text}'.\n\nUse the following rubric to assign a score from 1 to 5:\n\nScore 5: Grammatically flawless or only very minor errors that do not affect clarity.\nScore 4: Mostly grammatically correct with minor errors that slightly affect flow but not meaning.\nScore 3: Noticeable grammar errors that somewhat affect clarity or naturalness.\nScore 2: Frequent grammar errors that make the sentence hard to understand but not impossible.\nScore 1: Very poor grammar that severely impairs understanding.\n\nProvide your answer by first stating the score in the format 'Score: X', followed by a rationale starting with 'Rationale:' explaining your judgment."}
        ],
        max_tokens=200
    )

    response_text = response.choices[0].message.content.strip()
    try:
        score, explain = response_text.split("Rationale:", 1)
        score = score.replace("Score:", "").strip()
        explain = explain.strip()
    except ValueError:
        score, explain = response_text, "Explanation not provided"

    return score, explain

# Run the scoring process
results = []
num_iterations = 2

total_steps = num_iterations * len(Sentences)

with tqdm(total=total_steps, desc="Grading Grammar", unit="sentence") as pbar:
    for iteration in range(1, num_iterations + 1):
        shuffled_sentences = Sentences[:]
        random.shuffle(shuffled_sentences)
        for sentence_id, sentence in enumerate(shuffled_sentences, start=1):
            original_order = Sentences.index(sentence) + 1
            score_value, explanation = get_grammar_score(sentence_text=sentence)
            results.append({
                "Rater": "ChatGPT",
                "Participant": f"ChatGPT{iteration}",
                "Iteration": iteration,
                "Testing Order": sentence_id,
                "Original Order": original_order,
                "Student Sentence": sentence,
                "Score": score_value,
                "Explanation": explanation
            })
            time.sleep(1)
            pbar.update(1)

# Convert results to DataFrame and save

df_results = pd.DataFrame(results)
df_results.to_csv("chatgpt_esl_grammar_scores.csv", index=False)
