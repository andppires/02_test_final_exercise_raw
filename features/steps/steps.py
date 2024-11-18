from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup do Selenium
@given('que o usuário está na página principal')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://tdd-detroid.onrender.com/")
    context.driver.set_window_size(970, 555)
    aguarda_elemento(context)

@when('o usuário adiciona o estudante com o nome "{nome}"')
def step_impl(context, nome):
    adicionar_estudante(context, nome)

@then('a mensagem "{mensagem}" deve ser exibida')
def step_impl(context, mensagem):
    verificar_mensagem(context, mensagem)

@when('o usuário cria o curso "{nome_curso}"')
def step_impl(context, nome_curso):
    criar_curso(context, nome_curso)

@when('o usuário inscreve o estudante no curso "{curso}"')
def step_impl(context, curso):
    se_inscreve_curso(context, curso)

@when('o usuário cria as disciplinas "{disciplinas}"')
def step_impl(context, disciplinas):
    for disciplina in disciplinas.split(","):
        criar_disciplina(context, disciplina.strip())

@when('o usuário tenta se inscrever em mais disciplinas do que o mínimo necessário')
def step_impl(context):
    # Implementar lógica para tentar se inscrever em mais disciplinas do que o mínimo
    pass

@then('a mensagem "{mensagem}" deve ser exibida para o curso "{curso}"')
def step_impl(context, mensagem, curso):
    verificar_mensagem_para_curso(context, mensagem, curso)

@then('a inscrição deve ser bem-sucedida')
def step_impl(context):
    # Implementar verificação de sucesso na inscrição
    pass

# Fechar o navegador após os testes
@then('fechar o navegador')
def step_impl(context):
    context.driver.quit()


# Funções Auxiliares:

def aguarda_elemento(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".smooth"))
    )

def adicionar_estudante(context, nome):
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "student-nome"))
    )
    element.click()
    context.driver.find_element(By.ID, "student-nome").send_keys(nome)
    context.driver.find_element(By.ID, "student-btn").click()

def verificar_mensagem(context, mensagem):
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".py-p"))
    )
    assert element, "Elemento com a mensagem não encontrado."
    assert mensagem in element.text, f"Esperado: {mensagem}, mas obtido: {element.text}"

def criar_curso(context, nome_curso):
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "course-nome"))
    )
    element.click()
    context.driver.find_element(By.ID, "course-nome").send_keys(nome_curso)
    context.driver.find_element(By.ID, "course-btn").click()

def se_inscreve_curso(context, curso):
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "subscribe-discipline-id"))
    )
    element.click()
    context.driver.find_element(By.ID, "subscribe-discipline-id").send_keys(curso)
    context.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn").click()

def criar_disciplina(context, disciplina):
    element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "discipline-nome"))
    )
    element.click()
    actions = ActionChains(context.driver)
    actions.double_click(element).perform()
    context.driver.find_element(By.ID, "discipline-nome").send_keys(disciplina)
    context.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()

def verificar_mensagem_para_curso(context, mensagem, curso):
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".py-p"))
    )
    assert element, f"Mensagem não encontrada para o curso {curso}."
    assert mensagem in element.text, f"Esperado: {mensagem} para o curso {curso}, mas obtido: {element.text}"
