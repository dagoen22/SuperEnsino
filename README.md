
# Teste Super Ensino

  

Teste desenvolvido para a empresa super ensino

  

# Começando

  

O teste está todo em container docker, então para sua instalação é necessário ter o docker instalado localmente juntamente com o docker-compose.

  

# Instalando

Para rodar o projeto, faça um clone desse repositório.
entre no repositório src e execute o comando para construir a imagem que hospedará a aplicação django

    $ docker build .

em seguida, utilize vamos iniciar as instancias utilizando docker-compose

    $ docker-compose up -d

agora, vamos subir as migrations

    $ docker-compose exec web python manage.py migrate
e criar um superusuário no django

     $ docker-compose exec web python manage.py createsuperuser
   
 crie suas credenciais de acesso e em seguida acesse localhost:8000 para ter acesso a plataforma. 

#### Projeto

O projeto está dividido em duas partes. O site e as Api's REST.
O acesso as apis está no endpoint /api.

### Tempo de execução

3 horas

### Notas Finais

Acabei colocando um sistema de autenticação, não sabia se era necessário mas por vier das dúvidas aumenta a segurança do projeto.