import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = 'sqlite:///albums.sqlite3'
Base = declarative_base()


class Albums(Base):
    __tablename__ = 'album'
    id = sa.Column(sa.Integer, primary_key=True)
    year = sa.Column(sa.Integer)
    artist = sa.Column(sa.Text)
    genre = sa.Column(sa.Text)
    album = sa.Column(sa.Text)

    
def connect_db():
    engine = sa.create_engine(DB_PATH)
    session = sessionmaker(engine)

    return session()


def save_artist(new_artist):
    session = connect_db()
    if session.query(Albums).filter(Albums.artist == new_artist.get('artist') and Albums.album == new_artist.get('album')).first():
        return False
    else:
        user = Albums(
            year=new_artist.get('name'),
            artist=new_artist.get('artist'),
            genre=new_artist.get('genre'),
            album=new_artist.get('album'))
        session.add(user)
        session.commit()
    return True


def find_albums(artist):    
    session = connect_db()
    all_albums = session.query(Albums).filter(Albums.artist == artist).all()
    albums_counter = session.query(Albums).filter(Albums.artist == artist).count()

    return all_albums, albums_counter
