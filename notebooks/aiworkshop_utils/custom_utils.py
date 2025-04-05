import base64
import json
from IPython.display import Markdown, display
import os
from glob import glob
import numpy as np

def truncate_lists(obj, max_items=10):
    """
    Rekursive Funktion, die in allen Listen (auch in verschachtelten Strukturen)
    alle Listen auf max_items Einträge beschränkt.
    Unterstützt auch Objekte mit einer .tolist()-Methode (z. B. NumPy-Arrays oder Torch-Tensoren).
    """
    # Falls das Objekt eine .tolist()-Methode hat, in Liste umwandeln
    if hasattr(obj, "tolist"):
        obj = obj.tolist()
    
    if isinstance(obj, (list, tuple)):
        if len(obj) > max_items:
            # Bei langen Listen: Trunkiere und hänge einen Hinweis an
            return list(obj[:max_items]) + [f"... ({len(obj) - max_items} more elements)"]
        else:
            # Für kürzere Listen: rekursiv verarbeiten
            return [truncate_lists(item, max_items) for item in obj]
    elif isinstance(obj, dict):
        return {k: truncate_lists(v, max_items) for k, v in obj.items()}
    else:
        return obj

def show_pretty_json(obj, indent=2, max_list_items=10):
    """
    Schöne Ausgabe eines dict-ähnlichen Objekts als JSON in einem Markdown-Codeblock.
    Längere Listen werden auf max_list_items Einträge gekürzt.
    """
    if hasattr(obj, "model_dump"):
        obj = obj.model_dump()
    
    truncated = truncate_lists(obj, max_list_items)
    formatted = json.dumps(truncated, indent=indent)
    display(Markdown(f"```json\n{formatted}\n```"))

def encode_image(image_path):
    """
    Encodes an image file to a Base64 string.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Text-Lines-Liste erstellen
def load_md_sections_from_path(path_pattern: str) -> list[str]:
    """
    Lädt alle Markdown-Dateien, die dem Pfadmuster entsprechen, und
    splittet deren Inhalt anhand der Markdown-Überschriftsebene "# ".

    Args:
        path_pattern (str): Glob-Pfadmuster zu den Markdown-Dateien (z. B. 'docs/**/*.md').

    Returns:
        list[str]: Liste der Abschnittstexte, jeweils getrennt an "# ".
    """
    text_lines = []

    for file_path in glob(path_pattern, recursive=True):
        if not os.path.isfile(file_path):
            continue
        with open(file_path, "r", encoding="utf-8") as file:
            file_text = file.read()

        text_lines += file_text.split("# ")

    return text_lines