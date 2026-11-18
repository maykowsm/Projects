import os
import qrcode
basePath = "https://3dviewer.net/index.html#model=https://github.com/maykowsm/Projects/blob/main/projetos/"

arquivos = os.listdir(os.getcwd())
nome_pasta = os.path.basename(os.getcwd())

listaLinks = []


def gerarQRCode(link, nome):
    img = qrcode.make(link)
    img.save(nome)

# GERA A LISTA DE LINKS
for nomeArquivo in arquivos:
    if not "gerador_links" in nomeArquivo and not "links_modelos_3D" in nomeArquivo:
        tipoArquivo = ""
        if "concreto" in nomeArquivo.lower() or "armado" in nomeArquivo.lower() or "CA" in nomeArquivo:
            tipoArquivo = "CONCRETO ARMADO - \n"            
        elif "eletrico" in nomeArquivo.lower() :
            tipoArquivo = "ELÉTRICO - \n"
        elif "hidraulico" in nomeArquivo.lower() or "hidráulico" in nomeArquivo.lower():
            tipoArquivo = "HIDRÁULICO - \n"
        elif "sanitario" in nomeArquivo.lower() :
            tipoArquivo = "SANITÁRIO - \n"
        elif "hidrosanitario" in nomeArquivo.lower() :
            tipoArquivo = "HIDROSANITÁRIO - \n"
        
        listaLinks.append(tipoArquivo)
        link  = basePath + nome_pasta.replace(" ", "%20") + "/" + nomeArquivo.replace(" ", "%20") + "\n\n"
        listaLinks.append(link)
        gerarQRCode(link=link.split('\n')[0], nome = "QR_" + tipoArquivo.split("-")[0] + ".jpg")


# ESCREVE UM ARQUIVO TXT COM OS LINKS
with open("links_modelos_3D_" + nome_pasta.replace(" ", "_") + ".txt", "w") as arq:
    arq.writelines(listaLinks)


print(listaLinks)