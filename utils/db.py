from pymongo import MongoClient

print("Connecting to database...")
client = MongoClient(
    "mongodb+srv://AviaxMusic:AviaxMusic@cluster0.qtfk4yn.mongodb.net/?retryWrites=true&w=majority"
)

db = client["ResourceRise"]
subjectsdb = db["subjects"]
modulesdb = db["modules"]
resourcesdb = db["resources"]

print("Connected to database...")

CACHE = {}


# Function to get all available subjects from db
def get_subjects():
    # Checking if the data is in cache
    if "subjects" in CACHE:
        return CACHE["subjects"]

    result = []
    for i in subjectsdb.find({}, sort=[("num", 1)]):
        result.append({"code": i["code"], "name": i["name"]})

    # Saving to cache
    CACHE["subjects"] = result

    return result


# Function to get all modules of a subject from db
def get_subject_modules(subject_code):
    # Checking if the data is in cache
    if subject_code in CACHE:
        return CACHE[subject_code]

    i = modulesdb.find_one({"code": subject_code})
    result = {"code": i["code"], "name": i["name"], "modules": i["modules"]}

    # Saving to cache
    CACHE[subject_code] = result

    return result


# Function to get all resources of a module from db
def get_resources_module(module_code):
    # Checking if the data is in cache
    if module_code in CACHE:
        return CACHE[module_code]

    result = resourcesdb.find_one({"mid": module_code})
    
    # Saving to cache
    CACHE[module_code] = result

    return result
