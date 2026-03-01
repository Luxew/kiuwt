function crearGifsAlAzar() {
    const cantidad = 30; // Puedes cambiar cuántos quieres ver
    for (let i = 0; i < cantidad; i++) {
        const gif = document.createElement('img');
        gif.src = 'WONEJO.gif';
        gif.className = 'gif-random';
        
        // Posiciones al azar
        const x = Math.random() * window.innerWidth;
        const y = Math.random() * window.innerHeight;
        
        gif.style.left = x + 'px';
        gif.style.top = y + 'px';
        
        // Rotación al azar para que se vea más aesthetic
        const rotacion = Math.random() * 360;
        gif.style.transform = `rotate(${rotacion}deg)`;
        
        document.body.appendChild(gif);
    }
}

// Ejecutar cuando cargue la página
window.onload = crearGifsAlAzar;