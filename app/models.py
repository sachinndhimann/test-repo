from sqlalchemy import Table, Column, Integer, String, ForeignKey
from app.database import metadata

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True),
    Column("email", String, unique=True),
    Column("hashed_password", String),
)

organisations = Table(
    "organisations", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True),
    Column("owner_id", Integer, ForeignKey("users.id")),
)

projects = Table(
    "projects", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("organisation_id", Integer, ForeignKey("organisations.id")),
)

data_projects = Table(
    "data_projects", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("project_id", Integer, ForeignKey("projects.id")),
)

synthesizers = Table(
    "synthesizers", metadata,
    Column("id", Integer, primary_key=True),
    Column("model_name", String),
)
