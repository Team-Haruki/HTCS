import os
from typing import Dict

from .utils import regex_replace, load_data, save_data
from .configs import merge_keys, replace_keys
from .configs import ReplacementType, BondReplacementType, MasterType

modified_master_dir = 'data'
save_modified_data = True

async def master_handler(original_master: Dict) -> Dict:
    for key, values in original_master.items():
        modified_file_path = None
        is_not_replace = True
        match key:
            case key if key in replace_keys:
                modified_file_path = os.path.join(modified_master_dir, 'replace', f"{key}.json")
                if os.path.exists(modified_file_path):
                    original_master[key] = await load_data(modified_file_path)
                    is_not_replace = False
            case key if key in merge_keys:
                modified_file_path = os.path.join(modified_master_dir, 'merge', f"{key}.json")
                if os.path.exists(modified_file_path):
                    modified_data = await load_data(modified_file_path)
                    keys_to_merge = merge_keys[key]
                    modified_data_map = {item['id']: item for item in modified_data}
                    for item in values:
                        if item['id'] in modified_data_map:
                            for merge_key in keys_to_merge:
                                if merge_key in modified_data_map[item['id']]:
                                    lower_case = modified_data_map[item['id']][merge_key].lower()
                                    if not ("happy birthday" in lower_case or "happy anniversary" in lower_case
                                        or "2020" in lower_case
                                        or "2021" in lower_case
                                        or "2022" in lower_case
                                        or "2023" in lower_case
                                        or "2024" in lower_case
                                        or "2025" in lower_case
                                        or "2026" in lower_case
                                        or "2027" in lower_case
                                        or "2028" in lower_case
                                        or "生日快乐" in lower_case
                                        or "周年" in lower_case
                                        or "新年" in lower_case
                                    ):
                                        item[merge_key] = modified_data_map[item['id']][merge_key]
            case MasterType.WORDINGS.value:
                modified_file_path = os.path.join(modified_master_dir, 'merge', f"{key}.json")
                tw_wordings = await load_data(modified_file_path)
                tw_wordings_map = {item['wordingKey']: item['value'] for item in tw_wordings}
                for item in values:
                    k = item.get('wordingKey')
                    if k in tw_wordings_map:
                        item['value'] = tw_wordings_map[k]
            case MasterType.APPEALS.value:
                for data in values:
                    data['text'] = await regex_replace(data['text'], ReplacementType.APPEALS)
            case MasterType.EVENT_ITEMS.value:
                for data in values:
                    data['name'] = await regex_replace(data['name'], ReplacementType.EVENT_ITEMS)
                    data['flavorText'] = '可在活動交換所中交換物品。'
            case MasterType.BONDS_HONORS.value:
                for data in values:
                    data['name'] = (await regex_replace(data["name"], ReplacementType.CHARACTER)).replace('と', '和')
                    _description = await regex_replace(data["description"], BondReplacementType.SHORT_DESCRIPTION)
                    data["description"] = await regex_replace(_description, ReplacementType.CHARACTER)
                    for level in data['levels']:
                        _description = await regex_replace(level["description"], BondReplacementType.LONG_DESCRIPTION)
                        level["description"] = await regex_replace(_description, ReplacementType.CHARACTER)
            case MasterType.BONDS_HONOR_WORDS.value:
                modified_file_path = os.path.join(modified_master_dir, 'merge', f"{key}.json")
                tw_bonds = await load_data(modified_file_path)
                tw_bonds_map = {item['id']: {'name': item['name'], 'description': item['description']} for item in
                                tw_bonds}
                for data in values:
                    k = data.get('id')
                    if k in tw_bonds_map:
                        data['name'] = tw_bonds_map[k]['name']
                        data['description'] = tw_bonds_map[k]['description']
                    else:
                        _name = await regex_replace(data['name'], BondReplacementType.GENERAL_FAN_NAME)
                        data['name'] = await regex_replace(_name, ReplacementType.CHARACTER)
                        _description = await regex_replace(data['description'], BondReplacementType.LONG_DESCRIPTION)
                        data['description'] = await regex_replace(_description, ReplacementType.CHARACTER)
            case MasterType.EVENT_MISSIONS.value:
                for data in values:
                    data['sentence'] = await regex_replace(data['sentence'], ReplacementType.EVENT_MISSIONS)
            case MasterType.LIVE_MISSION_PERIODS.value:
                for data in values:
                    data['sentence'] = await regex_replace(data['sentence'], ReplacementType.LIVE_MISSION_PERIODS)
            case MasterType.MUSIC_VOCALS.value:
                for data in values:
                    data['caption'] = await regex_replace(data['caption'], ReplacementType.MUSIC_VOCALS)

        if save_modified_data and modified_file_path and is_not_replace:
            await save_data(modified_file_path, values)

    return original_master
