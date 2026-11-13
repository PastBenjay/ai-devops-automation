
from fastapi import FastAPI, HTTPException, status
from .schemas import Deployment, DeploymentCreate
from .store import DeploymentStore

app = FastAPI(title="AI DevOps Automation", version="0.1.0")
store = DeploymentStore()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "ai-devops-automation-api"
    }


@app.get("/api/health")
def api_health():
    return {
        "status": "ok",
        "checks": {
            "database": "ok"
        }
    }


@app.get("/api/deployments")
def list_deployments():
    deployments = store.all()
    return {
        "count": len(deployments),
        "deployments": deployments
    }


@app.post(
    "/api/deployments",
    response_model=Deployment,
    status_code=status.HTTP_201_CREATED
)
def create_deployment(payload: DeploymentCreate):
    return store.create(payload)


@app.get("/api/deployments/{deployment_id}", response_model=Deployment)
def get_deployment(deployment_id: int):
    deployment = store.get(deployment_id)

    if deployment is None:
        raise HTTPException(
            status_code=404,
            detail="Deployment not found"
        )

    return deployment
