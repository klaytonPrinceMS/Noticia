import unittest

import httpx

import classesKBP
site = classesKBP.Sites()
print(site.gn_internacional)

class Testes:
    def test_construtor_site(self):
        siteTeste = classesKBP.Sites()
        assert siteTeste.gn_brasil == f'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNREUxWm5JU0JYQjBMVUpTS0FBUAE?hl=pt-BR&gl=BR&ceid=BR%3Apt-419'

    def test_construtor_noticias(self):
        noticia = classesKBP.Noticias()
        assert noticia.retorna == []

    def test_noticia_versaoClasse(self):
        noticia = classesKBP.Noticias()
        assert noticia.versao != ''

    def test_noticia_get_html_text_retornaTexto(self):
        noticia = classesKBP.Noticias()
        verifica = noticia.get_html_text(urlSite=site.gn_entretenimento)
        assert verifica != ''

    def test_noticia_get_selectores_html_retornaSeletores(self):
        noticia = classesKBP.Noticias()
        verifica = noticia.get_selectores_html(urlSite=site.gn_brasil)
        assert verifica != ''

    def test_get_html_text_valid_url(self):
        """Testa se a função retorna o texto HTML corretamente para uma URL válida."""
        noticia = classesKBP.Noticias()
        html_text = noticia.get_html_text(urlSite=site.gn_brasil)
        html_text.


teste = Testes()
