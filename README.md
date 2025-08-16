# bot-stop

Um bot que gera automaticamente respostas para o jogo Stop (Adedanha) usando inteligência artificial.

## Como funciona

O usuário informa uma letra. O bot utiliza a API da OpenAI para gerar respostas válidas para 12 categorias do jogo, todas começando com a letra escolhida.

## Categorias

- Nome
- País
- Fruta
- Animal
- Cor
- Cidade
- Objeto
- Profissão
- Filme
- Marca
- Comida
- Time de futebol

## Requisitos

- Python 3.10+
- Conta e chave de API da OpenAI
- Pacotes: `openai`, `python-dotenv`

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/bot-stop.git
   cd bot-stop
   ```

2. Instale as dependências:
   ```sh
   pip install openai python-dotenv
   ```

3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da OpenAI:
   ```
   OPENAI_API_KEY="sua-chave-aqui"
   ```

## Uso

Execute o script:

```sh
python bot.py
```

Digite uma letra quando solicitado. O bot irá gerar e exibir as respostas para cada categoria.

## Exemplo

```
Digite uma letra: A
```

Respostas geradas:

- Nome: Ana
- País: Argentina
- Fruta: Abacaxi
- Animal: Anta
- Cor: Azul
- Cidade: Amsterdam
- Objeto: Abajur
- Profissão: Arquiteto
- Filme: A Origem
- Marca: Adidas
- Comida: Arroz
- Time de futebol: Atlético

Divirta-se jogando Stop com a ajuda do bot!

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.