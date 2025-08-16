from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

categorias = [
    "Nome",
    "País",
    "Fruta",
    "Animal",
    "Cor",
    "Cidade",
    "Objeto",
    "Profissão",
    "Filme",
    "Marca",
    "Comida",
    "Time de futebol"
]

letra = ""
while not letra.isalpha() or len(letra) != 1:
    letra = input("Digite a letra para o jogo Stop: ").strip().upper()
    if not letra.isalpha() or len(letra) != 1:
        print("Por favor, digite apenas uma letra.")

prompt = (
    f"Aja como um especialista no jogo de palavras Stop (também conhecido como Adedanha) e gere respostas para a letra '{letra}'.\n"
    "Siga estas regras estritamente:\n"
    f"1. Todas as respostas devem, obrigatoriamente, começar com a letra '{letra}'.\n"
    "2. As respostas devem ser em português do Brasil.\n"
    "3. Forneça respostas que sejam válidas e conhecidas. Evite inventar palavras ou nomes.\n"
    "4. Se não encontrar uma resposta válida para alguma categoria, escreva 'Passo'.\n"
    "5. Mantenha o formato exato 'Categoria: Resposta' para cada item da lista, com um item por linha, sem marcadores ou números.\n\n"
    "Categorias para responder:\n" +
    "\n".join(categorias)
)

try:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("A chave OPENAI_API_KEY não foi encontrada no seu ambiente. Verifique seu arquivo .env")

    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        top_p=1,
        stream=False,
        stop=None
    )

    print("\n--- Respostas Sugeridas ---")
    print(completion.choices[0].message.content)
    print("--------------------------")

except Exception as e:
    print(f"\nOcorreu um erro: {e}")
