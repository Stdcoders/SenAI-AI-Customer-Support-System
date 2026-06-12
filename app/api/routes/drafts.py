from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.action_repository import action_repository
from app.schemas.response import APIResponse

router = APIRouter(
    prefix="/drafts",
    tags=["Drafts"],
)


@router.patch(
    "/{draft_id}",
    response_model=APIResponse,
)
def edit_draft(
    draft_id: int,
    proposed_content: str,
    db: Session = Depends(get_db),
):

    draft = action_repository.get_by_id(
        db=db,
        object_id=draft_id,
    )

    if draft is None:

        raise HTTPException(
            status_code=404,
            detail="Draft not found",
        )

    draft.proposed_content = proposed_content

    db.add(draft)
    db.commit()
    db.refresh(draft)

    return APIResponse(

        success=True,

        message="Draft updated successfully",

        data=draft,

    )


@router.post(
    "/{draft_id}/approve",
    response_model=APIResponse,
)
def approve_draft(
    draft_id: int,
    db: Session = Depends(get_db),
):

    draft = action_repository.get_by_id(
        db=db,
        object_id=draft_id,
    )

    if draft is None:

        raise HTTPException(
            status_code=404,
            detail="Draft not found",
        )

    draft.is_approved = True

    db.add(draft)
    db.commit()
    db.refresh(draft)

    return APIResponse(

        success=True,

        message="Draft approved successfully",

        data=draft,

    )