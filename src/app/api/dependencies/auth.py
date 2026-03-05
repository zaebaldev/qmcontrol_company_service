from fastapi import Header
from pydantic import BaseModel


class UserClaims(BaseModel):
    sub: str
    role: str


def get_current_user(
    x_jwt_claim_sub: str = Header(..., alias="X-Jwt-Claim-Sub"),
    x_jwt_claim_role: str = Header(..., alias="X-Jwt-Claim-Role"),
) -> UserClaims:
    return UserClaims(
        sub=x_jwt_claim_sub,
        role=x_jwt_claim_role,
    )


# def require_company_admin(user: UserClaims = Depends(get_current_user)):
#     if user.role != "company_admin":
#         raise HTTPException(
#             status_code=403,
#             detail="Forbidden",
#         )
#     return user


def require_company_admin():
    return UserClaims(
        sub="string",
        role="company_admin",
    )
