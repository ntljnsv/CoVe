BASELINE_PROMPT = """
  You are tasked with adjusting the tone of the following sentence to make it **a bit more polished and grammatically correct**, while keeping the **original tone and intent intact**.

  - Do not make the sentence academic or overly formal.
  - Avoid using complex or uncommon words in place of simple ones.
  - Maintain the sentence’s original structure, emotional intensity, and colloquial style unless minimal changes are needed for clarity or correctness.
  - Your goal is to make it feel like a **cleaner, slightly more professional version of how someone might naturally speak**.

  Now adjust the tone of the sentence below. Return only the changed sentence.

  Sentence for changing: **"{input}"**

  Respond only in the following JSON format:
  {{
    "original_sentence": "{input}",
    "changed_sentence": "changed sentence"
  }}
"""




VERIFICATION_QUESTIONS_PROMPT = """
  Based on the original sentence and its revised version, create questions that assess whether the revised sentence meets the following criteria:

  1. **Intent and Meaning**: Does the new sentence keep the same meaning and emotional intent?
  2. **Grammaticality and Polishing**: Has the grammar and fluency improved in a way that's natural and appropriate for everyday or professional conversation?
  3. **Lexical & Structural Similarity**: Has the sentence kept most of the original wording or sentence structure, only changing what was necessary?

  Original Sentence: "{original_sentence}"
  Baseline Changed Sentence: "{baseline_response}"

  Respond only in the following JSON format:
  {{
    "questions": [
      "Question 1",
      "Question 2",
      "Question 3"
    ]
  }}
"""


VERIFICATION_ANSWER_PROMPT = """
  Answer the following verification questions based on the context. Your goal is to assess the **quality and correctness** of the revised sentence.

  Please consider:
  - Whether the meaning and tone are preserved
  - Whether grammar and fluency improved
  - Whether the changes stayed close to the original

  If anything is off, briefly explain what could be improved.

  Original Sentence: {original_sentence}
  Baseline Changed Sentence: {baseline_response}
  Verification Questions: {questions}

  Respond only in the following JSON format:
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
  Use the following information to improve the original sentence, using the answers to verification questions as guidance.

  Your goal is to produce a final version that:
  - Preserves the **original meaning and emotional tone**
  - Improves **grammatical correctness** and fluency
  - Is slightly more formal and polished, without sounding academic or stiff
  - Keeps the **sentence close to its original structure and vocabulary** unless a change is clearly needed

  Original Sentence: {original_sentence}
  Baseline Changed Sentence: {baseline_response}
  Verification Answers:
  {verification_answers}

  Respond only in the following JSON format:
  {{
    "final_sentence": "final changed sentence",
    "reasoning": "reasoning" 
  }}
"""


