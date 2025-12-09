import asyncio
import sys
from server.weather import get_alerts

async def main():
    state = sys.argv[1] if len(sys.argv) > 1 else "CA"
    result = await get_alerts(state)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())


