import unittest
from pickletools import pydict

import pytest
from pytest import mark

import httpx

import classesKBP
site = classesKBP.Sites()
print(site.gn_internacional)

class Testes:
    @mark.construtor_site
    def test_construtor_site(self):
        siteTeste = classesKBP.Sites()
        assert siteTeste.gn_brasil == f'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNREUxWm5JU0JYQjBMVUpTS0FBUAE?hl=pt-BR&gl=BR&ceid=BR%3Apt-419'

    @mark.construtor_noticias
    def test_construtor_noticias(self):
        noticia = classesKBP.Noticias()
        assert noticia.retorna == []

    @mark.noticia_versao
    def test_noticia_versaoClasse(self):
        noticia = classesKBP.Noticias()
        assert noticia.versao != ''


    @mark.get_selectores_html
    def test_get_selectores_html_retornaSeletores(self):
        noticia = classesKBP.Noticias()
        verifica = noticia.get_selectores_html(urlSite=site.gn_brasil)
        assert verifica != ''

    @mark.get_html_text
    def test_get_html_text_valid_url(self):
        """Testa se a função retorna o texto HTML corretamente para uma URL válida."""
        noticia = classesKBP.Noticias()
        html_text = noticia.get_html_text(urlSite=site.gn_brasil)
        assert '<!doctype html>' in html_text

    @mark.get_html_text
    def test_get_html_text_invalid_url(self):
        """Testa se a função retorna o texto HTML corretamente para uma URL válida."""
        noticia = classesKBP.Noticias()
        html_text = noticia.get_html_text(urlSite='https://naoexasdfiste.com')
        assert 'erro na captura do site' or 'Moved' in html_text

teste = Testes()
