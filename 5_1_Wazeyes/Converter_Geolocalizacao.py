from pygeocoders import Geocoder
geolocator = Geocoder(user_agent="Wazeyes") #Nome do seu app

endereco = {}

#armazena os inputs em uma lista de dicionário de dados
endereco = [input("Digite um endereço com o número  e cidade: ")]

resultado = geolocator.gecode(endereco)

if resultado.valid_address == True:  #Mostra as coordenadas do endereço completo pela key(chave)
    print("Endereço completo..: ", (Geocoder('AIzaSyAR3KdmvdCKEx6Obe_-G-FUS053OccVo0g').geocode(resultado).coordinates)

for r in resultado:
    print(f"Número........: ", {r.street_number})
    print(f"Cidade........: ", {r.state})
    print(f"País..........: ", {r.country})
    print(f"Logradouro....: ", {r.route})

print("Foi(ram) encontrado(s) ",resultado.count, " endereço(s).")