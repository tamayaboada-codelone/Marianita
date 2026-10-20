// ==========================================================
//  GALERÍA — abre cada foto en grande al hacer clic.
//  Usa <dialog>, que es HTML nativo (no hace falta librería).
// ==========================================================

document.addEventListener('DOMContentLoaded', () => {
    const dialog = document.getElementById('lightbox');
    if (!dialog) return;

    const grande = dialog.querySelector('img');
    const pie = dialog.querySelector('figcaption');

    document.querySelectorAll('.galeria-item img').forEach(foto => {
        foto.addEventListener('click', () => {
            grande.src = foto.src;
            grande.alt = foto.alt;
            pie.textContent = foto.alt;
            dialog.showModal();
        });
    });

    // Cerrar haciendo clic fuera de la foto.
    // (la tecla Escape ya cierra el <dialog> por sí solo)
    dialog.addEventListener('click', (evento) => {
        if (evento.target === dialog) dialog.close();
    });
});
