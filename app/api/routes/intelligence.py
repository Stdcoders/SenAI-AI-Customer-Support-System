import requests
from bs4 import BeautifulSoup

from fastapi import APIRouter
from app.schemas.response import APIResponse

router = APIRouter(
    prefix="/intelligence",
    tags=["Web Intelligence"],
)


def get_reputation():

    url = "https://www.trustpilot.com/review/openai.com"

    try:

        response = requests.get(

            url,

            headers={

                "User-Agent": "Mozilla/5.0",

            },

            timeout=5,

        )

        soup = BeautifulSoup(

            response.text,

            "html.parser",

        )

        rating = soup.find("p")

        return {

            "source": "Trustpilot",

            "rating": rating.text if rating else "Unavailable",

        }

    except Exception as e:

        return {

            "source": "Trustpilot",

            "rating": "Unavailable",

            "error": str(e),

        }


@router.get(
    "/reputation",
    response_model=APIResponse,
)
def reputation():

    return APIResponse(

        success=True,

        message="Reputation fetched successfully",

        data=get_reputation(),

    )