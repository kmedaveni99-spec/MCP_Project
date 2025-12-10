# Weather Alerts MCP Server

Real-time U.S. weather alerts powered by the **National Weather Service (NWS) API**.  
Ask your AI:  
→ “Any active alerts in Texas?”  
→ “Is Florida under a hurricane warning?”  
→ “What’s happening in California right now?”

It answers instantly using official NWS data.

## Features

- Official NWS data (no API key needed)
- Full alert details: event, severity, areas, description & instructions
- State lookup by 2-letter code or natural language
- Conversation memory (remembers previous states you asked about)
- Lightning-fast with Groq (Qwen-32B) or any LLM you prefer

| Client            | Status | Notes                          |
|-------------------|--------|--------------------------------|
| Cursor            | Works  | Native MCP integration         |
| Claude Desktop    | Works  | Drag & drop `weather.json`     |
| Groq Chat         | Works  | Via MCP Inspector or direct    |
| MCP Inspector     | Works  | Great for debugging tools      |
