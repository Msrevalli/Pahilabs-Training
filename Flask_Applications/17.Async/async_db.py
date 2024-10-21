import asyncio

async def async_db_query():
    # Simulate a database query with async delay
    await asyncio.sleep(2)
    return {"message": "Data fetched from database!"}
