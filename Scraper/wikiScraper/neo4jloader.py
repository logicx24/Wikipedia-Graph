import neo4j

connection = neo4j.connect("http://localhost:7474")
cursor = connection.cursor()

