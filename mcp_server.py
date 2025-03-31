from flask import Flask, request, jsonify
app = Flask(__name__)
# Example data: a simple dictionary mapping resource IDs to their content.
resources = {
    "1": "This is the content of resource 1.",
    "2": "Content for resource 2 is here.",
    "3": "Resource 3 contains important information."
}
@app.route('/mcp', methods=['POST'])
def mcp_handler():
    # Parse the incoming JSON-RPC request.
    req = request.get_json()
    if req.get("jsonrpc") != "2.0":
        return jsonify({
            "jsonrpc": "2.0",
            "error": {"code": -32600, "message": "Invalid Request: JSON-RPC version must be 2.0"},
            "id": req.get("id")
        })
    method = req.get("method")
    params = req.get("params", {})
    request_id = req.get("id")
    # Handle the MCP methods.
    if method == "resources/list":
        # Return the list of available resource IDs.
        result = list(resources.keys())
    elif method == "resources/read":
        # Retrieve a specific resource based on its ID.
        resource_id = params.get("resource_id")
        if resource_id in resources:
            result = resources[resource_id]
        else:
            return jsonify({
                "jsonrpc": "2.0",
                "error": {"code": -32602, "message": f"Resource with id {resource_id} not found."},
                "id": request_id
            })
    else:
        # Return an error for any unknown method.
        return jsonify({
            "jsonrpc": "2.0",
            "error": {"code": -32601, "message": f"Method {method} not found."},
            "id": request_id
        })
    # Return the successful JSON-RPC response.
    return jsonify({
        "jsonrpc": "2.0",
        "result": result,
        "id": request_id
    })
if __name__ == '__main__':
    # Run the MCP server on localhost port 8000.
    app.run(host='0.0.0.0', port=8000)