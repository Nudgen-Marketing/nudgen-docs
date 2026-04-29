import os
import json

langs = ["ar", "id", "vi", "ur", "ko", "cn", "fr", "ru", "es", "jp", "tr", "de"]
source_dir = "en"

to_translate = {}

def is_untranslated(lang, rel_path):
    source_path = os.path.join(source_dir, rel_path)
    target_path = os.path.join(lang, rel_path)
    
    if not os.path.exists(target_path):
        return True
        
    with open(source_path, 'r', encoding='utf-8') as f:
        source_content = f.read()
    with open(target_path, 'r', encoding='utf-8') as f:
        target_content = f.read()
        
    # Split frontmatter and body
    def get_body(content):
        parts = content.split('---')
        if len(parts) >= 3:
            return '---'.join(parts[2:]).strip()
        return content.strip()
        
    source_body = get_body(source_content)
    target_body = get_body(target_content)
    
    # If body is identical, it's likely untranslated
    if source_body == target_body:
        return True
        
    # Heuristic for non-Latin languages: check for target script characters
    # (Simplified: if it's mostly Latin and should be something else)
    latin_only_langs = ["id", "vi", "fr", "es", "tr", "de"]
    if lang not in latin_only_langs:
        # Check if it has any non-ASCII characters that are not in source
        # This is a bit complex, let's stick to identity for now or a percentage match
        pass
        
    return False

for lang in langs:
    to_translate[lang] = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".mdx"):
                rel_path = os.path.relpath(os.path.join(root, file), source_dir)
                if is_untranslated(lang, rel_path):
                    to_translate[lang].append(rel_path)

print(json.dumps(to_translate, indent=2))
