from mcp.server.fastmcp import FastMCP

mcp = FastMCP("email_triage")


@mcp.tool()
def emails_list() -> list:
    """List of emails to be triaged."""

    return emails_list



