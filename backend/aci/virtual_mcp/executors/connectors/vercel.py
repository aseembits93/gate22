import json

from mcp import types as mcp_types

from aci.common.logging_setup import get_logger
from aci.common.schemas.virtual_mcp import VirtualMCPAuthTokenData
from aci.virtual_mcp.executors.connectors.base import BaseConnector

_RESULT = {
    "url": "https://github.com/apps/vercel/installations/select_target",
    "description": "Asks the user to use this URL to install the Vercel app in their GitHub account.",  # noqa: E501
}

_RESULT_JSON = json.dumps(_RESULT)

_TEXT_CONTENT = mcp_types.TextContent(type="text", text=_RESULT_JSON)

_CONTENT = [_TEXT_CONTENT]

logger = get_logger(__name__)


class Vercel(BaseConnector):
    def __init__(
        self,
        auth_token_data: VirtualMCPAuthTokenData,
    ):
        super().__init__(auth_token_data)
        self.api_key = auth_token_data.token

    def get_url_to_install_vercel_app_in_github(self) -> mcp_types.CallToolResult:
        """
        Get the URL to install the Vercel app in a GitHub repository.
        """
        return mcp_types.CallToolResult(
            structuredContent=_RESULT,
            content=_CONTENT,
        )
