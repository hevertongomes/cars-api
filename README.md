# CARS-API

Uma api para gerência de carros e marcas

## Iniciando

O Cars-API foi construido utilizando o Framework Python Django em sua versão 3.2.5 justamente com o Djando rest framework versão 3.12.4 e interpretador Python 3.7.3.


### Pré-requisitos

* Docker e Docker-Compose.

### Instalação do Docker

Digite o comando no seu terminal linux:

```
curl -sSL https://get.docker.com | sh

```

### Instalação do Docker Compose    

Digite o comando no seu terminal linux para download da versão atual do Docker Compose:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

```
Em seguida, execute o comando a seguir para dar as permissões necessárias:

```
sudo chmod +x /usr/local/bin/docker-compose
```
**ATENÇÃO** Talvez a versão em questão não seja a mais atual. Para maiores informações, consulte a documentação do [Docker Compose](https://docs.docker.com/compose/install/)


### Clonar o Projeto no Repositório GitLab com HTTPS

No seu terminal linux, em um diretório de sua preferência para projetos, digite:

```
git clone https://github.com/hevertongomes/cars-api/

```

No diretório do projeto no mesmo nível de pasta de **docker-compose.yml** digite para construir a imagem contida em Dockerfile e suba o ambiente com o comando:

```
docker-compose up
```
O ambiente está quase pronto, no entanto, alguns procedimentos de migrações. O Comando a seguir fará isso pra você:

```
docker-compose run web python3 manage.py migrate
```


Para testar a aplicação no navegador, utilize o caminho a seguir:

[Testar CARS-API](http://localhost:8000/api/v1/swagger/)

Para remover o ambiente de desenvolvimento, execute o comando abaixo:

```
docker-compose down
```
