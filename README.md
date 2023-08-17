# FHIR TESTE

***

# Infra

A infra está dentro do diretório infra

Os arquivos docker-compose.yaml e hapi.application.yaml foram retirados do endereço abaixo
O intuito é ter o server fhir com banco de dados externo, postgres.

https://github.com/hapifhir/hapi-fhir-jpaserver-starter

- Para iniciar o docker-compose será necessário criar o diretório infra/fahir-server/hapi.postgress.data

***

# Código
O script de carga está no diretório src

## Passos para execução do script de carga

- Para iniciar o projeto iniciar o ambiente python virtual digitando: python -m venv .venv
- Após inicializar o ambiente digitar source source .venv/bin/activate
- Quando ativado o ambiente executar: pip install -r requirements.txt para instalação do módulo fhirpy

***

# Dados do paciente

Os dados do paciente estão no diretório data


