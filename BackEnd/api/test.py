from venv import create
from utils.auth import get_current_user_from_token

print(
    get_current_user_from_token(
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjYxNDYzMTAyLCJ1c2VyX2lkIjoiNTUwZTg0MDBlMjliNDFkNGE3MTY0NDY2NTU0NDAwMDAifQ.F_C-kT4cK5z0Lp92pKz861OMJRsnCDV1d19OqBdLd-A",
        "access_token",
    )
)
