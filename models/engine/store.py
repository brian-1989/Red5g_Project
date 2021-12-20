"""Search engine.

"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.model_food import food, Base

class Storage():
    __engine = None
    __session = None
    def __init__(self):
        """ This function is for initializing the motor.

        """
        user = 'root'
        pwd = 'brian1995'
        host = 'localhost'
        db = 'food'
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db))

    def all(self, cls=None):
        """ This function is for store the information.

        """
        dict_class = {"food": food}
        new_dict = {}
        if cls in dict_class:
            objs = self.__session.query(dict_class[cls]).all()
            for obj in objs:
                key = obj.id
                new_dict[key] = obj
            return new_dict

    def save(self):
        """ This function is for save the information.

        """
        self.__session.commit()

    def new_obj(self, obj):
        """ This function is for create a new object.

        """
        self.__session.add(obj)

    def reload(self):
        """This function reloads data from the database.

        """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session
