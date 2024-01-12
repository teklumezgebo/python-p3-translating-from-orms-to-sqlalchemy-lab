from models import Dog

def create_table(base):
    pass

def save(session, dog):
    pass

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == f"{name}").first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == f"{name}", Dog.breed == f"{breed}").first()

def update_breed(session, dog, breed):
    session.query(Dog).filter(Dog.id == dog.id).update({dog.breed: f"{breed}"})