import pytest
from unittest.mock import MagicMock
from hamcrest import assert_that, equal_to
from aitool.models import ConfigModel
from aitool.commands import ChatCommand
from aitool.client import AiClient, FakeAiClient

def test_chat_command_execution():
    # Setup
    prompt = "What is 2+2"
    
    # Fake AiClient
    fake_client = FakeAiClient(response="4")
    
    # Execute
    command = ChatCommand(client=fake_client)
    result = command.execute(prompt=prompt)
    
    # Verify
    assert_that(result, equal_to("4"))

def test_chat_command_initialization():
    fake_client = FakeAiClient()
    command = ChatCommand(client=fake_client)
    
    assert_that(command.client, equal_to(fake_client))
