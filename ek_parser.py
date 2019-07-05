#!/usr/bin/env python3
import csv
from elasticsearch_dsl import Document, Keyword, Text, connections, Date


class Csv(Document):
    testA = Keyword()
    testB = Text(analyzer='snowball', fields={'keyword': Keyword()})

    class Index:
        name = 'test_index_name'


def ingest_csv(filename: str):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
        for row in reader:
            doc = Csv()
            doc.testA = row.get('Test A')
            doc.testB = row.get('Test B')

            doc.save(skip_empty="false", refresh="true")


if __name__ == '__main__':
    def main():
        connections.create_connection(hosts=['localhost'])
        Csv.init()
        ingest_csv('test.csv')
        print()


    main()
