import re
from typing import Union, Dict, List

import aiofiles
import ujson as json

from .configs import ReplacementType, BondReplacementType


async def load_data(file_path: str) -> Union[Dict, List]:
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
        content = await f.read()
        return json.loads(content)


async def save_data(file_path: str, data: Union[Dict, List]) -> None:
    async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
        await f.write(json.dumps(data, indent=4, ensure_ascii=False))


async def regex_replace(text: str, replace_type: Union[ReplacementType, BondReplacementType]) -> str:
    if isinstance(replace_type, ReplacementType):
        for pattern, replacement in replace_type.value:
            text = re.sub(pattern, replacement, text)
    elif isinstance(replace_type, BondReplacementType):
        pattern, repl = replace_type.value
        text = re.sub(pattern, repl, text)
    return text
