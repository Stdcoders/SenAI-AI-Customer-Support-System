from fastapi import APIRouter

from app.api.routes.agent import router as agent_router
from app.api.routes.analytics import router as analytics_router
from app.api.routes.audit import router as audit_router
from app.api.routes.contacts import router as contacts_router
from app.api.routes.dashboard import router as dashboard_router
from app.api.routes.drafts import router as drafts_router
from app.api.routes.ingest import router as ingest_router
from app.api.routes.intelligence import router as intelligence_router
from app.api.routes.rag import router as rag_router
from app.api.routes.respond import router as respond_router
from app.api.routes.threads import router as threads_router
from app.api.routes.status import router as status_router
api_router = APIRouter()

api_router.include_router(agent_router)
api_router.include_router(analytics_router)
api_router.include_router(audit_router)
api_router.include_router(contacts_router)
api_router.include_router(dashboard_router)
api_router.include_router(drafts_router)
api_router.include_router(ingest_router)
api_router.include_router(intelligence_router)
api_router.include_router(rag_router)
api_router.include_router(respond_router)
api_router.include_router(threads_router)
api_router.include_router(status_router)