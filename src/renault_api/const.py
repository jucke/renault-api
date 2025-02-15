"""Constants for Renault API."""
CONF_COUNTRY = "country"
CONF_LOCALE = "locale"
CONF_GIGYA_APIKEY = "gigya-api-key"
CONF_GIGYA_URL = "gigya-root-url"
CONF_KAMEREON_APIKEY = "kamereon-api-key"
CONF_KAMEREON_URL = "kamereon-root-url"

PERMANENT_KEYS = [
    CONF_COUNTRY,
    CONF_LOCALE,
    CONF_GIGYA_APIKEY,
    CONF_GIGYA_URL,
    CONF_KAMEREON_APIKEY,
    CONF_KAMEREON_URL,
]


GIGYA_URL_EU = "https://accounts.eu1.gigya.com"
GIGYA_URL_US = "https://accounts.us1.gigya.com"
KAMEREON_APIKEY = "VAX7XYKGfa92yMvXculCkEFyfZbuM7Ss"
KAMEREON_URL_EU = "https://api-wired-prod-1-euw1.wrd-aws.com"
KAMEREON_URL_US = "https://api-wired-prod-1-usw2.wrd-aws.com"

LOCALE_BASE_URL = (
    "https://renault-wrd-prod-1-euw1-myrapp-one.s3-eu-west-1.amazonaws.com"
)

AVAILABLE_LOCALES = {
    "bg_BG": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3__3ER_6lFvXEXHTP_faLtq6eEdbKDXd9F5GoKwzRyZq37ZQ-db7mXcLzR1Jtls5sn",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "cs_CZ": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_oRlKr5PCVL_sPWUZdJ8c5NOl5Ej8nIZw7VKG7S9Rg36UkDszFzfHfxCaUAUU5or2",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "da_DK": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_5x-2C8b1R4MJPQXkwTPdIqgBpcw653Dakw_ZaEneQRkTBdg9UW9Qg_5G-tMNrTMc",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "de_DE": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_7PLksOyBRkHv126x5WhHb-5pqC1qFR8pQjxSeLB6nhAnPERTUlwnYoznHSxwX668",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "de_AT": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3__B4KghyeUb0GlpU62ZXKrjSfb7CPzwBS368wioftJUL5qXE0Z_sSy0rX69klXuHy",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "de_CH": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_UyiWZs_1UXYCUqK_1n7l7l44UiI_9N9hqwtREV0-UYA_5X7tOV-VKvnGxPBww4q2",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "en_GB": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_e8d4g4SE_Fo8ahyHwwP7ohLGZ79HKNN2T8NjQqoNnk6Epj6ilyYwKdHUyCw3wuxz",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "en_IE": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_Xn7tuOnT9raLEXuwSI1_sFFZNEJhSD0lv3gxkwFtGI-RY4AgiePBiJ9EODh8d9yo",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "es_ES": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_DyMiOwEaxLcPdBTu63Gv3hlhvLaLbW3ufvjHLeuU8U5bx3zx19t5rEKq7KMwk9f1",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "es_MX": {
        CONF_GIGYA_URL: GIGYA_URL_US,
        CONF_GIGYA_APIKEY: "3_BFzR-2wfhMhUs5OCy3R8U8IiQcHS-81vF8bteSe8eFrboMTjEWzbf4pY1aHQ7cW0",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_US,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "fi_FI": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_xSRCLDYhk1SwSeYQLI3DmA8t-etfAfu5un51fws125ANOBZHgh8Lcc4ReWSwaqNY",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "fr_FR": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_4LKbCcMMcvjDm3X89LU4z4mNKYKdl_W0oD9w-Jvih21WqgJKtFZAnb9YdUgWT9_a",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "fr_BE": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_ZK9x38N8pzEvdiG7ojWHeOAAej43APkeJ5Av6VbTkeoOWR4sdkRc-wyF72HzUB8X",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "fr_CH": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_h3LOcrKZ9mTXxMI9clb2R1VGAWPke6jMNqMw4yYLz4N7PGjYyD0hqRgIFAIHusSn",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "fr_LU": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_zt44Wl_wT9mnqn-BHrR19PvXj3wYRPQKLcPbGWawlatFR837KdxSZZStbBTDaqnb",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "hr_HR": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_HcDC5GGZ89NMP1jORLhYNNCcXt7M3thhZ85eGrcQaM2pRwrgrzcIRWEYi_36cFj9",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "hu_HU": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_nGDWrkSGZovhnVFv5hdIxyuuCuJGZfNmlRGp7-5kEn9yb0bfIfJqoDa2opHOd3Mu",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "it_IT": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_js8th3jdmCWV86fKR3SXQWvXGKbHoWFv8NAgRbH7FnIBsi_XvCpN_rtLcI07uNuq",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "it_CH": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_gHkmHaGACxSLKXqD_uDDx415zdTw7w8HXAFyvh0qIP0WxnHPMF2B9K_nREJVSkGq",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "nl_NL": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_ZIOtjqmP0zaHdEnPK7h1xPuBYgtcOyUxbsTY8Gw31Fzy7i7Ltjfm-hhPh23fpHT5",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "nl_BE": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_yachztWczt6i1pIMhLIH9UA6DXK6vXXuCDmcsoA4PYR0g35RvLPDbp49YribFdpC",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "no_NO": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_QrPkEJr69l7rHkdCVls0owC80BB4CGz5xw_b0gBSNdn3pL04wzMBkcwtbeKdl1g9",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "pl_PL": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_2YBjydYRd1shr6bsZdrvA9z7owvSg3W5RHDYDp6AlatXw9hqx7nVoanRn8YGsBN8",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "pt_PT": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3__afxovspi2-Ip1E5kNsAgc4_35lpLAKCF6bq4_xXj2I2bFPjIWxAOAQJlIkreKTD",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "ro_RO": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_WlBp06vVHuHZhiDLIehF8gchqbfegDJADPQ2MtEsrc8dWVuESf2JCITRo5I2CIxs",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "ru_RU": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_N_ecy4iDyoRtX8v5xOxewwZLKXBjRgrEIv85XxI0KJk8AAdYhJIi17LWb086tGXR",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "sk_SK": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_e8d4g4SE_Fo8ahyHwwP7ohLGZ79HKNN2T8NjQqoNnk6Epj6ilyYwKdHUyCw3wuxz",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "sl_SI": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_QKt0ADYxIhgcje4F3fj9oVidHsx3JIIk-GThhdyMMQi8AJR0QoHdA62YArVjbZCt",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
    "sv_SE": {
        CONF_GIGYA_URL: GIGYA_URL_EU,
        CONF_GIGYA_APIKEY: "3_EN5Hcnwanu9_Dqot1v1Aky1YelT5QqG4TxveO0EgKFWZYu03WkeB9FKuKKIWUXIS",  # noqa
        CONF_KAMEREON_URL: KAMEREON_URL_EU,
        CONF_KAMEREON_APIKEY: KAMEREON_APIKEY,
    },
}
