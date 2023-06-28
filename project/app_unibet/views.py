from venv import logger
from django.shortcuts import render
import requests
from .models import Apostas, Partidas, TipoAposta, Odds, Campeonatos, Carteira

url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

url2 = "https://api-football-v1.p.rapidapi.com/v3/odds"

paramFixtures = {
    "league": "",
    "season": "2023",
    "date": "",
    "timezone": "America/Sao_Paulo"
}

paramOdds = {
    "league": "",
    "season": "2023",
    "date": "",
    "bet": "1",
    "bookmaker": "8",
    "timezone": "America/Sao_Paulo"
}

headers = {
	"X-RapidAPI-Key": "9d491ea861msh4f7cb0d4c26297cp1323cdjsn20be71ee6048",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

# Create your views here.

def apostas(request):
    carteira = Carteira.objects.get(id_carteira=1)
    campeonato = request.GET.get('campeonato')
    data = request.GET.get('data')
    paramFixtures["date"] = data
    paramOdds["date"] = data
    paramFixtures["league"] = campeonato
    paramOdds["league"] = campeonato
    
    partida_response = requests.get(url, params=paramFixtures, headers=headers).json()
    odds_response = requests.get(url2, params=paramOdds, headers=headers).json()

    partidas = partida_response['response']
    odds = odds_response['response']
    response = []

    for partida in partidas:
        partida_id = partida['fixture']['id']
        for odd in odds:
            if odd['fixture']['id'] == partida_id:
                response.append({
                    'partida':{
                        'fixture_id': partida['fixture']['id'],
                        'info': {
                            'league_id':partida['league']['id'],
                            'league_name': partida['league']['name'],
                            'date': partida['fixture']['date']
                        },
                        'status': partida['fixture']['status'],
                        'teams': partida['teams'],
                        'goals': partida['goals'],
                        'odds': odd['bookmakers'][0]['bets'][0]['values']
                    },
                    'carteiras': carteira
                })
                break
    return render(request, 'apostas.html', {'response':response})

def registrar_aposta(request):
    nova_aposta = Apostas()
    nova_partida = Partidas()
    novo_odds = Odds()
    carteira = Carteira.objects.get(id_carteira=1)

    team_home = request.POST.get('input-team-home')
    team_away = request.POST.get('input-team-away')
    odd_home = request.POST.get('input-odd-home')
    odd_draw = request.POST.get('input-odd-draw')
    odd_away = request.POST.get('input-odd-away')
    valor = request.POST.get('valor-aposta')
    retorno = request.POST.get('retorno-aposta')
    date = request.POST.get('input-date')
    id_partida = request.POST.get('input-id-partida')
    id_tipo = request.POST.get('input-id-tipo')
    id_league = request.POST.get('input-id-league')

    novo_odds.odd_casa = float(odd_home)
    novo_odds.odd_empate = float(odd_draw)
    novo_odds.odd_fora = float(odd_away)

    novo_odds.save()

    nova_partida.id_partida = id_partida
    nova_partida.time_casa = team_home
    nova_partida.time_fora = team_away
    nova_partida.horario = date
    nova_partida.id_odds = novo_odds
    nova_partida.id_campeonato = Campeonatos.objects.get(id_campeonato=int(id_league))

    nova_partida.save()

    nova_aposta.valor = valor
    nova_aposta.retorno = retorno
    nova_aposta.id_partida = nova_partida
    nova_aposta.id_tipo = TipoAposta.objects.get(id_tipo=id_tipo)

    nova_aposta.save()

    carteira.valor = carteira.valor - float(valor)
    carteira.save()

    return render(request, 'apostas.html')

def lista_apostas(request):
    response = {
    'apostas': Apostas.objects.all(),
    'tipos': TipoAposta.objects.all(),
    'partidas': Partidas.objects.all(),
    'odds': Odds.objects.all()
    } 
    
    return render(request, 'lista_apostas.html', response)

def carteira(request):
    response = {
        'carteiras': Carteira.objects.all()
    }
    return render(request, 'carteira.html', response)

def depositar(request):
    id_carteira = request.POST.get('id-carteira-dep')
    valor_adicionar = request.POST.get('depositar-input')

    response = {
        'carteiras': Carteira.objects.all()
    }

    carteira = Carteira.objects.get(id_carteira=int(id_carteira))

    valor_atual = carteira.valor
    if valor_adicionar == '':
        return render(request, 'carteira.html', response)

    valor_novo = float(valor_adicionar) + valor_atual

    carteira.valor = valor_novo

    carteira.save()

    return render(request, 'carteira.html', response)

def sacar(request):
    id_carteira = request.POST.get('id-carteira-sac')
    valor_adicionar = request.POST.get('sacar-input')

    response = {
        'carteiras': Carteira.objects.all()
    }

    carteira = Carteira.objects.get(id_carteira=int(id_carteira))

    valor_atual = carteira.valor

    if valor_adicionar == '' or valor_atual < float(valor_adicionar):
        return render(request, 'carteira.html', response)
    
    valor_novo = float(valor_adicionar) - valor_atual

    carteira.valor = valor_novo

    carteira.save()

    return render(request, 'carteira.html', response)

def checar_status(request):
    id_aposta = request.GET.get('id_aposta')
    aposta = Apostas.objects.get(id_aposta=id_aposta)
    id_partida = aposta.id_partida
    id_tipo = aposta.id_tipo
    retorno = aposta.retorno
    valor = aposta.valor
    carteira = Carteira.objects.get(id_carteira=1)


    paramsFixId = {
        'id': id_partida.id_partida
    }

    response = requests.get(url, params=paramsFixId, headers=headers).json()

    status = response['response'][0]['fixture']['status']
    score = response['response'][0]['score']
    fulltime_home = score['fulltime']['home']
    fulltime_away = score['fulltime']['away']

    if status['short'] == 'MT':
        aposta.finalizada = 1
        if id_tipo == 1:
            if fulltime_home > fulltime_away:
                aposta.resultado = 1
                carteira.valor += retorno
            else:
                aposta.resultado = 0
                carteira.valor -= valor
        if id_tipo == 2:
            if fulltime_home == fulltime_away:
                aposta.resultado = 1
                carteira.valor += retorno
            else:
                aposta.resultado = 0
                carteira.valor -= valor
        if id_tipo == 3:
            if fulltime_home < fulltime_away:
                aposta.resultado = 1
                carteira.valor += retorno
            else:
                aposta.resultado = 0
                carteira.valor -= valor

    response = {
        'apostas': Apostas.objects.all(),
        'tipos': TipoAposta.objects.all(),
        'partidas': Partidas.objects.all(),
        'odds': Odds.objects.all()
    } 

    return render(request, 'lista_apostas.html', response)

