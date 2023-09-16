import os 
import mysql.connector
import json
from enum import Enum
from tqdm import tqdm
from mysql.connector import errorcode
from sqlalchemy import CHAR, Column, Float, ForeignKey, Index, String, Table, Text, text, Date
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, MEDIUMINT, SMALLINT, TINYINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


Base = declarative_base()
metadata = Base.metadata

class ItemDisplayInfo(Base):
    __tablename__ = 'ItemDisplayInfo'

    ID = Column(INTEGER(11), primary_key=True, server_default=text("'0'"))
    ModelName_1 = Column(Text)
    ModelName_2 = Column(Text)
    ModelTexture_1 = Column(Text)
    ModelTexture_2 = Column(Text)
    InventoryIcon = Column(Text)
    GroundModel = Column(Text)
    GeosetGroup_1 = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    GeosetGroup_2 = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    GeosetGroup_3 = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    GeosetGroup_4 = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    Flags = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    SpellVisualID = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    GroupSoundIndex = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    ItemSize = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    HelmetGeosetVisID = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    Texture_1 = Column(Text)
    Texture_2 = Column(Text)
    Texture_3 = Column(Text)
    Texture_4 = Column(Text)
    Texture_5 = Column(Text)
    Texture_6 = Column(Text)
    Texture_7 = Column(Text)
    Texture_8 = Column(Text)
    ItemVisual = Column(INTEGER(11), nullable=False, server_default=text("'0'"))

class ItemTemplate(Base):
    __tablename__ = 'item_template'

    entry = Column(MEDIUMINT(8), primary_key=True, server_default=text("'0'"))
    class_ = Column('class', TINYINT(3), nullable=False, index=True, server_default=text("'0'"))
    subclass = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    name = Column(String(255), nullable=False, server_default=text("''"))
    description = Column(String(255), nullable=False, server_default=text("''"))
    display_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    quality = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    flags = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    buy_count = Column(TINYINT(3), nullable=False, server_default=text("'1'"))
    buy_price = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    sell_price = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    inventory_type = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    allowable_class = Column(MEDIUMINT(9), nullable=False, server_default=text("'-1'"))
    allowable_race = Column(MEDIUMINT(9), nullable=False, server_default=text("'-1'"))
    item_level = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    required_level = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    required_skill = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    required_skill_rank = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    required_spell = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    required_honor_rank = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    required_city_rank = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    required_reputation_faction = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    required_reputation_rank = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    max_count = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    stackable = Column(SMALLINT(5), nullable=False, server_default=text("'1'"))
    container_slots = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    stat_type1 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    stat_value1 = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    stat_type2 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    stat_value2 = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    stat_type3 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    stat_value3 = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    stat_type4 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    stat_value4 = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    stat_type5 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    stat_value5 = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    stat_type6 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    stat_value6 = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    stat_type7 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    stat_value7 = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    stat_type8 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    stat_value8 = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    stat_type9 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    stat_value9 = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    stat_type10 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    stat_value10 = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    delay = Column(SMALLINT(5), nullable=False, server_default=text("'1000'"))
    range_mod = Column(Float, nullable=False, server_default=text("'0'"))
    ammo_type = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    dmg_min1 = Column(Float, nullable=False, server_default=text("'0'"))
    dmg_max1 = Column(Float, nullable=False, server_default=text("'0'"))
    dmg_type1 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    dmg_min2 = Column(Float, nullable=False, server_default=text("'0'"))
    dmg_max2 = Column(Float, nullable=False, server_default=text("'0'"))
    dmg_type2 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    dmg_min3 = Column(Float, nullable=False, server_default=text("'0'"))
    dmg_max3 = Column(Float, nullable=False, server_default=text("'0'"))
    dmg_type3 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    dmg_min4 = Column(Float, nullable=False, server_default=text("'0'"))
    dmg_max4 = Column(Float, nullable=False, server_default=text("'0'"))
    dmg_type4 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    dmg_min5 = Column(Float, nullable=False, server_default=text("'0'"))
    dmg_max5 = Column(Float, nullable=False, server_default=text("'0'"))
    dmg_type5 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    block = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    armor = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    holy_res = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    fire_res = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    nature_res = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    frost_res = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    shadow_res = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    arcane_res = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    spellid_1 = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    spelltrigger_1 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    spellcharges_1 = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    spellppmrate_1 = Column(Float, nullable=False, server_default=text("'0'"))
    spellcooldown_1 = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    spellcategory_1 = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    spellcategorycooldown_1 = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    spellid_2 = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    spelltrigger_2 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    spellcharges_2 = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    spellppmrate_2 = Column(Float, nullable=False, server_default=text("'0'"))
    spellcooldown_2 = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    spellcategory_2 = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    spellcategorycooldown_2 = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    spellid_3 = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    spelltrigger_3 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    spellcharges_3 = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    spellppmrate_3 = Column(Float, nullable=False, server_default=text("'0'"))
    spellcooldown_3 = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    spellcategory_3 = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    spellcategorycooldown_3 = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    spellid_4 = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    spelltrigger_4 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    spellcharges_4 = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    spellppmrate_4 = Column(Float, nullable=False, server_default=text("'0'"))
    spellcooldown_4 = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    spellcategory_4 = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    spellcategorycooldown_4 = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    spellid_5 = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    spelltrigger_5 = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    spellcharges_5 = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    spellppmrate_5 = Column(Float, nullable=False, server_default=text("'0'"))
    spellcooldown_5 = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    spellcategory_5 = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    spellcategorycooldown_5 = Column(INTEGER(11), nullable=False, server_default=text("'-1'"))
    bonding = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    page_text = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    page_language = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    page_material = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    start_quest = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    lock_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    material = Column(TINYINT(4), nullable=False, server_default=text("'0'"))
    sheath = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    random_property = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    set_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    max_durability = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    area_bound = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    map_bound = Column(SMALLINT(6), nullable=False, server_default=text("'0'"))
    duration = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    bag_family = Column(MEDIUMINT(9), nullable=False, server_default=text("'0'"))
    disenchant_id = Column(MEDIUMINT(8), nullable=False, server_default=text("'0'"))
    food_type = Column(TINYINT(3), nullable=False, server_default=text("'0'"))
    min_money_loot = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    max_money_loot = Column(INTEGER(10), nullable=False, server_default=text("'0'"))
    extra_flags = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    ignored = Column(TINYINT(1), nullable=False, server_default=text("'0'"))

