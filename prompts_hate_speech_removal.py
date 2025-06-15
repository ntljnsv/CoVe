BASELINE_PROMPT = """
  You are tasked with changing the following sentence to remove any toxic, hateful, or profane language. The changed sentence should preserve the **original meaning** and maintain a **neutral tone**.

  Now, please change the following sentence while keeping the meaning intact and ensuring it is free from offensive language. Please return the changed sentence.
  Sentence for changing: "{input}"

  Respond only in the following json format:
  {{
    "original_sentence": "{input}",
    "changed_sentence": "changed sentence"
  }}
"""


VERIFICATION_QUESTIONS_PROMPT = """
  Based on the original sentence and its changed version provided below, generate a list of verification questions that evaluate the quality and correctness of the changed sentence.

  **Your task**: For each aspect, create a question to check the quality of the changed sentence. Specifically, evaluate:
  
  1. **Intent and Meaning**: Does the changed sentence preserve the **original intent** and meaning of the original sentence?
  2. **Tone**: Is the tone of the changed sentence **neutral**, without any offensive or inflammatory language?
  3. **Toxic Language**: Has all **toxic language** been removed from the changed sentence?
  4. **Profanity**: Has all **profane** or **offensive language** been removed?

  Original Sentence: "{original_sentence}"
  Baseline Response: "{baseline_response}"

  Please list **one question for each aspect** as shown above. Each question should be clear and easy to evaluate.
  Respond only in the following json format:
  {{
    "questions": [
      "Question 1",
      "Question 2",
      "Question 3",
      "Question 4"
    ]
  }}
"""



VERIFICATION_ANSWER_PROMPT = """
  Answer the following verification questions based on the context provided. Your answer should evaluate the **quality** of the baseline changed sentence according to the questions.

  Original sentence: {original_sentence}
  Baseline Response: {baseline_response}
  Verification Questions: {questions}
  
  **Your answer** should evaluate the baseline changed sentence based on the questions above.

  Respond only in the following json format:
  {{
    "answers": [
      {{
        "question": "Question",
        "answer": "Answer"
       }},
       {{
        "question": "Question",
        "answer": "Answer"
       }},
       {{
        "question": "Question",
        "answer": "Answer"
       }},
       {{
        "question": "Question",
        "answer": "Answer"
       }}
    ]
  }}
"""



FINAL_PROMPT = """
  Given the following information, analyze the verification questions and their answers to refine and change the original sentence. Your task is to return the **final changed sentence** after incorporating the insights from the verification answers.

  Original Sentence: {original_sentence}
  Baseline Response: {baseline_response}
  Verification Questions and their Answers:
  {verification_answers}

  Use the insights from the answers to improve the baseline changed sentence. Ensure that the changed sentence:
  - Is **neutral** and **appropriate** in tone.
  - **Preserves the original meaning**.
  - Has **removed toxic and offensive language**.

  **Return the final changed sentence** after these adjustments.

  Respond only in the following json format:
  {{
    "reasoning": "reasoning",
    "final_sentence": "Final changed sentence"
  }}
"""

