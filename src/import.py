import asyncio
from fhirpy import AsyncFHIRClient
import csv

filepath = '../data/patients.csv'
client = AsyncFHIRClient(
        'http://localhost:8080/fhir/',
        authorization='Bearer TOKEN',
    )

async def main():

    with open(filepath, encoding='ISO 8859-1') as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:
            #print(row)
            Nome, Sobrenome = row['Nome'].split(' ', 1)
            name = [{'use': 'usual' , 'text': row['Nome'] , 'family': Sobrenome, 'given': Nome}] 
            contactPhone = [{'system':'phone', 'value':row['Telefone'], 'use':'home', 'rank':1}]

            patient = client.resource('Patient', 
            active=True,
            identifier=row['CPF'],
            name=name, 
            birthdate=row['Data de Nascimento'], 
            telecom=contactPhone,
            country=row['País de Nascimento'],

            )
            await patient.save()

async def get_patient(id):
    patient = await client.reference('Patient', id).to_resource()
    #print(patient)
    return patient


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    patient = (loop.run_until_complete(get_patient(1)))
    print(patient)