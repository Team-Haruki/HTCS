from enum import Enum

merge_keys = {
    'areas': ['name', 'subName'],
    'avatarAccessories': ['name'],
    'avatarCostumes': ['name'],
    'avatarMotions': ['name'],
    'avatarSkinColors': ['name'],
    'beginnerMissions': ['sentence'],
    'beginnerMissionV2s': ['sentence'],
    'boostItems': ['name', 'flavorText'],
    'cards': ['cardSkillName', 'prefix', 'gachaPhrase'],
    'characterArchiveVoices': ['displayPhrase', 'displayPhrase2'],
    'characterMissionV2s': ['sentence', 'progressSentence'],
    'costume2dGroups': ['name'],
    'customProfileCollectionResources': ['name'],
    'customProfileEtcResources': ['name'],
    'customProfileGeneralBackgroundResources': ['name'],
    'customProfileMemberStandingPictureResources': ['name'],
    'customProfilePlayerInfoResources': ['name'],
    'customProfileShapeResources': ['name'],
    'customProfileStoryBackgroundResources': ['name'],
    'honorMissions': ['sentence'],
    'loginBonusLive2ds': ['serif'],
    'materials': ['name', 'flavorText', 'flavorText2'],
    'normalMissions': ['sentence'],
    'penlightColors': ['name'],
    'practiceTickets': ['name', 'flavorText'],
    'skillPracticeTickets': ['name', 'flavorText'],
    'skills': ['description'],
    'stamps': ['name', 'description'],
    'subGameCharacters': ['name'],
    'systemLive2ds': ['serif'],
    'tips': ['title', 'description'],
    'mysekaiConvertItemObtainMysekaiBlueprintChoices': ['name'],
    'mysekaiConvertItemTabs': ['name'],
    'mysekaiFixtureMainGenres': ['name'],
    'mysekaiFixtureSubGenres': ['name'],
    'mysekaiGateCommonSkins': ['name'],
    'mysekaiGates': ['name'],
    'mysekaiGateUnitSkins': ['name'],
    'mysekaiHousingExhibitions': ['displayUserName'],
    'mysekaiItems': ['name', 'description'],
    'mysekaiItemTabs': ['name'],
    'mysekaiLiveMissionRewardGameCharacters': ['name'],
    'mysekaiMaterialTabs': ['name'],
    'mysekaiMusicRecordCategories': ['name'],
    'mysekaiNormalMissionSheets': ['name'],
    'mysekaiPhenomenas': ['name', 'description'],
    'mysekaiPhotoDecorations': ['name', 'description'],
    'mysekaiSiteHousingPresetGroups': ['name'],
    'mysekaiSites': ['name'],
    'mysekaiTools': ['name', 'description'],
    'mysekaiToolTabs': ['name'],
    'mysekaiNormalMissions': ['sentence'],
    'mysekaiMaterials': ['name', 'description'],
    'mysekaiFixtures': ['name', 'flavorText'],
    'mysekaiFixtureTags': ['name']
}
replace_keys = [
    'areaItemLevels',
    'areaItems',
    'characterArchiveVoiceTags',
    'characterProfiles',
    'colorfulPassV2s',
    'liveStages',
    'multiLiveLobbies',
    'rankMatchClasses',
    'rankMatchGrades',
    'unitProfiles',
    'unitStoryEpisodeGroups',
    'musicCollaborations',
    'unitStories',
    'gameCharacters'
]


class MasterType(Enum):
    WORDINGS = 'wordings'
    APPEALS = 'appeals'
    EVENT_ITEMS = 'eventItems'
    BONDS_HONORS = 'bondsHonors'
    BONDS_HONOR_WORDS = 'bondsHonorWords'
    EVENT_MISSIONS = 'eventMissions'
    LIVE_MISSION_PERIODS = 'liveMissionPeriods'
    MUSIC_VOCALS = 'musicVocals'


