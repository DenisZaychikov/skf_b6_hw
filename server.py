from bottle import route, run, HTTPError, request
import albums_script

@route('/albums/<artist>')
def albums(artist):
    artist_albums = ''
    all_albums, albums_counter = albums_script.find_albums(artist)
    if not all_albums:
        result = HTTPError(404, f'{artist} is not found!')
        
        return result
    else:
        for album in all_albums:
            artist_albums += album.album + '<br>'
    number_of_albums = f'<h3>Amount of {artist} albums found = {albums_counter}</h3>'
    
    return number_of_albums, artist_albums


@route('/albums/', method='POST')
def albums():
    new_artist = request.forms
    result = albums_script.save_artist(new_artist)
    if not result:
        return HTTPError(409, f'artist - {new_artist["artist"]} and album - {new_artist["album"]} are already saved in DB')

run(
    host='localhost',
    port=8000)
