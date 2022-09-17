const urlsToCache = ["/", "static/app.js", "static/main.css", "static/logo.png","/home","static/icons/admin.png","static/icons/games.png","static/icons/maths.png","static/icons/number.png","static/icons/settings.png","static/icons/tasks.png","static/icons/toplogo.png","static/icons/write.png","static/background.jpg"]
self.addEventListener("install", event => {
   event.waitUntil(
      caches.open("pwa-assets")
      .then(cache => {
         return cache.addAll(urlsToCache);
      }));
});