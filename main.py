from database import Database
from motoristaCLI import MotoristaCLI
from motoristaDAO import MotoristaDAO


db = Database(database="atlas-cluster", collection="Motorista")

motoristaDAO = MotoristaDAO(database=db)

motorista_cli = MotoristaCLI(motoristaDAO)

motorista_cli.run()

