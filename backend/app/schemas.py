from enum import Enum
from pydantic import BaseModel, Field


class DeploymentStatus(str, Enum):
    pending = "pending"
    running = "running"
    succeeded = "succeeded"
    failed = "failed"


class DeploymentCreate(BaseModel):
    service: str = Field(min_length=1, max_length=100)
    image: str = Field(min_length=1, max_length=255)
    environment: str = Field(pattern=r"^(dev|staging|production)$")


class Deployment(DeploymentCreate):
    id: int
    status: DeploymentStatus = DeploymentStatus.pending
