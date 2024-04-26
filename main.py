from qaseio.pytest import qase

from backend.flowwow_api.profile.requests.ChangeProfileRequestDto import ChangeProfileRequestDto
from common.qase.constants import QASEPriority

@qase.title("Невозможность изменить email на невалидный в профиле")
@qase.description("""
1. Попытка изменить email на невалидный в профиле
""")
@qase.priority(QASEPriority.high.name)
@qase.suite("Профиль")
def test_change_invalid_email_in_profile(api, client, generators):
    flowwow_web_api = api.flowwow_web(client)
    invalid_email_profile = ChangeProfileRequestDto(
    name=generators.users.name,
    email="123",
    yii_csrf_token=flowwow_web_api.current_yii_csrf_token
)

    save_info_to_profile_response = flowwow_web_api.profile.save_info_to_profile(invalid_email_profile).model

    assert save_info_to_profile_response.result is False
