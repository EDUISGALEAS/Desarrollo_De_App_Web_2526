function mostrarAlerta() {
  alert("¡Gracias por interactuar con nuestra página!");
}

document.getElementById("contactForm").addEventListener("submit", function(e) {
  e.preventDefault();

  let valido = true;

  let nombre = document.getElementById("nombre").value.trim();
  let correo = document.getElementById("correo").value.trim();
  let mensaje = document.getElementById("mensaje").value.trim();

  document.getElementById("errorNombre").textContent = "";
  document.getElementById("errorCorreo").textContent = "";
  document.getElementById("errorMensaje").textContent = "";

  if (nombre === "") {
    document.getElementById("errorNombre").textContent = "El nombre es obligatorio";
    valido = false;
  }

  if (correo === "") {
    document.getElementById("errorCorreo").textContent = "El correo es obligatorio";
    valido = false;
  }

  if (mensaje === "") {
    document.getElementById("errorMensaje").textContent = "El mensaje es obligatorio";
    valido = false;
  }

  if (valido) {
    alert("Formulario enviado correctamente ✅");
    this.reset();
  }
});
