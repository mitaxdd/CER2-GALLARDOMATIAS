function actualizar() {

    var tipoReciclaje = document.getElementById("tipoReciclaje").value;
    var subtipoReciclaje = document.getElementById("subtipoReciclaje");

    subtipoReciclaje.innerHTML = '';

    var opciones = [];

    if (tipoReciclaje === "plastico") {
        opciones = [
            { value: "botellas", text: "Botellas de plástico" },
            { value: "envases", text: "Envases plásticos" },
            { value: "bolsas", text: "Bolsas plásticas" }
        ];
    } else if (tipoReciclaje === "papel") {
        opciones = [
            { value: "carton", text: "Cartón" },
            { value: "revistas", text: "Revistas" },
            { value: "papel", text: "Papel" }
        ];
    } else if (tipoReciclaje === "vidrio") {
        opciones = [
            { value: "botellas-vidrio", text: "Botellas de vidrio" },
            { value: "frascos", text: "Frascos de vidrio" },
            { value: "ventanas", text: "Vidrios de ventanas" }
        ];
    } else if (tipoReciclaje === "metales") {
        opciones = [
            { value: "latas-aluminio", text: "Latas de aluminio" },
            { value: "chatarra", text: "Chatarra metálica" },
            { value: "tapas-botellas", text: "Tapas de botellas metálicas" }
        ];
    } else if (tipoReciclaje === "electronicos") {
        opciones = [
            { value: "celulares", text: "Celulares" },
            { value: "computadoras", text: "Computadoras" },
            { value: "cargadores", text: "Cargadores" },
            { value: "otros", text: "Otros" }
        ];
    }
    
    opciones.forEach(function(opcion) {
        var nueva = document.createElement("option");
        nueva.value = opcion.value;
        nueva.text = opcion.text;
        subtipoReciclaje.appendChild(nueva);
    });
}