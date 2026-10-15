const ring = document.querySelector('#ring');
const scene = document.querySelector('#scene');
const status = document.querySelector('#status');
const startAR = document.querySelector('#startAR');
const demoMode = document.querySelector('#demoMode');
const reticle = document.querySelector('#reticle');

function setBehavior(name) {
  ring.className = `ring ${name}`;
  const messages = {
    wave: 'Ring-A-Ding waves from your space.',
    happy: 'Ring-A-Ding is excited to see you.',
    think: 'Ring-A-Ding is studying the world around him.',
    dream: 'Ring-A-Ding has entered dream mode.',
    follow: 'Ring-A-Ding is ready to follow your movement.'
  };
  status.textContent = messages[name] || 'Ring-A-Ding is ready.';
}

document.querySelectorAll('[data-action]').forEach(button => {
  button.addEventListener('click', () => setBehavior(button.dataset.action));
});

demoMode.addEventListener('click', async () => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({video:{facingMode:'environment'}, audio:false});
    const video = document.createElement('video');
    video.autoplay = true;
    video.playsInline = true;
    video.srcObject = stream;
    video.style.cssText = 'position:fixed;inset:0;width:100%;height:100%;object-fit:cover;z-index:-1';
    scene.classList.add('cameraDemo');
    scene.prepend(video);
    status.textContent = 'Camera demo active. Ring-A-Ding is overlaid on the camera view.';
    reticle.hidden = false;
  } catch (error) {
    status.textContent = `Camera unavailable: ${error.message}`;
  }
});

startAR.addEventListener('click', async () => {
  if (!('xr' in navigator)) {
    status.textContent = 'WebXR is not available in this browser/device. Use the camera demo instead.';
    return;
  }
  try {
    const supported = await navigator.xr.isSessionSupported('immersive-ar');
    if (!supported) {
      status.textContent = 'Immersive AR is not supported on this device. Use the camera demo instead.';
      return;
    }
    const session = await navigator.xr.requestSession('immersive-ar', {
      requiredFeatures: ['local-floor'],
      optionalFeatures: ['hit-test']
    });
    status.textContent = 'WebXR AR session started. Ring-A-Ding can be connected to the world renderer next.';
    session.addEventListener('end', () => {
      status.textContent = 'AR session ended.';
      reticle.hidden = true;
    });
  } catch (error) {
    status.textContent = `AR could not start: ${error.message}`;
  }
});
