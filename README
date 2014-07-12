# Como rodar a aplicação

A aplicação implementada é uma aplicação Django, portanto, basta instalar as bibliotecas necessárias,
criar a estrutura de banco de dados e rodar o servidor de desenvolvimento.

## Preparação do ambiente

Para rodar a aplicação é necessário ter uma instalação Python com as seguintes bibliotecas: Django, 
django-rest-framework, django-nose e coverage. Como em ambientes *nix o Python é utilizado em funções
importantes do sistema operacional, é mais seguro utilizar uma instalação virtual. virtualenv é uma
ferramenta que permite construir múltiplas instalações Python em uma mesma máquina, permitindo que
cada uma tenha suas próprias bibliotecas.

### Instale o virtualenv
```
sudo pip install virtualenv
``` 

Assumimos que a máquina já possui o pip instalado. 

### Crie um ambiente novo na pasta da aplicação

```
git clone https://github.com/casimiro/mluiza.git
cd mluiza
virtualenv env
```

### Ative o ambiente e instale as dependencias

```
source env/bin/activate
pip install -r requirements
```

### Crie a estrutra de banco de dados

```
python manager.py syncdb
```

### Rode a aplicação

```
python manager.py runserver
```

### Rodando os testes

Para rodar os testes e gerar os relatórios sobre cobertura basta executar:

```
python manager.py test
```
