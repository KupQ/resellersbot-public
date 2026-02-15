"""
Multi-language support for the Telegram bot.
Supported languages: English (en), Russian (ru), Arabic (ar), Indonesian (id).
"""

# ── Custom emoji helpers ─────────────────────────────────────────────────
def _e(eid: str, fallback: str) -> str:
    return f'<tg-emoji emoji-id="{eid}">{fallback}</tg-emoji>'

# Reusable custom emoji snippets
E_BOT      = _e("5458904472598095631", "🤖")
E_MONEY    = _e("5316711376876485361", "💰")
E_CHECK    = _e("5316561083085895267", "✅")
E_ERROR    = _e("5985346521103604145", "❌")
E_SIGNED   = _e("5204403818946640514", "✅")  # green — cert signed
E_REVOKED  = _e("5852753450382659113", "❌")  # red — cert revoked
E_DEVICE   = _e("5931250188239770853", "📱")
E_KEY      = _e("6005570495603282482", "🔑")
E_GEAR     = _e("5408910121264756249", "⚙️")
E_SEARCH   = _e("5874960879434338403", "🔎")
E_CERT     = _e("5899757765743615694", "📜")
E_NEW      = _e("5316702348855227508", "🆕")
E_PACK     = _e("5818920837645867167", "📦")
E_LOCK     = _e("5886505193180239900", "🔐")
E_LANG     = _e("5316832074047441823", "🌐")
E_WAIT     = _e("5316561083085895267", "⏳")
E_NUMS     = _e("5316858509571144216", "🔢")
E_SHIELD   = _e("5877629862306385808", "🛡")

