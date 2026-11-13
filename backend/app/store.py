from .schemas import Deployment, DeploymentCreate


class DeploymentStore:
    """In-memory store for local development only; data resets on restart."""

    def __init__(self):
        self._deployments: dict[int, Deployment] = {}
        self._next_id = 1

    def all(self) -> list[Deployment]:
        return list(self._deployments.values())

    def create(self, data: DeploymentCreate) -> Deployment:
        deployment = Deployment(id=self._next_id, **data.model_dump())
        self._deployments[deployment.id] = deployment
        self._next_id += 1
        return deployment

    def get(self, deployment_id: int) -> Deployment | None:
        return self._deployments.get(deployment_id)
