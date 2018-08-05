#curl --request POST --header "Content-Type: application/json" --data @Payload_json 'https://api.gdc.cancer.gov/files' > files.json
curl --request POST --header "Content-Type: application/json" --data @Payload_projects 'https://api.gdc.cancer.gov/projects' > projects.tsv

#curl --request POST --header "Content-Type: application/json" --data @Payload 'https://api.gdc.cancer.gov/cases' > cases.tsv

