###APYthonForNews

##Api para site de noticias em Python + Mongodb

Como rodar o projeto:

Na maquina deve conter Python + Flask (Ultimas releases) + Pymongo.
O mongodb roda em nuvem e é consumido em um app gratuido chamado ATLASDB. Basta alterar a string de login linha 9 e 10.
Para rodar no terminal utilizar o comando "python -m flask run"

Consumindo as APIs: 

ADICIONANDO UMA NOTICIA :
  POST /news HTTP/1.1
    Cookie: PHPSESSID=bpf7obgqhcre6v8grhqk3sp2il
    Content-Type: application/json
    Host: 127.0.0.1:5000
    Content-Length: 95

     { 
      "author": "Author",
      "text": "Teste de titulo 2012",
      "title": "tITULOS 2012"
     }
     
UPDATE NOTICIA: 
 PATCH /news HTTP/1.1
    Cookie: PHPSESSID=bpf7obgqhcre6v8grhqk3sp2il
    Content-Type: application/json
    Host: 127.0.0.1:5000
    Content-Length: 133

       { 
         "id" : "5f29dc43e424664bd2affea5",
        "author": "Author",
        "text": "Teste de titulo 2013",
        "title": "tITULOS 2015"
       }
       
       
GET TODAS AS NOTICIAS:

GET /news HTTP/1.1
  Cookie: PHPSESSID=bpf7obgqhcre6v8grhqk3sp2il
  Host: 127.0.0.1:5000
  
  
GET UMA NOTICIA:

 GET /news/?title=Titulo%20Test HTTP/1.1
  Cookie: PHPSESSID=bpf7obgqhcre6v8grhqk3sp2il
  Host: 127.0.0.1:5000

DELETE UMA NOTICIA:

  DELETE /news/?id=5f29b7dbf0d23c920a1c973b HTTP/1.1
    Cookie: PHPSESSID=bpf7obgqhcre6v8grhqk3sp2il
    Host: 127.0.0.1:5000

     
