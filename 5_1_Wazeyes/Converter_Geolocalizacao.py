from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Wazeyes") #Nome do seu app

endereco = input("Digite um endereço com o número  e cidade: ")

resultado = geolocator.gecode(endereco)

if resultado.valid_address == True:
    print("Endereço completo.: ", resultado)
    print("Coordenadas........: ", resultado.coordinates)
    print("Número.............: ", resultado.street_number)
    print("CEP................: ", resultado.postal_code)

print("Foram encontrados ", resultado.count, "endereços.")
for r in resultado:
    print("Cidade........: ", r.state)
    print("País..........: ", r.country)
    print("Logradouro....: ", r.route)
    print("############################")