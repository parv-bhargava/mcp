import requests

# URL of the running MCP server.
url = "http://localhost:8000/mcp"

def send_request(method, params, request_id=1):
    # Build a JSON-RPC 2.0 compliant payload.
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": request_id
    }
    # Send the POST request to the MCP server.
    response = requests.post(url, json=payload)
    return response.json()

# Example 1: List available resources.
list_response = send_request("resources/list", {})
print("List of resources:", list_response.get("result"))

# Example 2: Read a specific resource (e.g., resource with id "1").
read_response = send_request("resources/read", {"resource_id": "1"}, request_id=2)
print("Content of resource 1:", read_response.get("result"))