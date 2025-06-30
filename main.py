from fastmcp import FastMCP
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr
from wolframclient.exception import WolframClientException

# Initialize FastMCP server
eval_mcp = FastMCP("Wolfram REPL MCP")

# Start a persistent Wolfram Language session
session = WolframLanguageSession()

@eval_mcp.tool
def eval_wolfram(code: str) -> str:
    """Evaluate a Wolfram Language expression and return its result as a string."""
    try:
        expr = wlexpr(code)
        result = session.evaluate(expr)
        return repr(result)
    except WolframClientException as e:
        return f"Wolfram Client Error: {e}"
    except Exception as e:
        return f"Unexpected Error: {e}"

@eval_mcp.tool
def terminate_session() -> str:
    """Terminate the Wolfram Language session and free resources."""
    try:
        session.terminate()
        return "Wolfram session terminated successfully."
    except Exception as e:
        return f"Error terminating session: {e}"

if __name__ == "__main__":
    # Run the MCP server (default STDIO transport)
    eval_mcp.run()
