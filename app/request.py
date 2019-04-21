from app import app
from .models import pitch

Pitch = pitch.Pitch

def get_pitches(category):
    pitch_results = None

    if get_pitches_response['results']:
        pitches_result_list = get_piches_response['results']
        pitches_results = process_results(pitches_result_list)


   return pitch_results

def process_results(pitch_list):
    '''
    Function that processes the pitch result and transforms it into a list of objects

    Args:
        pitch_list: a list of dictionaries that contain pitch details

    Returns:
        pitch_results: A list of pitch objects
    '''

    pitch_results = []
    for pitch_item in pitch_list:
            id = pitch_item.get('id')
            pitch = pitch_item.get('pitch')   

    return pitch_results             