BASELINE_PROMPT = """
  You are tasked with changing the following sentence to make its sentiment more positive while preserving the original meaning. 
  Keep the language simple, clear, and close to the original. Avoid metaphors, extra interpretation, or adding unnecessary descriptive words.
  Do not alter the structure of the sentence or words unless strictly necessary. Only change the words in relation to the sentiment.
  
  Change the following sentence to ensure the meaning stays intact and the tone becomes positive. Please return only the changed sentence.
  Sentence for changing: **"{input}"**
  
  Respond only in the following json format:
  {{
    "original_sentence": "{input}",
    "changed_sentence": "changed sentence"
  }}
"""



VERIFICATION_QUESTIONS_PROMPT = """
  Based on the original sentence and its changed version provided below, generate a list of verification questions evaluate the quality and correctness of the changed sentence.
  The quality and correctness are defined by the preservation of the **original meaning** and the **positive sentiment** of the sentence.
  
  **Your task**: For each aspect, create a question to check the quality of the changed sentence. Specifically, evaluate:
  
  1. **Intent and Meaning**: Does the changed sentence preserve the **original intent** and meaning of the original sentence?
  2. **Tone Shift**: Has the tone of the original sentence been successfully changed from **negative** to **positive**?
  3. **Lexical & Structural Similarity**: Does the changed sentence maintain **lexical** or **structural similarity** to the original?

  Original Sentence: "{original_sentence}"
  Baseline Rephrasing: "{baseline_response}"

  Please list **one question for each aspect** as shown above. Each question should be clear and easy to evaluate.
  Respond only in the following json format:
  {{
    "questions": [
      "Question 1",
      "Question 2",
      "Question 3"
    ]
  }}
"""


VERIFICATION_ANSWER_PROMPT = """
  Answer the following verification questions based on the context provided. Your answer should evaluate the **quality** of the baseline changed sentence according to the questions.
  The quality and correctness are defined by the preservation of the **original meaning** and the **positive sentiment** of the sentence.

  Original sentence: {original_sentence}
  Baseline Response: {baseline_response}
  Verification Questions: {questions}
  
  **Your answer** should evaluate the baseline changed sentence based on the questions above.

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
        "answer": "Answer"
       }}
    ]
  }}
"""


FINAL_PROMPT = """
  Given the following information, analyze the verification questions and their answers to refine and change the original sentence. 
  Your task is to return the **final changed sentence** after using the insights from the verification answers.

  Original Sentence: {original_sentence}
  Baseline Changed Sentence: {baseline_response}
  Verification Questions and their Answers:
  {verification_answers}

  Use the insights from the answers to improve the baseline changed sentence. Ensure that the final sentence:
    - Preserves the **original meaning**.
    - Has a **positive tone**.
    - Retains **lexical or structural similarity** to the original sentence.

  Respond only in the following JSON format:
  {{
    "final_sentence": "final changed sentence",
    "reasoning": "reasoning" 
  }}
"""

