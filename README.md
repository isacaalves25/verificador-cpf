# Validador de CPF em Python 🛡️

Este projeto é um script simples e funcional para validar números de CPF (Cadastro de Pessoa Física). O código remove caracteres especiais, calcula os dígitos verificadores com base nas regras da Receita Federal e verifica se o CPF informado é autêntico.

## ⚙️ Como o algoritmo funciona

O processo de validação segue a lógica dos pesos matemáticos:
1. **Limpeza:** Remove `.` e `-` da string original.
2. **Primeiro Dígito:** Multiplica-se os 9 primeiros dígitos por uma contagem regressiva de 10 a 2.
3. **Segundo Dígito:** Multiplica-se os 10 primeiros dígitos (incluindo o primeiro dígito calculado) por uma contagem regressiva de 11 a 2.
4. **Verificação:** Se o resto da divisão da soma por 11 resultar em um dígito diferente do informado, o CPF é considerado inválido.

## 🚀 Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Copie o código do validador para um arquivo chamado `validador_cpf.py`.
3. Abra o terminal ou prompt de comando na pasta do arquivo.
4. Execute o comando:
   ```bash
   python validador_cpf.py

## 📁 Estrutura do código
### A lógica está dividida em:
- primeiro_digito() = Calcula o peso de 10 a 2
- segundo_digito() = Calcula o peso de 11 a 2
- validar_cpf() = Gerencia inputs, limpa a string e exibe o resultado

## 🛠️ Tecnologias Utilizadas
- Python - Linguagem de programação.
- VS Code - Editor de código.

## 📝 Licença
Este projeto é para fins educacionais. Sinta-se à vontade para usar, modificar e compartilhar!
---
Desenvolvido por isacalves25