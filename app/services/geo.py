import httpx


async def get_timezone_from_ip(ip: str) -> str:
    """
    Resolve timezone from IP using ipapi.co (public API).
    Returns e.g. "Africa/Tunis".
    """
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"https://ipapi.co/{ip}/json/")
            data = resp.json()
            return data.get("timezone", "UTC")
    except Exception:
        return "UTC"