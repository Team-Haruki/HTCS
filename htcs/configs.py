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
    'mysekaiFixtureTags': ['name'],
    'billingShopTabParents': ['name'],
    'billingShopTabChildren': ['name'],
    'mysekaiCharacterTalkTweets': ['text']
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
    'gameCharacters',
    'gameCharacterUnits'
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
        (r"3900's前夜祭ハピネスパッケージガチャ開催", '举办3900\'s前夜祭欢乐礼物包招募'),
        (r'リコレクションフェスティバルガチャ開催', '举办回憶庆典招募'),
        (r'\[([^\]]+)\]ハピネスパッケージガチャ開催', r'[\1]举办欢乐礼物包招募'),
        (r'(.*?)前夜祭ハピネスパッケージガチャ開催', r'举办\1前夜祭欢乐礼物包招募'),
        (r'(.*?)前夜祭スペシャルプライズガチャ開催', r'举办\1前夜祭特別奖品招募'),
        (r'プレミアムプレゼントガチャ\s+(.*?)開催', r'举办\1高级礼物包招募'),
        (r'プレミアムプレゼントガチャ開催', '举办高级礼物包招募'),
        (r'\[([^\]]+)\]プレミアムプレゼントガチャ開催', r'[\1]举办高级礼物包招募'),
        # 静态匹配
        (r'★4メンバー确定ガチャ開催', '举办★4成员确定招募'),
        (r'期間限定メンバー登場', '期间限定成员登场'),
        (r'フェス限定メンバー登場', '庆典限定成员登场'),
        (r'セレクトリストガチャ開催', '举办选择清单招募'),
        (r'バースデーメンバー登場', '生日成员登场'),
        (r'アニバーサリーメンバー登場', '纪念日成员登场'),
        (r'コラボ限定メンバー登場', '联动限定成员登场'),
        (r'コラボガチャ登場', '联动招募登場'),
        (r'ハピネスパッケージガチャ開催', '举办欢乐礼物包招募'),
        (r'カラフェス限定メンバー登場', '彩色庆典限定成员登场'),
        (r'ユニットイベント限定メンバー登場', '团体活動限定成员登场'),
        (r'ブルフェス限定メンバー登場', '蓝色庆典限定成员登场'),
        (r'セレクトリストガチャ LIMITED EDITION開催', '举办选择清单招募 LIMITED EDITION'),
        (r'ベストコレクションガチャ開催', '举办最佳收藏招募')
    ]
    CHARACTER = [
        (r'花里みのり', '花里实乃理'),
        (r'小豆沢こはね', '小豆泽心羽'),
        (r'鳳えむ', '凤笑梦'),
        (r'草薙寧々', '草薙宁宁'),
        (r'朝比奈まふゆ', '朝比奈真冬'),
        (r'初音ミク', '初音未来'),
        (r'鏡音リン', '镜音铃'),
        (r'鏡音レン', '镜音连'),
        (r'巡音ルカ', '巡音流歌'),
        (r'みのり', '实乃理'),
        (r'こはね', '心羽'),
        (r'えむ', '笑梦'),
        (r'寧々', '宁宁'),
        (r'まふゆ', '真冬'),
        (r'ミク', '初音未来'),
        (r'リン', '镜音铃'),
        (r'レン', '镜音连'),
        (r'ルカ', '巡音流歌')
    ]
    EVENT_ITEMS = [
        (r'チャプター(\d+)バッジ', r'章节\1徽章'),
        (r'イベントバッジ', '活动徽章'),
        (r'ワールドバッジ', '世界徽章')
    ]
    EVENT_MISSIONS = [
        (r'累計(\d+)日ライブを1日1回クリアしよう。', r'连续\1日每天通过1次演出吧。'),
        (r'ライブを(\d+)回クリアしよう。', r'通过\1次演出吧。'),
        (r'ライブで楽曲をフルコンボで(\d+)回クリアしよう。', r'在演出中达成\1次FULL COMBO吧。'),
        (r'ライブで(\d+)種類の楽曲をクリアしよう。', r'在演出中通过\1首歌曲吧。'),
        (r'イベント「(.*?)」のイベントストーリー第(\d+)話を読もう。', r'观赏活动「\1」的第\2章活动剧情吧。'),
        (r'イベント「(.*?)」の交換所でバッジを(\d+)個消費しよう。', r'在活动「\1」的交换所消耗\2個徽章吧。'),
        (r'「(.*?) アフターライブ」に参加しよう。', r'參加「\1 After LIVE」吧。'),
        (r'(\d+)つのミッションを全て達成しよう。', r'通过所有\1个任务吧。')
    ]
    MUSIC_VOCALS = [
        (r'エイプリルフールver.', '愚人节ver.'),
        (r'アナザーボーカルver.', 'Another Vocal ver.'),
        (r'セカイver.', '「世界」ver.'),
        (r'バーチャル・シンガーver.', '虚拟歌手ver.'),
        (r'コネクトライブver.', 'Connect Live ver.')
    ]
    LIVE_MISSION_PERIODS = [
        (r'(.*?)年(.*?)月ライブミッション', r'\1年\2月LIVE任务')
    ]


class BondReplacementType(Enum):
    SHORT_DESCRIPTION = (r'(.*?)と(.*?)を一定ランクまで上げた', r'已将\1和\2提升至一定等级')
    LONG_DESCRIPTION = (r'(.*?)と(.*?)のキズナランクを(\d+)まで上げよう。', r'将\1和\2的情谊等级提升至\3吧。')
    GENERAL_FAN_NAME = (r'(.*?)＆(.*?)ファン', r'\1＆\2粉丝')
