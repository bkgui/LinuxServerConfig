from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import EngineOil, Base, EngineOilItem, User

engine = create_engine('sqlite:///engineoil.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Gui", email="jasongui8@gmail.com",
             picture='https://scontent.fkul6-1.fna.fbcdn.net/v/t1.0-9/13445650_10207207495649264_2247837608154913258_n.jpg?_nc_eui2=v1%3AAeHxbggw7a7gzAjVKND4eZOMcdplkiAYMs634fupmSbctKVkAIPl7CS3zWVqATzMPYIbPF1Ztt4yzIEXBqWPQsss-gbhEcgezKoMZqbJy34DVQ&oh=dbb19d21f08c3c21d620a185ca28598a&oe=59CD56CE')
session.add(User1)
session.commit()

# EngineOil for Bosch
EngineOil1 = EngineOil(user_id=1, brand="BOSCH")
session.add(EngineOil1)
session.commit()

       
EngineOilItem1 = EngineOilItem(user_id=1, name="GWS13-50VS", description="Small angle grinders",
                     price="$50.99", type="Normal", engineoil=EngineOil1)
session.add(EngineOilItem1)
session.commit()

EngineOilItem2 = EngineOilItem(user_id=1, name="1994-6/1994-6D", description="Large angle grinders",
                     price="$60.99", type="Normal", engineoil=EngineOil1)
session.add(EngineOilItem2)
session.commit()

EngineOilItem3 = EngineOilItem(user_id=1, name="PS31", description="Cordless drill",
                     price="$103.99", type="Normal", engineoil=EngineOil1)
session.add(EngineOilItem3)
session.commit()

EngineOilItem4 = EngineOilItem(user_id=1, name="GP712VS", description="Die Grinders",
                     price="$67.99", type="Normal", engineoil=EngineOil1)
session.add(EngineOilItem4)
session.commit()

EngineOilItem5 = EngineOilItem(user_id=1, name="CM10GD", description="10inch DUAL-BEVEL GLIDE MITER SAW",
                     price="$211.99", type="Normal", engineoil=EngineOil1)
session.add(EngineOilItem5)
session.commit()

EngineOilItem6 = EngineOilItem(user_id=1, name="GAM 220 MF", description="Digital angle finder and inclinometer",
                     price="$111.59", type="Normal", engineoil=EngineOil1)

session.add(EngineOilItem6)
session.commit()

EngineOilItem7 = EngineOilItem(user_id=1, name="D-TECT 150", description="Wall scanner with radar",
                    price="$3.49", type="Normal", engineoil=EngineOil1)
session.add(EngineOilItem7)
session.commit()

EngineOilItem8 = EngineOilItem(user_id=1, name="GLL 2-20", description="Self-Leveling, horizontal cross-line laser",
                     price="$315.59", type="Normal", engineoil=EngineOil1)
session.add(EngineOilItem8)
session.commit()
 



# EngineOil for Makita
EngineOil2 = EngineOil(user_id=1, brand="MAKITA")
session.add(EngineOil2)
session.commit()
       
EngineOilItem1 = EngineOilItem(user_id=1, name="XAG01", description="Cut-off angle grinder",
                     price="$40.99", type="Normal", engineoil=EngineOil2)
session.add(EngineOilItem1)
session.commit()

EngineOilItem2 = EngineOilItem(user_id=1, name="GA5042C", description="Cordless 18V grinder",
                     price="$150.99", type="Normal", engineoil=EngineOil2)
session.add(EngineOilItem2)
session.commit()

EngineOilItem3 = EngineOilItem(user_id=1, name="GA7911", description="Angle sander",
                     price="$113.99", type="Normal", engineoil=EngineOil2)
session.add(EngineOilItem3)
session.commit()

EngineOilItem4 = EngineOilItem(user_id=1, name="GD0801C", description="Die Grinders",
                     price="$67.99", type="Normal", engineoil=EngineOil2)
session.add(EngineOilItem4)
session.commit()

EngineOilItem5 = EngineOilItem(user_id=1, name="LD080P", description="Range 262 feet",
                     price="$89.00", type="Normal", engineoil=EngineOil2)
session.add(EngineOilItem5)
session.commit()

EngineOilItem6 = EngineOilItem(user_id=1, name="SK103PZ", description="Self-Leveling, horizontal cross-line laser",
                     price="$325.00", type="Normal", engineoil=EngineOil2)
session.add(EngineOilItem6)
session.commit()

EngineOilItem7 = EngineOilItem(user_id=1, name="RP2301FC", description="3-1/4 HP* PLUNGE ROUTER",
                     price="$689.00", type="Normal", engineoil=EngineOil2)
session.add(EngineOilItem7)
session.commit()

EngineOilItem8 = EngineOilItem(user_id=1, name="BO6050J", description="6inch RANDOM ORBIT SANDER",
                     price="$65.50", type="Normal", engineoil=EngineOil2)
session.add(EngineOilItem8)
session.commit()




print "added menu items!"
