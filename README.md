Instalação e execução do exemplo
Este projeto demonstra um conjunto de testes automáticos utilizando Selenium WebDriver e pytest para testar funcionalidades de gestão de estudantes, cursos e disciplinas em um sistema web.

Requisitos
Python 3
Google Chrome (ou outro navegador compatível com o Selenium)
Passos para execução
1. Criação de um Ambiente Virtual
Crie um ambiente virtual (virtual environment) utilizando a sua versão padrão do Python:

bash
Copiar código
python3 -m venv venv
2. Ativação do Ambiente Virtual
Ative o ambiente virtual:

No macOS/Linux:
bash
Copiar código
source venv/bin/activate
No Windows:
bash
Copiar código
venv\Scripts\activate
3. Instalação dos Requisitos
Instale as dependências do projeto listadas no arquivo requirements.txt:

bash
Copiar código
pip install -r requirements.txt
4. Execução do Teste
Garanta que o Google Chrome esteja instalado na sua máquina, pois o Selenium precisará dele para executar os testes.

Em seguida, execute o teste de exemplo:

bash
Copiar código
python -m pytest -k test_demo
Os testes serão executados e a página será exibida no browser conforme os comandos do script.

5. Resultado dos Testes
O teste simula interações como adicionar estudantes, cursos e disciplinas, além de inscrever estudantes nas disciplinas. O sistema será manipulado diretamente no navegador (Chrome) e as interações serão verificadas conforme os assertivos presentes no código.

Estrutura do Código
O código utiliza a biblioteca Selenium WebDriver para controlar o navegador e interagir com a interface do sistema, e pytest para gerenciar e executar os testes. O comportamento esperado para cada ação (adicionar estudante, adicionar curso, etc.) é verificado por meio de asserções.

Funções principais:
Adição de Estudante: Cria um novo estudante no sistema.
Adição de Curso: Cria um novo curso no sistema.
Inscrição em Curso: Inscreve um estudante em um curso.
Adição de Disciplina: Cria uma nova disciplina e associa-a a um curso.
Inscrição em Disciplina: Inscreve um estudante em uma disciplina.
Cada uma dessas funções é invocada em sequência durante a execução do teste.

6. Exemplo de Teste
O código executa um fluxo de testes onde são adicionados estudantes, cursos e disciplinas, e as inscrições são feitas da seguinte forma:

Adicionar Estudante: O script adiciona um estudante chamado "douglas".
Adicionar Curso: Um curso chamado "mat" é adicionado.
Inscrição em Curso: O estudante "douglas" é inscrito no curso "mat".
Adicionar Disciplina: A disciplina "mat" é criada para o curso "mat".
Inscrição em Disciplina: O estudante "douglas" é inscrito nas disciplinas "mat", "port" e "geo".
Verificações: A cada etapa, o script verifica se os elementos foram corretamente inseridos e exibidos na interface.
7. Captura de Tela
Durante a execução do teste, a página será manipulada conforme os comandos definidos no código, e você verá a interface sendo alterada.