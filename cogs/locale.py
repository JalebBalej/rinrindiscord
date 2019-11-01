def get_locale(lang, key):
    lang = lang.lower()
    key = key.lower()
    text = locale.get(key, {lang: "Error! Key not found."}).get(lang, None)
    if not text:
        text = locale.get(key, {"en": "Error! Key not found."}).get("en", "Error! Language not found")
    return text



locale = {
    "command_not_found": {
        "en": "Command not found! Check to see if it was a typo!",
        "ru": "Команда не найдена! Проверьте, может это опечатка!",
        "lt": "Komanda nerasta! Patikrinkite ar tai buvo rašybos klaida!"
    },
    "help_command_title": {
        "en": "Help",
        "ru": "Помощь",
        "lt": "Pagalba"
    },
    "help_command_help": {
        "en": "Shows this message",
        "ru": "Показать это сообщение.",
        "lt": "Parodo šitą žinutę"
    },
    "startnumber": {
        "en": "startnumber",
        "ru": "старт",
        "lt": "pradinisnumeris"
    },
    "endnumber": {
        "en": "endnumber",
        "ru": "стоп",
        "lt": "paskutinisnumeris"
    },
    "help_command_rn": {
        "en": "Gets a random number from start to end.",
        "ru": "Получить случайное число от старт до стоп.",
        "lt": "Parodo generuotą numerį nuo pirmo iki paskutinio skaičiaus."
    },
    "help_command_match": {
        "en": "Calculates compatibility with name and partner.",
        "ru": "Посчитать совместимость имени и партнера.",
        "lt": "Suskaičiuoja kiek vardas ir partneris tinka."
    },
    "help_command_ping": {
        "en": "Shows my ping!",
        "ru": "Показать мой пинг!",
        "lt": "Parodo mano pingą!"
    },
    "help_command_info": {
        "en": "Shows bot info!",
        "ru": "Показать информацию о боте!",
        "lt": "Parodo boto informaciją!"
    },
    "help_command_lang": {
        "en": "Changes bot's language!",
        "ru": "Сменить язык бота!",
        "lt": "Pakeita bot'o kalba!"
    },
    "help_command_credits": {
        "en": "Shows credits!",
        "ru": "Показать авторов!", # Translation probably isn't correct
        "lt": "Parodo kreditus!"
    },
    "bot_developer": {
        "en": "Bot Developer",
        "ru": "Разработчик",
        "lt": "Bot'o Kūrėjas"
    },
    "bot_assistant_developer": {
        "en": "Bot Assistant Developer",
        "ru": "Помощник разработчика",
        "lt": "Antras bot'o kūrėjas"
    },
    "russian_translation": {
        "en": "Russian Translation",
        "ru": "Переводчик на Русский",
        "lt": "Rusų vertėjas"
    },
    "lithuanian_translation": {
        "en": "Lithuanian Translation",
        "ru": "Переводчик на Литовский",
        "lt": "Lietuvių vertėjas"
    },
    "lithuanian_quality_check": {
        "en": "Lithuanian Translation Quality Checker",
        "ru": "Проверил качество перевода на Литовский язык",
        "lt": "Lietuviško Vertėjo Kokybės Prižiūrėtojas"
    },
    "lang_response": {
        "en": "Your current language is **English**!",
        "ru": "Ваш текущий язык **Русский**!",
        "lt": "Tavo dabartinė kalba yra **Lietuvių**!"
    },
    "credits_command_title": {
        "en": "Credits",
        "ru": "Авторы", # Translation probably isn't correct
        "lt": "Kreditai"
    },
    "error_no_permission": {
        "en": "You do not have permission to use this command!",
        "ru": None,
        "lt": None
    },
    "info_command_title": {
        "en": "Info",
        "ru": None,
        "lt": None
    },
    "bot_author": {
        "en": "Bot Author",
        "ru": None,
        "lt": None
    },
    "bot_version": {
        "en": "Bot Version",
        "ru": None,
        "lt": None
    },
    "github_link": {
        "en": "Github Link",
        "ru": None,
        "lt": None
    },
    "ping_command": {
        "en": "Bot Latency is",
        "ru": None,
        "lt": None
    },
    "random_number_command": {
        "en": "Your random number",
        "ru": None,
        "lt": None
    },
    "random_number_error": {
        "en": "You need to enter two numbers!",
        "ru": None,
        "lt": None
    },
    "match_command_compis": {
        "en": "Compatibility is",
        "ru": None,
        "lt": None
    },
    "match_command_100comp": {
        "en": "Congratulations on getting 100% compatibility",
        "ru": None,
        "lt": None
    },
    "and": {
        "en": "and",
        "ru": None,
        "lt": None
    },
    "match_command_error": {
        "en": "Don't forget to specify two names!",
        "ru": None,
        "lt": None
    },
    "match_command_gl": {
        "en": "Better luck next time!",
        "ru": None,
        "lt": None
    }
}
