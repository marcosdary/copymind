from sqlalchemy.ext.asyncio import AsyncSession
from groq.types.chat import ChatCompletionMessageToolCall
from json import loads
from typing import List

from app.repositories import ConversationRepository

async def execute_tool(
    tools_calls: List[ChatCompletionMessageToolCall],
    session: AsyncSession,
) -> str:
    
    conv_repo = ConversationRepository(session=session)

    responses = list()

    for tool_call in tools_calls:
        function = tool_call.function

        arguments = loads(function.arguments)
              
        name = function.name

        if name == "read_by_id":
            data = await conv_repo.read_by_id(**arguments)
            responses.append(data)

        if name == "read_all":
            data = await conv_repo.read_all()
            responses.extend(data)
    return responses