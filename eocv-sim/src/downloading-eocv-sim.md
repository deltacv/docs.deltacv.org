# Downloading EOCV-Sim

## Prerequisites: Java

EOCV-Sim requires **Java 17 or newer** to run. If you don't have it installed, grab it from one of these sources:

- [Oracle JDK](https://www.oracle.com/java/technologies/javase-downloads.html) — official, free for personal use
- [Adoptium (Eclipse Temurin)](https://adoptium.net/) — recommended open-source alternative

Once installed, verify your Java version by opening a terminal and running:

```
java -version
```

It should print `17` or higher. If it doesn't, make sure your `JAVA_HOME` environment variable points to the correct installation.

## Download Latest Release

<div class="download-hero">
<div class="download-card">
<div class="download-icon">
<i class="fa-solid fa-download" style="font-size: 2em;" aria-hidden="true"></i>
</div>
<h2 class="download-title">EOCV-Sim</h2>
<p class="download-subtitle">Download the latest release and get started in seconds.</p>
<a id="download-btn" class="download-btn" href="https://github.com/deltacv/EOCV-Sim/releases/latest" target="_blank">
Download Latest
</a>
<p class="download-version" id="download-version">Fetching latest version…</p>
</div>
</div>

<script>
(function() {
  fetch("https://api.github.com/repos/deltacv/EOCV-Sim/releases/latest")
    .then(function(r) { return r.json(); })
    .then(function(data) {
      var tag = data.tag_name || "";
      var assets = data.assets || [];
      var jar = assets.find(function(a) {
        return a.name && a.name.match(/EOCV-Sim-.*-all\.jar$/);
      });
      var versionEl = document.getElementById("download-version");
      var btnEl = document.getElementById("download-btn");
      if (versionEl && tag) {
        versionEl.textContent = "Version " + tag;
      }
      if (btnEl && jar && jar.browser_download_url) {
        btnEl.href = jar.browser_download_url;
        btnEl.removeAttribute("target");
      }
      
      if (btnEl) {
        btnEl.addEventListener("click", function() {
          setTimeout(function() {
            var runSection = document.getElementById("running-eocv-sim");
            if (runSection) {
              runSection.scrollIntoView({ behavior: "smooth", block: "start" });
            }
          }, 200);
        });
      }
    })
    .catch(function() {});
})();
</script>

<h2 id="running-eocv-sim">Running EOCV-Sim</h2>

Once downloaded, double-click the jar file to launch it, just like any other executable.

You can also run it from the command line. Navigate to the folder containing the jar file using `cd`, then run:

```
java -jar "EOCV-Sim-X.X.X-all.jar"
```

Replace `X.X.X` with the actual version number, e.g. `3.1.0`.

<div class="promo-card" id="pv-promo">
<span class="promo-icon" id="pv-eye-icon-container">
<i class="fa-solid fa-eye" aria-hidden="true"></i>
</span>
<div class="promo-body">
<div id="pv-promo-default">
<p class="promo-title">PaperVision is already included!</p>
<p class="promo-desc">PaperVision ships bundled inside EOCV-Sim — no separate download needed. Head to the PaperVision docs to start building visual pipelines right away.</p>
</div>
<div id="pv-promo-return" style="display: none;">
<p class="promo-title" style="display: flex; align-items: center; font-size: 1.2em; font-weight: bold; margin-bottom: 8px;">
<i class="fa-solid fa-triangle-exclamation" style="margin-right: 12px; font-size: 1.2em;"></i>
Return to PaperVision
</p>
<p class="promo-desc" style="font-size: 1em; opacity: 1;">
<strong>You should now return to the PaperVision documentation.</strong> The content that follows in the current guide focuses solely on EOCV-Sim and does not contain any content about the node editor.
</p>
</div>
</div>
<a class="promo-btn" id="pv-promo-btn" href="/papervision/downloading-papervision.html">Go to PaperVision Docs →</a>
</div>

<script>
  window.addEventListener('DOMContentLoaded', function() {
    if (window.location.hash === "#from-papervision") {
      var pvPromo = document.getElementById("pv-promo");
      var defaultContent = document.getElementById("pv-promo-default");
      var returnContent = document.getElementById("pv-promo-return");
      var eyeContainer = document.getElementById("pv-eye-icon-container");
      var promoBtn = document.getElementById("pv-promo-btn");
      
      if (pvPromo) {
        pvPromo.style.transform = "scale(1.03)";
        if (defaultContent) defaultContent.style.display = "none";
        if (eyeContainer) eyeContainer.style.display = "none";
        if (returnContent) returnContent.style.display = "block";
        if (promoBtn) {
          promoBtn.textContent = "Return to PaperVision Docs →";
          promoBtn.href = "/papervision/downloading-papervision.html#how-to-use";
        }
      }
    }
  });
</script>
