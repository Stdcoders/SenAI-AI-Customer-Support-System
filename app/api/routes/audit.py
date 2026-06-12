from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.response import APIResponse

router = APIRouter(
    prefix="/audit",
    tags=["Audit"],
)


@router.get(
    "/{entity_type}/{entity_id}",
    response_model=APIResponse,
)
def audit_history(
    entity_type: str,
    entity_id: int,
):

    return APIResponse(

        success=True,

        message="Audit history fetched successfully",

        data={

            "entity_type": entity_type,

            "entity_id": entity_id,

            "events": [

                {

                    "action": "Created",

                    "status": "Completed",

                }

            ],

        },

    )