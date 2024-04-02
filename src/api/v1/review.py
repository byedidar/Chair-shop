from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import review_service
from src.reposotories.all_repositories import ChairRepository, UserRepository
from src.schemas.review import ReviewCreate, ReviewRead
from src.services.review import ReviewService

review_router = APIRouter(prefix="/v1/review", tags=["review"])

@review_router.post(
    "/",
    status_code=200,
    summary="Добавить новый отзыв",
    response_model=ReviewRead  
)
async def post_review(review_create: ReviewCreate, review_service: ReviewService = Depends(review_service)):
    user_exists = await review_service.get_entity(user_id=review_create.user_id)
    if not user_exists:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    chair_exists = await review_service.get_entity(chair_id=review_create.chair_id)
    if not chair_exists:
        raise HTTPException(status_code=404, detail="Кресло не найдено")
    
    review_data = review_create.dict()
    review_id = await review_service.create_entity(review_data)
    return review_id
