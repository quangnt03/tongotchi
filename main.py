import asyncio

import uvicorn


async def main():
    config = uvicorn.Config(app="app.server:app", port=5000, reload=True)
    server = uvicorn.Server(config=config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
