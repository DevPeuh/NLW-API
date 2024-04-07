 O projeto em si foi uma aplicação para gerenciamento de eventos, onde explorei desde a configuração do ambiente de desenvolvimento até a implementação de funcionalidades cruciais, como manipulação de requisições HTTP, criação de rotas para diferentes recursos, modelagem de dados utilizando classes e persistência de dados em um banco SQL, criamos rotas como:
 01 - Cadastrar participante no evento
 02 - Consultar crachá do participante 
 03 - Consultar o evento

Nós também validamos para proibir participantes de cadastrarem no mesmo evento várias vezes e proibimos o participante no cadastro do evento se o número máximo de participantes foi atingido.

- PASS.IN -

O pass.in é uma aplicação de **gestão de participantes em eventos presenciais**.
A ferramenta permite que o organizador cadastre um evento e abra uma página pública de inscrição.
Os participantes inscritos podem emitir uma credencial para check-in no dia do evento.
O sistema fará um scan da credencial do participante para permitir a entrada no evento.

= REQUISITOS =

- REQUISITOS FUNCIONAIS -

- [✅]  O organizador deve poder cadastrar um novo evento;
- [✅]  O organizador deve poder visualizar dados de um evento;
- [✅]  O organizador deve poser visualizar a lista de participantes;
- [✅]  O participante deve poder se inscrever em um evento;
- [✅]  O participante deve poder visualizar seu crachá de inscrição;
- [✅]  O participante deve poder realizar check-in no evento;

- REGRAS DO NEGÓCO -

- [✅]  O participante só pode se inscrever em um evento uma única vez;
- [✅]  O participante só pode se inscrever em eventos com vagas disponíveis;
- [✅]  O participante só pode realizar check-in em um evento uma única vez;
