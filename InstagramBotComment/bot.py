from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):

        # ------------------------
        # Inicialização do firefox
        # ------------------------

        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"geckodriver"
        )

    def login(self):

        # ------------------------
        # Realiza o login no Instagram
        # ------------------------

        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        '''
        login_button = driver.find_element_by_xpath(
            "//a[@href='/accounts/login/?source=auth_switcher']"
        )
        login_button.click()
        '''
        time.sleep(3)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        agora_nao = driver.find_element_by_class_name("cmbtv")
        agora_nao.click()

        self.comenta_fotos()

    @staticmethod
    def type_like_a_person(sentence, single_input_field):

        # ---------------------------------------------------------------
        """ Código responsável por simular a digitação de uma pessoa """
        # ---------------------------------------------------------------

        print("Digitando comentário...")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1,3))

    def comenta_fotos(self):

        vezes_comentadas = 0

        # ---------------------------------------------------
        #Inserir manualmente uma Lista de comentários de todos os sorteios
        # ---------------------------------------------------

        comments = [
                '',
            ]

        # ---------------------------------------------
        # Criar comentários aleatórios para os sorteios
        # ---------------------------------------------

        '''listLetras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      '1','2','3','4','5','6','7','8','9']

        from random import randint

        listPalavras = []

        #Mínimo de caracteres do comentário
        minCaracteres = 3

        #Máximo de caracteres do comentário
        maxCaracteres = 10

        #Quantidade de comentários
        qntComentarios = 100

        for i in range(qntComentarios):
            palavra = []
            for i in range(randint(minCaracteres,maxCaracteres)):
                palavra.append(listLetras[randint(0, 34)])

            palavraString = ''.join(palavra)
            listPalavras.append(palavraString)

        comments = listPalavras'''

        # ---------------------------------------------------
        #Para pegar de um documento de texto
        # ---------------------------------------------------

        '''lista = open('referenciaTxt','r')
        for i in lista:
            comments.append(i)'''



        #Lista de comentário de cada um dos 5 sorteios
        comments01 = []
        comments02 = []
        comments03 = []
        comments04 = []
        comments05 = []

        #Adiciona todas as palavras do comments a cada lista
        for i in comments:
            comments01.append(i)
            comments02.append(i)
            comments03.append(i)
            comments04.append(i)
            comments05.append(i)

        # Insere o link dos sorteios que quer comentar nas variáveis
        sorteio01 = ''
        sorteio02 = ''
        sorteio03 = ''
        sorteio04 = ''
        sorteio05 = ''

        sorteios = []

        # somente adicionará na lista /sorteios/ as variaveis que foram atribuídas a uma link
        if sorteio01 != '' and len(comments01) != 0:
            sorteios.append(sorteio01)
        if sorteio02 != '' and len(comments02) != 0:
            sorteios.append(sorteio02)
        if sorteio03 != '' and len(comments03) != 0:
            sorteios.append(sorteio03)
        if sorteio04 != '' and len(comments04) != 0:
            sorteios.append(sorteio04)
        if sorteio05 != '' and len(comments05) != 0:
            sorteios.append(sorteio05)

        while (1):
            try:
                #Escolhe um sorteio da lista
                sorteio_da_vez = random.choice(sorteios)
                driver = self.driver
                time.sleep(5)
                driver.get(sorteio_da_vez)
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")

                # Codigo pra pegar o input que escreve o comentário
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(1, 20))

                # Insira aqui a quantidade de comentarios que devem ser feitos em cada sorteio
                quantidadeSorteio01 = 0
                quantidadeSorteio02 = 0
                quantidadeSorteio03 = 0
                quantidadeSorteio04 = 0
                quantidadeSorteio05 = 0

                # Encerra o programa quando se esgota as opções de comentários de todos os sorteios
                if len(comments01) < quantidadeSorteio01 & len(comments02) < quantidadeSorteio02 & len(comments03) < quantidadeSorteio03 & len(comments04) < quantidadeSorteio04 & len(comments05) < quantidadeSorteio05:
                    break

                # Verifica qual sorteio o programa escolheu para comentar
                if sorteio_da_vez == sorteio01:

                    '''Verifica se os comentários da lista do sorteio01 são maiores ou igual
                    a quantidade que deve ser comentada por vez no sorteio01'''

                    if len(comments01) >= quantidadeSorteio01:

                        marcados = ''

                        # Comentários escolhidos da lista do sorteio01
                        pessoa_1 = random.choice(comments01)
                        pessoa_2 = random.choice(comments01)
                        pessoa_3 = random.choice(comments01)

                        # Verifica se os comentários são iguais para tornarem diferentes
                        if quantidadeSorteio01 == 2:
                            while pessoa_1 == pessoa_2:
                                pessoa_1 = random.choice(comments01)
                                pessoa_2 = random.choice(comments01)
                        elif quantidadeSorteio01 == 3:
                            while pessoa_3 == pessoa_2 or pessoa_3 == pessoa_1 or pessoa_1 == pessoa_2:
                                pessoa_1 = random.choice(comments01)
                                pessoa_2 = random.choice(comments01)
                                pessoa_3 = random.choice(comments01)

                        # verificando quantas pessoas é para marcar no sorteio

                        ''' obs: se nao quiser remover o comentário da lista dos comentários do sorteio01,
                        comente as linhas "comments01.remove(pessoa_)" '''

                        if quantidadeSorteio01 == 1:
                                marcados = pessoa_1
                                comments01.remove(pessoa_1)
                        elif quantidadeSorteio01 == 2:
                                marcados = f'{pessoa_2} {pessoa_1}'
                                comments01.remove(pessoa_1)
                                comments01.remove(pessoa_2)
                        elif quantidadeSorteio01 == 3:
                                marcados = f'{pessoa_2} {pessoa_1} {pessoa_3}'
                                comments01.remove(pessoa_1)
                                comments01.remove(pessoa_2)
                                comments01.remove(pessoa_3)

                        # Digita o comentário
                        self.type_like_a_person(marcados, comment_input_box)
                        print("Comentei: ", marcados, " no post: ", sorteio_da_vez, "")

                    else:
                        sorteios.remove(sorteio01)

                elif sorteio_da_vez == sorteio02:

                    if len(comments02) >= quantidadeSorteio02:
                        marcados = ''
                        # Pessoas que poderão ser marcadas
                        pessoa2_1 = random.choice(comments02)
                        pessoa2_2 = random.choice(comments02)
                        pessoa2_3 = random.choice(comments02)

                        if quantidadeSorteio02 == 2:
                            while pessoa2_1 == pessoa2_2:
                                pessoa2_1 = random.choice(comments02)
                                pessoa2_2 = random.choice(comments02)
                        elif quantidadeSorteio02 == 3:
                            while pessoa2_3 == pessoa2_2 or pessoa2_3 == pessoa2_1 or pessoa2_1 == pessoa2_2:
                                pessoa2_1 = random.choice(comments02)
                                pessoa2_2 = random.choice(comments02)
                                pessoa2_3 = random.choice(comments02)

                        # verificando quantas pessoas é para marcar no sorteio
                        if quantidadeSorteio02 == 1:
                                marcados = pessoa2_1
                                comments02.remove(pessoa2_1)
                        elif quantidadeSorteio02 == 2:
                                marcados = f'{pessoa2_2} {pessoa2_1}'
                                comments02.remove(pessoa2_1)
                                comments02.remove(pessoa2_2)

                        elif quantidadeSorteio02 == 3:
                                marcados = f'{pessoa2_2} {pessoa2_1} {pessoa2_3}'
                                comments02.remove(pessoa2_1)
                                comments02.remove(pessoa2_2)
                                comments02.remove(pessoa2_3)

                        # Digita o comentário
                        self.type_like_a_person(marcados, comment_input_box)
                        print("Comentei: ", marcados, " no post: ", sorteio_da_vez, "")

                    else:
                        sorteios.remove(sorteio02)

                elif sorteio_da_vez == sorteio03:

                    if len(comments03) >= quantidadeSorteio03:
                        marcados = ''
                        # Pessoas que poderão ser marcadas
                        pessoa3_1 = random.choice(comments03)
                        pessoa3_2 = random.choice(comments03)
                        pessoa3_3 = random.choice(comments03)

                        if quantidadeSorteio03 == 2:
                            while pessoa3_1 == pessoa3_2:
                                pessoa3_1 = random.choice(comments03)
                                pessoa3_2 = random.choice(comments03)
                        elif quantidadeSorteio03 == 3:
                            while pessoa3_3 == pessoa3_2 or pessoa3_3 == pessoa3_1 or pessoa3_1 == pessoa3_2:
                                pessoa3_1 = random.choice(comments03)
                                pessoa3_2 = random.choice(comments03)
                                pessoa3_3 = random.choice(comments03)

                        # verificando quantas pessoas é para marcar no sorteio
                        if quantidadeSorteio03 == 1:
                                marcados = pessoa3_1
                                comments03.remove(pessoa3_1)
                        elif quantidadeSorteio03 == 2:
                                marcados = f'{pessoa3_2} {pessoa3_1}'
                                comments03.remove(pessoa3_1)
                                comments03.remove(pessoa3_2)
                        elif quantidadeSorteio03 == 3:
                                marcados = f'{pessoa3_2} {pessoa3_1} {pessoa3_3}'
                                comments03.remove(pessoa3_1)
                                comments03.remove(pessoa3_2)
                                comments03.remove(pessoa3_3)

                        # Digita o comentário
                        self.type_like_a_person(marcados, comment_input_box)
                        print("Comentei: ", marcados, " no post: ", sorteio_da_vez, "")

                    else:
                        sorteios.remove(sorteio03)

                elif sorteio_da_vez == sorteio04:

                    if len(comments04) >= quantidadeSorteio04:
                        marcados = ''
                        # Pessoas que poderão ser marcadas
                        pessoa4_1 = random.choice(comments04)
                        pessoa4_2 = random.choice(comments04)
                        pessoa4_3 = random.choice(comments04)

                        if quantidadeSorteio04 == 2:
                            while pessoa4_1 == pessoa4_2:
                                pessoa4_1 = random.choice(comments04)
                                pessoa4_2 = random.choice(comments04)
                        elif quantidadeSorteio04 == 3:
                            while pessoa4_3 == pessoa4_2 or pessoa4_3 == pessoa4_1 or pessoa4_1 == pessoa4_2:
                                pessoa4_1 = random.choice(comments04)
                                pessoa4_2 = random.choice(comments04)
                                pessoa4_3 = random.choice(comments04)

                        # verificando quantas pessoas é para marcar no sorteio
                        if quantidadeSorteio04 == 1:
                                marcados = pessoa4_1
                                comments04.remove(pessoa4_1)
                        elif quantidadeSorteio04 == 2:
                                marcados = f'{pessoa4_2} {pessoa4_1}'
                                comments04.remove(pessoa4_1)
                                comments04.remove(pessoa4_2)
                        elif quantidadeSorteio04 == 3:
                                marcados = f'{pessoa4_2} {pessoa4_1} {pessoa4_3}'
                                comments04.remove(pessoa4_1)
                                comments04.remove(pessoa4_2)
                                comments04.remove(pessoa4_3)

                        # Digita o comentário
                        self.type_like_a_person(marcados, comment_input_box)
                        print("Comentei: ", marcados, " no post: ", sorteio_da_vez, "")

                    else:
                        sorteios.remove(sorteio04)

                elif sorteio_da_vez == sorteio05:

                    if len(comments05) >= quantidadeSorteio05:
                        marcados = ''
                        # Pessoas que poderão ser marcadas
                        pessoa5_1 = random.choice(comments05)
                        pessoa5_2 = random.choice(comments05)
                        pessoa5_3 = random.choice(comments05)

                        if quantidadeSorteio05 == 2:
                            while pessoa5_1 == pessoa5_2:
                                pessoa5_1 = random.choice(comments05)
                                pessoa5_2 = random.choice(comments05)
                        elif quantidadeSorteio05 == 3:
                            while pessoa5_3 == pessoa5_2 or pessoa5_3 == pessoa5_1 or pessoa5_1 == pessoa5_2:
                                pessoa5_1 = random.choice(comments05)
                                pessoa5_2 = random.choice(comments05)
                                pessoa5_3 = random.choice(comments05)

                        # verificando quantas pessoas é para marcar no sorteio
                        if quantidadeSorteio05 == 1:
                                marcados = pessoa5_1
                                comments05.remove(pessoa5_1)
                        elif quantidadeSorteio05 == 2:
                                marcados = f'{pessoa5_2} {pessoa5_1}'
                                comments05.remove(pessoa5_1)
                                comments05.remove(pessoa5_2)
                        elif quantidadeSorteio05 == 3:
                                marcados = f'{pessoa5_2} {pessoa5_1} {pessoa5_3}'
                                comments05.remove(pessoa5_1)
                                comments05.remove(pessoa5_2)
                                comments05.remove(pessoa5_3)

                        # Digita o comentário
                        self.type_like_a_person(marcados, comment_input_box)
                        print("Comentei: ", marcados, " no post: ", sorteio_da_vez, "")
                    else:
                        sorteios.remove(sorteio05)

                # Encerra o programa quando se esgota as opções de comentários de todos os sorteios
                if len(sorteios) == 0:
                    break

                # Publica o comentário
                time.sleep(random.randint(1, 15))
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()

                vezes_comentadas += 1

                '''Aqui ele te informará quantas vezes já comentou o todo, desde o momento do start do script'''
                print('Vezes comentadas:')
                print(vezes_comentadas)

                time.sleep(random.randint(40,55))
                # Tempo do intervalo em que ocorrerá um comentário e outro.
                # Não é aconselhável reduzir este tempo, corre o risco de ser bloqueado pelo Instagram

            except:
                print('Um erro ocorreu, mas sem problemas vamos continuar')

print('Script Iniciado')
print('-'*20)

# Entre com o usuário e senha aqui
Bot = InstagramBot("user", "password")
Bot.login()

print('-'*20)
print('Script Finalizado')
