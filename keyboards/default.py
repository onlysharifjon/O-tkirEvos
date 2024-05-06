from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tel_raqam_uchun = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('📲Telefon raqamini yuborish', request_contact=True)
        ],

    ],
    resize_keyboard=True
)

asosiy_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🍴 Menyu")
        ],
        [
            KeyboardButton('📋 Mening buyurtmalarim')
        ],
        [
            KeyboardButton('📥 Savat'),
            KeyboardButton('📞 Aloqa')
        ],
        [
            KeyboardButton("📨 Xabar yuborish"),
            KeyboardButton("⚙️ Sozlamalar")
        ],
        [
            KeyboardButton("ℹ️ Biz haqimizda")
        ]
    ], resize_keyboard=True
)
menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Setlar (8)")

        ],
        [
            KeyboardButton("Lavash (9)"),
            KeyboardButton("Shaurma (4)")

        ],
        [
            KeyboardButton("Burger (4)"),
            KeyboardButton("Hot-Dog (8)")
        ],
        [
            KeyboardButton("Ichimliklar (11)")

        ],
        [

            KeyboardButton("Shirinlik va disertlar (4)")
        ],
        [
            KeyboardButton("Garnirlar (10)")
        ],
        [
            KeyboardButton("Ortga qaytish 🔙")
        ]

    ],
    resize_keyboard=True
)

setlar_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Combo Plus Isituvchan (Qora choy)"),
            KeyboardButton("FitCombo"),
        ],
        [
            KeyboardButton("Iftar kofte grill mol go'shtidan"),
            KeyboardButton("Donar boks  mol go'shtidan")

        ],
        [
            KeyboardButton("Donar boks tovuq go'shtidan"),
            KeyboardButton("COMBO+")
        ],
        [
            KeyboardButton("Iftar strips tovuq go'shtidan"),
            KeyboardButton("Kids COMBO")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish")
        ]
    ],
    resize_keyboard=True
)

lavash_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Mol goʼshtidan qalampir lavash"),
            KeyboardButton("Tovuq goʼshtli qalampir lavash")
        ],
        [
            KeyboardButton("Mol goʼshtidan pishloqli lavash Standard"),
            KeyboardButton("Lavash cheese tovuq go'sht Standart")
        ],
        [
            KeyboardButton("FITTER"),
            KeyboardButton("Lavash tovuq go'sht")
        ],
        [
            KeyboardButton("Lavash mol go'sht")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish")
        ]
        ],
    resize_keyboard=True
)

shaurma_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Shaurma qalampir mol go'sht"),
            KeyboardButton("Shaurma tovuq go'sht")
        ],
        [
            KeyboardButton("Shaurma qalampir tovuq go'sht"),
            KeyboardButton("Shaurma mol go'sht")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish")
        ]
    ],
    resize_keyboard=True
)

burger_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Gamburger"),
            KeyboardButton("Double burger")
        ],
        [
            KeyboardButton("Cheese burger"),
            KeyboardButton("Double cheese")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish"),
        ]

    ],
    resize_keyboard=True
)

hot_dog_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Hot-dog baguette"),
            KeyboardButton("Sub tovuq cheese")
        ],
        [
            KeyboardButton("Sub tovuq"),
            KeyboardButton("Hot-dog baguette double")
        ],
        [
            KeyboardButton('Hot-dog kids'),
            KeyboardButton("Sub go'sht cheese")
        ],
        [
            KeyboardButton("Hot-dog classic"),
            KeyboardButton("Sub go'sht")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish"),
        ]
    ],
    resize_keyboard=True
)
ichimliklar_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Sok dena 0,33l"),
            KeyboardButton("Suv 0,5")
        ],
        [
            KeyboardButton("Pepsi 0,5"),
            KeyboardButton("Pepsi 1,5")
        ],
        [
            KeyboardButton("Quyib beriladigan Pepsi"),
            KeyboardButton("Bliss sharbati")
        ],
        [
            KeyboardButton("Amerikano"),
            KeyboardButton("Latte")
        ],
        [
            KeyboardButton("Ko'k choy"),
            KeyboardButton("Qora choy")
        ],
        [
            KeyboardButton("Limonli ko'k choy")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish")
        ]
    ],
    resize_keyboard=True
)

shirinliklar_va_desertlar_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Medovik Asalim"),
            KeyboardButton("Chizkeyk")
        ],
        [
            KeyboardButton("Donut karameli"),
            KeyboardButton("Donut mevali")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish")
        ]
    ],
    resize_keyboard=True
)

garnirlar_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ketchup"),
            KeyboardButton("Guruch")
        ],
        [
            KeyboardButton("Po-derevenski"),
            KeyboardButton("Sarimsoqli qayla")
        ],
        [
            KeyboardButton("Chili qaylasi"),
            KeyboardButton("Mayonez")
        ],
        [
            KeyboardButton("Salat"),
            KeyboardButton("Guruch")
        ],
        [
            KeyboardButton("Ketchup"),
            KeyboardButton("Sir qaylasi")
        ],
        [
            KeyboardButton("Tovuq Strips"),
            KeyboardButton("Fri")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish")
        ]
    ],
    resize_keyboard=True
)