import wikipedia
busca=input("Digite sua pesquisa: ")
wiki=wikipedia.set_lang('pt')
resposta=wikipedia.summary(busca,2)
print(resposta)
