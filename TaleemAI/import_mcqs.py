import json
import os
import django

# ------------- Setup Django -------------
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TaleemAI.settings")
django.setup()

from datamanager.models import MCQ

# ------------- Load JSON -------------
data = []
with open("./Maths_MCQ_Dataset/content/train.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:  # skip empty lines
            data.append(json.loads(line))

# ------------- Insert into DB -------------
for item in data:
    output = item["output"]

    # Split into parts
    parts = output.split("Options:")
    question = parts[0].replace("Question:", "").strip()
    options_part, correct_part = parts[1].split("Correct Answer:")

    # Build options JSON
    options = {}
    for line in options_part.strip().split("\n"):
        if line.strip():
            key, value = line.split(")", 1)
            options[key.strip()] = value.strip()

    correct_answer = correct_part.strip()

    # Derive topic from instruction (basic parse, you can refine)
    topic = item["instruction"].split("on")[-1].split("at")[0].strip()

    # Save into DB
    MCQ.objects.create(
        question=question,
        options_json=options,
        correct_answer=correct_answer,
        topic=topic
    )

print("✅ Import completed!")
