from alembic import command
from alembic.config import Config


def initialize_database():
    alembic_config = Config("alembic.ini")
    command.upgrade(alembic_config, "head")


if __name__ == "__main__":
    initialize_database()

