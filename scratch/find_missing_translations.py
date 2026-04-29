import os
import json

langs = ["ar", "id", "vi", "ur", "ko", "cn", "fr", "ru", "es", "jp", "tr", "de"]
source_dir = "en"

missing_files = {}

for lang in langs:
    missing_files[lang] = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".mdx"):
                rel_path = os.path.relpath(os.path.join(root, file), source_dir)
                target_path = os.path.join(lang, rel_path)
                if not os.path.exists(target_path):
                    missing_files[lang].append(rel_path)

print(json.dumps(missing_files, indent=2))
