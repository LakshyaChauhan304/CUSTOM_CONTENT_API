// main.js — basic DOM ready and event example
document.addEventListener('DOMContentLoaded', function () {
  console.log('Main JS loaded');

  // Example: add a button programmatically
  const btn = document.createElement('button');
  btn.textContent = 'Click me';
  btn.className = 'btn btn-primary';
  btn.addEventListener('click', () => {
    alert('Hello from Django + JS!');
  });

  // Append to main container if present
  const container = document.querySelector('main.container');
  if (container) container.prepend(btn);
});
