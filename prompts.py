BASELINE_PROMPT = """
  You are tasked with rephrasing the following sentence to remove any toxic, hateful, or profane language. The rephrased sentence should preserve the **original meaning** and maintain a **neutral tone**.

  Now, please rephrase the following sentence while keeping the meaning intact and ensuring it is free from offensive language. Please return the rephrased sentence.
  Sentence for rephrased: "{input}"

  Respond in the following json format:
  {{
    "original_sentence": "{input}",
    "rephrased_sentence": "rephrased sentence"
  }}
"""


VERIFICATION_QUESTIONS_PROMPT = """
  Based on the original sentence and its rephrased version provided below, generate a list of verification questions that evaluate the quality and correctness of the rephrased sentence.

  **Your task**: For each aspect, create a question to check the quality of the rephrased sentence. Specifically, evaluate:
  
  1. **Intent and Meaning**: Does the rephrased sentence preserve the **original intent** and meaning of the original sentence?
  2. **Tone**: Is the tone of the rephrased sentence **neutral**, without any offensive or inflammatory language?
  3. **Toxic Language**: Has all **toxic language** been removed from the rephrased sentence?
  4. **Profanity**: Has all **profane** or **offensive language** been removed?

  Original Sentence: "{original_sentence}"
  Baseline Rephrasing: "{baseline_response}"

  Please list **one question for each aspect** as shown above. Each question should be clear and easy to evaluate.
  Respond in the following json format:
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
  Answer the following verification questions based on the context provided. Your answer should evaluate the **quality** of the baseline rephrasing according to the questions.

  Original sentence: {original_sentence}
  Baseline Response: {baseline_response}
  Verification Questions: {questions}
  
  **Your answer** should evaluate the baseline rephrasing based on the questions above.

  Respond in the following json format:
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
        "answer": "answer"
       }},
       {{
        "question": "Question",
        "answer": "Answer"
       }}
    ]
  }}
"""



FINAL_PROMPT = """
  Given the following information, analyze the verification questions and their answers to refine and rephrase the original sentence. Your task is to return the **final rephrased sentence** after incorporating the insights from the verification answers.

  Original Sentence: {original_sentence}
  Baseline Rephrasing: {baseline_response}
  Verification Questions and their Answers:
  {verification_answers}

  Use the insights from the answers to improve the baseline rephrasing. Ensure that the rephrased sentence:
  - Is **neutral** and **appropriate** in tone.
  - **Preserves the original meaning**.
  - Has **removed toxic and offensive language**.

  **Return the final rephrased sentence** after these adjustments.

  Respond in the following json format:
  {{
    "analysis": "analysis",
    "final_sentence": "Final rephrased sentence"
  }}
"""

