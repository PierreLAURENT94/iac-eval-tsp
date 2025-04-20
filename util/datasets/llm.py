import requests

def to_french(prompt):
    system_message = (
        "Your ONLY task is to translate the given text from English to French."
        "You MUST NOT solve, explain, extend, complete, or interpret the text."
        "You MUST NOT invent any additional information."
        "STRICT RULE: If any part of the text is inside quotation marks, you MUST NOT translate, modify, or touch it in any way."
        "Variables, code names, technical terms, and text patterns like 'reverse_zone', 'host.example53.com', or 'passwordpassword' MUST NEVER be translated or modified."
        "Quotation marks protect their content — the text inside MUST stay exactly as it is."
        "You MUST NOT translate technical terms related to Terraform, AWS, or any cloud computing concepts."
        "You MUST strictly preserve variable names, resource names, object keys, bucket names, domain names, zone names, or any values inside code-like structures."
        "You MUST provide only the pure, raw translation without any introduction, explanation, or formatting."
        "If unsure, translate literally without adding or removing anything."
        "Strictly preserve the original structure, formatting, and length."
        "EXAMPLES:"
        "Input: 'Set up a record that maps a domain name to an IPv4 address using Route 53 resources.'"
        "Output: 'Configurer un enregistrement qui associe un nom de domaine à une adresse IPv4 en utilisant des ressources Route 53.'"
        "Input: 'Set up a Pointer record for reverse DNS using Route 53 resources. The domain name should be \"host.example53.com\" and name the zone \"reverse_zone\".'"
        "Output: 'Configurer un enregistrement de type Pointeur pour le DNS inverse en utilisant des ressources Route 53. Le nom de domaine doit être \"host.example53.com\" et nommer la zone \"reverse_zone\".'"
    )

    payload = {
        "model": "gemma3:12b",
        "prompt": prompt,
        "system": system_message,
        "stream": False
    }

    try:
        response = requests.post("http://172.26.32.1:11434/api/generate" , json=payload)
        if response.status_code == 200:
            return response.json().get("response")
    except requests.exceptions.ConnectionError:
        print("Impossible de se connecter à Ollama.")
        return None

def to_short(prompt):
    system_message = (
        "Shorten EACH given text in English."
        "You MUST NOT mix instructions from different sources."
        "You MUST NOT add new information."
        "You MUST NOT translate."
        "You MUST ONLY summarize the current text by making it more concise."
        "Keep all technical terms exactly as they are (e.g., AWS, Terraform, S3, Route 53)."
        "If the text includes specific strings (like domain names, bucket names), KEEP them as-is."
        "Examples:"
        "Input: 'Set up a TXT record for domain ownership verification purposes using Route 53 resources. The verification string should be \"passwordpassword\" and the name of the zone should be \"example\".'"
        "Output: 'Create a TXT record for domain ownership verification with Route 53. String: \"passwordpassword\", Zone: \"example\".'"
        "Input: 'Create a template of an elastic beanstalk application that is running a version of Go.'"
        "Output: 'Create an Elastic Beanstalk app template running Go.'"
    )

    payload = {
        "model": "gemma3:12b",
        "prompt": system_message + prompt,
        "system": "",
        "stream": False
    }

    try:
        response = requests.post("http://172.26.32.1:11434/api/generate" , json=payload)
        if response.status_code == 200:
            return response.json().get("response")
    except requests.exceptions.ConnectionError:
        print("Impossible de se connecter à Ollama.")
        return None
