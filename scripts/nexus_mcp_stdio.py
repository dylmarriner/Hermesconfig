#!/usr/bin/env python3
"""Nexus Memory MCP STDIO Adapter

Connects Hermes to Synapse Memory via the Nexus bridge.
Exposes tools for memory save, recall, search, and agent context.
"""
import json, os, sys, urllib.request, urllib.error, uuid

NEXUS_URL = os.environ.get("NEXUS_URL", "http://100.68.0.96:7777")
AGENT_ID = os.environ.get("NEXUS_AGENT_ID", "hermes")
DEVICE = os.environ.get("NEXUS_DEVICE", "lin-hp")
NEXUS_SECRET = os.environ.get("NEXUS_SECRET", "581af6b5d2676e586d892ac3e520d2e600ae7ea2e297789c41ba3558317d6f7a")

def nexus_call(endpoint, data=None, method="GET"):
    url = f"{NEXUS_URL}{endpoint}"
    headers = {"X-Nexus-Secret": NEXUS_SECRET, "Content-Type": "application/json"}
    req = urllib.request.Request(url, data=json.dumps(data).encode() if data else None, headers=headers, method=method)
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}"}
    except Exception as e:
        return {"error": str(e)}

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    rid = req.get("id")
    
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": rid, "result": {"protocolVersion": "2024-11-05", "capabilities": {"tools": {}}, "serverInfo": {"name": "nexus-memory", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": rid, "result": {"tools": [
            {"name": "memory_save", "description": "Save memory to Nexus", "inputSchema": {"type": "object", "properties": {"content": {"type": "string"}, "memory_type": {"type": "string"}, "importance": {"type": "number", "default": 0.5}}, "required": ["content"]}},
            {"name": "memory_recall", "description": "Recall relevant Nexus memories", "inputSchema": {"type": "object", "properties": {"query": {"type": "string"}, "limit": {"type": "integer", "default": 10}}, "required": ["query"]}},
            {"name": "memory_profile", "description": "Get agent profile", "inputSchema": {"type": "object", "properties": {}}}
        ]}}
    elif method == "tools/call":
        tool = params.get("name")
        args = params.get("arguments", {})
        if tool == "memory_save":
            r = nexus_call("/v1/memory/save", {"agent_id": AGENT_ID, "content": args["content"], "memory_type": args.get("memory_type", "observation"), "importance": args.get("importance", 0.5), "metadata": {"device": DEVICE, "source": "hermes-mcp"}}, "POST")
            return {"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": json.dumps(r)}]}}
        elif tool == "memory_recall":
            r = nexus_call(f"/v1/memory/recall/{AGENT_ID}?q={args['query']}&limit={args.get('limit', 10)}")
            return {"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": json.dumps(r)}]}}
        elif tool == "memory_profile":
            r = nexus_call(f"/v1/memory/profile/{AGENT_ID}")
            return {"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": json.dumps(r)}]}}
    
    return {"jsonrpc": "2.0", "id": rid, "result": {"content": [{"type": "text", "text": "unknown method"}]}}

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except json.JSONDecodeError:
            continue
