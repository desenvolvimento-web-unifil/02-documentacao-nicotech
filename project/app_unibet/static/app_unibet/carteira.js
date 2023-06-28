var inputSacar = document.getElementById('sacar-input');
var inputSaldoNovo = document.getElementById('saldo-novo');
var btnSacar = document.getElementById('sacar-btn');
var btnSaldo = document.getElementById('saldo-btn');
var inputDepositar = document.getElementById('depositar-input');
var btnDepositar = document.getElementById('depositar-btn');
var saldoAtual = document.getElementById('saldo-atual');

inputSacar.addEventListener('input', () =>  { 
    var regex = /^[0-9]+$/;
    var valor = inputSacar.value;
  
    if (!regex.test(valor)) {
        var aviso = document.createElement("p");
        aviso.classList.add("danger", "alert-danger");
        aviso.textContent = "Digite apenas números!";
        inputSacar.parentNode.insertBefore(aviso, inputSacar.nextSibling);

        
        setTimeout(function() {
        aviso.parentNode.removeChild(aviso);
      }, 1000);
  
      inputSacar.value = "";
    }

})

inputDepositar.addEventListener('input', () =>  { 
    var regex = /^[0-9.]+$/;
    var valor = inputDepositar.value;
  
    if (!regex.test(valor)) {
        var aviso = document.createElement("p");
        aviso.classList.add("danger", "alert-danger");
        aviso.textContent = "Digite apenas números!";
        inputDepositar.parentNode.insertBefore(aviso, inputDepositar.nextSibling);

        
        setTimeout(function() {
        aviso.parentNode.removeChild(aviso);
      }, 1000);
  
      inputDepositar.value = "";
    }

})

btnSaldo.addEventListener('click', ()=> {
    value_retirar = parseFloat(inputSacar.value)
    value_atual = parseFloat(saldoAtual.value)

    
    var value_novo =  value_atual - value_retirar;

    console.log(value_retirar)
    console.log(value_atual)
    console.log(value_novo)

    inputSaldoNovo.value = value_novo
})
