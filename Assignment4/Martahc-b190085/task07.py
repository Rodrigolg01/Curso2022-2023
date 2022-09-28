# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZvkY5z9mr1qjpMc4uNVLSgzt6VSS92Au

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
NS = Namespace("http://somewhere#")

print("\n 7.1 resultados SPARQL:")
q1= prepareQuery('''
SELECT ?subclasses
WHERE {
  ?subclasses rdfs:subClassOf ns:Person
}
''',
  initNs = {"ns": NS,"rdfs":RDFS}
)

for r in g.query(q1):
  print(r.subclasses)

print("\n 7.1 resultados RDFLib:")
for subC, p, o in g.triples((None,RDFS.subClassOf,NS.Person)):
    print(subC)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
# Visualize the results
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
NS = Namespace("http://somewhere#")

print("\n 7.2 resultados SPARQL:")
q2= prepareQuery('''
SELECT ?individuals
WHERE {
  { ?individuals rdf:type ns:Person
  
  }
UNION
  {
  ?individuals rdf:type ?type .
  ?type rdfs:subClassOf ns:Person
  }
}''',
  initNs = {"ns": NS, "rdf":RDF, "rdfs":RDFS}
)

for r in g.query(q2):
  print(r.individuals)




print("\n 7.2 resultados RDFLib:")
for suj, p, o in g.triples((None,RDF.type,NS.Person)):
  print(suj)

for subC, p, o in g.triples((None,RDFS.subClassOf,NS.Person)):
  for suj, p, o in g.triples((None,RDF.type,subC)):
    print(suj)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
# Visualize the results
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
NS = Namespace("http://somewhere#")


print("\n 7.3 resultados SPARQL:")
q3= prepareQuery('''
SELECT ?individuals ?properties ?values
WHERE {
  { ?individuals rdf:type ns:Person .
    ?individuals ?properties ?values
  
  }
UNION
  {
  ?individuals rdf:type ?type .
  ?type rdfs:subClassOf ns:Person .
  ?individuals ?properties ?values
  }
}''',
  initNs = {"ns": NS, "rdf":RDF, "rdfs":RDFS}
)

for r in g.query(q3):
  print(r.individuals, r.properties, r.values)





print("\n 7.3 resultados RDFLib:")
for s, p, o in g.triples((None,RDF.type,NS.Person)):
  for s1, p1, o1 in g.triples((s,None,None)):
    print(s1,p1,o1)

for subC, p, o in g.triples((None,RDFS.subClassOf,NS.Person)):
  for s, p, o in g.triples((None,RDF.type,subC)):
    for s1, p1, o1 in g.triples((s,None,None)):
      print(s1,p1,o1)