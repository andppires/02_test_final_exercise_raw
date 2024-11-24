# Projeto: Test Final Exercise
Este repositório contém o código para o exercício final de testes automatizados, utilizando pytest e Behave. O projeto foi estruturado para demonstrar testes unitários e comportamentais em Python.

# Pré-requisitos
Certifique-se de que o ambiente possui os seguintes itens instalados:

Python (versão 3.8 ou superior)
pip (gerenciador de pacotes do Python)
Para verificar se estão instalados, execute no terminal:

bash
python --version
pip --version

Além disso, instale as dependências necessárias do projeto.

# Instalação das Dependências

# Clone o repositório:

*git clone https://github.com/andppires/02_test_final_exercise_raw.git*

# Acesse o diretório do projeto:
cd 02_test_final_exercise_raw

# Criação e ativação do ambiente virtual (opcional, mas recomendado):
É recomendado usar um ambiente virtual para isolar as dependências do projeto. Para criar e ativar o ambiente virtual, execute:

No Windows:

python -m venv venv
.\venv\Scripts\activate

No macOS/Linux:

python -m venv venv
source venv/bin/activate

# Instale as dependências do projeto:
Utilize o comando abaixo para instalar as bibliotecas listadas no requirements.txt:
*pip install -r requirements.txt*

# Executando os Testes
Após configurar o ambiente, utilize os comandos abaixo para rodar os testes:

# Testes com pytest:

Execute o comando para rodar os testes unitários:
*python -m pytest test_final_exercise_raw.py*

Este comando executará os testes presentes no arquivo test_final_exercise_raw.py e exibirá os resultados no terminal.

# Testes com Behave:

Execute o comando abaixo para rodar os testes comportamentais:
*behave*

Este comando executará os testes comportamentais definidos no diretório features/ (arquivo .feature).

# Estrutura do Projeto
# test_final_exercise_raw.py: 
Arquivo contendo os testes unitários escritos com pytest.
# features/: 
Contém arquivos .feature e a implementação dos passos para testes comportamentais.
# requirements.txt: 
Lista as dependências necessárias para rodar o projeto.

# Possíveis Problemas e Soluções

# Erro: ModuleNotFoundError ao rodar os testes:
Certifique-se de que instalou todas as dependências com o comando pip install -r requirements.txt.

# Comando pytest ou behave não encontrado:
Verifique se os pacotes estão instalados corretamente no ambiente. Reinstale com pip install pytest behave.

# Testes falhando inesperadamente:
Revise os cenários e as configurações iniciais no código para garantir que os testes estejam sendo executados no ambiente esperado.
