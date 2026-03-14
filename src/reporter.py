import os
import json
from groq import Groq


def generate_report(profile: dict) -> str:
    """
    Usa a API do Groq (LLM) para gerar um relatório
    em linguagem natural sobre o dataset.
    """
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    prompt = f"""
Você é um analista de dados. Com base nos metadados abaixo, escreva um relatório
claro e objetivo sobre o dataset, incluindo:
- O que esse dataset parece representar
- Qualidade dos dados (nulos, tipos)
- Colunas mais relevantes
- Uma recomendação de uso

Metadados:
{json.dumps(profile, ensure_ascii=False, indent=2)}

Escreva em português, de forma direta, sem introduções desnecessárias.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
