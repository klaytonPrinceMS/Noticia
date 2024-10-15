from classesKBP import Sites, Noticias
from urllib.parse import quote as converterUrl
import os
def menu():
    '''
    Função cria o menu que será exibido no terminal para o usuário
    EXECUÇÂO:
    Limpa tela
    cria uma instância da classe Sites() com os links dos sites para ser usado no programa
    cria uma instÂncia da classe Noticias()
    Gera o menu e apos escolha faz a leitura das noticias solicitadas e gera um arquivo index.html e abre o arquivo no navegador padrão
    :return: Sem retorno
    '''
    os.system('cls')
    site = Sites()
    noticias = Noticias()
    print('''
    ====================================================
    ===          Agregador DTI - Noticias            ===
    ====================================================
    0  - Pesquisar
    1  - Brasil
    2  - Internacional
    3  - Economia
    4  - Saúde
    5  - Ciências e Tecnologia
    6  - Entretenimento
    7  - Esporte
    10 - Monte Santo de Minas
    ''')
    opcao = str(input('Qual opção de noticias:'))

    match opcao:
        case '0':
            pesquisar = str(input("Qual tema vamos buscar: "))
            print('''\n1 - Fonte Google News\n2 - Fonte JFP Noticias''')
            opcao1 = str(input("Qual base de dados usar: "))
            match opcao1:
                case '1':
                    os.system('cls')
                    noticias.get_noticiasGN(urlSite=fr'https://news.google.com/search?q={converterUrl(string=pesquisar)}&hl=pt-BR&gl=BR&ceid=BR%3Apt-419', tagPrincipal='.JtKRv')
                    noticias.gerarSite(titulo=pesquisar)
                    menu()
                case '2':
                    os.system('cls')
                    noticias.get_noticiasJFP(urlSite=f'https://jfpnoticias.com.br/?s={converterUrl(string=pesquisar)}')
                    noticias.gerarSite(titulo=pesquisar)
                    menu()
        case '1': # Brasil
            noticias.get_noticiasGN(urlSite=site.gn_brasil)
            noticias.get_noticiasBBC(urlSite=site.bbc_brasil)
            noticias.gerarSite(titulo='Brasil')
            menu()
        case '2': # Internacional
            noticias.get_noticiasGN(urlSite=site.gn_internacional)
            noticias.get_noticiasBBC(urlSite=site.bbc_internacional)
            noticias.gerarSite(titulo='Internacional')
            menu()
        case '3': # economia
            noticias.get_noticiasGN(urlSite=site.gn_economia)
            noticias.get_noticiasBBC(urlSite=site.bbc_economia)
            noticias.gerarSite(titulo='Economia')
            menu()
        case '4': # Saúde
            noticias.get_noticiasGN(urlSite=site.gn_saude)
            noticias.get_noticiasBBC(urlSite=site.bbc_saude)
            noticias.gerarSite(titulo='Saúde')
            menu()
        case '5': # Ciencia e Tecnologia
            noticias.get_noticiasGN(urlSite=site.gn_ciencia_tecnologia)
            noticias.get_noticiasBBC(urlSite=site.bbc_ciencia)
            noticias.gerarSite(titulo="Ciências e tecnologia")
            menu()
        case '6': # entretenimento
            noticias.get_noticiasGN(urlSite=site.gn_entretenimento)
            noticias.gerarSite(titulo='Entretenimento')
            menu()
        case '7': # esporte
            noticias.get_noticiasGN(urlSite=site.gn_esporte)
            noticias.gerarSite(titulo='Esporte')
            menu()
        case '10': # Monte Santo de Minas
            noticias.get_noticiasJFP(urlSite=site.msm_jfp)
            noticias.gerarSite(titulo='Monte Santo de Minas')
            menu()
        case _:
            print('Opção valida')
            menu()
menu()
