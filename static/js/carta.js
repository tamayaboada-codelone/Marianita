document.addEventListener('DOMContentLoaded', () => {
  const envelope = document.getElementById('envelope');
  const hint = document.getElementById('hint');
  const canvas = document.getElementById('canvas-hearts');

  // Si no estamos en la página de la carta, no hacemos nada
  if (!envelope || !hint || !canvas) return;

  envelope.addEventListener('click', () => {
    const isOpen = envelope.classList.toggle('open');
    hint.textContent = isOpen ? "✨ Toca de nuevo para cerrar ✨" : "✨ Toca el sobre para abrirlo ✨";

    // El título se desvanece mientras el sobre está abierto
    document.body.classList.toggle('envelope-abierto', isOpen);

    if (isOpen) {
      createHeartBurst();
    }
  });

  // Fondo animado de partículas de corazones
  const ctx = canvas.getContext('2d');

  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  const hearts = Array.from({ length: 25 }, () => ({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    size: Math.random() * 12 + 8,
    speedY: Math.random() * 0.8 + 0.3,
    opacity: Math.random() * 0.5 + 0.3,
    swing: Math.random() * 0.02
  }));

  function drawHeart(x, y, size, color, opacity) {
    ctx.save();
    ctx.globalAlpha = opacity;
    ctx.fillStyle = color;
    ctx.beginPath();
    const topCurveHeight = size * 0.3;
    ctx.moveTo(x, y + topCurveHeight);
    ctx.bezierCurveTo(x, y, x - size / 2, y, x - size / 2, y + topCurveHeight);
    ctx.bezierCurveTo(x - size / 2, y + (size + topCurveHeight) / 2, x, y + size, x, y + size);
    ctx.bezierCurveTo(x, y + size, x + size / 2, y + (size + topCurveHeight) / 2, x + size / 2, y + topCurveHeight);
    ctx.bezierCurveTo(x + size / 2, y, x, y, x, y + topCurveHeight);
    ctx.closePath();
    ctx.fill();
    ctx.restore();
  }

  function animateBackground() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    hearts.forEach(h => {
      h.y -= h.speedY;
      h.x += Math.sin(h.y * h.swing) * 0.5;
      if (h.y < -20) {
        h.y = canvas.height + 20;
        h.x = Math.random() * canvas.width;
      }
      drawHeart(h.x, h.y, h.size, '#e91e63', h.opacity);
    });
    requestAnimationFrame(animateBackground);
  }
  animateBackground();

  // Ráfaga de corazones al abrir
  function createHeartBurst() {
    const rect = envelope.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    for (let i = 0; i < 15; i++) {
      const burstHeart = document.createElement('div');
      burstHeart.textContent = '❤️';
      burstHeart.style.position = 'fixed';
      burstHeart.style.left = centerX + 'px';
      burstHeart.style.top = centerY + 'px';
      burstHeart.style.fontSize = (Math.random() * 15 + 15) + 'px';
      burstHeart.style.pointerEvents = 'none';
      burstHeart.style.zIndex = '100';
      burstHeart.style.transition = 'transform 1s ease-out, opacity 1s ease-out';
      document.body.appendChild(burstHeart);

      const angle = Math.random() * Math.PI * 2;
      const dist = Math.random() * 100 + 50;
      const tx = Math.cos(angle) * dist;
      const ty = Math.sin(angle) * dist - 50;

      setTimeout(() => {
        burstHeart.style.transform = `translate(${tx}px, ${ty}px) scale(0)`;
        burstHeart.style.opacity = '0';
      }, 10);

      setTimeout(() => burstHeart.remove(), 1000);
    }
  }
});
