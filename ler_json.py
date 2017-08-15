import json
serialized = """{ "title" : "Data Science Book",
                  "author" : "Joel Grus", 
                  "publicationYear" : 2014,
                  "topics" : [ "data", "science", "data science"] }"""

#analisa o json para criar um dict do python
deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
    print deserialized