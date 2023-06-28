var modalPartida = document.getElementById('modal-partida');
var inputCarteira = document.getElementById('input-id-carteira');
var inputIdPartida = document.getElementById('input-id-partida');
var inputIdLeague = document.getElementById('input-id-league');
var inputTeamHome = document.getElementById('input-team-home');
var inputTeamAway = document.getElementById('input-team-away');
var inputOddHome = document.getElementById('input-odd-home');
var inputOddDraw = document.getElementById('input-odd-draw');
var inputOddAway = document.getElementById('input-odd-away');
var inputDate = document.getElementById('input-date');
var inputTipo = document.getElementById('input-id-tipo');
var modalPartidaHomeName = document.getElementById('modal-team-home-name');
var modalPartidaAwayName = document.getElementById('modal-team-away-name');
var modalPartidaOddHome = document.getElementById('modal-odd-home');
var modalPartidaOddDraw = document.getElementById('modal-odd-draw');
var modalPartidaOddAway = document.getElementById('modal-odd-away');
var inputValor = document.getElementById('valor-aposta');
var inputRetorno = document.getElementById('retorno-aposta');
var btnRetorno = document.getElementById('gerar-retorno');
var btnApostar = document.getElementById('apostar-btn');
var form = document.getElementById('form-aposta');

var oddTempHome = document.getElementById('modal-odd-home');
var oddTempDraw = document.getElementById('modal-odd-draw');
var oddTempAway = document.getElementById('modal-odd-away');


function calcula_retorno(valor, odd) {
    return valor * odd
}

inputValor.addEventListener('input', () =>  { 
    var regex = /^[0-9]+$/;
    var valor = inputValor.value;
  
    if (!regex.test(valor)) {
        var aviso = document.createElement("p");
        aviso.classList.add("danger", "alert-danger");
        aviso.textContent = "Digite apenas números!";
        inputValor.parentNode.insertBefore(aviso, inputValor.nextSibling);

        
        setTimeout(function() {
        aviso.parentNode.removeChild(aviso);
      }, 1000);
  
      inputValor.value = "";
    }

})


modalPartida.addEventListener('show.bs.modal', function(event) {
    var button = event.relatedTarget;
    var idPartida = button.getAttribute('data-id-partida');
    var Carteira = button.getAttribute('data-carteira');
    var idLeague = button.getAttribute('data-id-league');
    var oddHome = button.getAttribute('data-odd-Home');
    var oddDraw = button.getAttribute('data-odd-Draw');
    var oddAway = button.getAttribute('data-odd-Away');
    var date = button.getAttribute('data-date');
    var teamNameHome = button.getAttribute('data-team-home');
    var teamNameAway = button.getAttribute('data-team-away');

    if (form && btnApostar) {
        form.addEventListener('submit', ()=> {
            if (parseFloat(Carteira ) < parseFloat(inputValor.value)) {
                var aviso = document.createElement("p");
                aviso.classList.add("danger", "alert-danger");
                aviso.textContent = "Digite apenas números!";
                inputValor.parentNode.insertBefore(aviso, inputValor.nextSibling);
        
                
                setTimeout(function() {
                aviso.parentNode.removeChild(aviso);
            }, 1000);
        
            inputValor.value = "";

            event.preventDefault();
            location.reload(true)
            }
        })
    }
    
    inputIdPartida.value = idPartida;

    if (idLeague == '71') {
        inputIdLeague.value = 1
    } else if (idLeague == '13') {
        inputIdLeague.value = 2
    } else if (idLeague == '72') {
        inputIdLeague.value = 3
    }

    inputTeamHome.value = teamNameHome
    inputTeamAway.value = teamNameAway
    inputOddHome.value = oddHome
    inputOddDraw.value = oddDraw
    inputOddAway.value = oddAway
    inputDate.value = date
    modalPartidaHomeName.textContent = teamNameHome;
    modalPartidaAwayName.textContent = teamNameAway;
    modalPartidaOddHome.textContent = oddHome;
    modalPartidaOddDraw.textContent = oddDraw;
    modalPartidaOddAway.textContent = oddAway;
    // Obtém os elementos dos radio buttons
    const radioButtons = document.querySelectorAll('.btn-check');

    // Adiciona o evento de mudança para os radio buttons
    radioButtons.forEach((radioButton) => {
    radioButton.addEventListener('change', function() {
    // Verifica qual radio button está selecionado
    if (this.id === 'btnradio1') {
        inputTipo.value = 1
    } else if (this.id === 'btnradio2') {
    // Exibe o conteúdo correspondente ao Option 2
        inputTipo.value = 2
    } else if (this.id === 'btnradio3') {
    // Exibe o conteúdo correspondente ao Option 3
        inputTipo.value = 3
    }

    btnRetorno.addEventListener('click', ()=> {
        if (inputTipo.value == 1) {
            inputRetorno.value = parseFloat(inputValor.value )* parseFloat(oddHome)
        } else if (inputTipo.value == 2) {
            inputRetorno.value = parseFloat(inputValor.value )* parseFloat(oddDraw)
        } else if (inputTipo.value == 3) {
            inputRetorno.value = parseFloat(inputValor.value )* parseFloat(oddAway)
        }
    })

});
});
});