class MysqlDatabase:

    def __init__(
        self, user="root", 
        password="pwd", 
        host="localhost", 
        database_name="alpha_world"):

        self.user = user
        self.password = password
        self.host = host
        self.database_name = database_name
        self.database_session = None

    def connect(self):  
        db_engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database_name}?charset=utf8mb4',
                                    pool_pre_ping=True)
        self.database_session = SessionHolder = scoped_session(sessionmaker(bind=db_engine, autoflush=True))

    def close(self):
        self.database_session.close()

    def get_all(self, model):
        return self.database_session.query(model).all()

    def get_by_entry(self, model, entry):
        return self.database_session.query(model).filter_by(entry=entry).first()

    def get_by_id(self, model, id):
        return self.database_session.query(model).filter_by(ID=id).first()

    def get_by_display_id(self, model, display_id):
                return self.database_session.query(model).filter_by(display_id=display_id).all()

    def get_by_name(self, model, name):
        return self.database_session.query(model).filter_by(name=name).first()

    def get_by_title(self, model, title):
        return self.database_session.query(model).filter_by(Title=title).first()

    def has_multiple_entry(self, model, name):
        results = [r for r in self.database_session.query(model).filter_by(Title=name)]
        
        if len(results) > 1:
            return True

        return False

if __name__ == "__main__":

    print("START PARSING DATA")
        
    media_path = os.path.join(os.getcwd(), "static/models")
    media_folders = os.listdir(media_path)

    alpha_dbc = MysqlDatabase(database_name="alpha_dbc")
    alpha_world = MysqlDatabase(database_name="alpha_world")
    alpha_dbc.connect()
    alpha_world.connect()

    results = []

    for folder in tqdm(media_folders):
        folder_path = os.path.join(media_path, folder)
        display_ids = os.listdir(folder_path)
        display_ids = [int(d.split(".")[0]) for d in display_ids]
        display_ids.sort()

        for display_id in display_ids:
            items_obj = alpha_world.get_by_display_id(ItemTemplate, display_id)
            formatted_items = [{"entry": item.entry, "name": item.name} for item in items_obj]
            display_obj = alpha_dbc.get_by_id(ItemDisplayInfo, display_id)

            json_display = {
                "id": display_id,
                "path": folder, 
                "icon": display_obj.InventoryIcon,
                "item_size": display_obj.ItemSize,
                "used": True if formatted_items else False,
                "used_by": formatted_items
            }

            results.append(json_display)

    alpha_dbc.close()
    alpha_world.close()

    json_path = os.path.join(os.getcwd(), "static/images.json")
    with open(json_path, "w") as f:
        f.write(json.dumps(results))

    print("SUCCESSFULLY UPDATED AND SAVED")