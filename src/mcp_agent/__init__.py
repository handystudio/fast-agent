"""fast-agent - (fast-agent-mcp) An MCP native agent application framework"""

# Import important MCP types
from mcp.types import (
    CallToolResult,
    EmbeddedResource,
    GetPromptResult,
    ImageContent,
    Prompt,
    PromptMessage,
    ReadResourceResult,
    Role,
    TextContent,
    Tool,
)

# Core agent components
from mcp_agent.agents.agent import Agent, AgentConfig
from mcp_agent.core.direct_agent_app import DirectAgentApp

# Workflow decorators
from mcp_agent.core.direct_decorators import (
    agent,
    chain,
    evaluator_optimizer,
    orchestrator,
    parallel,
    router,
)

# FastAgent components
from mcp_agent.core.fastagent import FastAgent

# Request configuration
from mcp_agent.core.request_params import RequestParams

# Core protocol interfaces
from mcp_agent.mcp.interfaces import AgentProtocol, AugmentedLLMProtocol
from mcp_agent.mcp.mcp_aggregator import MCPAggregator, MCPCompoundServer
from mcp_agent.mcp.prompt_message_multipart import PromptMessageMultipart

__all__ = [
    # MCP types
    "Prompt",
    "Tool",
    "CallToolResult",
    "TextContent",
    "ImageContent",
    "PromptMessage",
    "GetPromptResult",
    "ReadResourceResult",
    "EmbeddedResource",
    "Role",
    # Core protocols
    "AgentProtocol",
    "AugmentedLLMProtocol",
    # Core agent components
    "Agent",
    "AgentConfig",
    "MCPAggregator",
    "MCPCompoundServer",
    "PromptMessageMultipart",
    # FastAgent components
    "FastAgent",
    "DirectAgentApp",
    # Workflow decorators
    "agent",
    "orchestrator",
    "router",
    "chain",
    "parallel",
    "evaluator_optimizer",
    # Request configuration
    "RequestParams",
]
