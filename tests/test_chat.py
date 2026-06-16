from hamcrest import assert_that, equal_to
from aitool.command import ChatCommand
from aitool.client import FakeAiClient


def test_chat_command_returns_response():
    fake_client = FakeAiClient()
    fake_client.add_response("model-1", "Prompt A", "Response A")
    command = ChatCommand(client=fake_client)
    
    result = command.execute(model="model-1", prompt="Prompt A")
    
    assert_that(result, equal_to("Response A"))


def test_chat_command_returns_different_response_for_different_model_and_prompt():
    fake_client = FakeAiClient()
    fake_client.add_response("model-2", "Prompt B", "Response B")
    command = ChatCommand(client=fake_client)
    
    result = command.execute(model="model-2", prompt="Prompt B")
    
    assert_that(result, equal_to("Response B"))