class ReplacementType(Enum):
    APPEALS = [
        # 动态匹配
        (r"3900's前夜祭ハピネスパッケージガチャ開催", '舉辦3900\'s前夜祭歡樂禮物包招募'),
        (r'リコレクションフェスティバルガチャ開催', '舉辦回憶慶典招募'),
        (r'\[([^\]]+)\]ハピネスパッケージガチャ開催', r'[\1]舉辦歡樂禮物包招募'),
        (r'(.*?)前夜祭ハピネスパッケージガチャ開催', r'舉辦\1前夜祭歡樂禮物包招募'),
        (r'(.*?)前夜祭スペシャルプライズガチャ開催', r'舉辦\1前夜祭特別獎品招募'),
        (r'プレミアムプレゼントガチャ\s+(.*?)開催', r'舉辦\1高級禮物包招募'),
        (r'プレミアムプレゼントガチャ開催', '舉辦高級禮物包招募'),
        (r'\[([^\]]+)\]プレミアムプレゼントガチャ開催', r'[\1]舉辦高級禮物包招募'),
        # 静态匹配
        (r'★4メンバー確定ガチャ開催', '舉辦★4成員確定招募'),
        (r'期間限定メンバー登場', '期間限定成員登場'),
        (r'フェス限定メンバー登場', '慶典限定成員登場'),
        (r'セレクトリストガチャ開催', '舉辦選擇清單招募'),
        (r'バースデーメンバー登場', '生日成員登場'),
        (r'アニバーサリーメンバー登場', '紀念日成員登場'),
        (r'コラボ限定メンバー登場', '聯動限定成員登場'),
        (r'コラボガチャ登場', '聯動招募登場'),
        (r'ハピネスパッケージガチャ開催', '舉辦歡樂禮物包招募'),
        (r'カラフェス限定メンバー登場', '彩色慶典限定成員登場'),
        (r'ユニットイベント限定メンバー登場', '團體活動限定成員登場'),
        (r'ブルフェス限定メンバー登場', '藍色慶典限定成員登場'),
        (r'セレクトリストガチャ LIMITED EDITION開催', '舉辦選擇清單招募 LIMITED EDITION'),
        (r'ベストコレクションガチャ開催', '舉辦最佳收藏招募')
    ]
    CHARACTER = [
        (r'花里みのり', '花里實乃理'),
        (r'小豆沢こはね', '小豆澤心羽'),
        (r'鳳えむ', '鳳笑夢'),
        (r'草薙寧々', '草薙寧寧'),
        (r'朝比奈まふゆ', '朝比奈真冬'),
        (r'初音ミク', '初音未來'),
        (r'鏡音リン', '鏡音鈴'),
        (r'鏡音レン', '鏡音連'),
        (r'巡音ルカ', '巡音流歌'),
        (r'みのり', '實乃理'),
        (r'こはね', '心羽'),
        (r'えむ', '笑夢'),
        (r'寧々', '寧寧'),
        (r'まふゆ', '真冬'),
        (r'ミク', '初音未來'),
        (r'リン', '鏡音鈴'),
        (r'レン', '鏡音連'),
        (r'ルカ', '巡音流歌')
    ]
    EVENT_ITEMS = [
        (r'チャプター(\d+)バッジ', r'章節\1徽章'),
        (r'イベントバッジ', '活動徽章'),
        (r'ワールドバッジ', '世界徽章')
    ]
    EVENT_MISSIONS = [
        (r'累計(\d+)日ライブを1日1回クリアしよう。', r'連續\1日每天通過1次LIVE吧。'),
        (r'ライブを(\d+)回クリアしよう。', r'通過\1次LIVE吧。'),
        (r'ライブで楽曲をフルコンボで(\d+)回クリアしよう。', r'在LIVE中達成\1次FULL COMBO吧。'),
        (r'ライブで(\d+)種類の楽曲をクリアしよう。', r'在LIVE中通過\1首歌曲吧。'),
        (r'イベント「(.*?)」のイベントストーリー第(\d+)話を読もう。', r'觀賞活動「\1」的第\2章活動劇情吧。'),
        (r'イベント「(.*?)」の交換所でバッジを(\d+)個消費しよう。', r'在活動「\1」的交換所消耗\2個徽章吧。'),
        (r'「(.*?) アフターライブ」に参加しよう。', r'參加「\1 After LIVE」吧。'),
        (r'(\d+)つのミッションを全て達成しよう。', r'通過所有\1個任務吧。')
    ]
    MUSIC_VOCALS = [
        (r'エイプリルフールver.', '愚人節ver.'),
        (r'アナザーボーカルver.', 'Another Vocal ver.'),
        (r'セカイver.', '「世界」ver.'),
        (r'バーチャル・シンガーver.', '虛擬歌手ver.'),
        (r'コネクトライブver.', 'Connect Live ver.')
    ]
    LIVE_MISSION_PERIODS = [
        (r'(.*?)年(.*?)月ライブミッション', r'\1年\2月LIVE任務')
    ]


class BondReplacementType(Enum):
    SHORT_DESCRIPTION = (r'(.*?)と(.*?)を一定ランクまで上げた', r'已將\1和\2提升至一定等級')
    LONG_DESCRIPTION = (r'(.*?)と(.*?)のキズナランクを(\d+)まで上げよう。', r'將\1和\2的情誼等級提升至\3吧。')
    GENERAL_FAN_NAME = (r'(.*?)＆(.*?)ファン', r'\1＆\2粉絲')
