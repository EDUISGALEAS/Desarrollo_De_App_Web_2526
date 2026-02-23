const formulario = document.getElementById("formulario");
const btnEnviar = document.getElementById("btnEnviar");

const nombre = document.getElementById("nombre");
const correo = document.getElementById("correo");
const password = document.getElementById("password");
const confirmarPassword = document.getElementById("confirmarPassword");
const edad = document.getElementById("edad");

function validarNombre() {
    if (nombre.value.length >= 3) {
        marcarValido(nombre, "errorNombre", "");
        return true;
    } else {
        marcarInvalido(nombre, "errorNombre", "Mínimo 3 caracteres");
        return false;
    }
}

function validarCorreo() {
    const regex = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (regex.test(correo.value)) {
        marcarValido(correo, "errorCorreo", "");
        return true;
    } else {
        marcarInvalido(correo, "errorCorreo", "Correo no válido");
        return false;
    }
}

function validarPassword() {
    const regex = /^(?=.*[0-9])(?=.*[!@#$%^&*])/;
    if (password.value.length >= 8 && regex.test(password.value)) {
        marcarValido(password, "errorPassword", "");
        return true;
    } else {
        marcarInvalido(password, "errorPassword", "Mínimo 8 caracteres, número y símbolo");
        return false;
    }
}

function validarConfirmacion() {
    if (password.value === confirmarPassword.value && confirmarPassword.value !== "") {
        marcarValido(confirmarPassword, "errorConfirmar", "");
        return true;
    } else {
        marcarInvalido(confirmarPassword, "errorConfirmar", "No coinciden");
        return false;
    }
}

function validarEdad() {
    if (edad.value >= 18) {
        marcarValido(edad, "errorEdad", "");
        return true;
    } else {
        marcarInvalido(edad, "errorEdad", "Debes ser mayor de 18");
        return false;
    }
}

function marcarValido(input, errorId, mensaje) {
    input.classList.add("valido");
    input.classList.remove("invalido");
    document.getElementById(errorId).textContent = mensaje;
}

function marcarInvalido(input, errorId, mensaje) {
    input.classList.add("invalido");
    input.classList.remove("valido");
    document.getElementById(errorId).textContent = mensaje;
}

function validarFormulario() {
    if (
        validarNombre() &&
        validarCorreo() &&
        validarPassword() &&
        validarConfirmacion() &&
        validarEdad()
    ) {
        btnEnviar.disabled = false;
    } else {
        btnEnviar.disabled = true;
    }
}

nombre.addEventListener("input", validarFormulario);
correo.addEventListener("input", validarFormulario);
password.addEventListener("input", validarFormulario);
confirmarPassword.addEventListener("input", validarFormulario);
edad.addEventListener("input", validarFormulario);

formulario.addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Formulario validado correctamente ✔️");
});
