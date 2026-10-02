# Projeto Flask

Aplicação introdutória em Flask com exemplos de rotas, respostas em texto/HTML e uma função auxiliar de saudação. Este README descreve o comportamento de `appFlask_v1.py`.

## Requisitos

- Python 3 instalado
- Flask

## Instalação

No terminal, na pasta do projeto, crie e ative um ambiente virtual e instale o Flask:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install Flask
```

No macOS ou Linux, ative o ambiente com:

```bash
source .venv/bin/activate
```

## Executar

```bash
python appFlask_v1.py
```

O servidor começa na porta `7000`. Acesse `http://127.0.0.1:7000/` no navegador.

## Rotas disponíveis

| Caminho | Resposta |
| --- | --- |
| `/` | Saudação para a turma |
| `/ola` | A mesma saudação da rota inicial |
| `/contato` | Endereço de e-mail definido no código |
| `/rota2` | Saudação em HTML indicando a rota 2 |

## Função auxiliar

A função `saudacaoes(nome)` retorna uma saudação personalizada. Ela não está associada a uma rota neste exemplo.

## Observação sobre a execução

O arquivo contém uma chamada a `app_cassia.run(port=7000)` dentro do bloco `if __name__ == '__main__'` e outra chamada a `app_cassia.run(port=6000)` fora dele. Executando o arquivo diretamente, a primeira chamada inicia o servidor na porta `7000`; a segunda só será alcançada quando a primeira terminar. Ao importar o módulo, a chamada fora do bloco também tenta iniciar um servidor. Para evitar esse comportamento e permitir importações sem iniciar o servidor, mantenha a inicialização em uma única chamada dentro do bloco principal.