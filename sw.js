/* ByteSumCookies legacy Chirpy PWA cache cleanup.
   A previously registered /sw.js may keep serving obsolete HTML.
   This temporary worker immediately activates, clears stale PWA caches,
   and unregisters itself. It does not intercept navigation. */
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    try {
      const names = await caches.keys();
      await Promise.all(names.map(name => caches.delete(name)));
    } catch (error) {
      // Keep unregistering even when cache storage is unavailable.
    }
    try { await self.registration.unregister(); } catch (error) {}
  })());
});
