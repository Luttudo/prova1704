import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Eu fiz criando o app mesmo, foi oq deu certo no meu caso

# Configuração do OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='a5586643247a4186a47d90538c17941a',
                                               client_secret='4be9150a0069493daac386cb55db80e0',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-top-read'))

# Obtendo as top 5 faixas
results = sp.current_user_top_tracks(limit=5)

# Obtendo os IDs das faixas
track_ids = [item['id'] for item in results['items']]

# Obtendo recomendações baseadas nas top 5 faixas
recommendations = sp.recommendations(seed_tracks=track_ids, limit=5)

# Imprimindo as informações do artista e da música
for track in recommendations['tracks']:
    print(f"Artista: {track['artists'][0]['name']}, Música: {track['name']}")

# Artista: CASHFILTER, Música: Racks! - Bônus Track
# Artista: Gype Strike, Música: Virar Dinheiro
# Artista: bastos, Música: Bag da Molly
# Artista: ALEF, Música: Menina de Oyá
# Artista: Giovanni, Música: Slow