TRANSLATIONS = {
    # ─── Main Menu ────────────────────────────────────────────────────────
    "welcome": {
        "en": f'{E_BOT} <b>Welcome!</b>',
        "ru": f'{E_BOT} <b>Добро пожаловать!</b>',
        "ar": f'{E_BOT} <b>!مرحباً</b>',
        "id": f'{E_BOT} <b>Halo!</b>',
    },
    "welcome_balance": {
        "en": f'{E_BOT} <b>Welcome!</b>\n\n{E_MONEY} Balance: <b>${{balance}}</b>',
        "ru": f'{E_BOT} <b>Добро пожаловать!</b>\n\n{E_MONEY} Баланс: <b>${{balance}}</b>',
        "ar": f'{E_BOT} <b>!مرحباً</b>\n\n{E_MONEY} الرصيد: <b>${{balance}}</b>',
        "id": f'{E_BOT} <b>Halo!</b>\n\n{E_MONEY} Balance: <b>${{balance}}</b>',
    },
    "btn_get_udid": {
        "en": "Register",
        "ru": "Регистрация",
        "ar": "تسجيل",
        "id": "Register",
    },
    "btn_check_udid": {
        "en": "UDID",
        "ru": "UDID",
        "ar": "UDID",
        "id": "UDID",
    },
    "btn_use_key": {
        "en": "Key",
        "ru": "Ключ",
        "ar": "مفتاح",
        "id": "Key",
    },
    "btn_settings": {
        "en": "Settings",
        "ru": "Настройки",
        "ar": "الإعدادات",
        "id": "Pengaturan",
    },

    # ─── UDID ─────────────────────────────────────────────────────────────
    "udid_title": {
        "en": f'{E_DEVICE} <b>Your UDID</b>',
        "ru": f'{E_DEVICE} <b>Ваш UDID</b>',
        "ar": f'{E_DEVICE} <b>UDID الخاص بك</b>',
        "id": f'{E_DEVICE} <b>UDID</b>',
    },
    "udid_hint": {
        "en": "Tap the ID above to copy it.",
        "ru": "Нажмите на ID выше, чтобы скопировать.",
        "ar": "اضغط على المعرّف أعلاه لنسخه.",
        "id": "Tap ID di atas buat copy.",
    },
    "btn_copied": {
        "en": f'{E_CHECK} Copied!',
        "ru": f'{E_CHECK} Скопировано!',
        "ar": f'{E_CHECK} !تم النسخ',
        "id": f'{E_CHECK} Copied!',
    },
    "copied_alert": {
        "en": f'{E_CHECK} UDID shown above — tap to copy!',
        "ru": f'{E_CHECK} UDID показан выше — нажмите, чтобы скопировать!',
        "ar": f'{E_CHECK} UDID معروض أعلاه — اضغط للنسخ!',
        "id": f'{E_CHECK} UDID ada di atas — tap buat copy!',
    },

    # ─── Register ─────────────────────────────────────────────────────────
    "register_udid_prompt": {
        "en": f'{E_DEVICE} <b>Register</b>\n\nSend your UDID to register:',
        "ru": f'{E_DEVICE} <b>Регистрация</b>\n\nОтправьте ваш UDID для регистрации:',
        "ar": f'{E_DEVICE} <b>تسجيل</b>\n\nأرسل UDID الخاص بك للتسجيل:',
        "id": f'{E_DEVICE} <b>Daftar</b>\n\nKirim UDID buat daftar:',
    },
    "register_waiting": {
        "en": f'{E_WAIT} <b>Registering...</b>',
        "ru": f'{E_WAIT} <b>Регистрация...</b>',
        "ar": f'{E_WAIT} <b>جارٍ التسجيل...</b>',
        "id": f'{E_WAIT} <b>Proses daftar...</b>',
    },
    "btn_get_cert": {
        "en": "Get Certificate",
        "ru": "Получить Сертификат",
        "ar": "الحصول على الشهادة",
        "id": "Get Certificate",
    },
    "register_success": {
        "en": f'{E_CHECK} <b>Registered successfully!</b>\n\n{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>\n{E_CERT} <b>Certificate:</b> <code>{{certificate_id}}</code>',
        "ru": f'{E_CHECK} <b>Регистрация успешна!</b>\n\n{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>\n{E_CERT} <b>Сертификат:</b> <code>{{certificate_id}}</code>',
        "ar": f'{E_CHECK} <b>تم التسجيل بنجاح!</b>\n\n{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>\n{E_CERT} <b>الشهادة:</b> <code>{{certificate_id}}</code>',
        "id": f'{E_CHECK} <b>Daftar sukses!</b>\n\n{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>\n{E_CERT} <b>Certificate:</b> <code>{{certificate_id}}</code>',
    },
    "register_error": {
        "en": f'{E_ERROR} Registration failed. Try again later.',
        "ru": f'{E_ERROR} Ошибка регистрации. Попробуйте позже.',
        "ar": f'{E_ERROR} فشل التسجيل. حاول لاحقاً.',
        "id": f'{E_ERROR} Daftar gagal. Coba lagi nanti.',
    },
    "register_error_detail": {
        "en": f'{E_ERROR} Registration failed: {{error}}',
        "ru": f'{E_ERROR} Ошибка регистрации: {{error}}',
        "ar": f'{E_ERROR} فشل التسجيل: {{error}}',
        "id": f'{E_ERROR} Daftar gagal: {{error}}',
    },
    "register_invalid_udid": {
        "en": f'{E_ERROR} Please send a valid UDID.',
        "ru": f'{E_ERROR} Отправьте корректный UDID.',
        "ar": f'{E_ERROR} أرسل UDID صالحاً.',
        "id": f'{E_ERROR} Kirim UDID yang valid.',
    },
    "register_no_api": {
        "en": f'{E_ERROR} API key not configured. Contact admin.',
        "ru": f'{E_ERROR} API ключ не настроен. Обратитесь к администратору.',
        "ar": f'{E_ERROR} مفتاح API غير مُعدّ. تواصل مع المسؤول.',
        "id": f'{E_ERROR} API key belum diset. Hubungi admin.',
    },

    # ─── UDID / Certificate ───────────────────────────────────────────────
    "get_cert_udid_prompt": {
        "en": f'{E_DEVICE} <b>UDID</b>\n\nSend your UDID to view certificates:',
        "ru": f'{E_DEVICE} <b>UDID</b>\n\nОтправьте UDID для просмотра сертификатов:',
        "ar": f'{E_DEVICE} <b>UDID</b>\n\nأرسل UDID لعرض الشهادات:',
        "id": f'{E_DEVICE} <b>UDID</b>\n\nKirim UDID buat liat certificate:',
    },
    "get_cert_found": {
        "en": f'{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>\n\n{E_CERT} Found <b>{{count}}</b> certificate(s). Tap to view:',
        "ru": f'{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>\n\n{E_CERT} Найдено <b>{{count}}</b> сертификат(ов). Нажмите для просмотра:',
        "ar": f'{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>\n\n{E_CERT} تم العثور على <b>{{count}}</b> شهادة(ات). اضغط للعرض:',
        "id": f'{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>\n\n{E_CERT} Ketemu <b>{{count}}</b> certificate. Tap buat liat:',
    },
    "get_cert_not_found": {
        "en": f'{E_ERROR} No certificates found for this UDID.',
        "ru": f'{E_ERROR} Сертификаты для этого UDID не найдены.',
        "ar": f'{E_ERROR} لم يتم العثور على شهادات لهذا UDID.',
        "id": f'{E_ERROR} Gak ada certificate buat UDID ini.',
    },
    "udid_device_info": {
        "en": f'{E_DEVICE} <code>{{udid}}</code>\n{E_PACK} <b>Device:</b> {{device}}',
        "ru": f'{E_DEVICE} <code>{{udid}}</code>\n{E_PACK} <b>Устройство:</b> {{device}}',
        "ar": f'{E_DEVICE} <code>{{udid}}</code>\n{E_PACK} <b>:الجهاز</b> {{device}}',
        "id": f'{E_DEVICE} <code>{{udid}}</code>\n{E_PACK} <b>Device:</b> {{device}}',
    },
    "udid_unknown_device": {
        "en": f'{E_DEVICE} <code>{{udid}}</code>\n{E_ERROR} Unknown device',
        "ru": f'{E_DEVICE} <code>{{udid}}</code>\n{E_ERROR} Неизвестное устройство',
        "ar": f'{E_DEVICE} <code>{{udid}}</code>\n{E_ERROR} جهاز غير معروف',
        "id": f'{E_DEVICE} <code>{{udid}}</code>\n{E_ERROR} Device gak dikenal',
    },
    "udid_invalid": {
        "en": f'{E_ERROR} <code>{{udid}}</code>\n{E_ERROR} <b>Invalid UDID</b>',
        "ru": f'{E_ERROR} <code>{{udid}}</code>\n{E_ERROR} <b>Недействительный UDID</b>',
        "ar": f'{E_ERROR} <code>{{udid}}</code>\n{E_ERROR} <b>UDID غير صالح</b>',
        "id": f'{E_ERROR} <code>{{udid}}</code>\n{E_ERROR} <b>UDID gak valid</b>',
    },
    "cert_not_found": {
        "en": f'{E_ERROR} Certificate data not available.',
        "ru": f'{E_ERROR} Данные сертификата недоступны.',
        "ar": f'{E_ERROR} بيانات الشهادة غير متاحة.',
        "id": f'{E_ERROR} Data certificate gak ada.',
    },
    "signed_apps": {
        "en": f'<b>Following applications have been signed for</b> {E_DEVICE} <code>{{udid}}</code>',
        "ru": f'<b>Следующие приложения подписаны для</b> {E_DEVICE} <code>{{udid}}</code>',
        "ar": f'<b>التطبيقات التالية تم توقيعها لـ</b> {E_DEVICE} <code>{{udid}}</code>',
        "id": f'<b>App berikut udah di-sign buat</b> {E_DEVICE} <code>{{udid}}</code>',
    },
    "signing_apps": {
        "en": f'{E_WAIT} <b>Creating app links...</b>',
        "ru": f'{E_WAIT} <b>Создание ссылок...</b>',
        "ar": f'{E_WAIT} <b>...جاري إنشاء روابط التطبيقات</b>',
        "id": f'{E_WAIT} <b>Lagi bikin link app...</b>',
    },

    # ─── Use Key ──────────────────────────────────────────────────────────
    "use_key_title": {
        "en": f'{E_KEY} <b>Use Key</b>',
        "ru": f'{E_KEY} <b>Использовать ключ</b>',
        "ar": f'{E_KEY} <b>استخدام المفتاح</b>',
        "id": f'{E_KEY} <b>Pake Key</b>',
    },
    "use_key_prompt": {
        "en": "Enter your activation key:",
        "ru": "Введите ваш ключ активации:",
        "ar": "أدخل مفتاح التفعيل:",
        "id": "Masukin activation key:",
    },
    "use_key_result": {
        "en": f'{E_CHECK} <b>Key Activated!</b>\n\nYour key <code>{{key}}</code> has been applied successfully.',
        "ru": f'{E_CHECK} <b>Ключ активирован!</b>\n\nВаш ключ <code>{{key}}</code> успешно применён.',
        "ar": f'{E_CHECK} <b>!تم تفعيل المفتاح</b>\n\nتم تطبيق مفتاحك <code>{{key}}</code> بنجاح.',
        "id": f'{E_CHECK} <b>Key activated!</b>\n\nKey <code>{{key}}</code> berhasil dipake.',
    },
    "use_key_udid_prompt": {
        "en": f'{E_KEY} <b>Key received!</b>\n\nNow enter your device <b>UDID</b> to register:',
        "ru": f'{E_KEY} <b>Ключ получен!</b>\n\nТеперь введите <b>UDID</b> вашего устройства для регистрации:',
        "ar": f'{E_KEY} <b>!تم استلام المفتاح</b>\n\nالآن أدخل <b>UDID</b> جهازك للتسجيل:',
        "id": f'{E_KEY} <b>Key diterima!</b>\n\nSekarang masukin <b>UDID</b> device buat daftar:',
    },
    "use_key_invalid": {
        "en": f'{E_ERROR} <b>Invalid Key!</b>\n\nPlease provide a valid activation key.',
        "ru": f'{E_ERROR} <b>Неверный ключ!</b>\n\nПожалуйста, предоставьте действительный ключ активации.',
        "ar": f'{E_ERROR} <b>!مفتاح غير صالح</b>\n\nيرجى تقديم مفتاح تفعيل صالح.',
        "id": f'{E_ERROR} <b>Key gak valid!</b>\n\nMasukin activation key yang bener.',
    },
    "use_key_error": {
        "en": f'{E_ERROR} <b>Registration Failed!</b>\n\n{{error}}',
        "ru": f'{E_ERROR} <b>Ошибка регистрации!</b>\n\n{{error}}',
        "ar": f'{E_ERROR} <b>!فشل التسجيل</b>\n\n{{error}}',
        "id": f'{E_ERROR} <b>Daftar Gagal!</b>\n\n{{error}}',
    },
    "use_key_not_found": {
        "en": f'{E_ERROR} <b>Key Not Found!</b>',
        "ru": f'{E_ERROR} <b>Ключ не найден!</b>',
        "ar": f'{E_ERROR} <b>!المفتاح غير موجود</b>',
        "id": f'{E_ERROR} <b>Key gak ketemu!</b>',
    },
    "use_key_used": {
        "en": f'{E_ERROR} <b>Key Already Used!</b>',
        "ru": f'{E_ERROR} <b>Ключ уже использован!</b>',
        "ar": f'{E_ERROR} <b>!المفتاح مستخدم بالفعل</b>',
        "id": f'{E_ERROR} <b>Key udah dipake!</b>',
    },

    # ─── Settings ─────────────────────────────────────────────────────────
    "settings_title": {
        "en": f'{E_GEAR} <b>Settings</b>\n\nManage your preferences:',
        "ru": f'{E_GEAR} <b>Настройки</b>\n\nУправляйте предпочтениями:',
        "ar": f'{E_GEAR} <b>الإعدادات</b>\n\nإدارة تفضيلاتك:',
        "id": f'{E_GEAR} <b>Settings</b>\n\nAtur preferensi:',
    },
    "btn_set_api_key": {
        "en": "Set Api Key",
        "ru": "Задать Api Ключ",
        "ar": "تعيين مفتاح API",
        "id": "Set API Key",
    },
    "btn_create_key": {
        "en": "Create Key",
        "ru": "Создать Ключ",
        "ar": "إنشاء مفتاح",
        "id": "Create Key",
    },
    "btn_language": {
        "en": "Language",
        "ru": "Язык",
        "ar": "اللغة",
        "id": "Bahasa",
    },
    "btn_back": {
        "en": "Back",
        "ru": "Назад",
        "ar": "رجوع",
        "id": "Kembali",
    },

    # ─── Check Key ────────────────────────────────────────────────────────
    "btn_check_key": {
        "en": "Check Key",
        "ru": "Проверить Ключ",
        "ar": "فحص المفتاح",
        "id": "Cek Key",
    },
    "check_key_prompt": {
        "en": f'{E_SEARCH} <b>Check Key</b>\n\nSend the key to check:',
        "ru": f'{E_SEARCH} <b>Проверить ключ</b>\n\nОтправьте ключ для проверки:',
        "ar": f'{E_SEARCH} <b>فحص المفتاح</b>\n\nأرسل المفتاح للتحقق:',
        "id": f'{E_SEARCH} <b>Cek Key</b>\n\nKirim key buat di-check:',
    },
    "check_key_not_found": {
        "en": f'{E_ERROR} Key not found.',
        "ru": f'{E_ERROR} Ключ не найден.',
        "ar": f'{E_ERROR} المفتاح غير موجود.',
        "id": f'{E_ERROR} Key gak ketemu.',
    },
    "check_key_error": {
        "en": f'{E_ERROR} Error checking key. Try again later.',
        "ru": f'{E_ERROR} Ошибка при проверке ключа. Попробуйте позже.',
        "ar": f'{E_ERROR} خطأ في فحص المفتاح. حاول لاحقاً.',
        "id": f'{E_ERROR} Error waktu check key. Coba lagi nanti.',
    },
    "check_key_invalid": {
        "en": f'{E_ERROR} Please send a valid key.',
        "ru": f'{E_ERROR} Отправьте корректный ключ.',
        "ar": f'{E_ERROR} أرسل مفتاحاً صالحاً.',
        "id": f'{E_ERROR} Kirim key yang valid.',
    },

    # ─── Set API Key ──────────────────────────────────────────────────────
    "set_api_key_title": {
        "en": f'{E_LOCK} <b>Set API Key</b>',
        "ru": f'{E_LOCK} <b>Задать API ключ</b>',
        "ar": f'{E_LOCK} <b>تعيين مفتاح API</b>',
        "id": f'{E_LOCK} <b>Atur Kunci API</b>',
    },
    "set_api_key_prompt": {
        "en": "Send your API key to save it:",
        "ru": "Отправьте ваш API ключ для сохранения:",
        "ar": "أرسل مفتاح API الخاص بك لحفظه:",
        "id": "Kirim API key buat disimpan:",
    },
    "set_api_key_saved": {
        "en": f'{E_CHECK} <b>API Key Saved!</b>\n\nYour API key has been updated.',
        "ru": f'{E_CHECK} <b>API ключ сохранён!</b>\n\nВаш API ключ обновлён.',
        "ar": f'{E_CHECK} <b>!تم حفظ مفتاح API</b>\n\nتم تحديث مفتاح API الخاص بك.',
        "id": f'{E_CHECK} <b>API Key Disimpan!</b>\n\nAPI key udah di-update.',
    },
    "set_api_key_invalid": {
        "en": f'{E_ERROR} <b>Invalid API Key!</b>\n\nThe API key you provided is not valid. Please check and try again.',
        "ru": f'{E_ERROR} <b>Неверный API ключ!</b>\n\nУказанный API ключ недействителен. Проверьте и попробуйте снова.',
        "ar": f'{E_ERROR} <b>!مفتاح API غير صالح</b>\n\nمفتاح API الذي أدخلته غير صالح. يرجى التحقق والمحاولة مرة أخرى.',
        "id": f'{E_ERROR} <b>API Key Gak Valid!</b>\n\nAPI key yang dimasukin gak valid. Cek lagi dan coba lagi.',
    },

    # ─── Create Key ───────────────────────────────────────────────────────
    "create_key_select_plan": {
        "en": f'{E_NEW} <b>Create Key</b>\n\nSelect a plan to generate keys:',
        "ru": f'{E_NEW} <b>Создать ключ</b>\n\nВыберите план для генерации ключей:',
        "ar": f'{E_NEW} <b>إنشاء مفتاح</b>\n\nاختر باقة لإنشاء المفاتيح:',
        "id": f'{E_NEW} <b>Create Key</b>\n\nPilih plan buat bikin key:',
    },
    "create_key_how_many": {
        "en": f'{E_NUMS} <b>How many keys?</b>\n\nEnter a number (1–100):',
        "ru": f'{E_NUMS} <b>Сколько ключей?</b>\n\nВведите число (1–100):',
        "ar": f'{E_NUMS} <b>كم مفتاح؟</b>\n\nأدخل رقمًا (1–100):',
        "id": f'{E_NUMS} <b>Mau berapa key?</b>\n\nMasukin angka (1–100):',
    },
    "create_key_result": {
        "en": f'{E_NEW} <b>{{count}} Key(s) Created!</b>\n\n{E_PACK} Plan: <b>{{plan}}</b>\n\n{{keys}}',
        "ru": f'{E_NEW} <b>{{count}} ключ(ей) создано!</b>\n\n{E_PACK} План: <b>{{plan}}</b>\n\n{{keys}}',
        "ar": f'{E_NEW} <b>تم إنشاء {{count}} مفتاح!</b>\n\n{E_PACK} الباقة: <b>{{plan}}</b>\n\n{{keys}}',
        "id": f'{E_NEW} <b>{{count}} Key Dibuat!</b>\n\n{E_PACK} Plan: <b>{{plan}}</b>\n\n{{keys}}',
    },
    "create_key_error": {
        "en": f'{E_ERROR} Failed to create keys. Please try again.',
        "ru": f'{E_ERROR} Не удалось создать ключи. Попробуйте снова.',
        "ar": f'{E_ERROR} فشل إنشاء المفاتيح. حاول مرة أخرى.',
        "id": f'{E_ERROR} Gagal bikin key. Coba lagi.',
    },
    "create_key_invalid_count": {
        "en": f'{E_ERROR} Invalid number. Enter a number between 1 and 100.',
        "ru": f'{E_ERROR} Неверное число. Введите число от 1 до 100.',
        "ar": f'{E_ERROR} رقم غير صالح. أدخل رقمًا بين 1 و 100.',
        "id": f'{E_ERROR} Angka gak valid. Masukin angka 1 sampai 100.',
    },
    "create_key_no_api": {
        "en": f'{E_ERROR} No API key set. Please set your API key first in Settings.',
        "ru": f'{E_ERROR} API ключ не задан. Сначала задайте ключ в настройках.',
        "ar": f'{E_ERROR} لم يتم تعيين مفتاح API. يرجى تعيينه أولاً في الإعدادات.',
        "id": f'{E_ERROR} API key belum diset. Set API key dulu di Settings.',
    },

    # ─── Language ─────────────────────────────────────────────────────────
    "lang_title": {
        "en": f'{E_LANG} <b>Select Language</b>',
        "ru": f'{E_LANG} <b>Выберите язык</b>',
        "ar": f'{E_LANG} <b>اختر اللغة</b>',
        "id": f'{E_LANG} <b>Pilih Bahasa</b>',
    },
    "lang_changed": {
        "en": f'{E_CHECK} Language set to English!',
        "ru": f'{E_CHECK} Язык изменён на русский!',
        "ar": f'{E_CHECK} !تم تغيير اللغة إلى العربية',
        "id": f'{E_CHECK} Bahasa diubah ke Indonesia!',
    },

    # ─── Plans ────────────────────────────────────────────────────────────
    "plans_title": {
        "en": f'{E_NEW} <b>Available Plans</b>\n\nSelect a plan:',
        "ru": f'{E_NEW} <b>Доступные планы</b>\n\nВыберите план:',
        "ar": f'{E_NEW} <b>الباقات المتاحة</b>\n\nاختر باقة:',
        "id": f'{E_NEW} <b>Plan Tersedia</b>\n\nPilih plan:',
    },
    "plans_error": {
        "en": f'{E_ERROR} <b>Error</b>\n\nFailed to load plans. Please try again later.',
        "ru": f'{E_ERROR} <b>Ошибка</b>\n\nНе удалось загрузить планы. Попробуйте позже.',
        "ar": f'{E_ERROR} <b>خطأ</b>\n\nفشل تحميل الباقات. حاول مرة أخرى لاحقاً.',
        "id": f'{E_ERROR} <b>Error</b>\n\nGagal muat plan. Coba lagi nanti.',
    },
    "plan_details": {
        "en": f'{E_PACK} <b>{{name}}</b>\n\n{E_MONEY} Cost: <b>${{cost}}</b>\n{E_SHIELD} Warranty: <b>{{warranty}} days</b>',
        "ru": f'{E_PACK} <b>{{name}}</b>\n\n{E_MONEY} Цена: <b>${{cost}}</b>\n{E_SHIELD} Гарантия: <b>{{warranty}} дней</b>',
        "ar": f'{E_PACK} <b>{{name}}</b>\n\n{E_MONEY} السعر: <b>${{cost}}</b>\n{E_SHIELD} الضمان: <b>{{warranty}} يوم</b>',
        "id": f'{E_PACK} <b>{{name}}</b>\n\n{E_MONEY} Harga: <b>${{cost}}</b>\n{E_SHIELD} Garansi: <b>{{warranty}} hari</b>',
    },
    "plan_not_found": {
        "en": f'{E_ERROR} Plan not found.',
        "ru": f'{E_ERROR} План не найден.',
        "ar": f'{E_ERROR} الباقة غير موجودة.',
        "id": f'{E_ERROR} Plan gak ketemu.',
    },

    # ─── Certificate Display ──────────────────────────────────────────────
    "cert_status_signed": {
        "en": f'{_e("5776375003280838798", "📊")} <b>Status:</b> {E_SIGNED} Signed',
        "ru": f'{_e("5776375003280838798", "📊")} <b>Статус:</b> {E_SIGNED} Активный',
        "ar": f'{_e("5776375003280838798", "📊")} <b>:الحالة</b> {E_SIGNED} موقّع',
        "id": f'{_e("5776375003280838798", "📊")} <b>Status:</b> {E_SIGNED} Signed',
    },
    "cert_status_revoked": {
        "en": f'{_e("5776375003280838798", "📊")} <b>Status:</b> {E_REVOKED} Revoked',
        "ru": f'{_e("5776375003280838798", "📊")} <b>Статус:</b> {E_REVOKED} Отозван',
        "ar": f'{_e("5776375003280838798", "📊")} <b>:الحالة</b> {E_REVOKED} ملغى',
        "id": f'{_e("5776375003280838798", "📊")} <b>Status:</b> {E_REVOKED} Revoked',
    },
    "cert_id_label": {
        "en": f'{E_CERT} <b>Certificate ID:</b> <code>{{id}}</code>',
        "ru": f'{E_CERT} <b>ID сертификата:</b> <code>{{id}}</code>',
        "ar": f'{E_CERT} <b>:معرّف الشهادة</b> <code>{{id}}</code>',
        "id": f'{E_CERT} <b>Certificate ID:</b> <code>{{id}}</code>',
    },
    "cert_udid_label": {
        "en": f'{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>',
        "ru": f'{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>',
        "ar": f'{E_DEVICE} <b>:UDID</b> <code>{{udid}}</code>',
        "id": f'{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>',
    },
    "cert_device_label": {
        "en": f'{E_PACK} <b>Device:</b> {{device}}',
        "ru": f'{E_PACK} <b>Устройство:</b> {{device}}',
        "ar": f'{E_PACK} <b>:الجهاز</b> {{device}}',
        "id": f'{E_PACK} <b>Device:</b> {{device}}',
    },
    "cert_name_label": {
        "en": f'{_e("5316992572680320646", "👤")} <b>Name:</b> {{name}}',
        "ru": f'{_e("5316992572680320646", "👤")} <b>Имя:</b> {{name}}',
        "ar": f'{_e("5316992572680320646", "👤")} <b>:الاسم</b> {{name}}',
        "id": f'{_e("5316992572680320646", "👤")} <b>Nama:</b> {{name}}',
    },
    "cert_warranty_label": {
        "en": f'{_e("5316575093269214796", "⏰")} <b>Warranty:</b> {{remaining}}',
        "ru": f'{_e("5316575093269214796", "⏰")} <b>Гарантия:</b> {{remaining}}',
        "ar": f'{_e("5316575093269214796", "⏰")} <b>:الضمان</b> {{remaining}}',
        "id": f'{_e("5316575093269214796", "⏰")} <b>Garansi:</b> {{remaining}}',
    },
    "cert_registered_at": {
        "en": f'{_e("5967412305338568701", "📅")} <b>Registered:</b> {{date}}',
        "ru": f'{_e("5967412305338568701", "📅")} <b>Зарегистрирован:</b> {{date}}',
        "ar": f'{_e("5967412305338568701", "📅")} <b>:تاريخ التسجيل</b> {{date}}',
        "id": f'{_e("5967412305338568701", "📅")} <b>Terdaftar:</b> {{date}}',
    },
    "cert_expired": {
        "en": "Expired",
        "ru": "Истекла",
        "ar": "منتهي",
        "id": "Kedaluwarsa",
    },
    "cert_time_left": {
        "en": "left",
        "ru": "осталось",
        "ar": "متبقي",
        "id": "tersisa",
    },
    "cert_password_label": {
        "en": f'{_e("5316858509571144216", "🔐")} <b>Password:</b> <code>{{password}}</code>',
        "ru": f'{_e("5316858509571144216", "🔐")} <b>Пароль:</b> <code>{{password}}</code>',
        "ar": f'{_e("5316858509571144216", "🔐")} <b>:كلمة المرور</b> <code>{{password}}</code>',
        "id": f'{_e("5316858509571144216", "🔐")} <b>Password:</b> <code>{{password}}</code>',
    },
    "cert_rate_limit": {
        "en": "Please wait {seconds}s before requesting again.",
        "ru": "Подождите {seconds}с перед повторным запросом.",
        "ar": ".يرجى الانتظار {seconds} ثانية قبل الطلب مرة أخرى",
        "id": "Tunggu {seconds} detik sebelum request lagi.",
    },
    "cert_loading": {
        "en": "Loading certificate...",
        "ru": "Загрузка сертификата...",
        "ar": "...جارٍ تحميل الشهادة",
        "id": "Memuat certificate...",
    },
    "cert_no_files": {
        "en": f'{E_ERROR} No certificate files available.',
        "ru": f'{E_ERROR} Файлы сертификата недоступны.',
        "ar": f'{E_ERROR} .لا توجد ملفات شهادة متاحة',
        "id": f'{E_ERROR} Gak ada file certificate.',
    },
    "install_link": {
        "en": '📲 <b>Install Link:</b>\n{url}',
        "ru": '📲 <b>Ссылка для установки:</b>\n{url}',
        "ar": '📲 <b>:رابط التثبيت</b>\n{url}',
        "id": '📲 <b>Install Link:</b>\n{url}',
    },
    "install_expired": {
        "en": "Install link expired",
        "ru": "Ссылка установки истекла",
        "ar": "انتهت صلاحية رابط التثبيت",
        "id": "Install link expired",
    },
    "admin_only": {
        "en": "Admin only",
        "ru": "Только для администратора",
        "ar": "للمسؤول فقط",
        "id": "Admin only",
    },

    # ─── Key Info Display ─────────────────────────────────────────────────
    "key_status_used": {
        "en": f'{_e("5852753450382659113", "❌")} Used',
        "ru": f'{_e("5852753450382659113", "❌")} Использован',
        "ar": f'{_e("5852753450382659113", "❌")} مستخدم',
        "id": f'{_e("5852753450382659113", "❌")} Used',
    },
    "key_status_active": {
        "en": f'{E_CHECK} Active',
        "ru": f'{E_CHECK} Активный',
        "ar": f'{E_CHECK} نشط',
        "id": f'{E_CHECK} Aktif',
    },
    "key_info_key": {
        "en": f'{E_KEY} <b>Key:</b> <code>{{key}}</code>',
        "ru": f'{E_KEY} <b>Ключ:</b> <code>{{key}}</code>',
        "ar": f'{E_KEY} <b>:المفتاح</b> <code>{{key}}</code>',
        "id": f'{E_KEY} <b>Key:</b> <code>{{key}}</code>',
    },
    "key_info_status": {
        "en": f'{_e("5776375003280838798", "📊")} <b>Status:</b> {{status}}',
        "ru": f'{_e("5776375003280838798", "📊")} <b>Статус:</b> {{status}}',
        "ar": f'{_e("5776375003280838798", "📊")} <b>:الحالة</b> {{status}}',
        "id": f'{_e("5776375003280838798", "📊")} <b>Status:</b> {{status}}',
    },
    "key_info_plan": {
        "en": f'{E_PACK} <b>Plan:</b> {{plan}}',
        "ru": f'{E_PACK} <b>План:</b> {{plan}}',
        "ar": f'{E_PACK} <b>:الباقة</b> {{plan}}',
        "id": f'{E_PACK} <b>Plan:</b> {{plan}}',
    },
    "key_info_created": {
        "en": f'{_e("5316591603123502631", "📅")} <b>Created:</b> {{date}}',
        "ru": f'{_e("5316591603123502631", "📅")} <b>Создан:</b> {{date}}',
        "ar": f'{_e("5316591603123502631", "📅")} <b>:تاريخ الإنشاء</b> {{date}}',
        "id": f'{_e("5316591603123502631", "📅")} <b>Dibuat:</b> {{date}}',
    },
    "key_info_claimed_by": {
        "en": f'{_e("5316992572680320646", "👤")} <b>Claimed by:</b> <code>{{user}}</code>',
        "ru": f'{_e("5316992572680320646", "👤")} <b>Получен:</b> <code>{{user}}</code>',
        "ar": f'{_e("5316992572680320646", "👤")} <b>:تم المطالبة بواسطة</b> <code>{{user}}</code>',
        "id": f'{_e("5316992572680320646", "👤")} <b>Claimed by:</b> <code>{{user}}</code>',
    },
    "key_info_udid": {
        "en": f'{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>',
        "ru": f'{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>',
        "ar": f'{E_DEVICE} <b>:UDID</b> <code>{{udid}}</code>',
        "id": f'{E_DEVICE} <b>UDID:</b> <code>{{udid}}</code>',
    },
    "key_info_claimed_at": {
        "en": f'{_e("5776213190387961618", "📅")} <b>Claimed at:</b> {{date}}',
        "ru": f'{_e("5776213190387961618", "📅")} <b>Получен:</b> {{date}}',
        "ar": f'{_e("5776213190387961618", "📅")} <b>:تاريخ المطالبة</b> {{date}}',
        "id": f'{_e("5776213190387961618", "📅")} <b>Claimed at:</b> {{date}}',
    },

    # ─── Settings Descriptions ────────────────────────────────────────────
    "settings_header": {
        "en": f'{_e("5316832430529722441", "⚙️")} <b>Settings:</b>',
        "ru": f'{_e("5316832430529722441", "⚙️")} <b>Настройки:</b>',
        "ar": f'{_e("5316832430529722441", "⚙️")} <b>:الإعدادات</b>',
        "id": f'{_e("5316832430529722441", "⚙️")} <b>Settings:</b>',
    },
    "settings_desc_api_key": {
        "en": f'━ {_e("5886505193180239900", "🔑")} Set up API key',
        "ru": f'━ {_e("5886505193180239900", "🔑")} Настроить API ключ',
        "ar": f'━ {_e("5886505193180239900", "🔑")} إعداد مفتاح API',
        "id": f'━ {_e("5886505193180239900", "🔑")} Set API key',
    },
    "settings_desc_create_key": {
        "en": f'━ {_e("5886505193180239900", "🔐")} Generate Keys 1-100',
        "ru": f'━ {_e("5886505193180239900", "🔐")} Создать ключи 1-100',
        "ar": f'━ {_e("5886505193180239900", "🔐")} إنشاء مفاتيح 1-100',
        "id": f'━ {_e("5886505193180239900", "🔐")} Generate Key 1-100',
    },
    "settings_desc_check_key": {
        "en": f'━ {E_KEY} Validate Keys 1-10',
        "ru": f'━ {E_KEY} Проверить ключи 1-10',
        "ar": f'━ {E_KEY} التحقق من المفاتيح 1-10',
        "id": f'━ {E_KEY} Validate Key 1-10',
    },
    "settings_desc_thumbnail": {
        "en": f'━ {_e("5931629923478278721", "🖼")} Set Thumbnail',
        "ru": f'━ {_e("5931629923478278721", "🖼")} Установить миниатюру',
        "ar": f'━ {_e("5931629923478278721", "🖼")} تعيين الصورة المصغرة',
        "id": f'━ {_e("5931629923478278721", "🖼")} Set Thumbnail',
    },
    "settings_desc_instruction": {
        "en": f'━ {_e("5906995262378741881", "📋")} Set Instructions link',
        "ru": f'━ {_e("5906995262378741881", "📋")} Ссылка на инструкцию',
        "ar": f'━ {_e("5906995262378741881", "📋")} رابط التعليمات',
        "id": f'━ {_e("5906995262378741881", "📋")} Link Instruksi',
    },
    "btn_set_instruction": {
        "en": "Instructions",
        "ru": "Инструкция",
        "ar": "التعليمات",
        "id": "Instruksi",
    },
    "btn_instructions": {
        "en": "Instructions",
        "ru": "Инструкция",
        "ar": "التعليمات",
        "id": "Instruksi",
    },
    "set_instruction_title": {
        "en": f'{_e("5906995262378741881", "📋")} <b>Set Instructions URL</b>',
        "ru": f'{_e("5906995262378741881", "📋")} <b>Ссылка на инструкцию</b>',
        "ar": f'{_e("5906995262378741881", "📋")} <b>رابط التعليمات</b>',
        "id": f'{_e("5906995262378741881", "📋")} <b>Link Instruksi</b>',
    },
    "set_instruction_prompt": {
        "en": "Send a valid URL (e.g. https://t.me/yourchannel)",
        "ru": "Отправьте ссылку (напр. https://t.me/yourchannel)",
        "ar": "(https://t.me/yourchannel :أرسل رابطًا صالحًا (مثال",
        "id": "Kirim URL yang valid (misal https://t.me/yourchannel)",
    },
    "set_instruction_saved": {
        "en": f'{E_CHECK} Instructions URL saved!',
        "ru": f'{E_CHECK} Ссылка на инструкцию сохранена!',
        "ar": f'{E_CHECK} !تم حفظ رابط التعليمات',
        "id": f'{E_CHECK} Link instruksi tersimpan!',
    },
    "set_instruction_invalid": {
        "en": f'{E_ERROR} Invalid URL. Must start with http:// or https://',
        "ru": f'{E_ERROR} Неверная ссылка. Должна начинаться с http:// или https://',
        "ar": f'{E_ERROR} https:// أو http:// رابط غير صالح. يجب أن يبدأ بـ',
        "id": f'{E_ERROR} URL tidak valid. Harus dimulai dengan http:// atau https://',
    },
    "settings_desc_language": {
        "en": f'━ {E_LANG} Change bot language',
        "ru": f'━ {E_LANG} Изменить язык бота',
        "ar": f'━ {E_LANG} تغيير لغة البوت',
        "id": f'━ {E_LANG} Ganti bahasa bot',
    },
    "btn_set_thumbnail": {
        "en": "Set Thumbnail",
        "ru": "Миниатюра",
        "ar": "الصورة المصغرة",
        "id": "Set Thumbnail",
    },

    # ─── Thumbnail Steps ──────────────────────────────────────────────────
    "thumb_step_1": {
        "en": f'{_e("5931629923478278721", "🖼")} <b>Set Thumbnail (1/4)</b>\n\nSend a photo for <b>.p12</b> files:',
        "ru": f'{_e("5931629923478278721", "🖼")} <b>Миниатюра (1/4)</b>\n\nОтправьте фото для файлов <b>.p12</b>:',
        "ar": f'{_e("5931629923478278721", "🖼")} <b>(1/4) تعيين الصورة المصغرة</b>\n\nأرسل صورة لملفات <b>.p12</b>:',
        "id": f'{_e("5931629923478278721", "🖼")} <b>Set Thumbnail (1/4)</b>\n\nKirim foto buat file <b>.p12</b>:',
    },
    "thumb_step_2": {
        "en": f'{_e("5931629923478278721", "🖼")} <b>Set Thumbnail (2/4)</b>\n\nSend a photo for <b>.mobileprovision</b> files:',
        "ru": f'{_e("5931629923478278721", "🖼")} <b>Миниатюра (2/4)</b>\n\nОтправьте фото для файлов <b>.mobileprovision</b>:',
        "ar": f'{_e("5931629923478278721", "🖼")} <b>(2/4) تعيين الصورة المصغرة</b>\n\nأرسل صورة لملفات <b>.mobileprovision</b>:',
        "id": f'{_e("5931629923478278721", "🖼")} <b>Set Thumbnail (2/4)</b>\n\nKirim foto buat file <b>.mobileprovision</b>:',
    },
    "thumb_step_3": {
        "en": f'{_e("5931629923478278721", "🖼")} <b>Set Thumbnail (3/4)</b>\n\nSend a photo for <b>dev .p12</b> files:',
        "ru": f'{_e("5931629923478278721", "🖼")} <b>Миниатюра (3/4)</b>\n\nОтправьте фото для файлов <b>dev .p12</b>:',
        "ar": f'{_e("5931629923478278721", "🖼")} <b>(3/4) تعيين الصورة المصغرة</b>\n\nأرسل صورة لملفات <b>dev .p12</b>:',
        "id": f'{_e("5931629923478278721", "🖼")} <b>Set Thumbnail (3/4)</b>\n\nKirim foto buat file <b>dev .p12</b>:',
    },
    "thumb_step_4": {
        "en": f'{_e("5931629923478278721", "🖼")} <b>Set Thumbnail (4/4)</b>\n\nSend a photo for <b>dev .mobileprovision</b> files:',
        "ru": f'{_e("5931629923478278721", "🖼")} <b>Миниатюра (4/4)</b>\n\nОтправьте фото для файлов <b>dev .mobileprovision</b>:',
        "ar": f'{_e("5931629923478278721", "🖼")} <b>(4/4) تعيين الصورة المصغرة</b>\n\nأرسل صورة لملفات <b>dev .mobileprovision</b>:',
        "id": f'{_e("5931629923478278721", "🖼")} <b>Set Thumbnail (4/4)</b>\n\nKirim foto buat file <b>dev .mobileprovision</b>:',
    },
    "thumb_done": {
        "en": f'{E_CHECK} <b>All 4 thumbnails saved!</b>',
        "ru": f'{E_CHECK} <b>Все 4 миниатюры сохранены!</b>',
        "ar": f'{E_CHECK} <b>!تم حفظ جميع الصور المصغرة الأربع</b>',
        "id": f'{E_CHECK} <b>Semua 4 thumbnail tersimpan!</b>',
    },
    "thumb_cleared": {
        "en": f'{E_CHECK} <b>Thumbnails cleared!</b>',
        "ru": f'{E_CHECK} <b>Миниатюры очищены!</b>',
        "ar": f'{E_CHECK} <b>!تم مسح الصور المصغرة</b>',
        "id": f'{E_CHECK} <b>Thumbnail terhapus!</b>',
    },
    # ─── Re-register ─────────────────────────────────────────────────────
    "btn_reregister": {
        "en": "Re-register",
        "ru": "Перерегистрация",
        "ar": "إعادة التسجيل",
        "id": "Daftar Ulang",
    },
    "reregister_waiting": {
        "en": f'{E_WAIT} <b>Re-registering…</b>',
        "ru": f'{E_WAIT} <b>Перерегистрация…</b>',
        "ar": f'{E_WAIT} <b>…جاري إعادة التسجيل</b>',
        "id": f'{E_WAIT} <b>Daftar ulang…</b>',
    },
    "reregister_success": {
        "en": f'{E_CHECK} <b>Re-registered successfully!</b>',
        "ru": f'{E_CHECK} <b>Перерегистрация прошла успешно!</b>',
        "ar": f'{E_CHECK} <b>!تمت إعادة التسجيل بنجاح</b>',
        "id": f'{E_CHECK} <b>Sukses daftar ulang!</b>',
    },
    "reregister_error": {
        "en": f'{E_ERROR} <b>Re-registration failed.</b>',
        "ru": f'{E_ERROR} <b>Ошибка перерегистрации.</b>',
        "ar": f'{E_ERROR} <b>.فشل إعادة التسجيل</b>',
        "id": f'{E_ERROR} <b>Gagal daftar ulang.</b>',
    },
    "popup_already_reregistered": {
        "en": "Already re-registered!",
        "ru": "Уже перерегистрировано!",
        "ar": "!تمت إعادة التسجيل بالفعل",
        "id": "Udah daftar ulang!",
    },

    # ─── List UDIDs ──────────────────────────────────────────────────────
    "list_loading": {
        "en": f'{E_WAIT} <b>Fetching certificates…</b>',
        "ru": f'{E_WAIT} <b>Загрузка сертификатов…</b>',
        "ar": f'{E_WAIT} <b>…جارٍ تحميل الشهادات</b>',
        "id": f'{E_WAIT} <b>Memuat certificate…</b>',
    },
    "list_checking": {
        "en": f'{E_WAIT} <b>Checking {"{count}"} UDIDs…</b>',
        "ru": f'{E_WAIT} <b>Проверка {"{count}"} UDID…</b>',
        "ar": f'{E_WAIT} <b>…{"{count}"} UDID جارٍ فحص</b>',
        "id": f'{E_WAIT} <b>Cek {"{count}"} UDID…</b>',
    },
    "list_done": {
        "en": f'{E_CHECK} <b>UDID Export</b>\n\n{E_DEVICE} Total: <b>{"{total}"}</b>\n{E_SIGNED} Signed: <b>{"{signed}"}</b>\n{E_REVOKED} Revoked: <b>{"{revoked}"}</b>',
        "ru": f'{E_CHECK} <b>Экспорт UDID</b>\n\n{E_DEVICE} Всего: <b>{"{total}"}</b>\n{E_SIGNED} Подписано: <b>{"{signed}"}</b>\n{E_REVOKED} Отозвано: <b>{"{revoked}"}</b>',
        "ar": f'{E_CHECK} <b>تصدير UDID</b>\n\n{E_DEVICE} المجموع: <b>{"{total}"}</b>\n{E_SIGNED} موقّع: <b>{"{signed}"}</b>\n{E_REVOKED} ملغى: <b>{"{revoked}"}</b>',
        "id": f'{E_CHECK} <b>Ekspor UDID</b>\n\n{E_DEVICE} Total: <b>{"{total}"}</b>\n{E_SIGNED} Signed: <b>{"{signed}"}</b>\n{E_REVOKED} Revoked: <b>{"{revoked}"}</b>',
    },
    "list_empty": {
        "en": f'{E_ERROR} No registered UDIDs found.',
        "ru": f'{E_ERROR} Зарегистрированные UDID не найдены.',
        "ar": f'{E_ERROR} لا توجد أجهزة UDID مسجّلة.',
        "id": f'{E_ERROR} Gak ada UDID terdaftar.',
    },
    "list_error": {
        "en": f'{E_ERROR} Failed to fetch certificates. Try again later.',
        "ru": f'{E_ERROR} Не удалось загрузить сертификаты. Попробуйте позже.',
        "ar": f'{E_ERROR} فشل تحميل الشهادات. حاول لاحقاً.',
        "id": f'{E_ERROR} Gagal muat certificate. Coba lagi nanti.',
    },
}

# In-memory user language preferences  {user_id: "en"|"ru"|"ar"}
_user_langs: dict[int, str] = {}

DEFAULT_LANG = "en"


def t(key: str, lang: str | None = None) -> str:
    """Get translated string by key and language code."""
    lang = lang or DEFAULT_LANG
    entry = TRANSLATIONS.get(key, {})
    return entry.get(lang, entry.get(DEFAULT_LANG, key))


def get_lang(user_id: int) -> str:
    """Get language preference for a user."""
    return _user_langs.get(user_id, DEFAULT_LANG)


def set_lang(user_id: int, lang: str) -> None:
    """Set language preference for a user."""
    if lang in ("en", "ru", "ar", "id"):
        _user_langs[user_id] = lang
