"""Asynchronous release checks for Flet's single event loop."""

import httpx

from lib import log, platform_check

sys_platform = platform_check.os_platform()
all_info = []
latest_ver = ""


async def update_api():
    global all_info
    async with httpx.AsyncClient(timeout=10, follow_redirects=True) as client:
        response = await client.get(
            "https://api.github.com/repos/suntrise/Pseudo-localization-Demo/releases"
        )
        response.raise_for_status()
        releases = response.json()
    if not isinstance(releases, list) or not releases:
        raise ValueError("No releases returned")
    all_info = releases


async def version_check(ver):
    global latest_ver
    await update_api()
    latest_ver = all_info[0]["tag_name"]
    return ver != latest_ver


async def update(ver):
    try:
        if not await version_check(ver):
            return "NUL"
        release = all_info[0]
        detail = release.get("body") or "暂无更新说明"
        prerelease = (
            "\n\n## 注意\n本版本为预发布版本, 可能存在稳定性问题!"
            if release.get("prerelease") else ""
        )
        source_notice = (
            "\n\n## 源代码须知\n未知操作系统将提供源代码包。"
            if sys_platform == "unknow" else ""
        )
        return (f"- 当前版本: {ver}\n- 新版本: {latest_ver}\n\n"
                f"## 详细信息\n\n{detail}{prerelease}{source_notice}")
    except (httpx.HTTPError, ValueError, KeyError, TypeError) as exc:
        log.out(2, f"Check for update failure: {exc}")
        return "ERR"


def get_link():
    if sys_platform == "darwin":
        return "https://github.com/suntrise/Pseudo-localization-Demo/actions"
    if sys_platform == "unknow" and all_info:
        return all_info[0]["tarball_url"]
    return "https://github.com/suntrise/Pseudo-localization-Demo/releases"
