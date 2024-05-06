from aiogram import executor, Bot, Dispatcher, types
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import state

from statates import EvosStates
from keyboards.default import *
from database import mashulot_ombori
from aiogram.dispatcher import FSMContext

API_TOKEN = "6597297326:AAENgyOMwxllHeuLmG_SVMgoHZz5KuakF1k"
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start',state='*')
async def start_uchun(message: types.Message,state: FSMContext):
    await message.answer('<b>EVOS | Доставка</b> botiga xush kelibsiz!')
    await message.answer('''
Avval telefon raqamingizni yuboring,
yoki +998XX XXXXXXX ko'rinishida yozing.

https://evos.uz/uz/about/
''', reply_markup=tel_raqam_uchun)
    await state.finish()


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def asosiy_menyu_state(message: types.Message):
    await message.answer('Assosiya menyu', reply_markup=asosiy_menyu)


@dp.message_handler(text="🍴 Menyu")
async def birinchi_menyu(message: types.Message):
    await message.answer("Menyu", reply_markup=menyu)


@dp.message_handler(text='Setlar (8)')
async def setlama(message: types.Message):
    await message.answer('Setlar', reply_markup=setlar_menyu)
    await EvosStates.mahsulot_xonasi.set()


@dp.message_handler(text='Lavash (9)')
async def lavash(message: types.Message):
    await message.answer('Lavash', reply_markup=lavash_menyu)
    await EvosStates.mahsulot_xonasi.set()


@dp.message_handler(text='Shaurma (4)')
async def Shaurma(message: types.Message):
    await message.answer('Shaurma', reply_markup=shaurma_menyu)
    await EvosStates.mahsulot_xonasi.set()


@dp.message_handler(text="Burger (4)")
async def Burger(message: types.Message):
    await message.answer('Burger', reply_markup=burger_menyu)
    await EvosStates.mahsulot_xonasi.set()


@dp.message_handler(text="Hot-Dog (8)")
async def HotDog(message: types.Message):
    await message.answer('Hot-Dog', reply_markup=hot_dog_menyu)
    await EvosStates.mahsulot_xonasi.set()


@dp.message_handler(text="Ichimliklar (11)")
async def Ichimliklar(message: types.Message):
    await message.answer('Ichimliklar', reply_markup=ichimliklar_menyu)
    await EvosStates.mahsulot_xonasi.set()


@dp.message_handler(text="Shirinlik va disertlar (4)")
async def Shirinlik(message: types.Message):
    await message.answer('shirinliklar', reply_markup=shirinliklar_va_desertlar_menyu)
    await EvosStates.mahsulot_xonasi.set()


@dp.message_handler(text="Garnirlar (10)")
async def garnirlar(message: types.Message):
    await message.answer('garnirlar', reply_markup=garnirlar_menyu)
    await EvosStates.mahsulot_xonasi.set()


@dp.message_handler(text='Ortga qaytish 🔙', state='*')
async def qaytish(message: types.Message):
    print(True)
    await message.answer('orqaga qaytish', reply_markup=asosiy_menyu)


@dp.message_handler(text='🔙 Ortga qaytish', state='*')
async def qaytish(message: types.Message):
    print(False)
    await message.answer('orqaga qaytish', reply_markup=menyu)


@dp.message_handler(state=EvosStates.mahsulot_xonasi)
async def mashulot_funksiyasi(message: types.Message, state: FSMContext):
    try:
        mahsulot_nomi = message.text
        print(mahsulot_nomi)
        photo_path = mashulot_ombori[mahsulot_nomi][1]
        narxi = mashulot_ombori[mahsulot_nomi][0]
        await message.answer_photo(photo=open(photo_path, 'rb'), caption=f"Narxi: {narxi}")
        await state.finish()
    except:
        await message.reply('Mahsulotlar menyusida bunday mahsulot mavjud emas')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
