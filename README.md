# ELK_Parser
Docker setup ready with Elasticsearch, Kibana and ElasticsearchDSL

1. Install and setup docker, docker-compose first
2. To run kibana just run ./run_docker.sh and it spins up a docker image with kibana and elasticsearch
3. Kibana can be viewed by opening localhost:5601 on any browser
4. To insert data directly from CSV files, I have created a simple ElasticsearchDSL script which is a rather nifty library for writing and running queries against Elasticsearch. 
5. Modify the ek_parser.py file to fit with dataset
6. Run python3 ek_parser.py and then view the data on Kibana!
