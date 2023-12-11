#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#bibliotecas
import pickle


# In[ ]:


#função para importar um modelo no formato pickle

def carregar_modelo(caminho_do_modelo):
    with open(caminho_do_modelo, 'rb') as arquivo:
        modelo = pickle.load(arquivo)
    return modelo


# In[ ]:


#função para prever valores
def fazer_predicao(modelo, dados):
    # Faça a lógica de predição utilizando o modelo carregado
    resultado = modelo.predict(dados)
    return resultado

