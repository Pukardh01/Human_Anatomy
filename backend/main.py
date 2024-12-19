from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os,re
from owlready2 import *
from rdflib import Graph, Namespace



app = FastAPI(title="Basic Human Anatomy")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)


FILE_NAME = "updated_anatomy.owl"


rdf_graph = Graph()
rdf_graph.parse(FILE_NAME, format="xml")


ANATOMY = Namespace("http://www.example.org/anatomy.owl#")

onto = get_ontology(f"{FILE_NAME}").load()


IMAGE_FOLDER = "images"
BASE_IMAGE_URL = "http://localhost:8000"

def get_image_url(name):
    name = re.sub(r'\s+', '_', name).lower()
    image_path = os.path.join(IMAGE_FOLDER, f"{name}.png")
    print(image_path)
    if os.path.exists(image_path):
        return f"{BASE_IMAGE_URL}/{image_path}"
    return None

app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/systems")
def get_systems():
    sparql_query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX anatomy: <http://www.example.org/anatomy.owl#>

    SELECT ?system ?label ?description
    WHERE {
      ?system rdf:type anatomy:System .
      OPTIONAL { ?system anatomy:label ?label . }
      OPTIONAL { ?system anatomy:description ?description . }
    }
    """
    results = rdf_graph.query(sparql_query)
    systems = []

    for row in results:
        systems.append({
            "name": str(row.label),
            "image_url" : get_image_url(str(row.label))
        })
    return {"systems": systems}


@app.get("/system/{system_name}")
def get_specific_system_with_organs(system_name: str):
    matching_system = None
    for system in onto.System.instances():
        if str(system.label).lower() == system_name.lower():
            matching_system = system
            break

    if not matching_system:
        raise HTTPException(status_code=404, detail=f"System '{system_name}' not found")


    organs = []
    for organ in onto.Organs.instances():
        if matching_system in organ.isPartOf:
            organs.append({
                "name": str(organ.name),
                "latin": str(organ.latin),
                "main_function": str(organ.mainFunction),
                "image_url": get_image_url(str(organ.name))
            })

    return {
        "name": str(matching_system.label),
        "description": str(matching_system.description),
        "image_url": get_image_url(str(matching_system.label)),
        "organs": organs
    }