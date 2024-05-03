document.addEventListener('DOMContentLoaded', async function() {
    const searchInput = document.getElementById('searchInput');
    const mp3List = document.getElementById('mp3List');
    const audioPlayer = document.getElementById('audioPlayer');
    let mp3Files = []; // Variable para almacenar la lista de archivos MP3

    // Obtener la lista de archivos MP3 disponibles en la carpeta "downloads"
    async function fetchMP3List() {
        try {
            const response = await fetch('/downloads'); // Cambiar la ruta según tu servidor
            if (!response.ok) {
                throw new Error('Error al obtener la lista de MP3');
            }
            mp3Files = await response.json(); // Almacenar la lista de archivos MP3
            displayMP3List(mp3Files);
        } catch (error) {
            console.error(error);
        }
    }

    // Función para mostrar la lista de archivos MP3
    function displayMP3List(mp3Array) {
        mp3List.innerHTML = mp3Array.map(item => `
            <div class="audioItem" data-url="${item.url}">
                ${item.name}
            </div>
        `).join('');
    }

    // Función para reproducir un archivo MP3
    function playMP3(mp3Url) {
        audioPlayer.src = mp3Url;
        audioPlayer.play();
    }

    // Cargar la lista de archivos MP3 al cargar la página
    await fetchMP3List();

    // Evento de búsqueda al escribir en el input
    searchInput.addEventListener('input', function(event) {
        const query = event.target.value.trim().toLowerCase();
        const filteredMP3 = mp3Files.filter(item =>
            item.name.toLowerCase().includes(query)
        );
        displayMP3List(filteredMP3);
    });

    // Evento de reproducción al hacer clic en un archivo MP3
    mp3List.addEventListener('click', function(event) {
        if (event.target.classList.contains('audioItem')) {
            const mp3Url = event.target.dataset.url;
            playMP3(mp3Url);
        }
    });
});
