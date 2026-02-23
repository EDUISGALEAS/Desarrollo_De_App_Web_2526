// Arreglo de productos inicial
const productos = [
    {
        nombre: "PLAYSTATION 5",
        precio: 750,
        descripcion: "producto para diversion en casa"
    },
    {
        nombre: "juegos de PS5",
        precio: 85,
        descripcion: "completento para el PS5"
    },
    {
        nombre: "Tv 4k" ,
        precio: 500,
        descripcion: "PRODUCTO IDEAL PARA DISFRUTAR DE SU PS5"
    }
];

// Referencias al DOM
const lista = document.getElementById("listaProductos");
const botonAgregar = document.getElementById("btnAgregar");

// Función para renderizar los productos en el HTML
function renderizarProductos() {
    lista.innerHTML = "";

    productos.forEach(producto => {
        const li = document.createElement("li");

        li.innerHTML = `
            <h3>${producto.nombre}</h3>
            <p class="precio">$${producto.precio}</p>
            <p>${producto.descripcion}</p>
        `;

        lista.appendChild(li);
    });
}

// Evento del botón para agregar un nuevo producto
botonAgregar.addEventListener("click", () => {
    const nombre = prompt("Ingrese el nombre del producto:");
    const precio = prompt("Ingrese el precio del producto:");
    const descripcion = prompt("Ingrese una breve descripción:");

    if (nombre && precio && descripcion) {
        const nuevoProducto = {
            nombre: nombre,
            precio: precio,
            descripcion: descripcion
        };

        productos.push(nuevoProducto);
        renderizarProductos();
    } else {
        alert("Por favor complete todos los campos.");
    }
});

// Renderizar la lista al cargar la página
renderizarProductos();
