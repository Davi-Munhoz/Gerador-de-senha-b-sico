# Gerador de Senhas básico

Este projeto é um **Gerador de Senhas Aleatórias** em Python. Ele permite ao usuário criar senhas simples (somente números), medianas (números e letras) e complexas (números, letras e caracteres especiais), com a possibilidade de personalizar a quantidade de caracteres.

## Funcionalidades

- Geração de senhas simples, medianas ou complexas.
- Personalização da quantidade de caracteres.
- Geração de senhas únicas e aleatórias.

## Como Usar

### Requisitos

- Python 3.x
- Biblioteca **random** (inclusa por padrão no Python)

### Passos para Rodar o Projeto

1. Clone este repositório em sua máquina local:
   ```bash
   git clone https://github.com/seuusuario/gerador-de-senhas.git

2. Navegue até a pasta do projeto:
  
   cd gerador-de-senhas
   
3. Execute o Script em pyhton:

  python gerador_de_senhas.py

4. O sistema perguntará:
   - Qual tipo de senha você deseja 1. simples, 2. mediana, 3. complexa e 4 para sair do sistema
   - Quantos caracteres a senha deve ter
    
5. A senha sera gerada conforme as opções escolhidas.

## Exemplo de Execução

Quando você rodar o programa, ele pedirá para o usuário escolher o tipo de senha e a quantidade de caracteres. Aqui está um exemplo de interação:

Escolha uma opção:

1 - Senha Simples (Somente números)

2 - Senha Média (Números e letras)

3 - Senha Complexa (Números, letras e caracteres especiais)

4 - Sair

R: 1

Quantos digitos terá a senha: 8

Sua senha é: 48395721

Neste exemplo, a senha gerada é composta apenas por números (opção "Senha Simples") e tem 8 dígitos. O programa pode gerar senhas de diferentes tipos (simples, médias ou complexas) dependendo da escolha do usuário.

## Como funciona
- O projeto utiliza a biblioteca **random** para gerar números e caracteres aleatórios.
- O usuário escolhe o tipo de senha (simples, mediana ou complexa) e a quatidade de caracteres.
- As funções responsáveis por cada tipo de senha são chamadas com base na escolha do usuário.
- A senha gerada e mostrada na tela como resultado.

## Licença
Este projeto está licenciado sob a MIT License.
