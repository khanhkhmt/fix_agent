-- Add FPT TTS provider/model/voices and native web search plugin seed

INSERT INTO `ai_model_provider` (`id`, `model_type`, `provider_code`, `name`, `fields`, `sort`, `creator`, `create_date`, `updater`, `update_date`)
VALUES (
    'SYSTEM_TTS_fpt',
    'TTS',
    'fpt',
    'FPT AI语音合成',
    JSON_ARRAY(
        JSON_OBJECT('key', 'api_key', 'type', 'string', 'label', 'FPT API 密钥', 'default', ''),
        JSON_OBJECT('key', 'voice', 'type', 'string', 'label', '默认音色', 'default', 'banmai'),
        JSON_OBJECT('key', 'speed', 'type', 'string', 'label', '语速', 'default', '0'),
        JSON_OBJECT('key', 'output_dir', 'type', 'string', 'label', '输出目录', 'default', 'tmp/')
    ),
    24, 0, NOW(), 0, NOW()
)
ON DUPLICATE KEY UPDATE
    `provider_code` = VALUES(`provider_code`),
    `name` = VALUES(`name`),
    `fields` = VALUES(`fields`),
    `sort` = VALUES(`sort`),
    `updater` = 0,
    `update_date` = NOW();

INSERT INTO `ai_model_config`
(`id`, `model_type`, `model_code`, `model_name`, `is_default`, `is_enabled`, `config_json`, `doc_link`, `remark`, `sort`, `creator`, `create_date`, `updater`, `update_date`)
VALUES (
    'TTS_FptTTS',
    'TTS',
    'FptTTS',
    'FPT AI语音合成',
    0,
    1,
    '{"type":"fpt","api_key":"","voice":"banmai","speed":"0","output_dir":"tmp/"}',
    'https://fpt.ai/tts',
    '越南语语音合成',
    24,
    0,
    NOW(),
    0,
    NOW()
)
ON DUPLICATE KEY UPDATE
    `model_code` = VALUES(`model_code`),
    `model_name` = VALUES(`model_name`),
    `is_enabled` = VALUES(`is_enabled`),
    `config_json` = VALUES(`config_json`),
    `doc_link` = VALUES(`doc_link`),
    `remark` = VALUES(`remark`),
    `sort` = VALUES(`sort`),
    `updater` = 0,
    `update_date` = NOW();

INSERT INTO `ai_tts_voice`
(`id`, `tts_model_id`, `name`, `tts_voice`, `languages`, `voice_demo`, `remark`, `sort`, `creator`, `create_date`, `updater`, `update_date`)
VALUES
('TTS_FptTTS0001', 'TTS_FptTTS', 'FPT-越南女声-banmai', 'banmai', 'Vietnamese', NULL, NULL, 1, 0, NOW(), 0, NOW()),
('TTS_FptTTS0002', 'TTS_FptTTS', 'FPT-越南女声-thuminh', 'thuminh', 'Vietnamese', NULL, NULL, 2, 0, NOW(), 0, NOW()),
('TTS_FptTTS0003', 'TTS_FptTTS', 'FPT-越南男声-leminh', 'leminh', 'Vietnamese', NULL, NULL, 3, 0, NOW(), 0, NOW()),
('TTS_FptTTS0004', 'TTS_FptTTS', 'FPT-越南女声-lannhi', 'lannhi', 'Vietnamese', NULL, NULL, 4, 0, NOW(), 0, NOW()),
('TTS_FptTTS0005', 'TTS_FptTTS', 'FPT-越南女声-linhsan', 'linhsan', 'Vietnamese', NULL, NULL, 5, 0, NOW(), 0, NOW()),
('TTS_FptTTS0006', 'TTS_FptTTS', 'FPT-越南女声-myan', 'myan', 'Vietnamese', NULL, NULL, 6, 0, NOW(), 0, NOW()),
('TTS_FptTTS0007', 'TTS_FptTTS', 'FPT-越南男声-giahuy', 'giahuy', 'Vietnamese', NULL, NULL, 7, 0, NOW(), 0, NOW())
ON DUPLICATE KEY UPDATE
    `tts_model_id` = VALUES(`tts_model_id`),
    `name` = VALUES(`name`),
    `tts_voice` = VALUES(`tts_voice`),
    `languages` = VALUES(`languages`),
    `sort` = VALUES(`sort`),
    `updater` = 0,
    `update_date` = NOW();

INSERT INTO `ai_model_provider` (`id`, `model_type`, `provider_code`, `name`, `fields`, `sort`, `creator`, `create_date`, `updater`, `update_date`)
VALUES (
    'SYSTEM_PLUGIN_WEB_SEARCH',
    'Plugin',
    'web_search',
    '联网搜索',
    JSON_ARRAY(
        JSON_OBJECT('key', 'description', 'type', 'string', 'label', '工具描述', 'default', '联网搜索实时信息，适合价格、新闻、人物职务、比赛结果等问题'),
        JSON_OBJECT('key', 'region', 'type', 'string', 'label', '搜索区域', 'default', 'vn-vi'),
        JSON_OBJECT('key', 'max_results', 'type', 'number', 'label', '默认结果数', 'default', 3),
        JSON_OBJECT('key', 'source_chars', 'type', 'number', 'label', '单源正文截断长度', 'default', 2500),
        JSON_OBJECT('key', 'timeout', 'type', 'number', 'label', '请求超时（秒）', 'default', 10)
    ),
    45, 0, NOW(), 0, NOW()
)
ON DUPLICATE KEY UPDATE
    `provider_code` = VALUES(`provider_code`),
    `name` = VALUES(`name`),
    `fields` = VALUES(`fields`),
    `sort` = VALUES(`sort`),
    `updater` = 0,
    `update_date` = NOW();
