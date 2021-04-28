# Chess

## Para preparar o ambiente

 - Criar uma pasta "ES2" no seu diretorio de projetos ou onde guarda seus codigos.
 - Dentro dessa pasta criada:
	 - Criar uma virtualenv, e nela usar o Python.3.8.2: python -m venv “nome_do_ambiente”
	 - Clonar o projeto backend do github
	 - Após isso, na pasta ES2 vao ter duas pastas, uma é o nome do ambiente virtual e outro a pasta do projeto que foi clonado
	 - Ativar a virtual env
	  > No linux é “source  nome_do_ambiente/bin/activate” 
	  > No windows, com o PowerShell aberto: ".\{nomeDoAmbienteVirtual}\Scripts\Activate.ps1"
	 - com o ambiente virtual ativo, entrar na pasta do projeto clonado e rodar “pip install -r requirements.txt”

## Para rodar os testes

 - Estando na raiz do projeto executar: `python3 -m pytest`

## Para executar o programa e jogar
 - Ativar o ambiente virtual com as dependencias instaladas(do requirements.txt) no terminal
 - Pelo terminal com ambiente virtual ativo, executar "python ./main.py"
 - Com o programa sendo executado, escolher no menu a opção desejada
