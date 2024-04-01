from fastapi import HTTPException


def validate_user_admin(user_role_id):
    if user_role_id == 1:
        raise HTTPException(status_code=403, detail="Недостаточно прав")
    return True


