Feature: Cadastro e Inscrição de Estudante, Curso e Disciplina

  Scenario: Adicionar um estudante e verificar se o cadastro foi realizado
    Given que o usuário está na página principal
    When o usuário adiciona o estudante com o nome "douglas"
    Then a mensagem "INFO Added student id: 1, Name: douglas" deve ser exibida

  Scenario: Criar cursos e verificar se os cursos foram adicionados
    Given que o usuário está na página principal
    When o usuário cria o curso "mat"
    Then a mensagem "INFO Added student id: 1, Name: douglas" deve ser exibida para o curso "mat"
    
    When o usuário cria o curso "port"
    When o usuário cria o curso "geo"
    Then a mensagem "INFO Added student id: 1, Name: douglas" deve ser exibida para o curso "port" e "geo"

  Scenario: Inscrever estudante em cursos e disciplinas
    Given que o usuário está na página de inscrição de cursos
    When o usuário inscreve o estudante no curso "mat"
    Then a mensagem "INFO Added discipline id: 1, Name: mat, Course: 1" deve ser exibida para o curso "mat"
    
    When o usuário cria as disciplinas "mat2", "mat3" e "mat4"
    When o usuário tenta se inscrever em mais disciplinas do que o mínimo necessário
    Then a mensagem "WARN Aluno deve se inscrever em 3 materias no minimo" deve ser exibida

    When o usuário inscreve o estudante nas disciplinas "2", "3" e "4"
    Then a inscrição deve ser bem-sucedida
