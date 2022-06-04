self.addEventListener("install",e=>{
    e.waitUntill(
        caches.open("static").then(cache => {
            return cache.addAll(["./index.js","./src/test-xl.xlsx","./attendace.html","./","./src/styles.css","./img/icon-192x192.png"]);
        })
    );
});
self.addEventListener("fetch", e =>{
    console.log("intercepting fetch request for : ${e.request.url}");
    e.respondWith(
        caches.match(e.request).then(response=>{
            return response ||fetch(e.request);
        })
    )
});
