from dasornis.db import Entity,Query,Field

class Fruit(Entity):
    id = Field()
    name = Field()

class GetFruits(Query):
    code = 'SELECT id,name FROM fruits'
    entitiy = Fruit

class CreateFruit(Query):
    code = "INSERT INTO fruits(name) VALUES ('%s')"
